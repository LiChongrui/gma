---
title: Feature
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.gio.Feature</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">Feature</span><span style="font-style: italic; color: black;font-size: 130%;">(geom = <span style="color:#48566B">None</span>, values = <span style="color:#48566B">[]</span>, gtype = <span style="color:#48566B">None</span>, ftypes = <span style="color:#48566B">None</span>, crs = <span style="color:#48566B">None</span>):</span></span>

<p>Create a Feature object.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>geom </b> = <code style="text-indent: 0em;">None||Geometry</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The geometry of the feature. If None, create an empty geometry.</p>
<p style="margin-left: 2em;"><b>values </b> = <code style="text-indent: 0em;">list</code>. <span style="color:#48566B;"> Default []</span>. </p>
<p style="margin-left: 4em;">The field values of the feature.</p>
<p style="margin-left: 2em;"><b>gtype </b> = <code style="text-indent: 0em;">str||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The geometry type of the feature. See `dtypes.DefinedGeomTypes` for valid types. If None, use the geometry type of `geom`.</p>
<p style="margin-left: 2em;"><b>ftypes </b> = <code style="text-indent: 0em;">None||list of FieldType</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The FieldTypes of the feature. If None, create an empty FieldTypes.</p>
<p style="margin-left: 2em;"><b>crs </b> = <code style="text-indent: 0em;">str||int||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The projection of the geometry. If None, no projection is set.</p>

## Method

### copy<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span>

<p style="margin-left: 2em;">copy self. --> <code style="text-indent: 0em;">Feature</code></p>

### plot<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(ax = None, **kwargs)</span>

<p>Make plots of Geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>ax </b> = <code style="text-indent: 0em;">None||matplotlib</code>. <span style="color:#48566B;">~.AxesSubplot. Default None</span>. </p>
<p style="margin-left: 4em;">A matplotlib subplot. If None, a default axes will be created.</p>
<p style="margin-left: 2em;"><b>**kwargs</b></p>
<p style="margin-left: 4em;">Other plotting parameters. For more, see:</p>
<p style="margin-left: 6em;">~.carto.utils.PolyCollection/LineCollection/PointCollection.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>matplotlib.~.AxesSubplot</b></p>

### set_fid<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(fid)</span>

<p>Set the feature identifier.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>fid</b>: <code style="text-indent: 0em;">int</code>. </p>
<p style="margin-left: 4em;">the new feature identifier value to assign.</p>

### set_geom<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(geom)</span>

<p>Set feature geometry. This function updates the features geometry, except that this function does not assume ownership of the passed geometry, but instead makes a copy of it.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>geom</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">new geometry to apply to feature.</p>

### update<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other)</span>

<p>Set one feature from another. Overwrite the contents of this feature from the geometry and attributes of another.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Feature</code>. </p>
<p style="margin-left: 4em;">feature from which geometry and field values will be copied.</p>

## Property

### crs

<p style="margin-left: 2em;">Get coordinate reference system. --> <code style="text-indent: 0em;">CoordinateReferenceSystem</code></p>

### fid

<p style="margin-left: 2em;">Get feature identifier. --> <code style="text-indent: 0em;">int</code></p>

### fields

<p style="margin-left: 2em;">Get fields for feature. --> <code style="text-indent: 0em;">dict</code></p>

### ftypes

<p style="margin-left: 2em;">Get field types for feature. --> <code style="text-indent: 0em;">FieldTypes</code></p>

### geom

<p style="margin-left: 2em;">Get geometry for feature. --> <code style="text-indent: 0em;">Geometry</code></p>

## Example

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
