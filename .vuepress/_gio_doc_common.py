"""gio 文档页再设计的公共流程：真实样例数据 + 实测输出 + 幂等重建。
每个页面脚本只需提供配置并调用 run(cfg)。gma 必须第一个导入。"""
import sys
sys.path.insert(0, r'D:\github\gma\.vuepress\_gma341')
from gma import gio
import io, os, re, shutil, tempfile
from contextlib import redirect_stdout
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SRC = r'D:\BaiduNetdiskDownload\ne\第3章'
WORK = tempfile.mkdtemp(prefix='giodoc_')
for _f in os.listdir(SRC):
    shutil.copy(os.path.join(SRC, _f), os.path.join(WORK, _f))
os.chdir(WORK)

DOCS = r'D:\github\gma\docs\UserGuide\gio'
IMGDIR = r'D:\github\gma\.vuepress\public\img\gio'
os.makedirs(IMGDIR, exist_ok=True)

LBL = '<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>'
EX_LBL = '<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Example:</p>'

def prepare_extra(files):
    """拷贝第3章以外的样例文件到工作目录（如 ne/NewGDB.gpkg）。"""
    for src, dst in files:
        shutil.copy(src, os.path.join(WORK, dst))

def capture(code):
    """每个示例在独立子进程中执行：gma 的对象累积会导致后续调用段错误，
    隔离后单个示例的崩溃不会影响其他示例，也不会中断文档生成。"""
    import subprocess
    head = ("import sys, os\nsys.path.insert(0, r'D:\\github\\gma\\.vuepress\\_gma341')\n"
            "from gma import gio\nimport numpy as np\n"
            "import matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\n")
    # 部分 Layer 方法会写回打开的文件；每个示例前恢复矢量数据，避免互相污染
    for _f in ('Australia.shp', 'Australia.dbf', 'Australia.shx', 'Australia.prj', 'Australia.cpg',
               'NewGDB.gpkg'):
        _src = os.path.join(SRC, _f) if os.path.exists(os.path.join(SRC, _f)) else os.path.join(r'D:\BaiduNetdiskDownload\ne', _f)
        if os.path.exists(_src):
            shutil.copy(_src, os.path.join(WORK, _f))
    script = os.path.join(WORK, '_capture_one.py')
    with open(script, 'w', encoding='utf-8') as f:
        f.write(head + code + '\n')
    try:
        p = subprocess.run([sys.executable, '-u', script], cwd=WORK,
                           capture_output=True, text=True, timeout=180)
    except subprocess.TimeoutExpired:
        return {}, '[ERROR] timeout (180s)'
    if p.returncode != 0:
        tail = (p.stderr or '').strip().splitlines()[-1:] or [f'exit {p.returncode}']
        return {}, '[ERROR] ' + tail[0][:160]
    return {}, p.stdout.rstrip('\n')

def run(cfg):
    """cfg keys: page, base, base_result(None=实测), examples, properties,
    returns, images, img_funcs(list of callables), backup(optional)."""
    page = cfg['page']
    MD = os.path.join(DOCS, page + '.md')
    BAK = cfg.get('backup', os.path.join(r'D:\github\gma\.vuepress', f'_{page}_before_redesign.md'))
    examples, properties = cfg['examples'], cfg['properties']
    returns, images = cfg.get('returns', {}), cfg.get('images', {})

    forced = cfg.get('forced_results', {})
    results, prop_results = {}, {}
    for name, code in examples.items():
        if name in forced:
            results[name] = forced[name]          # 已知会使进程崩溃的调用不执行
        else:
            try:
                _, out = capture(code)
                results[name] = out
            except Exception as e:
                results[name] = f'[ERROR] {type(e).__name__}: {e}'
        print(f'--- {name} ---\n{results[name]}\n')
    for name, code in properties.items():
        try:
            _, out = capture(code)
            prop_results[name] = out
        except Exception as e:
            prop_results[name] = f'[ERROR] {type(e).__name__}: {e}'
        print(f'--- prop:{name} ---\n{out}\n')
    if cfg.get('base_result') is None:
        _, base_out = capture(cfg['base'])
    else:
        base_out = cfg['base_result']

    if cfg.get('dry_run'):
        print('[DRY RUN] no files written')
        return

    for fn in cfg.get('img_funcs', []):
        fn()

    if not os.path.exists(BAK):
        shutil.copy(MD, BAK)
    lines = open(MD, encoding='utf-8').read().splitlines()
    idx_method = next((i for i, l in enumerate(lines) if l.strip() == '## Method'), None)
    idx_property = next((i for i, l in enumerate(lines) if l.strip() == '## Property'), None)

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

    def example_block(code, output, name=None):
        s = EX_LBL + '\n\n```python\n' + code + '\n```\n\n```text\n' + output + '\n```'
        if name in images:
            s += f'\n\n![{images[name]}](/img/gio/{page.lower()}_{name}.png)'
        return s

    def process_method(sec_lines, name):
        sec = clean_tail('\n'.join(sec_lines))
        m = re.search(r'\n*<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>.*?(?=\n\n|\n###|\Z)', sec, re.S)
        if m:
            sec = sec[:m.start()] + sec[m.end():]
        sec = sec.rstrip('\n')
        out = sec
        if name in returns:
            typ, desc = returns[name]
            out += ('\n\n' + LBL + f'\n<p style="margin-left: 2em;"><b>Type</b>: '
                    f'<code style="text-indent: 0em;">{typ}</code>. </p>'
                    f'\n<p style="margin-left: 4em;">{desc}</p>')
        return out + '\n\n' + example_block(examples[name], results[name], name)

    def process_property(sec_lines, name):
        return clean_tail('\n'.join(sec_lines)).rstrip('\n') + '\n\n' + example_block(properties[name], prop_results[name])

    # 头部：截掉已有底座 Example（可能有多个，只保留第一个之前的说明）
    head = '\n'.join(lines[:idx_method])
    head = re.sub(r'\n*## Example\n.*\Z', '', head, flags=re.S).rstrip('\n')

    method_secs = [process_method(sec, n) for n, sec in split_sections(lines[idx_method + 1:idx_property])]
    prop_lines = lines[idx_property:]
    old_tail = next((i for i, l in enumerate(prop_lines) if l.strip() == '## Example'), None)
    if old_tail is not None:
        prop_lines = prop_lines[:old_tail]
    prop_secs = [process_property(sec, n) for n, sec in split_sections(prop_lines)]

    base_block = '## Example\n\n```python\n' + cfg['base'] + '\n```\n\n```text\n' + base_out + '\n```\n'
    parts = [head, '\n\n', base_block]
    if method_secs:
        parts += ['\n## Method\n\n', '\n\n\n'.join(method_secs)]
    if prop_secs:
        parts += ['\n\n\n## Property\n\n', '\n\n\n'.join(prop_secs)]
    new_md = ''.join(parts) + '\n'
    open(MD, 'w', encoding='utf-8', newline='\n').write(new_md)

    n_ex, n_ret, n_img = (new_md.count(EX_LBL), new_md.count(LBL),
                         new_md.count(f'](/img/gio/{page.lower()}_'))
    print(f'\n[OK] {page}: Example {n_ex}/{len(examples)+len(properties)} | '
          f'Returns {n_ret}/{len(returns)} | images {n_img}/{len(images)} | '
          f'lines {len(lines)} -> {len(new_md.splitlines())}')
    return new_md

def save(fig, page, name):
    fig.tight_layout()
    p = os.path.join(IMGDIR, f'{page.lower()}_{name}.png')
    fig.savefig(p, dpi=110)
    plt.close(fig)
    print(f'[IMG] {os.path.basename(p)}')
