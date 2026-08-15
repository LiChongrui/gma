---
title: RasterDriver
date: 2026-08-15
sidebar: true
---
<span style="font-size: 120%;font-weight: bold;">gma.driver.RasterDriver</span>


<span style="background-color:#EFF0FC;display: block;line-height:1.5"><span style="color: gray;font-size:90%;">class</span> <span style="color: #616AE5; font-weight: bold;font-size: 150%;">RasterDriver</span><span style="font-style: italic; color: black;font-size: 130%;">(name = <span style="color:#48566B">"GTiff"</span>):</span></span>

Raster driver object. Create a raster driver object.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>name  = </b> <code style="text-indent: 0">str</code>. <span style="color:#48566B;">Default 'GTiff'.</span></p><p style="padding-left: 1em;text-indent: 1em;">    A raster driver name.</p>

---

## Methods 



### create




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">create</span><span style="font-style: italic; color: black;font-size: 120%;">(out_dst, bands, ysize, xsize, dtype = <span style="color:#48566B">"Float32"</span>):</span></span>


Create a new Dataset with this driver.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>out_dst: </b> <code style="text-indent: 0">str</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Path of the dataset to create. None for memory.</p><p style="text-indent: 1em;"><b>xsize: </b> <code style="text-indent: 0">int</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Width of created raster in pixels. </p><p style="text-indent: 1em;"><b>ysize: </b> <code style="text-indent: 0">int</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Height of created raster in pixels. </p><p style="text-indent: 1em;"><b>bands: </b> <code style="text-indent: 0">int</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Number of bands. </p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>dtype: </b> <code style="text-indent: 0">int.str||RaterDataType||default='Float32'</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Raster data type. Set to `dtypes.DefinedRaterDataTypes` for raster datasets.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Dataset</b>.</p>

---

### open




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">open</span><span style="font-style: italic; color: black;font-size: 120%;">(in_src, sibling_files = <span style="color:#48566B">[]</span>):</span></span>


Open a raster file of this driver as a Dataset.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>in_src: </b> <code style="text-indent: 0">str</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    name of the file to open</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>sibling_files: </b> <code style="text-indent: 0">list||default=None</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    A list of filenames that are auxiliary to the main filename.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Dataset</b>.</p>

---

### set_creation_options




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">set_creation_options</span><span style="font-style: italic; color: black;font-size: 120%;">(**kwargs):</span></span>


Set create options! For more, see ~.creation_options_info!



---

### set_open_options




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">set_open_options</span><span style="font-style: italic; color: black;font-size: 120%;">(**kwargs):</span></span>


Set open options! For more, see ~.open_options_info!



---

## Property 



### category


<p style="text-indent: 1em;">Driver category. --> <code style="text-indent: 0em;"> str</code></p>



---

### compress_modes


<p style="text-indent: 1em;">The compression methods supported by the raster driver. --> <code style="text-indent: 0em;"> list</code></p>



---

### coordinate_epoch


<p style="text-indent: 1em;">Whether the raster driver supports georeferencing. --> <code style="text-indent: 0em;"> bool</code></p>



---

### copyable


<p style="text-indent: 1em;">Whether the target drive supports copy. --> <code style="text-indent: 0em;"> bool</code></p>



---

### creatable


<p style="text-indent: 1em;">Whether the target drive supports creation. --> <code style="text-indent: 0em;"> bool</code></p>



---

### creation_dtypes


<p style="text-indent: 1em;">Supported data storage types. --> <code style="text-indent: 0em;"> list</code></p>



---

### creation_options


<p style="text-indent: 1em;">Creation options. --> <code style="text-indent: 0em;"> dict</code></p>



---

### creation_options_info


<p style="text-indent: 1em;">creation options. --> <code style="text-indent: 0em;"> list</code></p>



---

### extension


<p style="text-indent: 1em;">Driver extension. --> <code style="text-indent: 0em;"> str</code></p>



---

### extensions


<p style="text-indent: 1em;">Driver extensions. --> <code style="text-indent: 0em;"> list</code></p>



---

### is_raster


<p style="text-indent: 1em;">Is a raster driver. --> <code style="text-indent: 0em;"> bool</code></p>



---

### is_vector


<p style="text-indent: 1em;">Is a vector driver. --> <code style="text-indent: 0em;"> bool</code></p>



---

### long_name


<p style="text-indent: 1em;">Driver long name. --> <code style="text-indent: 0em;"> str</code></p>



---

### name


<p style="text-indent: 1em;">Driver name. --> <code style="text-indent: 0em;"> str</code></p>



---

### open_options


<p style="text-indent: 1em;">Open options. --> <code style="text-indent: 0em;"> dict</code></p>



---

### open_options_info


<p style="text-indent: 1em;">open options. --> <code style="text-indent: 0em;"> list</code></p>



---

### sub_datasets


<p style="text-indent: 1em;">Whether the raster driver supports sub dataset. --> <code style="text-indent: 0em;"> bool</code></p>



---

### transformable


<p style="text-indent: 1em;">Whether the raster driver supports transformable. --> <code style="text-indent: 0em;"> bool</code></p>



---

### updatable


<p style="text-indent: 1em;">Whether the target driver can be modified/updated. --> <code style="text-indent: 0em;"> bool</code></p>



---

### virtualio


<p style="text-indent: 1em;">Whether the raster driver supports virtual dataset. --> <code style="text-indent: 0em;"> bool</code></p>



---