# -*- coding: utf-8 -*-
"""Dataset.md 示例与返回值重设计 v3 (真实样例数据版):
  样例数据: D:\\BaiduNetdiskDownload\\ne\\第3章 (HYP_50M_SR_W.tif + Australia.shp)
  1) 类示例底座 = open_raster 世界晕渲 + clip Australia, 全页共用
  2) 24 个方法示例真实代码, 输出实测捕获, 无 Result: 标签
  3) 15 个 Property 各加 Example(实测捕获)
  4) 9 个视觉方法附前后示意图 -> .vuepress/public/img/gio/dataset_*.png
     (全部 ds.plot()/res.plot() 直出, 3 波段渲染 = RGB 合成, 单波段 = viridis)
  5) Returns 段补全/增强
注意: gma 必须先于 matplotlib 导入 (hashlib/plt 先导会破坏 _core DLL 加载)。
幂等: 可对已处理过的文件重复运行。
"""
import os, sys, io, shutil, re, gc
from contextlib import redirect_stdout

sys.path.insert(0, r'D:\github\gma\.vuepress\_gma341')
from gma import gio
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

MD = r'D:\github\gma\docs\UserGuide\gio\Dataset.md'
BAK = r'D:\github\gma\.vuepress\_dataset_redesign_backup.md'
IMGDIR = r'D:\github\gma\.vuepress\public\img\gio'
SRC_DATA = r'D:\BaiduNetdiskDownload\ne\第3章'

# ---------- 实测环境: 拷贝样例数据到临时目录并切换(文档示例用相对文件名) ----------
WORK = os.path.join(os.environ['TEMP'], '_gma_ds_redesign')
shutil.rmtree(WORK, ignore_errors=True)
os.makedirs(WORK, exist_ok=True)
for f in ('HYP_50M_SR_W.tif', 'Australia.shp', 'Australia.dbf', 'Australia.shx',
          'Australia.prj', 'Australia.cpg'):
    shutil.copy(os.path.join(SRC_DATA, f), os.path.join(WORK, f))
os.chdir(WORK)

# ---------- 共用底座(文档中的类示例, 同时是每个示例的 exec 前置) ----------
BASE_SETUP = '''import numpy as np
from gma import gio

# Open the Natural Earth shaded relief raster (sample data)
ds = gio.open_raster('HYP_50M_SR_W.tif')

# Clip it by Australia for the following examples
ly = gio.open_vector('Australia.shp')
ds = ds.clip(ly)

print(ds.shape)
print(ds.bounds)

# All following method examples are based on this dataset'''

BASE_RESULT = '''(3, 1006, 1220)
(112.93333333330409, -43.599999999986636, 153.59999999996668, -10.066666666656673)'''

# ---------- 24 个方法示例(真实数据) ----------
EXAMPLES = {
'algebraic': '''# RGB values of a pixel before the operation
print(ds.to_numpy()[:, 500, 600])

# Convert to Float32 first to avoid uint8 overflow, then convert to grayscale
res = ds.to_dtype('float32').algebraic(lambda in_ar: (in_ar[0] + in_ar[1] + in_ar[2]) / 3)

# Grayscale value after the operation
print(res.to_numpy()[:, 500, 600])''',

'clip': '''# The sample raster (global) and the clip layer
world = gio.open_raster('HYP_50M_SR_W.tif')
ly = gio.open_vector('Australia.shp')

res = world.clip(ly)

print(world.shape, '->', res.shape)
print(res.bounds)''',

'extent': '''res = ds.extent()

print(res.gtype, res.bounds)''',

'gen_lonlat': '''res = ds.gen_lonlat()

print(res.shape)
print(res.to_numpy()[0, 500, :3])  # Band 1: longitude
print(res.to_numpy()[1, 500, :3])  # Band 2: latitude''',

'get_palette': '''# Palette is only supported for a single Byte/UInt16 band
ar = ds.to_numpy()[0]  # Band 1 of the dataset
ds_b = gio.Dataset(data=ar, crs=ds.crs, geo_transform=ds.geo_transform)
ds_b.set_nodata(255)

res = ds_b.reclassify({100: 20, 150: 128, 240: 230}, method='Range').to_dtype('Byte')
res.set_palette({20: (49, 54, 149, 255), 128: (255, 201, 101, 255), 230: (215, 90, 60, 255)})

print(type(res.get_palette()).__name__)''',

'isopleth': '''res = ds.isopleth(interval=100)

print(res.gtype, len(res))''',

'plot': '''import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax = ds.plot(ax=ax)

print(type(ax).__name__)''',

'reclassify': '''# Raw values of a pixel (RGB)
print(ds.to_numpy()[:, 500, 600])

res = ds.reclassify({100: 20, 150: 128, 240: 230}, method='Range')

print(ds.dtype, '->', res.dtype)
print(res.to_numpy()[:, 500, 600])''',

'resample': '''res = ds.resample(0.2)

print(ds.shape, '->', res.shape)
print(ds.resolution, '->', res.resolution)''',

'set_crs': '''ds.set_crs('EPSG:4326')

print(ds.crs)''',

'set_gcps': '''gcps = [(113.0, -12.0, 0.0, 0.0, 0.0, 'GCP1', '1'),
        (115.0, -14.0, 3.0, 3.0, 0.0, 'GCP2', '2')]

ds.set_gcps(gcps, crs='EPSG:4326')

print(ds.gcps)''',

'set_geo_transform': '''print('Before:', ds.bounds)

ds.set_geo_transform((112, 0.1, 0, -10, 0, -0.1))

print('After :', ds.bounds)''',

'set_metadata': '''ds.set_metadata({'': {'author': 'gma'}})

print(ds.metadata)''',

'set_nodata': '''print('Before:', ds.nodata)

ds.set_nodata(0)

print('After :', ds.nodata)''',

'set_palette': '''# Palette is only supported for a single Byte/UInt16 band
ar = ds.to_numpy()[0]  # Band 1 of the dataset
ds_b = gio.Dataset(data=ar, crs=ds.crs, geo_transform=ds.geo_transform)
ds_b.set_nodata(255)

res = ds_b.reclassify({100: 20, 150: 128, 240: 230}, method='Range').to_dtype('Byte')
res.set_palette({20: (49, 54, 149, 255), 128: (255, 201, 101, 255), 230: (215, 90, 60, 255)})

print(type(res.get_palette()).__name__)''',

'set_statistics': '''# Set band statistics as (vmin, vmax, vmean, vstddev) tuples
ds.set_statistics([(82, 233, 174, 19)])

# The stats property returns automatically computed statistics
print(ds.stats)''',

'shift': '''print('Before:', ds.bounds)

ds.shift(0.5)

print('After :', ds.bounds)''',

'to_bytearray': '''ba = ds.to_bytearray()

print(type(ba).__name__, len(ba))''',

'to_crs': '''res = ds.to_crs('EPSG:3857')

print(res.crs)
print(res.bounds)''',

'to_dtype': '''res = ds.to_dtype('float32')

print(ds.dtype, '->', res.dtype)''',

'to_file': '''ds.to_file('result.tif')

# Reopen the saved file to verify
ds2 = gio.open_raster('result.tif')

print(ds2.shape)''',

'to_layer': '''res = ds.reclassify({100: 20, 150: 128, 240: 230}, method='Range')
lay = res.to_layer()

print(lay.gtype, len(lay))''',

'to_numpy': '''ar = ds.to_numpy()

print(ar.shape, ar.dtype)
print(ar[0, 500, :3])''',

'write_array': '''print('Before:', ds.to_numpy()[0, 500, 600])

ds.write_array(np.zeros(ds.shape, dtype='uint8'))

print('After :', ds.to_numpy()[0, 500, 600])''',
}

# ---------- 15 个属性示例 ----------
PROPERTIES = {
'blocks':         "print(ds.blocks)",
'bounds':         "print(ds.bounds)",
'compression': '''# The clipped in-memory Dataset has no compression.
# Open the original file to get its compression
ds_f = gio.open_raster('HYP_50M_SR_W.tif')

print(ds_f.compression)''',
'crs':            "print(ds.crs)",
'driver':         "print(ds.driver)",
'dtype':          "print(ds.dtype)",
'gcps':           "print(ds.gcps)",
'geo_transform':  "print(ds.geo_transform)",
'link': '''# In-memory Datasets get a random link.
# Open a file to get its real link (the path of the file)
ds_f = gio.open_raster('HYP_50M_SR_W.tif')

print(ds_f.link)''',
'metadata':       "print(ds.metadata)",
'name': '''# In-memory Datasets get a random name.
# Open a file to get its real name
ds_f = gio.open_raster('HYP_50M_SR_W.tif')

print(ds_f.name)''',
'nodata':         "print(ds.nodata)",
'resolution':     "print(ds.resolution)",
'shape':          "print(ds.shape)",
'stats': '''for band, st in ds.stats.items():
    print(band, st)''',
}

# ---------- Returns 段 ----------
RETURNS = {
'algebraic':        ('Dataset', 'A new Dataset after the operation. The original dataset is unchanged.'),
'clip':             ('Dataset', 'A new Dataset clipped by the layer. The original dataset is unchanged.'),
'extent':           ('Layer', 'A new Layer of the dataset extent (bounding rectangle).'),
'gen_lonlat':       ('Dataset', 'A new Dataset with two bands: Band 1 is longitude, Band 2 is latitude.'),
'get_palette':      ('matplotlib', 'colors.ListedColormap or None', 'The palette (color table) of the band. None if the band has no palette.'),
'isopleth':         ('Layer', 'A new Layer of isopleths (MultiLineString).'),
'plot':             ('matplotlib', '~.GeoAxes', 'The axes with the plotted dataset. A new GeoAxes is created if ax is None; otherwise, the provided ax is returned.'),
'reclassify':       ('Dataset', 'A new Dataset with remapped values (Float64). The original dataset is unchanged.'),
'resample':         ('Dataset', 'A new Dataset with the target resolution. The original dataset is unchanged.'),
'set_crs':          ('None', 'Modify in place.'),
'set_gcps':         ('None', 'Modify in place.'),
'set_geo_transform':('None', 'Modify in place.'),
'set_metadata':     ('None', 'Modify in place.'),
'set_nodata':       ('None', 'Modify in place.'),
'set_palette':      ('None', 'Modify in place.'),
'set_statistics':   ('None', 'Modify in place.'),
'shift':            ('Dataset', 'The shifted dataset itself. Warning: this method modifies the original data in place.'),
'to_bytearray':     ('bytearray', 'The raster data as a bytearray.'),
'to_crs':           ('Dataset', 'A new Dataset reprojected to the target crs. The original dataset is unchanged.'),
'to_dtype':         ('Dataset', 'A new Dataset converted to the target dtype. The original dataset is unchanged.'),
'to_file':          ('None', 'The dataset is saved to the output file.'),
'to_layer':         ('Layer', 'A new Layer translated from the dataset.'),
'to_numpy':         ('array', 'The raster data as a 3-ndim NumPy array.'),
'write_array':      ('None', 'Modify in place.'),
}

# ---------- 带示意图的方法 ----------
IMAGES = {
'plot':        'The plotted dataset',
'clip':        'Before and after clip',
'resample':    'Before and after resample',
'reclassify':  'Before and after reclassify',
'set_palette': 'Before and after set_palette',
'to_crs':      'Before and after to_crs',
'isopleth':    'The dataset and its isopleths',
'to_layer':    'The dataset and its vectorized polygons',
'gen_lonlat':  'The longitude and latitude bands',
}

LBL = '<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>'
EX_LBL = '<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Example:</p>'

def returns_html(name):
    r = RETURNS[name]
    if len(r) == 2:
        typ, desc = r
        code = f'<code style="text-indent: 0em;">{typ}</code>'
    else:
        typ, suffix, desc = r
        code = f'<code style="text-indent: 0em;">{typ}</code>. <span style="color:#48566B;">{suffix}</span>'
    return [LBL,
            f'<p style="margin-left: 2em;"><b>Type</b>: {code}. </p>',
            f'<p style="margin-left: 4em;">{desc}</p>']

# ---------- 实测: 每个示例在干净底座上独立执行, 捕获 stdout ----------
def exec_example(code):
    ns = {}
    exec(BASE_SETUP, ns)
    buf = io.StringIO()
    with redirect_stdout(buf):
        exec(code, ns)
    return ns, buf.getvalue().rstrip('\n')

results, prop_results = {}, {}
for name, code in EXAMPLES.items():
    _, results[name] = exec_example(code)
    print(f'--- {name} ---'); print(results[name])

for name, code in PROPERTIES.items():
    _, prop_results[name] = exec_example(code)
    print(f'--- prop:{name} ---'); print(prop_results[name])

# ---------- 9 张示意图 ----------
os.makedirs(IMGDIR, exist_ok=True)

def fresh(name):
    ns, _ = exec_example(EXAMPLES[name])
    return ns

def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(IMGDIR, f'dataset_{name}.png'), dpi=110)
    plt.close(fig)
    print(f'[IMG] dataset_{name}.png')

def img_pair(name, after_ax, titles=('Before', 'After')):
    """通用双面板对比图: 左=ds.plot()(RGB 真彩), 右=after_ax 由调用方决定。"""
    ns = fresh(name)
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.5), dpi=110)
    ns['ds'].plot(ax=axs[0])
    after_ax(ns, axs[1])
    for ax, t in zip(axs, titles):
        ax.set_title(t, fontsize=10)
    save(fig, name)

def img_plot():
    ns = fresh('plot')
    fig = ns['ax'].get_figure()
    fig.savefig(os.path.join(IMGDIR, 'dataset_plot.png'), dpi=110)
    plt.close(fig); print('[IMG] dataset_plot.png')

def img_clip():
    ns = fresh('clip')
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.5), dpi=110)
    ns['world'].plot(ax=axs[0])     # 全球晕渲
    ns['res'].plot(ax=axs[1])       # 裁剪后的澳大利亚
    axs[0].set_title('Before', fontsize=10)
    axs[1].set_title('After', fontsize=10)
    save(fig, 'clip')

def img_resample():
    img_pair('resample', lambda ns, ax: ns['res'].plot(ax=ax))

def img_reclassify():
    # 3 波段输出渲染 = RGB 合成(灰), bands=1 显式单波段 = viridis 三色分类图
    img_pair('reclassify', lambda ns, ax: ns['res'].plot(ax=ax, bands=1))

def img_set_palette():
    ns = fresh('set_palette')
    pal = ns['res'].get_palette()
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.5), dpi=110)
    ns['ds_b'].plot(ax=axs[0])
    ns['res'].plot(ax=axs[1], cmap=pal, vmin=0, vmax=pal.N - 1)
    axs[0].set_title('Before', fontsize=10)
    axs[1].set_title('After', fontsize=10)
    save(fig, 'set_palette')

def img_to_crs():
    img_pair('to_crs', lambda ns, ax: ns['res'].plot(ax=ax))

def img_isopleth():
    def after(ns, ax):
        ns['ds'].plot(ax=ax)                     # 底图
        ns['res'].plot(ax=ax, edgecolor='red')   # 等值线
    img_pair('isopleth', after)

def img_to_layer():
    def after(ns, ax):
        ns['ds'].plot(ax=ax)                                      # 底图
        ns['lay'].plot(ax=ax, facecolor='none', edgecolor='red')  # 多边形边界(Layer)
    img_pair('to_layer', after)

def img_gen_lonlat():
    ns = fresh('gen_lonlat')
    res = ns['res']
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.5), dpi=110)
    res.plot(ax=axs[0], bands=1)
    res.plot(ax=axs[1], bands=2)
    axs[0].set_title('Band 1: Longitude', fontsize=10)
    axs[1].set_title('Band 2: Latitude', fontsize=10)
    save(fig, 'gen_lonlat')

print('\n--- images ---')
img_plot(); img_clip(); img_resample(); img_reclassify(); img_set_palette()
img_to_crs(); img_isopleth(); img_to_layer(); img_gen_lonlat()

# ---------- 重建 Dataset.md(幂等) ----------
shutil.copy(MD, BAK) if not os.path.exists(BAK) else None
lines = open(MD, encoding='utf-8').read().splitlines()

idx_method   = next(i for i, l in enumerate(lines) if l.strip() == '## Method')
idx_property = next(i for i, l in enumerate(lines) if l.strip() == '## Property')

def clean_example_tail(sec):
    m = re.search(r'\n*<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Example:</p>.*', sec, re.S)
    if m: sec = sec[:m.start()]
    return sec

def process_method_section(sec_lines, name):
    sec = clean_example_tail('\n'.join(sec_lines))
    m = re.search(r'\n*<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>.*?(?=\n\n|\n###|\Z)', sec, re.S)
    if m: sec = sec[:m.start()] + sec[m.end():]
    sec = sec.rstrip('\n')
    py = '```python\n' + EXAMPLES[name] + '\n```'
    tx = '```text\n' + results[name] + '\n```'
    out = sec + '\n\n' + '\n'.join(returns_html(name)) + '\n\n' + EX_LBL + '\n\n' + py + '\n\n' + tx
    if name in IMAGES:
        out += f'\n\n![{IMAGES[name]}](/img/gio/dataset_{name}.png)'
    return out

def process_property_section(sec_lines, name):
    sec = clean_example_tail('\n'.join(sec_lines)).rstrip('\n')
    py = '```python\n' + PROPERTIES[name] + '\n```'
    tx = '```text\n' + prop_results[name] + '\n```'
    return sec + '\n\n' + EX_LBL + '\n\n' + py + '\n\n' + tx

def split_sections(body):
    starts = [i for i, l in enumerate(body) if l.startswith('### ')]
    secs = []
    for k, st in enumerate(starts):
        name = re.match(r'### (\w+)', body[st]).group(1)
        end = starts[k + 1] if k + 1 < len(starts) else len(body)
        secs.append((name, body[st:end]))
    return secs

# head: 截掉已有底座 Example 块
head_lines = lines[:idx_method]
base_starts = [i for i, l in enumerate(head_lines) if l.strip() == '## Example']
if base_starts: head_lines = head_lines[:base_starts[-1]]
head_txt = '\n'.join(head_lines).rstrip('\n')

method_secs = [process_method_section(sec, n) for n, sec in split_sections(lines[idx_method + 1:idx_property])]
prop_secs   = [process_property_section(sec, n) for n, sec in split_sections(lines[idx_property:])]

base_block = ('## Example\n\n'
              '```python\n' + BASE_SETUP + '\n```\n\n'
              '```text\n' + BASE_RESULT + '\n```\n')

new_md = (head_txt + '\n\n' + base_block + '\n## Method\n\n'
          + '\n\n\n'.join(method_secs) + '\n\n\n'
          + '\n'.join(lines[idx_property:idx_property + 1]) + '\n\n'
          + '\n\n\n'.join(prop_secs) + '\n')

open(MD, 'w', encoding='utf-8', newline='\n').write(new_md)

# ---------- 自检统计 ----------
n_ex = new_md.count('>Example:</p>')
n_ret = new_md.count('>Returns:</p>')
n_img = new_md.count('](/img/gio/dataset_')
print(f'\n[OK] Example labels: {n_ex} (24 method + 15 property) | Returns: {n_ret} | images: {n_img}')
print(f'lines: {len(lines)} -> {len(new_md.splitlines())}')
