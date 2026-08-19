---
title: VectorDriver
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.driver.VectorDriver</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">VectorDriver</span><span style="font-style: italic; color: black;font-size: 130%;">(name = <span style="color:#48566B">"ESRI Shapefile"</span>):</span></span>

<p>Create a vector driver object.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>name </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'ESRI Shapefile'</span>. </p>
<p style="margin-left: 4em;">A vector driver.</p>

## Method

### create
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.create</span><span style="font-style: italic; color: black;font-size: 120%;">(out_dst):</span></span>

<p>Create a new GeoDatabase with this driver.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>out_dst</b>: <code style="text-indent: 0em;">str</code>. </p>
<p style="margin-left: 4em;">Path of the geo database to create. None for memory.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>GeoDatabase</b></p>

### open
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.open</span><span style="font-style: italic; color: black;font-size: 120%;">(in_src, sibling_files = <span style="color:#48566B">[]</span>):</span></span>

<p>Open a raster file of this driver as a Dataset.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>in_src</b>: <code style="text-indent: 0em;">str</code>. </p>
<p style="margin-left: 4em;">name of the file to open</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>sibling_files</b>: <code style="text-indent: 0em;">list||Default None</code>. </p>
<p style="margin-left: 4em;">A list of filenames that are auxiliary to the main filename.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Dataset</b></p>

### set_creation_options
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.set_creation_options</span><span style="font-style: italic; color: black;font-size: 120%;">(**kwargs):</span></span>

<p>Set create options! For more, see ~.creation_options_info!</p>

### set_open_options
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.set_open_options</span><span style="font-style: italic; color: black;font-size: 120%;">(**kwargs):</span></span>

<p>Set open options! For more, see ~.open_options_info!</p>

## Property

### category
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.category</span><span style=""></span></span>

<p style="margin-left: 2em;">Driver category. --> <code style="text-indent: 0em;">str</code></p>

### creatable
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.creatable</span><span style=""></span></span>

<p style="margin-left: 2em;">Whether the target drive supports creation. --> <code style="text-indent: 0em;">bool</code></p>

### creation_ftypes
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.creation_ftypes</span><span style=""></span></span>

<p style="margin-left: 2em;">Supported field storage types. --> <code style="text-indent: 0em;">list</code></p>

### creation_options
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.creation_options</span><span style=""></span></span>

<p style="margin-left: 2em;">Creation options. --> <code style="text-indent: 0em;">dict</code></p>

### creation_options_info
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.creation_options_info</span><span style=""></span></span>

<p style="margin-left: 2em;">creation options. --> <code style="text-indent: 0em;">list</code></p>

### dimension
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.dimension</span><span style=""></span></span>

<p style="margin-left: 2em;">Get the dimension vector driver. --> <code style="text-indent: 0em;">str</code></p>

### extension
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.extension</span><span style=""></span></span>

<p style="margin-left: 2em;">Driver extension. --> <code style="text-indent: 0em;">str</code></p>

### extensions
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.extensions</span><span style=""></span></span>

<p style="margin-left: 2em;">Driver extensions. --> <code style="text-indent: 0em;">list</code></p>

### is_raster
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.is_raster</span><span style=""></span></span>

<p style="margin-left: 2em;">Is a raster driver. --> <code style="text-indent: 0em;">bool</code></p>

### is_vector
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.is_vector</span><span style=""></span></span>

<p style="margin-left: 2em;">Is a vector driver. --> <code style="text-indent: 0em;">bool</code></p>

### long_name
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.long_name</span><span style=""></span></span>

<p style="margin-left: 2em;">Driver long name. --> <code style="text-indent: 0em;">str</code></p>

### multi_layers
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.multi_layers</span><span style=""></span></span>

<p style="margin-left: 2em;">Whether the vector driver supports multi layers. --> <code style="text-indent: 0em;">bool</code></p>

### name
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.name</span><span style=""></span></span>

<p style="margin-left: 2em;">Driver name. --> <code style="text-indent: 0em;">str</code></p>

### open_options
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.open_options</span><span style=""></span></span>

<p style="margin-left: 2em;">Open options. --> <code style="text-indent: 0em;">dict</code></p>

### open_options_info
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.open_options_info</span><span style=""></span></span>

<p style="margin-left: 2em;">open options. --> <code style="text-indent: 0em;">list</code></p>

### sql_dialects
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.sql_dialects</span><span style=""></span></span>

<p style="margin-left: 2em;">The vector driver support's sql dialects. --> <code style="text-indent: 0em;">list</code></p>

### transformable
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.transformable</span><span style=""></span></span>

<p style="margin-left: 2em;">Whether the vector driver supports transformable. --> <code style="text-indent: 0em;">bool</code></p>

### updatable
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.updatable</span><span style=""></span></span>

<p style="margin-left: 2em;">Whether the target driver can be modified/updated. --> <code style="text-indent: 0em;">bool</code></p>

### virtualio
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.virtualio</span><span style=""></span></span>

<p style="margin-left: 2em;">Whether the raster driver supports virtual dataset. --> <code style="text-indent: 0em;">bool</code></p>
