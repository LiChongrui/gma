---
title: FieldType
date: 2026-08-15
sidebar: true
---
# gma.gio.FieldType


<span style="background-color:#EFF0FC;display: block;line-height:1.5"><span style="color: gray;font-size:90%;">class</span> <span style="color: #616AE5; font-weight: bold;font-size: 150%;">FieldType</span><span style="font-style: italic; color: black;font-size: 130%;">(name = <span style="color:#48566B">None</span>, dtype = <span style="color:#48566B">"UNKNOWN"</span>):</span></span>

Field type object for vector data. Create a FieldType object.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>name: </b> <code style="text-indent: 0">str</code>. <span style="color:#48566B;">Default = None</span></p><p style="padding-left: 1em;text-indent: 1em;">    The name of the field. None for dtype name.</p><p style="text-indent: 1em;"><b>dtype: </b> <code style="text-indent: 0">str</code>. <span style="color:#48566B;">Default = 'UNKNOWN'</span></p><p style="padding-left: 1em;text-indent: 1em;">    The data type of the field. See `dtypes.DefinedFieldDataTypes` for valid types.</p>

---

## Methods 



### set_precision




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">set_precision</span><span style="font-style: italic; color: black;font-size: 120%;">(precision):</span></span>


Set the formatting precision for this field in characters.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>precision: </b> <code style="text-indent: 0">int</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    the new precision.</p>

---

### set_type




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">set_type</span><span style="font-style: italic; color: black;font-size: 120%;">(f_dtype):</span></span>


Set the formatting width for this field in characters.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>f_dtype: </b> <code style="text-indent: 0">int||str</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    the new field data type</p>

---

### set_width




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">set_width</span><span style="font-style: italic; color: black;font-size: 120%;">(width):</span></span>


Set the formatting width for this field in characters.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>width: </b> <code style="text-indent: 0">int</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    the new width</p>

---

## Property 



### default


Field default value. -> str/int/float/...



---

### ftype


Field data type. -> str



---

### name


Field name. -> str



---

### precision


Field precision. -> int



---

### width


Field width. -> int



---