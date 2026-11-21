---
title: FieldTypes
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.gio.FieldTypes</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">FieldTypes</span><span style="font-style: italic; color: black;font-size: 130%;">(ftypes = <span style="color:#48566B">None</span>):</span></span>

<p>Create a FeatureDefn object.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>ftype </b> = <code style="text-indent: 0em;">None||list of FieldType</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">If None, create an empty FieldTypes.</p>

## Example

```python
from gma import gio

ly = gio.open_vector('Australia.shp')
fts = ly.ftypes               # real field definitions of the vector data

print('number of fields :', len(fts.names))
print('first five names :', fts.names[:5])
print('first field type :', fts[0])
```

```text
number of fields : 123
first five names : ['featurecla', 'scalerank', 'adm1_code', 'diss_me', 'iso_3166_2']
first field type : "featurecla" - Type:"String", Width:80, Precision:0
```

## Method

### add_ftype<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(ftype)</span>

<p>Add a FieldType to this FieldTypes.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>ftype</b>: <code style="text-indent: 0em;">FieldType</code>. </p>
<p style="margin-left: 4em;">The FieldType to add.</p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">None</code>. </p>
<p style="margin-left: 4em;">Add the FieldType in place.</p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Example:</p>

```python
from gma import gio

fts = gio.FieldTypes()
print('Before:', fts.names)

fts.add_ftype(gio.FieldType('name', 'String'))
print('After :', fts.names)
```

```text
Before: []
After : ['name']
```


### set_gtype<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(gtype)</span>

<p>Set a geom type to this FieldTypes.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>gtype</b>: <code style="text-indent: 0em;">int||str</code>. </p>
<p style="margin-left: 4em;">The geom type to set.</p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">None</code>. </p>
<p style="margin-left: 4em;">Set the geometry type in place; field names are unchanged.</p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Example:</p>

```python
from gma import gio

fts = gio.FieldTypes()
fts.add_ftype(gio.FieldType('name', 'String'))

print('Before:', fts.names)
fts.set_gtype('Point')
print('After :', fts.names)
```

```text
Before: ['name']
After : ['name']
```


## Property

### ftypes

<p style="margin-left: 2em;">Field names. --> <code style="text-indent: 0em;">list</code></p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Example:</p>

```python
from gma import gio

fts = gio.open_vector('Australia.shp').ftypes

print('number of types:', len(fts.ftypes))
print('first five     :', fts.ftypes[:5])
```

```text
number of types: 123
first five     : ['String', 'Integer', 'String', 'Integer64', 'String']
```


### names

<p style="margin-left: 2em;">Field names. --> <code style="text-indent: 0em;">list</code></p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Example:</p>

```python
from gma import gio

fts = gio.open_vector('Australia.shp').ftypes

print('number of names:', len(fts.names))
print('first five     :', fts.names[:5])
```

```text
number of names: 123
first five     : ['featurecla', 'scalerank', 'adm1_code', 'diss_me', 'iso_3166_2']
```
