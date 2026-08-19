---
title: FieldType
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.gio.FieldType</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">FieldType</span><span style="font-style: italic; color: black;font-size: 130%;">(name = <span style="color:#48566B">None</span>, dtype = <span style="color:#48566B">"UNKNOWN"</span>):</span></span>

<p>Create a FieldType object.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>name </b> = <code style="text-indent: 0em;">str||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The name of the field. None for dtype name.</p>
<p style="margin-left: 2em;"><b>dtype </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'UNKNOWN'</span>. </p>
<p style="margin-left: 4em;">The data type of the field. See `dtypes.DefinedFieldDataTypes` for valid types.</p>

## Method

### set_precision
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.set_precision</span><span style="font-style: italic; color: black;font-size: 120%;">(precision):</span></span>

<p>Set the formatting precision for this field in characters.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>precision</b>: <code style="text-indent: 0em;">int</code>. </p>
<p style="margin-left: 4em;">the new precision.</p>

### set_type
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.set_type</span><span style="font-style: italic; color: black;font-size: 120%;">(f_dtype):</span></span>

<p>Set the formatting width for this field in characters.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>f_dtype</b>: <code style="text-indent: 0em;">int||str</code>. </p>
<p style="margin-left: 4em;">the new field data type</p>

### set_width
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.set_width</span><span style="font-style: italic; color: black;font-size: 120%;">(width):</span></span>

<p>Set the formatting width for this field in characters.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>width</b>: <code style="text-indent: 0em;">int</code>. </p>
<p style="margin-left: 4em;">the new width</p>

## Property

### default
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.default</span><span style=""></span></span>

<p style="margin-left: 2em;">Field default value. --> <code style="text-indent: 0em;">str/int/float/...</code></p>

### ftype
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.ftype</span><span style=""></span></span>

<p style="margin-left: 2em;">Field data type. --> <code style="text-indent: 0em;">str</code></p>

### name
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.name</span><span style=""></span></span>

<p style="margin-left: 2em;">Field name. --> <code style="text-indent: 0em;">str</code></p>

### precision
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.precision</span><span style=""></span></span>

<p style="margin-left: 2em;">Field precision. --> <code style="text-indent: 0em;">int</code></p>

### width
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.width</span><span style=""></span></span>

<p style="margin-left: 2em;">Field width. --> <code style="text-indent: 0em;">int</code></p>
