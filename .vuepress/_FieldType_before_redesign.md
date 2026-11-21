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

## Method

### set_precision<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(precision)</span>

<p>Set the formatting precision for this field in characters.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>precision</b>: <code style="text-indent: 0em;">int</code>. </p>
<p style="margin-left: 4em;">the new precision.</p>

### set_type<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(f_dtype)</span>

<p>Set the formatting width for this field in characters.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>f_dtype</b>: <code style="text-indent: 0em;">int||str</code>. </p>
<p style="margin-left: 4em;">the new field data type</p>

### set_width<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(width)</span>

<p>Set the formatting width for this field in characters.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>width</b>: <code style="text-indent: 0em;">int</code>. </p>
<p style="margin-left: 4em;">the new width</p>

## Property

### default

<p style="margin-left: 2em;">Field default value. --> <code style="text-indent: 0em;">str/int/float/...</code></p>

### ftype

<p style="margin-left: 2em;">Field data type. --> <code style="text-indent: 0em;">str</code></p>

### name

<p style="margin-left: 2em;">Field name. --> <code style="text-indent: 0em;">str</code></p>

### precision

<p style="margin-left: 2em;">Field precision. --> <code style="text-indent: 0em;">int</code></p>

### width

<p style="margin-left: 2em;">Field width. --> <code style="text-indent: 0em;">int</code></p>

## Example

```python
from gma import gio

# Create a field type
ft = gio.FieldType('String')

# Set the formatting precision
ft.set_precision(10)
```
