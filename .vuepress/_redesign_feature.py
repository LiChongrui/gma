import sys
sys.path.insert(0, r'D:\github\gma\.vuepress\_gma341')
from gma import gio                      # gma 必须最先导入（matplotlib/hashlib 的 DLL 会破坏 _core）
import io, os, re, shutil, tempfile
from contextlib import redirect_stdout
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ---------- 真实样例数据: 拷贝到临时工作目录, 文档里只写裸文件名 ----------
SRC = r'D:\BaiduNetdiskDownload\ne\第3章'
WORK = tempfile.mkdtemp(prefix='feature_doc_')
for f in os.listdir(SRC):
    shutil.copy(os.path.join(SRC, f), os.path.join(WORK, f))
os.chdir(WORK)

MD = r'D:\github\gma\docs\UserGuide\gio\Feature.md'
BAK = r'D:\github\gma\.vuepress\_feature_before_redesign.md'
IMGDIR = r'D:\github\gma\.vuepress\public\img\gio'
os.makedirs(IMGDIR, exist_ok=True)

# ---------- 类示例底座 ----------
BASE_SETUP = '''from gma import gio

ly = gio.open_vector('Australia.shp')
ft = ly.get_feature(0)                          # Western Australia

print('fid     :', ft.fid)
print('name    :', ft.fields['name'])
print('geometry:', ft.geom.gtype)

# Build a new Feature from the geometry and fields of an existing one
new_ft = gio.Feature(geom=ft.geom, values=list(ft.fields.values()), ftypes=ft.ftypes)
print('new ft  :', new_ft.fid, new_ft.fields['name'], repr(new_ft.crs))'''

BASE_RESULT = '''fid     : 0
name    : Western Australia
geometry: MultiPolygon
new ft  : -1 Western Australia <CoordinateReferenceSystem:WGS 84>'''

# ---------- 5 个方法示例（每个都自包含, 用新打开的 layer 避开 get_feature 的对象缓存） ----------
EXAMPLES = {
'copy': '''from gma import gio

ft = gio.open_vector('Australia.shp').get_feature(0)
cp = ft.copy()
cp.set_fid(999)

print('original:', ft.fid, ft.fields['name'])
print('copy    :', cp.fid, cp.fields['name'])
print('same object:', cp is ft)''',

'plot': '''import matplotlib.pyplot as plt
from gma import gio

ly = gio.open_vector('Australia.shp')
ft = ly.get_feature(0)

fig, ax = plt.subplots(figsize=(6, 4.5))
ly.plot(ax=ax, facecolor='none', edgecolor='gray')                 # all features
ax = ft.plot(ax=ax, facecolor='none', edgecolor='red', linewidth=1.5)  # highlight one

print(type(ax).__name__)''',

'set_fid': '''from gma import gio

ft = gio.open_vector('Australia.shp').get_feature(0)

print('Before:', ft.fid)
ft.set_fid(999)
print('After :', ft.fid)''',

'set_geom': '''from gma import gio

ly = gio.open_vector('Australia.shp')
ft = ly.get_feature(0)                  # Western Australia
new_geom = ly.get_feature(1).geom       # Northern Territory

print('Before:', ft.fields['name'], tuple(round(v, 2) for v in ft.geom.bounds))
ft.set_geom(new_geom)
print('After :', ft.fields['name'], tuple(round(v, 2) for v in ft.geom.bounds))''',

'update': '''from gma import gio

ly = gio.open_vector('Australia.shp')
ft = ly.get_feature(0)                  # Western Australia
other = ly.get_feature(2)               # South Australia

print('Before:', ft.fields['name'], tuple(round(v, 2) for v in ft.geom.bounds))
ft.update(other)
print('After :', ft.fields['name'], tuple(round(v, 2) for v in ft.geom.bounds))
print('fid   :', ft.fid)''',
}

# ---------- 5 个属性示例 ----------
PROPERTIES = {
'crs': '''from gma import gio

ft = gio.open_vector('Australia.shp').get_feature(0)

print(ft.crs)''',

'fid': '''from gma import gio

ft = gio.open_vector('Australia.shp').get_feature(0)

print(ft.fid)''',

'fields': '''from gma import gio

ft = gio.open_vector('Australia.shp').get_feature(0)

print('number of fields:', len(ft.fields))
for key in ('name', 'iso_3166_2', 'type', 'scalerank'):
    print(key, ':', ft.fields[key])''',

'ftypes': '''from gma import gio

ft = gio.open_vector('Australia.shp').get_feature(0)

print('number of field types:', len(ft.ftypes.names))
print('first five names     :', ft.ftypes.names[:5])
print('first field type     :', ft.ftypes[0])''',

'geom': '''from gma import gio

ft = gio.open_vector('Australia.shp').get_feature(0)

print('type  :', ft.geom.gtype)
print('bounds:', tuple(round(v, 2) for v in ft.geom.bounds))
print('area  :', round(ft.geom.get_area(), 2))''',
}

# ---------- Returns（实测返回类型） ----------
RETURNS = {
'copy':     ('Feature', 'An independent copy of this feature.'),
'plot':     ('Axes',    'The matplotlib axes with the feature geometry plotted on it.'),
'set_fid':  ('None',    'Modify the feature identifier in place.'),
'set_geom': ('None',    'Replace the geometry in place; field values are unchanged.'),
'update':   ('None',    'Overwrite geometry and field values in place. The fid is not copied (-1).'),
}

# ---------- 3 张示意图 ----------
IMAGES = {
'plot':     'Feature 0 (Western Australia) highlighted among all features',
'set_geom': 'Before / after replacing the geometry',
'update':   'Before / after overwriting geometry and fields',
}

def exec_example(code):
    ns = {}
    exec(code, ns)
    return ns

def capture(code):
    buf = io.StringIO()
    with redirect_stdout(buf):
        ns = exec_example(code)
    return ns, buf.getvalue().rstrip('\n')

results, prop_results = {}, {}
for name, code in EXAMPLES.items():
    ns, results[name] = capture(code)
    print(f'--- {name} ---'); print(results[name]); print()

for name, code in PROPERTIES.items():
    ns, prop_results[name] = capture(code)
    print(f'--- prop:{name} ---'); print(prop_results[name]); print()

# 底座结果也实测一次, 保证文档里的输出是真值
_, base_out = capture(BASE_SETUP)
assert base_out == BASE_RESULT, f'base output mismatch:\n{base_out}'

LBL = '<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>'
EX_LBL = '<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Example:</p>'

def returns_html(name):
    typ, desc = RETURNS[name]
    return [LBL,
            f'<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">{typ}</code>. </p>',
            f'<p style="margin-left: 4em;">{desc}</p>']

def example_block(code, output, name=None):
    s = EX_LBL + '\n\n```python\n' + code + '\n```\n\n```text\n' + output + '\n```'
    if name in IMAGES:
        s += f'\n\n![{IMAGES[name]}](/img/gio/feature_{name}.png)'
    return s

# ---------- 图: 全部由 Feature.plot / Layer.plot 直接出图 ----------
def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(IMGDIR, f'feature_{name}.png'), dpi=110)
    plt.close(fig)
    print(f'[IMG] feature_{name}.png')

def frame(ax, ly, ft, color, title, lw=1.5):
    ly.plot(ax=ax, facecolor='none', edgecolor='gray')
    ft.plot(ax=ax, facecolor='none', edgecolor=color, linewidth=lw)
    ax.set_xlim(111, 155); ax.set_ylim(-45, -8)
    ax.set_title(title, fontsize=10)

def img_plot():
    ly = gio.open_vector('Australia.shp')
    ft = ly.get_feature(0)
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.5), dpi=110)
    ly.plot(ax=axs[0], facecolor='none', edgecolor='gray')
    axs[0].set_title('Before: all features', fontsize=10)
    frame(axs[1], ly, ft, 'red', 'After: feature 0 highlighted')
    for ax in axs:
        ax.set_xlim(111, 155); ax.set_ylim(-45, -8)
    save(fig, 'plot')

def img_set_geom():
    ly = gio.open_vector('Australia.shp')
    ft = ly.get_feature(0)
    src_wa = ft.copy()
    ft.set_geom(ly.get_feature(1).geom)
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.5), dpi=110)
    frame(axs[0], ly, src_wa, 'tab:blue', 'Before: Western Australia')
    frame(axs[1], ly, ft, 'red', 'After: geometry of Northern Territory')
    save(fig, 'set_geom')

def img_update():
    ly = gio.open_vector('Australia.shp')
    ft = ly.get_feature(0)
    src_wa = ft.copy()
    ft.update(ly.get_feature(2))
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.5), dpi=110)
    frame(axs[0], ly, src_wa, 'tab:blue', 'Before: Western Australia')
    frame(axs[1], ly, ft, 'red', 'After: South Australia')
    save(fig, 'update')

img_plot(); img_set_geom(); img_update()

# ---------- 重建 Feature.md（幂等） ----------
shutil.copy(MD, BAK) if not os.path.exists(BAK) else None
lines = open(MD, encoding='utf-8').read().splitlines()
idx_method = next(i for i, l in enumerate(lines) if l.strip() == '## Method')
idx_property = next(i for i, l in enumerate(lines) if l.strip() == '## Property')

def clean_tail(sec):
    m = re.search(r'\n*<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Example:</p>.*', sec, re.S)
    return sec[:m.start()] if m else sec

def split_sections(body):
    starts = [i for i, l in enumerate(body) if l.startswith('### ')]
    out = []
    for k, st in enumerate(starts):
        name = re.match(r'### (\w+)', body[st]).group(1)
        end = starts[k + 1] if k + 1 < len(starts) else len(body)
        out.append((name, body[st:end]))
    return out

def process_method(sec_lines, name):
    sec = clean_tail('\n'.join(sec_lines))
    m = re.search(r'\n*<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>.*?(?=\n\n|\n###|\Z)', sec, re.S)
    if m:
        sec = sec[:m.start()] + sec[m.end():]
    return sec.rstrip('\n') + '\n\n' + '\n'.join(returns_html(name)) + '\n\n' + example_block(EXAMPLES[name], results[name], name)

def process_property(sec_lines, name):
    sec = clean_tail('\n'.join(sec_lines)).rstrip('\n')
    return sec + '\n\n' + example_block(PROPERTIES[name], prop_results[name])

head = '\n'.join(lines[:idx_method]).rstrip('\n')
head = re.sub(r'\n*## Example\n.*\Z', '', head, flags=re.S)
method_secs = [process_method(sec, n) for n, sec in split_sections(lines[idx_method + 1:idx_property])]
prop_lines = lines[idx_property:]
old_tail = next((i for i, l in enumerate(prop_lines) if l.strip() == '## Example'), None)
if old_tail is not None:
    prop_lines = prop_lines[:old_tail]          # 丢掉原页尾的类示例（已上移）
prop_secs = [process_property(sec, n) for n, sec in split_sections(prop_lines)]
base_block = '## Example\n\n```python\n' + BASE_SETUP + '\n```\n\n```text\n' + base_out + '\n```\n'

new_md = (head + '\n\n' + base_block + '\n## Method\n\n' + '\n\n\n'.join(method_secs)
          + '\n\n\n## Property\n\n' + '\n\n\n'.join(prop_secs) + '\n')
open(MD, 'w', encoding='utf-8', newline='\n').write(new_md)

n_ex = new_md.count('>Example:</p>')
n_ret = new_md.count('>Returns:</p>')
n_img = new_md.count('](/img/gio/feature_')
print(f'\n[OK] Example labels: {n_ex} (expect 10) | Returns: {n_ret} (expect 5) | images: {n_img} (expect 3)')
print(f'lines: {len(lines)} -> {len(new_md.splitlines())}')
