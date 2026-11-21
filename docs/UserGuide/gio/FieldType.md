---
title: FieldType
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.gio.FieldType</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">FieldType</span><span style="font-style: italic; color: black;font-size: 130%;">(name = <span style="color:#48566B">None</span>, dtype = <span style="color:#48566B">"UNKNOWN"</span>):</span></span>

<p>Create a FieldType object.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>name </b> = <code style="text-indent: 0em;">str||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The name of the field. None for dtype name.</p>
<p style="margin-left: 2em;"><b>dtype </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'UNKNOWN'</span>. </p>
<p style="margin-left: 4em;">The data type of the field. See `dtypes.DefinedFieldDataTypes` for valid types.</p>

## Example

```python
from gma import gio

ly = gio.open_vector('Australia.shp')
ftype = ly.ftypes[0]        # first field of the real vector data

print(ftype)
```

```text
"featurecla" - Type:"String", Width:80, Precision:0
```

## Method

### set_precision<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(precision)</span>

<p>Set the formatting precision for this field in characters.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>precision</b>: <code style="text-indent: 0em;">int</code>. </p>
<p style="margin-left: 4em;">the new precision.</p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">None</code>. </p>
<p style="margin-left: 4em;">Modify the precision in place.</p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Example:</p>

```python
from gma import gio

src = gio.open_vector('Australia.shp').ftypes[0]
ftype = gio.FieldType(src.name, src.ftype)     # a modifiable copy of a real field

print('Before:', ftype)
ftype.set_precision(10)
print('After :', ftype)
```

```text
Before: "featurecla" - Type:"String", Width:0, Precision:0
After : "featurecla" - Type:"String", Width:0, Precision:10
```


### set_type<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(f_dtype)</span>

<p>Set the formatting width for this field in characters.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>f_dtype</b>: <code style="text-indent: 0em;">int||str</code>. </p>
<p style="margin-left: 4em;">the new field data type</p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">None</code>. </p>
<p style="margin-left: 4em;">Modify the field data type in place.</p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Example:</p>

```python
from gma import gio

src = gio.open_vector('Australia.shp').ftypes[0]
ftype = gio.FieldType(src.name, src.ftype)     # a modifiable copy of a real field

print('Before:', ftype)
ftype.set_type('Integer')
print('After :', ftype)
```

```text
Before: "featurecla" - Type:"String", Width:0, Precision:0
After : "featurecla" - Type:"Integer", Width:0, Precision:0
```


### set_width<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(width)</span>

<p>Set the formatting width for this field in characters.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>width</b>: <code style="text-indent: 0em;">int</code>. </p>
<p style="margin-left: 4em;">the new width</p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">None</code>. </p>
<p style="margin-left: 4em;">Modify the field width in place.</p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Example:</p>

```python
from gma import gio

src = gio.open_vector('Australia.shp').ftypes[0]
ftype = gio.FieldType(src.name, src.ftype)     # a modifiable copy of a real field

print('Before:', ftype)
ftype.set_width(40)
print('After :', ftype)
```

```text
Before: "featurecla" - Type:"String", Width:0, Precision:0
After : "featurecla" - Type:"String", Width:40, Precision:0
```


## Property

### default

<p style="margin-left: 2em;">Field default value. --> <code style="text-indent: 0em;">str/int/float/...</code></p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Example:</p>

```python
from gma import gio

ftype = gio.open_vector('Australia.shp').ftypes[0]

print(ftype.default)
```

```text
None
```


### ftype

<p style="margin-left: 2em;">Field data type. --> <code style="text-indent: 0em;">str</code></p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Example:</p>

```python
from gma import gio

ftype = gio.open_vector('Australia.shp').ftypes[0]

print(ftype.ftype)
```

```text
String
```


### name

<p style="margin-left: 2em;">Field name. --> <code style="text-indent: 0em;">str</code></p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Example:</p>

```python
from gma import gio

ftype = gio.open_vector('Australia.shp').ftypes[0]

print(ftype.name)
```

```text
featurecla
```


### precision

<p style="margin-left: 2em;">Field precision. --> <code style="text-indent: 0em;">int</code></p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Example:</p>

```python
from gma import gio

ftype = gio.open_vector('Australia.shp').ftypes[0]

print(ftype.precision)
```

```text
0
```


### width

<p style="margin-left: 2em;">Field width. --> <code style="text-indent: 0em;">int</code></p>

<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Example:</p>

```python
from gma import gio

ftype = gio.open_vector('Australia.shp').ftypes[0]

print(ftype.width)
```

```text
80
```
