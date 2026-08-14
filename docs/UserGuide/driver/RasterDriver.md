---
title: RasterDriver
date: 2026-08-14
sidebar: true
---
# gma.driver.RasterDriver


<span style="background-color:#EFF0FC;display: block;line-height:1.5"><span style="color: gray;font-size:90%;">class</span> <span style="color: #616AE5; font-weight: bold;font-size: 150%;">RasterDriver</span><span style="font-style: italic; color: black;font-size: 130%;">(name = <span style="color:#48566B">"GTiff"</span>):</span></span>

Raster driver object. Create a raster driver object.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>name  = </b> <code>str</code>. <span style="color:#48566B;">Default 'GTiff'.</span></p><p style="padding-left: 1em;text-indent: 1em;">    A raster driver name.</p>

---

## Methods 



### create




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">create</span><span style="font-style: italic; color: black;font-size: 120%;">(out_dst, bands, ysize, xsize, dtype = <span style="color:#48566B">"Float32"</span>):</span></span>


Create a new Dataset with this driver.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>out_dst: </b> <code>str</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Path of the dataset to create. None for memory.</p><p style="text-indent: 1em;"><b>xsize: </b> <code>int</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Width of created raster in pixels. </p><p style="text-indent: 1em;"><b>ysize: </b> <code>int</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Height of created raster in pixels. </p><p style="text-indent: 1em;"><b>bands: </b> <code>int</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Number of bands. </p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>dtype: </b> <code>int.str||RaterDataType||default='Float32'</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Raster data type. Set to `dtypes.DefinedRaterDataTypes` for raster datasets.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Dataset</b>.</p>

---

### open




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">open</span><span style="font-style: italic; color: black;font-size: 120%;">(in_src, sibling_files = <span style="color:#48566B">[]</span>):</span></span>


Open a raster file of this driver as a Dataset.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>in_src: </b> <code>str</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    name of the file to open</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>sibling_files: </b> <code>list||default=None</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    A list of filenames that are auxiliary to the main filename.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Dataset</b>.</p>

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


Driver category. --> <code> str</code>



---

### compress_modes


The compression methods supported by the raster driver. --> <code> list</code>



---

### coordinate_epoch


Whether the raster driver supports georeferencing. --> <code> bool</code>



---

### copyable


Whether the target drive supports copy. --> <code> bool</code>



---

### creatable


Whether the target drive supports creation. --> <code> bool</code>



---

### creation_dtypes


Supported data storage types. --> <code> list</code>



---

### creation_options


Creation options. --> <code> dict</code>



---

### creation_options_info


creation options. --> <code> list</code>



---

### extension


Driver extension. --> <code> str</code>



---

### extensions


Driver extensions. --> <code> list</code>



---

### is_raster


Is a raster driver. --> <code> bool</code>



---

### is_vector


Is a vector driver. --> <code> bool</code>



---

### long_name


Driver long name. --> <code> str</code>



---

### name


Driver name. --> <code> str</code>



---

### open_options


Open options. --> <code> dict</code>



---

### open_options_info


open options. --> <code> list</code>



---

### sub_datasets


Whether the raster driver supports sub dataset. --> <code> bool</code>



---

### transformable


Whether the raster driver supports transformable. --> <code> bool</code>



---

### updatable


Whether the target driver can be modified/updated. --> <code> bool</code>



---

### virtualio


Whether the raster driver supports virtual dataset. --> <code> bool</code>



---