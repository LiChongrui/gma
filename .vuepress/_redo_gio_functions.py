import sys, os, re
sys.path.insert(0, r'D:\github\gma\.vuepress\_gio_doc_common.py')
from _gio_doc_common import run, prepare_extra, capture, DOCS

prepare_extra([(r'D:\BaiduNetdiskDownload\ne\NewGDB.gpkg', 'NewGDB.gpkg')])

EXAMPLES = {
'open_raster': '''from gma import gio

ds = gio.open_raster('HYP_50M_SR_W.tif')     # Natural Earth shaded relief

print(type(ds).__name__, ds.shape, ds.dtype)
print('bounds:', tuple(round(v, 2) for v in ds.bounds))
print('crs   :', ds.crs)''',

'open_vector': '''from gma import gio

ly = gio.open_vector('Australia.shp')

print(type(ly).__name__, ly.gtype, len(ly))
print('bounds:', tuple(round(v, 2) for v in ly.bounds))
print('name  :', ly.get_feature(0).fields['name'])''',

'open_file': '''from gma import gio

gdb = gio.open_file('NewGDB.gpkg')           # the sample GeoPackage

print(type(gdb).__name__, gdb.driver)
print('layers  :', gdb.layer_names)
print('features:', [len(gdb.get_layer(i)) for i in range(gdb.layer_count)])''',

'VirtualRasterDataset': '''from gma import gio

ds = gio.open_raster('HYP_50M_SR_W.tif')
vrd = gio.VirtualRasterDataset(ds)           # in-memory virtual mosaic

print(type(vrd).__name__, vrd.shape, vrd.dtype)
print('same data:', vrd.to_numpy().shape == ds.to_numpy().shape)''',

'VirtualVectorGeoDatabase': '''from gma import gio

ly = gio.open_vector('Australia.shp')
vvgd = gio.VirtualVectorGeoDatabase([ly])    # combine Layers into a virtual GeoDatabase

print(type(vvgd).__name__, vvgd.layer_names)
print('features:', len(vvgd.get_layer(0)))''',

'read_dataframe': '''import pandas as pd
from gma import gio

ly = gio.open_vector('Australia.shp')
df = ly.to_pandas(keep_geom=True)[['name', 'geometry']]

res = gio.read_dataframe(df, geom_col='geometry', gtype='Polygon')
print(type(res).__name__, len(res), res.gtype)
print('first:', res.get_feature(0).fields['name'])''',
}

for page, code in EXAMPLES.items():
    MD = os.path.join(DOCS, page + '.md')
    lines = open(MD, encoding='utf-8').read().splitlines()
    idx = next(i for i, l in enumerate(lines) if l.strip() == '## Example')
    head = '\n'.join(lines[:idx]).rstrip('\n')
    _, out = capture(code)
    if out.startswith('[ERROR]'):
        print('ERROR', page, out); continue
    new = (head + '\n\n## Example\n\n```python\n' + code +
           '\n```\n\n```text\n' + out + '\n```\n')
    open(MD, 'w', encoding='utf-8', newline='\n').write(new)
    print(f'[OK] {page}: {len(lines)} -> {len(new.splitlines())} lines')
