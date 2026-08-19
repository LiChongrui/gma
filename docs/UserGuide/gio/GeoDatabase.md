---
title: GeoDatabase
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.gio.GeoDatabase</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">GeoDatabase</span><span style="font-style: italic; color: black;font-size: 130%;">(data = <span style="color:#48566B">None</span>, driver = <span style="color:#48566B">None</span>, out_dst = <span style="color:#48566B">None</span>):</span></span>

<p>Initialize a GeoDatabase object.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>data </b> = <code style="text-indent: 0em;">None||str</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">If None, create a new empty GeoDatabase. If str, open the file path as GeoDatabase.</p>
<p style="margin-left: 2em;"><b>driver </b> = <code style="text-indent: 0em;">str||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">If data is None, the driver name to create the GeoDatabase.</p>
<p style="margin-left: 2em;"><b>out_dst </b> = <code style="text-indent: 0em;">str||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">If data is None, the output file path to create the GeoDatabase.</p>

## Method

### add_layer
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.add_layer</span><span style="font-style: italic; color: black;font-size: 120%;">(layer, new_name = <span style="color:#48566B">None</span>, over_write = <span style="color:#48566B">False</span>, **kwargs):</span></span>

<p>Add Layer to GeoDataBase.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>GMALayer</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<p style="margin-left: 4em;">Another GMA Layer!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>new_name </b> = <code style="text-indent: 0em;">str||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The new name of the added Layer. Default is the added Layer's name.</p>
<p style="margin-left: 2em;"><b>OverWrite </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Whether to force overwrite the layer with the same name.</p>

### create_layer
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.create_layer</span><span style="font-style: italic; color: black;font-size: 120%;">(name = <span style="color:#48566B">None</span>, crs = <span style="color:#48566B">None</span>, gtype = <span style="color:#48566B">"Polygon"</span>, options = <span style="color:#48566B">{}</span>):</span></span>

<p>Create a new layer in GeoDatabase.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>name </b> = <code style="text-indent: 0em;">str||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The name for the new layer. This should ideally not match any existing layer on the datasource. None for randint.</p>
<p style="margin-left: 2em;"><b>crs </b> = <code style="text-indent: 0em;">int||str||CoordinateReferenceSystem</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The coordinate system to use for the new layer, or None if no coordinate system is available.</p>
<p style="margin-left: 2em;"><b>gtype </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 'Polygon'</span>. </p>
<p style="margin-left: 4em;">Geometry type for the layer. Use 'Polygon' if there are no constraints on the types geometry to be written.</p>
<p style="margin-left: 2em;"><b>options </b> = <code style="text-indent: 0em;">dict||list</code>. <span style="color:#48566B;"> Default []</span>. </p>
<p style="margin-left: 4em;">Driver-specific dict or list of `name=value` options.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>

### delete_layer
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.delete_layer</span><span style="font-style: italic; color: black;font-size: 120%;">(name_or_id):</span></span>

<p>Delete a Layer in GeoDataBase.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>name_or_id</b>: <code style="text-indent: 0em;">int||str</code>. </p>
<p style="margin-left: 4em;">Layer name or ID in GeoDataBase!</p>

### get_dataset
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.get_dataset</span><span style="font-style: italic; color: black;font-size: 120%;">(name_or_id = <span style="color:#48566B">0</span>):</span></span>

<p>Get a Dataset in GeoDataBase.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>name_or_id </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 0</span>. </p>
<p style="margin-left: 4em;">Dataset ID or name in the GeoDataBase to get.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Dataset</code>. </p>

### get_layer
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.get_layer</span><span style="font-style: italic; color: black;font-size: 120%;">(name_or_id = <span style="color:#48566B">0</span>):</span></span>

<p>Get a Layer in GeoDatabase.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>name_or_id </b> = <code style="text-indent: 0em;">int||str</code>. <span style="color:#48566B;"> Default 0</span>. </p>
<p style="margin-left: 4em;">Layer id or name in the GeoDatabase to get.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>

### iteritems
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.iteritems</span><span style="font-style: italic; color: black;font-size: 120%;">(category = <span style="color:#48566B">None</span>, **kwargs):</span></span>

<p style="margin-left: 2em;">Iterate vector layers and raster datasets. --> <code style="text-indent: 0em;">iter</code></p>

### query
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.query</span><span style="font-style: italic; color: black;font-size: 120%;">(expr, tran_opts = <span style="color:#48566B">{}</span>, **kwargs):</span></span>

<p>Query the vector Layer with a SpatiaLite SQL expression.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>expr</b>: <code style="text-indent: 0em;">str</code>. </p>
<p style="margin-left: 4em;">The sql(ite) query string to evaluate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>tran_opts </b> = <code style="text-indent: 0em;">dict</code>. <span style="color:#48566B;"> Default {}</span>. </p>
<p style="margin-left: 4em;">Other parameters passed to ._aio.layer.vector_translate.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to ._aio.vrt.VRTGeoDatabase.add_file.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>

## Property

### dataset_count
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.dataset_count</span><span style=""></span></span>

<p style="margin-left: 2em;">Number of datasets. --> <code style="text-indent: 0em;">int</code></p>

### dataset_names
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.dataset_names</span><span style=""></span></span>

<p style="margin-left: 2em;">Names of datasets. --> <code style="text-indent: 0em;">list[str]</code></p>

### driver
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.driver</span><span style=""></span></span>

<p style="margin-left: 2em;">Database driver. --> <code style="text-indent: 0em;">VectorDriver/RasterDriver</code></p>

### files
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.files</span><span style=""></span></span>

<p style="margin-left: 2em;">GeoDatabase associated files. --> <code style="text-indent: 0em;">list[str]</code></p>

### info
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.info</span><span style=""></span></span>

<p style="margin-left: 2em;">Source metadata. --> <code style="text-indent: 0em;">dict</code></p>

### layer_count
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.layer_count</span><span style=""></span></span>

<p style="margin-left: 2em;">Number of layers. --> <code style="text-indent: 0em;">int</code></p>

### layer_names
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.layer_names</span><span style=""></span></span>

<p style="margin-left: 2em;">Name of Layers. --> <code style="text-indent: 0em;">list[str]</code></p>

### link
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.link</span><span style=""></span></span>

<p style="margin-left: 2em;">GeoDatabase path link. --> <code style="text-indent: 0em;">str</code></p>

### name
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.name</span><span style=""></span></span>

<p style="margin-left: 2em;">GeoDatabase Name. --> <code style="text-indent: 0em;">str</code></p>
