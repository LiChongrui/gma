# -*- coding: utf-8 -*-
"""gio 各页文末追加 ## Example(内容均已用 gma 3.0.4.1 实测)"""
import os, sys

DOCS = r'D:\github\gma\docs\UserGuide\gio'

# 每页: (文件名, Example 正文)
EXAMPLES = {
'open_file.md': """## Example

```python
import os
from gma import gio

# The world vector database bundled with gma
WORLD = os.path.join(os.environ['GMA_Data'], 'world.gdb.zip')

# Open it as a GeoDatabase
gdb = gio.open_file(WORLD)

print(gdb.layer_names)
```
""",
'open_vector.md': """## Example

```python
import os
from gma import gio

# The world vector database bundled with gma
WORLD = os.path.join(os.environ['GMA_Data'], 'world.gdb.zip')

# Open a Layer from the GeoDatabase
ly = gio.open_vector(WORLD, name_or_id='GMA_World_Country_50m')

print(ly.gtype)
```
""",
'open_raster.md': """## Example

```python
import os
from gma import gio

# The world DEM raster bundled with gma
DEM = os.path.join(os.environ['GMA_Data'], 'GMA_World_DEM_GEBCO.jp2')

# Open it as a Dataset
ds = gio.open_raster(DEM)

print(ds.bounds)
```
""",
'read_dataframe.md': """## Example

```python
import pandas as pd
from gma import gio

# Create a Layer from a DataFrame with x/y columns
df = pd.DataFrame({'name': ['A', 'B'], 'lon': [114.0, 118.0], 'lat': [30.0, 32.0]})

ly = gio.read_dataframe(df, gtype='Point', encoding='PointFromColumns', x='lon', y='lat')

print(ly.gtype)
```
""",
'GeoDatabase.md': """## Example

```python
import os
from gma import gio

# The world vector database bundled with gma
WORLD = os.path.join(os.environ['GMA_Data'], 'world.gdb.zip')

gdb = gio.open_file(WORLD)

print(gdb.layer_names)
print(gdb.layer_count)

# Get a Layer and query the GeoDatabase
ly = gdb.get_layer('GMA_World_Country_50m')
res = gdb.query('SELECT * FROM GMA_World_Country_50m LIMIT 3')
```
""",
'Layer.md': """## Example

```python
import os
from gma import gio

# The world vector database bundled with gma
WORLD = os.path.join(os.environ['GMA_Data'], 'world.gdb.zip')

ly = gio.open_vector(WORLD, name_or_id='GMA_World_Country_50m')

# Buffer all features by 10 degrees
buf = ly.buffer(10)

# Calculate geometry attributes in place
cg = ly.calculate_geometry(area=True)

# Save the Layer to a Shapefile
ly.to_file('Country.shp')
```
""",
'Feature.md': """## Example

```python
import os
from gma import gio

# The world vector database bundled with gma
WORLD = os.path.join(os.environ['GMA_Data'], 'world.gdb.zip')

ly = gio.open_vector(WORLD, name_or_id='GMA_World_Country_50m')

# Get the first feature
ft = ly.get_feature(0)

print(ft.fid)
print(ft.fields)
print(ft.geom.gtype)
```
""",
'Geometry.md': """## Example

```python
from gma import gio

# Create geometries from WKT strings
pt = gio.Geometry('POINT (114 30)')
pg = gio.Geometry('POLYGON ((110 28, 118 28, 118 32, 110 32, 110 28))')

# Spatial operations
buf = pg.buffer(1)
print(pg.contains(pt))

# Create a LineString from a coordinate list
ln = gio.Geometry([[114, 30], [115, 31]], gtype='LineString')
```
""",
'VirtualVectorGeoDatabase.md': """## Example

```python
import os
from gma import gio

# The world vector database bundled with gma
WORLD = os.path.join(os.environ['GMA_Data'], 'world.gdb.zip')

ly = gio.open_vector(WORLD, name_or_id='GMA_World_Country_50m')

# Combine Layers into an in-memory GeoDatabase
vvgd = gio.VirtualVectorGeoDatabase([ly])

print(vvgd.layer_names)
```
""",
'VirtualRasterDataset.md': """## Example

```python
import os
from gma import gio

# The world DEM raster bundled with gma
DEM = os.path.join(os.environ['GMA_Data'], 'GMA_World_DEM_GEBCO.jp2')

ds = gio.open_raster(DEM)

# Create a virtual dataset from the opened Dataset
vrd = gio.VirtualRasterDataset(ds)

vrd.to_file('result.tif')
```
""",
'FieldType.md': """## Example

```python
from gma import gio

# Create a field type
ft = gio.FieldType('String')

# Set the formatting precision
ft.set_precision(10)
```
""",
'FieldTypes.md': """## Example

```python
from gma import gio

# Build a fields definition
fts = gio.FieldTypes()
fts.add_ftype(gio.FieldType('String'))
fts.set_gtype('Point')

print(fts.names)
```
""",
}

def main():
    changed, skipped = [], []
    for fname, ex in EXAMPLES.items():
        path = os.path.join(DOCS, fname)
        if not os.path.exists(path):
            print(f'[MISS] {fname}')
            continue
        with open(path, 'r', encoding='utf-8') as f:
            src = f.read()
        if '## Example' in src:
            skipped.append(fname)
            continue
        if not src.endswith('\n'):
            src += '\n'
        new = src + '\n' + ex
        with open(path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(new)
        changed.append(fname)
    print(f'appended: {len(changed)} -> {changed}')
    print(f'skipped (already has Example): {skipped}')

if __name__ == '__main__':
    main()
