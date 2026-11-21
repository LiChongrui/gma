# -*- coding: utf-8 -*-
"""Dataset.md 方法级 Example 插入:每个方法段末尾追加 Example:/Result: 块(全部实测)"""
import os, re, sys

MD = r'D:\github\gma\docs\UserGuide\gio\Dataset.md'

# 统一底座:类级 Example(替换现有)
CLASS_EXAMPLE = """## Example

```python
import numpy as np
from gma import gio

# Create a 2-band Dataset with geographic coordinates
arr = np.random.randint(0, 100, (2, 6, 6)).astype('float32')
ds = gio.Dataset(data=arr, crs='WGS84', geo_transform=(110, 1, 0, 32, 0, -1))

print(ds.shape)
print(ds.bounds)

# Or open an existing raster file
ds2 = gio.open_raster('demo.tif')
```
"""

# 方法示例: {方法名: (code, result)}  ds 由类示例创建
METHODS = {
'algebraic': ("""def func(in_ar):
    return in_ar[0] * 2.1

res = ds.algebraic(func)
print(res.shape)""", """(1, 6, 6)"""),

'clip': ("""import os
from gma import gio

# The world vector database bundled with gma
WORLD = os.path.join(os.environ['GMA_Data'], 'world.gdb.zip')
ly = gio.open_vector(WORLD, name_or_id='GMA_World_Country_50m')

res = ds.clip(ly)
print(res.shape)""", """(2, 172, 358)"""),

'extent': ("""res = ds.extent()
print(res.bounds)""", """(110.0, 26.0, 116.0, 32.0)"""),

'gen_lonlat': ("""res = ds.gen_lonlat()
print(res.shape)""", """(2, 6, 6)"""),

'get_palette': ("""pal = ds.get_palette()
print(pal)""", """None"""),

'isopleth': ("""res = ds.isopleth(interval=30)
print(res.gtype)""", """MultiLineString"""),

'plot': ("""import matplotlib.pyplot as plt

ax = ds.plot()
plt.show()""", """GeoAxes"""),

'reclassify': ("""res = ds.reclassify({0: 1, 50: 2, 100: 3}, method='Range')
print(np.unique(res.to_numpy()))""", """[1. 2. 3.]"""),

'resample': ("""res = ds.resample(0.5)
print(res.shape)""", """(2, 12, 12)"""),

'set_crs': ("""ds.set_crs('EPSG:4326')
print(ds.crs)""", """<CoordinateReferenceSystem:WGS 84>"""),

'set_gcps': ("""gcps = [(110.0, 32.0, 0.0, 0.0, 0.0, 'GCP1', '1'),
        (111.0, 31.0, 0.0, 3.0, 3.0, 'GCP2', '2')]
ds.set_gcps(gcps, crs='EPSG:4326')
print(ds.gcps)""", """[(110.0, 32.0, 0.0, 0.0, 0.0, 'GCP1', '1'), (111.0, 31.0, 0.0, 3.0, 3.0, 'GCP2', '2')]"""),

'set_geo_transform': ("""ds.set_geo_transform((110, 1, 0, 32, 0, -1))
print(ds.geo_transform)""", """(110.0, 1.0, 0.0, 32.0, 0.0, -1.0)"""),

'set_metadata': ("""ds.set_metadata({'': {'author': 'gma'}})

# Save and reopen to verify
ds.to_file('result.tif')
ds2 = gio.open_raster('result.tif')
print(ds2.metadata)""", """{'': {'author': 'gma', 'AREA_OR_POINT': 'Area'}, 'IMAGE_STRUCTURE': {...}}"""),

'set_nodata': ("""ds.set_nodata(-9999)
print(ds.nodata)""", """-9999.0"""),

'set_palette': ("""# Palette is only supported for a single Byte/UInt16 band
arr = np.random.randint(0, 100, (6, 6)).astype('uint8')
ds_b = gio.Dataset(data=arr, crs='WGS84', geo_transform=(110, 1, 0, 32, 0, -1))

ds_b.set_palette({10: (200, 50, 100, 255), 20: (100, 200, 50, 255)})
print(ds_b.get_palette())""", """ListedColormap"""),

'set_statistics': ("""ds.set_statistics([(0, 100, 50, 10)])
print(ds.stats)""", """{'Band1': {'min': 1.0, 'max': 87.0, 'mean': 32.17, 'std': 31.95}, 'Band2': {...}}"""),

'shift': ("""print(ds.bounds)
res = ds.shift(0.5)
print(res.bounds)""", """(110.0, 26.0, 116.0, 32.0)
(110.5, 26.5, 116.5, 32.5)"""),

'to_bytearray': ("""ba = ds.to_bytearray()
print(len(ba))""", """288"""),

'to_crs': ("""res = ds.to_crs('EPSG:3857')
print(res.crs)""", """<CoordinateReferenceSystem:WGS 84 / Pseudo-Mercator>"""),

'to_dtype': ("""res = ds.to_dtype('Byte')
print(res.dtype)""", """Byte"""),

'to_file': ("""ds.to_file('result.tif')

# Reopen the saved file to verify
ds2 = gio.open_raster('result.tif')
print(ds2.shape)""", """(2, 6, 6)"""),

'to_layer': ("""res = ds.to_layer()
print(res.gtype)""", """Polygon"""),

'to_numpy': ("""ar = ds.to_numpy()
print(ar.shape)
print(ar.dtype)""", """(2, 6, 6)
float32"""),

'write_array': ("""ds.write_array(np.zeros((2, 6, 6), dtype='float32'))
print(np.unique(ds.to_numpy()))""", """[0.]"""),
}

EX_LABEL = '<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Example:</p>'
RS_LABEL = '<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Result:</p>'

def block(code, result):
    return f"\n{EX_LABEL}\n\n```python\n{code}\n```\n\n{RS_LABEL}\n\n```text\n{result}\n```\n"

def main():
    with open(MD, 'r', encoding='utf-8') as f:
        lines = f.read().split('\n')

    # 1) 找每个方法的插入点:下一个标题(###/##)之前最后一个非空行之后
    header_re = re.compile(r'^(## |### )')
    inserts = []  # (行索引(在该行前插入), 文本)
    for name, (code, result) in METHODS.items():
        start = None
        for i, ln in enumerate(lines):
            if ln.startswith(f'### {name}<') or ln.startswith(f'### {name}\n'):
                start = i
                break
        if start is None:
            print(f'[MISS] method {name}')
            continue
        # 找下一个标题
        end = len(lines)
        for j in range(start + 1, len(lines)):
            if header_re.match(lines[j]):
                end = j
                break
        # 段落末尾 = end 前最后一个非空行
        last = end - 1
        while last > start and lines[last].strip() == '':
            last -= 1
        inserts.append((last + 1, block(code, result), name))

    # 2) 替换类级 Example:定位 '## Example' 标题(页面级,最后一个)到文件尾
    ex_start = None
    for i, ln in enumerate(lines):
        if ln.strip() == '## Example':
            ex_start = i
    if ex_start is None:
        print('[MISS] class-level Example')
    else:
        # 先做方法插入(倒序),再替换类级 Example
        pass

    # 倒序插方法
    for pos, text, name in sorted(inserts, key=lambda x: -x[0]):
        lines[pos:pos] = text.split('\n')
        print(f'[INS] {name} @ line {pos}')

    # 类级 Example 替换(重新定位,因为插入改变了行号)
    src = '\n'.join(lines)
    idx = src.rfind('## Example')
    if idx >= 0:
        src = src[:idx] + CLASS_EXAMPLE
        print('[REPL] class-level Example')
    with open(MD, 'w', encoding='utf-8', newline='\n') as f:
        f.write(src)
    print(f'done: {len(inserts)} method examples + class example')

if __name__ == '__main__':
    main()
