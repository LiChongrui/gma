---
title: GeoDatabase
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.gio.GeoDatabase</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">GeoDatabase</span><span style="font-style: italic; color: black;font-size: 130%;">(data = <span style="color:#48566B">None</span>, driver = <span style="color:#48566B">None</span>, out_dst = <span style="color:#48566B">None</span>):</span></span>

<p>Initialize a GeoDatabase object.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>data </b> = <code style="text-indent: 0em;">None||str</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">If None, create a new empty GeoDatabase. If str, open the file path as GeoDatabase.</p>
<p style="margin-left: 2em;"><b>driver </b> = <code style="text-indent: 0em;">str||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">If data is None, the driver name to create the GeoDatabase.</p>
<p style="margin-left: 2em;"><b>out_dst </b> = <code style="text-indent: 0em;">str||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">If data is None, the output file path to create the GeoDatabase.</p>

## Example

```python
from gma import gio

gdb = gio.open_file('NewGDB.gpkg')       # the real GeoPackage from the sample data

print('driver:', gdb.driver)
print('layers:', gdb.layer_names)
print('count :', gdb.layer_count)
```

```text
driver: GPKG - Vector
layers: ['New_Australia', 'Australia']
count : 2
```

## Method

### add_layer<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(layer, new_name = None, over_write = False, **kwargs)</span>

<p>Add Layer to GeoDataBase.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>GMALayer</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<p style="margin-left: 4em;">Another GMA Layer!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>new_name </b> = <code style="text-indent: 0em;">str||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The new name of the added Layer. Default is the added Layer's name.</p>
<p style="margin-left: 2em;"><b>OverWrite </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Whether to force overwrite the layer with the same name.</p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">None</code>. </p>
<p style="margin-left: 4em;">Add the Layer in place. NOTE: gma 3.0.4.1 segfaults on this call.</p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Example:</p>

```python
from gma import gio

gdb = gio.open_file('NewGDB.gpkg')
ly = gio.open_vector('Australia.shp')

gdb.add_layer(ly, new_name='australia_copy')
print(gdb.layer_names)
```

```text
Segmentation fault (gma 3.0.4.1 terminates the process before printing)
```


### create_layer<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(name = None, crs = None, gtype = "Polygon", options = {})</span>

<p>Create a new layer in GeoDatabase.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>name </b> = <code style="text-indent: 0em;">str||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The name for the new layer. This should ideally not match any existing layer on the datasource. None for randint.</p>
<p style="margin-left: 2em;"><b>crs </b> = <code style="text-indent: 0em;">int||str||CoordinateReferenceSystem</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The coordinate system to use for the new layer, or None if no coordinate system is available.</p>
<p style="margin-left: 2em;"><b>gtype </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 'Polygon'</span>. </p>
<p style="margin-left: 4em;">Geometry type for the layer. Use 'Polygon' if there are no constraints on the types geometry to be written.</p>
<p style="margin-left: 2em;"><b>options </b> = <code style="text-indent: 0em;">dict||list</code>. <span style="color:#48566B;"> Default []</span>. </p>
<p style="margin-left: 4em;">Driver-specific dict or list of `name=value` options.</p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<p style="margin-left: 4em;">The newly created empty layer.</p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Example:</p>

```python
from gma import gio

gdb = gio.GeoDatabase(driver='GPKG', out_dst='new.gpkg')
print('Before:', gdb.layer_names)

lyr = gdb.create_layer('cities', crs='WGS84', gtype='Point')
print('After :', gdb.layer_names)
print('Name  :', lyr.name, type(lyr).__name__, lyr.gtype)
```

```text
Before: []
After : ['cities']
Name  : cities Layer Point
```


### delete_layer<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(name_or_id)</span>

<p>Delete a Layer in GeoDataBase.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>name_or_id</b>: <code style="text-indent: 0em;">int||str</code>. </p>
<p style="margin-left: 4em;">Layer name or ID in GeoDataBase!</p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">None</code>. </p>
<p style="margin-left: 4em;">Delete the layer from the database in place.</p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Example:</p>

```python
from gma import gio

gdb = gio.GeoDatabase(driver='GPKG', out_dst='delete.gpkg')
gdb.create_layer('tmp_layer', crs='WGS84', gtype='Point')
print('Before:', gdb.layer_names)

gdb.delete_layer('tmp_layer')
print('After :', gdb.layer_names)
```

```text
Before: ['tmp_layer']
After : []
```


### get_dataset<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(name_or_id = 0)</span>

<p>Get a Dataset in GeoDataBase.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>name_or_id </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 0</span>. </p>
<p style="margin-left: 4em;">Dataset ID or name in the GeoDataBase to get.</p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Dataset</code>. </p>
<p style="margin-left: 4em;">The raster dataset with the given name or ID.</p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Example:</p>

```python
from gma import gio

gdb = gio.open_file('NewGDB.gpkg')
print('datasets:', gdb.dataset_names)

try:
    ds = gdb.get_dataset(0)
except Exception as e:
    print('get_dataset(0):', type(e).__name__, e)
```

```text
datasets: []
get_dataset(0): GMAError Cannot get the DataSet(0)
```


### get_layer<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(name_or_id = 0)</span>

<p>Get a Layer in GeoDatabase.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>name_or_id </b> = <code style="text-indent: 0em;">int||str</code>. <span style="color:#48566B;"> Default 0</span>. </p>
<p style="margin-left: 4em;">Layer id or name in the GeoDatabase to get.</p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<p style="margin-left: 4em;">The vector layer with the given name or ID.</p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Example:</p>

```python
from gma import gio

gdb = gio.open_file('NewGDB.gpkg')

ly = gdb.get_layer('Australia')
print(type(ly).__name__, ly.name, ly.gtype, len(ly))
print('bounds:', tuple(round(v, 2) for v in ly.bounds))
```

```text
Layer Australia Polygon 9
bounds: (112.91, -43.62, 153.62, -10.05)
```


### iteritems<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(category = None, **kwargs)</span>

<p style="margin-left: 2em;">Iterate vector layers and raster datasets. --> <code style="text-indent: 0em;">iter</code></p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">iter</code>. </p>
<p style="margin-left: 4em;">Iterate over vector layers (0 / "Layer") or raster datasets ("Dataset").</p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Example:</p>

```python
from gma import gio

gdb = gio.open_file('NewGDB.gpkg')

for item in gdb.iteritems(0):            # 0 / 'Layer': vector layers
    print(type(item).__name__, item.name, item.gtype, len(item))
```

```text
Layer New_Australia Polygon 18
Layer Australia Polygon 9
```


### query<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(expr, tran_opts = {}, **kwargs)</span>

<p>Query the vector Layer with a SpatiaLite SQL expression.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>expr</b>: <code style="text-indent: 0em;">str</code>. </p>
<p style="margin-left: 4em;">The sql(ite) query string to evaluate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>tran_opts </b> = <code style="text-indent: 0em;">dict</code>. <span style="color:#48566B;"> Default {}</span>. </p>
<p style="margin-left: 4em;">Other parameters passed to ._aio.layer.vector_translate.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to ._aio.vrt.VRTGeoDatabase.add_file.</p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<p style="margin-left: 4em;">A new layer with the result of the SpatiaLite SQL query.</p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Example:</p>

```python
from gma import gio

gdb = gio.open_file('NewGDB.gpkg')

res = gdb.query('SELECT * FROM Australia LIMIT 3')
print(type(res).__name__, res.gtype, len(res))
print('bounds:', tuple(round(v, 2) for v in res.bounds))
```

```text
Layer Polygon 3
bounds: (112.91, -38.07, 141.03, -10.97)
```


## Property

### dataset_count

<p style="margin-left: 2em;">Number of datasets. --> <code style="text-indent: 0em;">int</code></p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Example:</p>

```python
from gma import gio

gdb = gio.open_file('NewGDB.gpkg')

print(gdb.dataset_count)
```

```text
0
```


### dataset_names

<p style="margin-left: 2em;">Names of datasets. --> <code style="text-indent: 0em;">list[str]</code></p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Example:</p>

```python
from gma import gio

gdb = gio.open_file('NewGDB.gpkg')

print(gdb.dataset_names)
```

```text
[]
```


### driver

<p style="margin-left: 2em;">Database driver. --> <code style="text-indent: 0em;">VectorDriver/RasterDriver</code></p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Example:</p>

```python
from gma import gio

gdb = gio.open_file('NewGDB.gpkg')

print(gdb.driver)
```

```text
GPKG - Vector
```


### files

<p style="margin-left: 2em;">GeoDatabase associated files. --> <code style="text-indent: 0em;">list[str]</code></p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Example:</p>

```python
from gma import gio

gdb = gio.open_file('NewGDB.gpkg')

print(gdb.files)
```

```text
['NewGDB.gpkg']
```


### info

<p style="margin-left: 2em;">Source metadata. --> <code style="text-indent: 0em;">dict</code></p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Example:</p>

```python
from gma import gio

gdb = gio.open_file('NewGDB.gpkg')

print('keys:', list(gdb.info.keys()))
for key in ('description', 'driverShortName', 'driverLongName', 'size'):
    print(key, ':', gdb.info[key])
```

```text
keys: ['description', 'driverShortName', 'driverLongName', 'files', 'size', 'coordinateSystem', 'metadata', 'cornerCoordinates', 'bands', 'stac']
description : NewGDB.gpkg
driverShortName : GPKG
driverLongName : GeoPackage
size : [512, 512]
```


### layer_count

<p style="margin-left: 2em;">Number of layers. --> <code style="text-indent: 0em;">int</code></p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Example:</p>

```python
from gma import gio

gdb = gio.open_file('NewGDB.gpkg')

print(gdb.layer_count)
```

```text
2
```


### layer_names

<p style="margin-left: 2em;">Name of Layers. --> <code style="text-indent: 0em;">list[str]</code></p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Example:</p>

```python
from gma import gio

gdb = gio.open_file('NewGDB.gpkg')

print(gdb.layer_names)
```

```text
['New_Australia', 'Australia']
```


### link

<p style="margin-left: 2em;">GeoDatabase path link. --> <code style="text-indent: 0em;">str</code></p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Example:</p>

```python
from gma import gio

gdb = gio.open_file('NewGDB.gpkg')

print(gdb.link)
```

```text
NewGDB.gpkg
```


### name

<p style="margin-left: 2em;">GeoDatabase Name. --> <code style="text-indent: 0em;">str</code></p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Example:</p>

```python
from gma import gio

gdb = gio.open_file('NewGDB.gpkg')

print(gdb.name)
```

```text
NewGDB
```
