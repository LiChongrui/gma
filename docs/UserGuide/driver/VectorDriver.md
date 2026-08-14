---
title: VectorDriver
date: 2026-08-14
sidebar: true
---
# gma.driver.VectorDriver


<span style="background-color:#EFF0FC;display: block;line-height:1.5"><span style="color: gray;font-size:90%;">class</span> <span style="color: #616AE5; font-weight: bold;font-size: 150%;">VectorDriver</span><span style="font-style: italic; color: black;font-size: 130%;">(name = <span style="color:#48566B">"ESRI Shapefile"</span>):</span></span>

Vector driver object. Create a vector driver object.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>name  = </b> <code>str</code>. <span style="color:#48566B;">Default 'ESRI Shapefile'.</span></p><p style="padding-left: 1em;text-indent: 1em;">    A vector driver.</p>

---

## Methods 



### create




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">create</span><span style="font-style: italic; color: black;font-size: 120%;">(out_dst):</span></span>


Create a new GeoDatabase with this driver.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>out_dst: </b> <code>str</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Path of the geo database to create. None for memory.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>GeoDatabase</b>.</p>

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

### creatable


Whether the target drive supports creation. --> <code> bool</code>



---

### creation_ftypes


Supported field storage types. --> <code> list</code>



---

### creation_options


Creation options. --> <code> dict</code>



---

### creation_options_info


creation options. --> <code> list</code>



---

### dimension


Get the dimension vector driver. --> <code> str</code>



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

### multi_layers


Whether the vector driver supports multi layers. --> <code> bool</code>



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

### sql_dialects


The vector driver support's sql dialects. --> <code> list</code>



---

### transformable


Whether the vector driver supports transformable. --> <code> bool</code>



---

### updatable


Whether the target driver can be modified/updated. --> <code> bool</code>



---

### virtualio


Whether the raster driver supports virtual dataset. --> <code> bool</code>



---