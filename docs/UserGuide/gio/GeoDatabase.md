---
title: GeoDatabase
date: 2026-08-14
sidebar: true
---
# gma.gio.GeoDatabase


<span style="background-color:#EFF0FC;display: block;line-height:1.5"><span style="color: gray;font-size:90%;">class</span> <span style="color: #616AE5; font-weight: bold;font-size: 150%;">GeoDatabase</span><span style="font-style: italic; color: black;font-size: 130%;">(data = <span style="color:#48566B">None</span>, driver = <span style="color:#48566B">None</span>, out_dst = <span style="color:#48566B">None</span>):</span></span>

A GeoDatabase wraps a GDAL Dataset object, and provides functions to access its layers and datasets. Initialize a GeoDatabase object.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>data  = </b> <code>None||str</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    If None, create a new empty GeoDatabase. If str, open the file path as GeoDatabase.</p><p style="text-indent: 1em;"><b>driver  = </b> <code>str||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    If data is None, the driver name to create the GeoDatabase.</p><p style="text-indent: 1em;"><b>out_dst: </b> <code>str||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    If data is None, the output file path to create the GeoDatabase.</p>

---

## Methods 



### add_layer




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">add_layer</span><span style="font-style: italic; color: black;font-size: 120%;">(layer, new_name = <span style="color:#48566B">None</span>, over_write = <span style="color:#48566B">False</span>, **kwargs):</span></span>


Add Layer to GeoDataBase.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>GMALayer: </b> <code>Layer</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Another GMA Layer!</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>new_name  = </b> <code>str||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The new name of the added Layer. Default is the added Layer's name.</p><p style="text-indent: 1em;"><b>OverWrite  = </b> <code>bool</code>. <span style="color:#48566B;">Default False.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Whether to force overwrite the layer with the same name.         </p>

---

### create_layer




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">create_layer</span><span style="font-style: italic; color: black;font-size: 120%;">(name = <span style="color:#48566B">None</span>, crs = <span style="color:#48566B">None</span>, gtype = <span style="color:#48566B">"Polygon"</span>, options = <span style="color:#48566B">{}</span>):</span></span>


Create a new layer in GeoDatabase.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>name  = </b> <code>str||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">the name for the new layer. This should ideally not match any existing layer on the datasource. None for randint.</p><p style="text-indent: 1em;"><b>crs  = </b> <code>int||str||CoordinateReferenceSystem</code>. <span style="color:#48566B;">Default None</span></p><p style="padding-left: 1em;text-indent: 1em;">the coordinate system to use for the new layer, or None if no coordinate system is available.</p><p style="text-indent: 1em;"><b>gtype  = </b> <code>int</code>. <span style="color:#48566B;">Default 'Polygon'.</span></p><p style="padding-left: 1em;text-indent: 1em;">geometry type for the layer. Use 'Polygon' if there are no constraints on the types geometry to be written.</p><p style="text-indent: 1em;"><b>options  = </b> <code>dict/list</code>. <span style="color:#48566B;">Default [].</span></p><p style="padding-left: 1em;text-indent: 1em;">    Driver-specific dict or list of `name=value` options</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code>Layer</code>.</p>

---

### delete_layer




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">delete_layer</span><span style="font-style: italic; color: black;font-size: 120%;">(name_or_id):</span></span>


Delete a Layer in GeoDataBase.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>name_or_id: </b> <code>int||str</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Layer name or ID in GeoDataBase!</p>

---

### get_dataset




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">get_dataset</span><span style="font-style: italic; color: black;font-size: 120%;">(name_or_id = <span style="color:#48566B">0</span>):</span></span>


Get a Dataset in GeoDataBase.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>name_or_id  = </b> <code>int</code>. <span style="color:#48566B;">Default 0.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Dataset ID or name in the GeoDataBase to get.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code>Dataset</code>.</p>

---

### get_layer




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">get_layer</span><span style="font-style: italic; color: black;font-size: 120%;">(name_or_id = <span style="color:#48566B">0</span>):</span></span>


Get a Layer in GeoDatabase.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>name_or_id  = </b> <code>int||str</code>. <span style="color:#48566B;">Default 0.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Layer id or name in the GeoDatabase to get.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code>Layer</code>.</p>

---

### iteritems




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">iteritems</span><span style="font-style: italic; color: black;font-size: 120%;">(category = <span style="color:#48566B">None</span>, **kwargs):</span></span>


Iterate vector layers and raster datasets. -> iter



---

### query




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">query</span><span style="font-style: italic; color: black;font-size: 120%;">(expr, tran_opts = <span style="color:#48566B">{}</span>, **kwargs):</span></span>


Query the vector Layer with a SpatiaLite SQL expression.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>expr: </b> <code>str</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    The sql(ite) query string to evaluate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>tran_opts  = </b> <code>dict</code>. <span style="color:#48566B;">Default {}.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to ._aio.layer.vector_translate.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to ._aio.vrt.VRTGeoDatabase.add_file.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code>Layer</code>.</p>

---

## Property 



### dataset_count


Number of datasets. -> int



---

### dataset_names


Names of datasets. --> <code> list[str]</code>



---

### driver


Database driver. --> <code> VectorDriver/RasterDriver</code>



---

### files


GeoDatabase associated files. --> <code> list[str]</code>



---

### info


Source metadata. -> dict



---

### layer_count


Number of layers. -> int



---

### layer_names


Name of Layers. --> <code> list[str]</code>



---

### link


GeoDatabase path link. --> <code> str</code>



---

### name


GeoDatabase Name. --> <code> str</code>



---