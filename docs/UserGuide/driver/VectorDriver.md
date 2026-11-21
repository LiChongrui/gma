---
title: VectorDriver
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.driver.VectorDriver</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">VectorDriver</span><span style="font-style: italic; color: black;font-size: 130%;">(name = <span style="color:#48566B">"ESRI Shapefile"</span>):</span></span>

<p>Create a vector driver object.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>name </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'ESRI Shapefile'</span>. </p>
<p style="margin-left: 4em;">A vector driver.</p>

## Method

### create<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(out_dst)</span>

<p>Create a new GeoDatabase with this driver.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>out_dst</b>: <code style="text-indent: 0em;">str</code>. </p>
<p style="margin-left: 4em;">Path of the geo database to create. None for memory.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>GeoDatabase</b></p>

### open<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(in_src, sibling_files = [])</span>

<p>Open a raster file of this driver as a Dataset.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>in_src</b>: <code style="text-indent: 0em;">str</code>. </p>
<p style="margin-left: 4em;">name of the file to open</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>sibling_files</b>: <code style="text-indent: 0em;">list||Default None</code>. </p>
<p style="margin-left: 4em;">A list of filenames that are auxiliary to the main filename.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Dataset</b></p>

### set_creation_options<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(**kwargs)</span>

<p>Set create options! For more, see ~.creation_options_info!</p>

### set_open_options<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(**kwargs)</span>

<p>Set open options! For more, see ~.open_options_info!</p>

## Property

### category

<p style="margin-left: 2em;">Driver category. --> <code style="text-indent: 0em;">str</code></p>

### creatable

<p style="margin-left: 2em;">Whether the target drive supports creation. --> <code style="text-indent: 0em;">bool</code></p>

### creation_ftypes

<p style="margin-left: 2em;">Supported field storage types. --> <code style="text-indent: 0em;">list</code></p>

### creation_options

<p style="margin-left: 2em;">Creation options. --> <code style="text-indent: 0em;">dict</code></p>

### creation_options_info

<p style="margin-left: 2em;">creation options. --> <code style="text-indent: 0em;">list</code></p>

### dimension

<p style="margin-left: 2em;">Get the dimension vector driver. --> <code style="text-indent: 0em;">str</code></p>

### extension

<p style="margin-left: 2em;">Driver extension. --> <code style="text-indent: 0em;">str</code></p>

### extensions

<p style="margin-left: 2em;">Driver extensions. --> <code style="text-indent: 0em;">list</code></p>

### is_raster

<p style="margin-left: 2em;">Is a raster driver. --> <code style="text-indent: 0em;">bool</code></p>

### is_vector

<p style="margin-left: 2em;">Is a vector driver. --> <code style="text-indent: 0em;">bool</code></p>

### long_name

<p style="margin-left: 2em;">Driver long name. --> <code style="text-indent: 0em;">str</code></p>

### multi_layers

<p style="margin-left: 2em;">Whether the vector driver supports multi layers. --> <code style="text-indent: 0em;">bool</code></p>

### name

<p style="margin-left: 2em;">Driver name. --> <code style="text-indent: 0em;">str</code></p>

### open_options

<p style="margin-left: 2em;">Open options. --> <code style="text-indent: 0em;">dict</code></p>

### open_options_info

<p style="margin-left: 2em;">open options. --> <code style="text-indent: 0em;">list</code></p>

### sql_dialects

<p style="margin-left: 2em;">The vector driver support's sql dialects. --> <code style="text-indent: 0em;">list</code></p>

### transformable

<p style="margin-left: 2em;">Whether the vector driver supports transformable. --> <code style="text-indent: 0em;">bool</code></p>

### updatable

<p style="margin-left: 2em;">Whether the target driver can be modified/updated. --> <code style="text-indent: 0em;">bool</code></p>

### virtualio

<p style="margin-left: 2em;">Whether the raster driver supports virtual dataset. --> <code style="text-indent: 0em;">bool</code></p>
