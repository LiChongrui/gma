# -*- coding: utf-8 -*-
"""从 gma 源码 AST 提取 docstring，按官网 md 格式补齐 D:/github/gma 缺失的帮助文档。

补齐内容：
  docs/UserGuide/crs/README.md                     Start
  docs/UserGuide/crs/CoordinateReferenceSystem.md
  docs/UserGuide/crs/Datum.md
  docs/UserGuide/crs/Ellipsoid.md
  docs/UserGuide/crs/GeographicCoordinateSystem.md
  docs/UserGuide/crs/ProjectedCoordinateSystem.md
  docs/UserGuide/crs/ProjMethods/<34 投影>.md
  docs/UserGuide/const/README.md                   Start（常量总表）
"""
import ast
import io
import os
import re

SRC_CRS = 'D:/github/gma-code/gma 3.0.x/gma/_algos/geo/crs.py'
SRC_CONST = 'D:/github/gma-code/gma 3.0.x/gma/const.py'
OUT = 'D:/github/gma/docs/UserGuide'
DATE = '2026-11-20'


def esc(s):
    s = str(s)
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


# ---------------- docstring 解析 ----------------
def split_doc_sections(doc):
    """NumPy 风格 docstring -> {'desc': [行], 'sections': [(标题, [行])]}"""
    lines = doc.strip('\n').split('\n')
    desc, sections, cur_title, cur_body = [], [], None, []
    i = 0
    while i < len(lines):
        line = lines[i]
        nxt = lines[i + 1] if i + 1 < len(lines) else ''
        if line.strip() and re.fullmatch(r'-{3,}\s*', nxt.strip() or 'x') and nxt.strip():
            # 节标题（下一行全是 -）
            if cur_title:
                sections.append((cur_title, cur_body))
            cur_title, cur_body = line.strip(), []
            i += 2
            continue
        if cur_title is None:
            desc.append(line)
        else:
            cur_body.append(line)
        i += 1
    if cur_title:
        sections.append((cur_title, cur_body))
    return {'desc': desc, 'sections': sections}


def parse_param_blocks(body_lines):
    """参数节内容 -> [(name, type, default, [desc 行])]"""
    params, cur = [], None
    for line in body_lines:
        if not line.strip():
            continue
        indented = line.startswith('    ') or line.startswith('\t')
        if not indented:
            if cur:
                params.append(cur)
            cur = {'head': line.strip(), 'desc': []}
        elif cur is not None:
            cur['desc'].append(line.strip())
    if cur:
        params.append(cur)
    out = []
    for p in params:
        head = p['head']
        if head.endswith(':') and '=' not in head:
            # 裸参数名（如 **kwargs:）
            out.append((head.rstrip(':'), None, None, p['desc']))
            continue
        m = re.match(r'^(\S+)\s*=\s*(.*)$', head)
        if m:
            name = m.group(1)
            rest = m.group(2)
            dm = re.search(r'\.\s*Default\s+(.*?)\.\s*$', rest)
            if dm:
                typ = rest[:dm.start()].strip().rstrip('.').strip()
                default = dm.group(1).strip()
            else:
                typ = rest.strip().rstrip('.').strip()
                default = None
        else:
            # 冒号风格：name: type. 或 name: type
            m2 = re.match(r'^(\S+?)\s*:\s*(.+)$', head)
            if m2:
                name = m2.group(1)
                typ = m2.group(2).strip().rstrip('.').strip()
                default = None
            else:
                name = head.strip()
                typ, default = None, None
        out.append((name, typ, default, p['desc']))
    return out


def doc_to_body_html(doc, indent_desc=True):
    """完整 docstring -> 官网正文 HTML（描述 + Optional/Returns/Parameters 节）"""
    sec = split_doc_sections(doc or '')
    out = []
    for line in sec['desc']:
        t = line.strip()
        if t:
            # 描述里的 "xxx --> Type" 转成官网 code 风格
            m = re.split(r'-->|->', t, maxsplit=1)
            if len(m) == 2:
                out.append('<p>%s --> <code style="text-indent: 0em;">%s</code></p>'
                           % (esc(m[0].strip()), esc(m[1].strip())))
            else:
                out.append('<p>%s</p>' % esc(t))
    for title, body in sec['sections']:
        tnorm = title.lstrip('*').strip().lower()
        if tnorm in ('optional', 'parameters'):
            label = '**Optional:' if 'optional' in title.lower() else 'Parameters:'
            out.append('<p style="font-size: 120%%;color:#9298ED; font-weight: bold;">%s</p>' % label)
            for (name, typ, default, desc) in parse_param_blocks(body):
                if typ:
                    if default is not None:
                        out.append('<p style="margin-left: 2em;"><b>%s</b> = <code style="text-indent: 0em;">%s</code>.'
                                   ' <span style="color:#48566B;"> Default %s</span>. </p>'
                                   % (esc(name), esc(typ), esc(default)))
                    else:
                        out.append('<p style="margin-left: 2em;"><b>%s</b>: <code style="text-indent: 0em;">%s</code>. </p>'
                                   % (esc(name), esc(typ)))
                else:
                    out.append('<p style="margin-left: 2em;"><b>%s</b>: </p>' % esc(name))
                for d in desc:
                    out.append('<p style="margin-left: 4em;">%s</p>' % esc(d))
        elif tnorm == 'returns':
            out.append('<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>')
            text = ' '.join(x.strip() for x in body if x.strip()).strip()
            if text.lower().startswith('type:'):
                text = text[5:].strip()
            out.append('<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">%s</code>. </p>'
                       % esc(text.rstrip('.')))
    return out


# ---------------- AST 提取 ----------------
def get_init(node):
    for n in node.body:
        if isinstance(n, ast.FunctionDef) and n.name == '__init__':
            return n
    return None


def sig_parts(fn):
    """__init__ 参数（去 self）-> [(name, default_or_None)]"""
    a = fn.args
    names = [x.arg for x in a.args if x.arg != 'self']
    defaults = [ast.unparse(d) for d in a.defaults]
    offs = len(names) - len(defaults)
    out = []
    for i, n in enumerate(names):
        out.append((n, defaults[i - offs] if i >= offs else None))
    return out


def args_html(parts):
    segs = []
    for n, d in parts:
        if d is None:
            segs.append(esc(n))
        else:
            if d.startswith(("'", '"')) and not d.startswith(("'''", '"""')):
                d = '"%s"' % d[1:-1]
            segs.append('%s = <span style="color:#48566B">%s</span>' % (esc(n), d))
    return ', '.join(segs)


def infer_type(default):
    if default is None:
        return 'None'
    if default.startswith(("'", '"')):
        return 'str'
    if default in ('True', 'False'):
        return 'bool'
    if re.fullmatch(r'-?\d+', default):
        return 'int'
    if re.fullmatch(r'-?\d+\.\d*(e-?\d+)?', default):
        return 'float'
    return 'str'


def class_sig_html(module_path, name, parts, tag='[class]'):
    return ('<p style="font-size: 120%%;font-weight: bold;">gma.%s</p>'
            '<span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;">'
            '<span style="color: gray;font-size:90%%;">%s </span>'
            '<span style="color: #616AE5; font-weight: bold;font-size: 150%%;">%s</span>'
            '<span style="font-style: italic; color: black;font-size: 130%%;">(%s):</span></span>'
            % (module_path, tag, name, args_html(parts)))


def method_sig_html(name, parts, tag='[method]', size=125):
    return ('<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;">'
            '<span style="color: gray;font-size:90%%;">%s </span>'
            '<span style="color: #616AE5; font-weight: bold;font-size: %d%%;">.%s</span>'
            '<span style="font-style: italic; color: black;font-size: 120%%;">(%s):</span></span>'
            % (tag, size, name, args_html(parts)))


def prop_html(name, doc):
    head = ('<span style=""><span style="color: gray;font-size:90%%;">[property] </span>'
            '<span style="color: #616AE5; font-weight: bold;font-size: 125%%;">.%s</span>'
            '<span style=""></span></span>' % name)
    text = (doc or '').strip()
    parts = re.split(r'-->|->', text, maxsplit=1)
    if len(parts) == 2:
        body = ('<p style="margin-left: 2em;">%s --> <code style="text-indent: 0em;">%s</code></p>'
                % (esc(parts[0].strip()), esc(parts[1].strip())))
    else:
        body = '<p style="margin-left: 2em;">%s</p>' % esc(text)
    return head + '\n\n' + body


def front(title):
    return '---\ntitle: %s\ndate: %s\n---\n\n' % (title, DATE)


def is_property(fn):
    for d in fn.decorator_list:
        if isinstance(d, ast.Name) and d.id == 'property':
            return True
        if isinstance(d, ast.Attribute) and d.attr == 'property':
            return True
    return False


def class_members(node):
    methods, props = [], []
    for n in node.body:
        if isinstance(n, ast.FunctionDef):
            if n.name.startswith('_'):
                continue
            (props if is_property(n) else methods).append(n)
    return methods, props


def write(path, content):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    io.open(full, 'w', encoding='utf-8', newline='\n').write(content)
    print('  write', path, len(content))


# ---------------- crs ----------------
def gen_crs(tree):
    classes = {n.name: n for n in tree.body if isinstance(n, ast.ClassDef)}
    crs_cls = classes['CoordinateReferenceSystem']

    init = get_init(crs_cls)
    doc = ast.get_docstring(init) or ''
    sec = split_doc_sections(doc)
    desc_first = next((x.strip() for x in sec['desc'] if x.strip()), 'Coordinate reference system object.')

    # CRS 自身参数 docstring 缺失 -> 从签名默认值生成最小 Optional
    parts = sig_parts(init)
    opt_html = ['<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>']
    for n, d in parts:
        opt_html.append('<p style="margin-left: 2em;"><b>%s</b> = <code style="text-indent: 0em;">%s</code>.'
                        ' <span style="color:#48566B;"> Default %s</span>. </p>'
                        % (esc(n), infer_type(d), esc(d or 'None')))
    opt_html.append('<p style="margin-left: 4em;">Coordinate system. Can be EPSG, WKT, Proj4 and other types'
                    ' of coordinate characters, or a CoordinateReferenceSystem object.</p>')

    methods, props = class_members(crs_cls)

    h = [front('CoordinateReferenceSystem')]
    h.append(class_sig_html('crs.CoordinateReferenceSystem', 'CoordinateReferenceSystem', parts))
    h.append('')
    h.append('<p>%s</p>' % esc(desc_first.rstrip('.')))
    h.extend(opt_html)
    if methods:
        h.append('\n## Method\n')
        for m in methods:
            h.append('### %s' % m.name)
            h.append(method_sig_html(m.name, sig_parts(m)))
            h.append('')
            h.extend(doc_to_body_html(ast.get_docstring(m)))
            h.append('')
    if props:
        h.append('\n## Property\n')
        for pr in props:
            h.append('### %s' % pr.name)
            h.append(prop_html(pr.name, ast.get_docstring(pr)))
            h.append('')
    write('crs/CoordinateReferenceSystem.md', '\n'.join(h))

    # GCS / PCS：docstring 自带完整 Optional/Returns
    for cls_name, desc_default in (('GeographicCoordinateSystem', 'geographic coordinate system'),
                                   ('ProjectedCoordinateSystem', 'projected coordinate system')):
        node = classes[cls_name]
        init = get_init(node)
        doc = ast.get_docstring(init) or ''
        s2 = split_doc_sections(doc)
        d_first = next((x.strip() for x in s2['desc'] if x.strip()), desc_default)
        h = [front(cls_name)]
        h.append(class_sig_html('crs.' + cls_name, cls_name, sig_parts(init)))
        h.append('')
        h.append('<p>%s</p>' % esc(d_first))
        body = doc_to_body_html(doc)
        h.extend(body)
        h.append('\n<p>Inherits all properties and methods from'
                 ' <a href="/docs/UserGuide/crs/CoordinateReferenceSystem.html">CoordinateReferenceSystem</a>.</p>')
        write('crs/%s.md' % cls_name, '\n'.join(h))

    # Ellipsoid / Datum
    for cls_name in ('Ellipsoid', 'Datum'):
        node = classes[cls_name]
        init = get_init(node)
        doc = ast.get_docstring(init) or ''
        s2 = split_doc_sections(doc)
        d_first = next((x.strip() for x in s2['desc'] if x.strip()), cls_name + ' object.')
        parts = sig_parts(init)
        h = [front(cls_name)]
        h.append(class_sig_html('crs.' + cls_name, cls_name, parts))
        h.append('')
        h.append('<p>%s</p>' % esc(d_first.rstrip('.')))
        body = doc_to_body_html(doc)
        if not any('Optional' in x for x in body):
            h.append('<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>')
            for n, d in parts:
                h.append('<p style="margin-left: 2em;"><b>%s</b> = <code style="text-indent: 0em;">%s</code>.'
                         ' <span style="color:#48566B;"> Default %s</span>. </p>'
                         % (esc(n), infer_type(d), esc(d or 'None')))
        h.extend([x for x in body if 'Optional' in x or 'margin-left' in x])
        _, props = class_members(node)
        if props:
            h.append('\n## Property\n')
            for pr in props:
                h.append('### %s' % pr.name)
                h.append(prop_html(pr.name, ast.get_docstring(pr)))
                h.append('')
        if cls_name == 'Datum':
            h.append('\n<p>Inherits all properties from'
                     ' <a href="/docs/UserGuide/crs/Ellipsoid.html">Ellipsoid</a>.</p>')
        write('crs/%s.md' % cls_name, '\n'.join(h))

    # ProjMethods 34 个投影子页
    pm = classes['ProjMethods']
    subs = [n for n in pm.body if isinstance(n, ast.ClassDef)]
    h = [front('ProjMethods')]
    h.append('<p style="font-size: 120%%;font-weight: bold;">gma.crs.ProjMethods</p>')
    h.append('<p>34 default projection methods. Each projection method is a class of ProjMethods.'
             ' Example: <code>ProjMethods.AlbersConicEqualArea()</code>.</p>')
    write('crs/ProjMethods/_index_note.md', '\n'.join(h)) if False else None
    for sub in subs:
        init = get_init(sub)
        doc = ast.get_docstring(sub) or ast.get_docstring(init) or ''
        parts = sig_parts(init)
        h = [front(sub.name)]
        h.append(class_sig_html('crs.ProjMethods.' + sub.name, sub.name, parts))
        h.append('')
        h.extend(doc_to_body_html(doc))
        write('crs/ProjMethods/%s.md' % sub.name, '\n'.join(h))
    print('  ProjMethods subpages:', len(subs))

    # crs/README.md（Start）
    rows = []
    intros = {
        'CoordinateReferenceSystem': 'Coordinate reference system object.',
        'Datum': 'Datum object.',
        'Ellipsoid': 'Ellipsoid object.',
        'GeographicCoordinateSystem': 'Create a geographic coordinate system!',
        'ProjectedCoordinateSystem': 'Create a projected coordinate system!',
    }
    order = ['CoordinateReferenceSystem', 'Datum', 'Ellipsoid',
             'GeographicCoordinateSystem', 'ProjectedCoordinateSystem']
    for i, n in enumerate(order, 1):
        rows.append('|%d|[crs.%s](/docs/UserGuide/crs/%s.html)|class|%s|' % (i, n, n, intros[n]))
    rows.append('|6|[crs.ProjMethods](/docs/UserGuide/crs/ProjMethods/AlbersConicEqualArea.html)|class|'
                '34 default projection methods.|')
    rd = [front('Contents'),
          'All items(functions/classes/consts) in this module are as follows:',
          '|No.|item|type|introduce|', '|---|---|---|---|']
    rd.extend(rows)
    write('crs/README.md', '\n'.join(rd) + '\n')


# ---------------- const ----------------
def gen_const():
    src = io.open(SRC_CONST, encoding='utf-8').read()
    tree = ast.parse(src)
    groups = [('FiDT_', 'Field data type.', []),
              ('GeDT_', 'Geometry type.', []),
              ('RaDT_', 'Raster data type.', []),
              ('RspM_', 'Resample method.', [])]
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name):
                    for pre, intro, lst in groups:
                        if t.id.startswith(pre):
                            lst.append((t.id, intro))
    rows = []
    i = 1
    for pre, intro, lst in groups:
        for n, it in lst:
            it2 = it
            if '_3D' in n:
                it2 = it.replace('type.', 'type (3D).').replace('Geometry type.', '3D geometry type.')
            rows.append('|%d|%s|const|%s|' % (i, n, it2))
            i += 1
    c = [front('Contents'),
         'All constants in this module are as follows:',
         '|No.|item|type|introduce|', '|---|---|---|---|']
    c.extend(rows)
    write('const/README.md', '\n'.join(c) + '\n')
    print('  const items:', i - 1)


def main():
    src = io.open(SRC_CRS, encoding='utf-8').read()
    gen_crs(ast.parse(src))
    gen_const()


if __name__ == '__main__':
    main()
