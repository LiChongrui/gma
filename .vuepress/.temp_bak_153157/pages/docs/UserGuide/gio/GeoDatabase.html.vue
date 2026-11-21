<template><div><p style="font-size: 120%;font-weight: bold;">gma.gio.GeoDatabase</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">GeoDatabase</span><span style="font-style: italic; color: black;font-size: 130%;">(data = <span style="color:#48566B">None</span>, driver = <span style="color:#48566B">None</span>, out_dst = <span style="color:#48566B">None</span>):</span></span>
<p>Initialize a GeoDatabase object.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>data </b> = <code style="text-indent: 0em;">None||str</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">If None, create a new empty GeoDatabase. If str, open the file path as GeoDatabase.</p>
<p style="margin-left: 2em;"><b>driver </b> = <code style="text-indent: 0em;">str||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">If data is None, the driver name to create the GeoDatabase.</p>
<p style="margin-left: 2em;"><b>out_dst </b> = <code style="text-indent: 0em;">str||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">If data is None, the output file path to create the GeoDatabase.</p>
<h2 id="method" tabindex="-1"><a class="header-anchor" href="#method"><span>Method</span></a></h2>
<h3 id="add-layer-layer-new-name-none-over-write-false-kwargs" tabindex="-1"><a class="header-anchor" href="#add-layer-layer-new-name-none-over-write-false-kwargs"><span>add_layer<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(layer, new_name = None, over_write = False, **kwargs)</span></span></a></h3>
<p>Add Layer to GeoDataBase.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>GMALayer</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<p style="margin-left: 4em;">Another GMA Layer!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>new_name </b> = <code style="text-indent: 0em;">str||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The new name of the added Layer. Default is the added Layer's name.</p>
<p style="margin-left: 2em;"><b>OverWrite </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Whether to force overwrite the layer with the same name.</p>
<h3 id="create-layer-name-none-crs-none-gtype-polygon-options" tabindex="-1"><a class="header-anchor" href="#create-layer-name-none-crs-none-gtype-polygon-options"><span>create_layer<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(name = None, crs = None, gtype = &quot;Polygon&quot;, options = {})</span></span></a></h3>
<p>Create a new layer in GeoDatabase.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
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
<h3 id="delete-layer-name-or-id" tabindex="-1"><a class="header-anchor" href="#delete-layer-name-or-id"><span>delete_layer<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(name_or_id)</span></span></a></h3>
<p>Delete a Layer in GeoDataBase.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>name_or_id</b>: <code style="text-indent: 0em;">int||str</code>. </p>
<p style="margin-left: 4em;">Layer name or ID in GeoDataBase!</p>
<h3 id="get-dataset-name-or-id-0" tabindex="-1"><a class="header-anchor" href="#get-dataset-name-or-id-0"><span>get_dataset<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(name_or_id = 0)</span></span></a></h3>
<p>Get a Dataset in GeoDataBase.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>name_or_id </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 0</span>. </p>
<p style="margin-left: 4em;">Dataset ID or name in the GeoDataBase to get.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Dataset</code>. </p>
<h3 id="get-layer-name-or-id-0" tabindex="-1"><a class="header-anchor" href="#get-layer-name-or-id-0"><span>get_layer<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(name_or_id = 0)</span></span></a></h3>
<p>Get a Layer in GeoDatabase.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>name_or_id </b> = <code style="text-indent: 0em;">int||str</code>. <span style="color:#48566B;"> Default 0</span>. </p>
<p style="margin-left: 4em;">Layer id or name in the GeoDatabase to get.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="iteritems-category-none-kwargs" tabindex="-1"><a class="header-anchor" href="#iteritems-category-none-kwargs"><span>iteritems<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(category = None, **kwargs)</span></span></a></h3>
<p style="margin-left: 2em;">Iterate vector layers and raster datasets. --> <code style="text-indent: 0em;">iter</code></p>
<h3 id="query-expr-tran-opts-kwargs" tabindex="-1"><a class="header-anchor" href="#query-expr-tran-opts-kwargs"><span>query<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(expr, tran_opts = {}, **kwargs)</span></span></a></h3>
<p>Query the vector Layer with a SpatiaLite SQL expression.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>expr</b>: <code style="text-indent: 0em;">str</code>. </p>
<p style="margin-left: 4em;">The sql(ite) query string to evaluate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>tran_opts </b> = <code style="text-indent: 0em;">dict</code>. <span style="color:#48566B;"> Default {}</span>. </p>
<p style="margin-left: 4em;">Other parameters passed to ._aio.layer.vector_translate.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to ._aio.vrt.VRTGeoDatabase.add_file.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h2 id="property" tabindex="-1"><a class="header-anchor" href="#property"><span>Property</span></a></h2>
<h3 id="dataset-count" tabindex="-1"><a class="header-anchor" href="#dataset-count"><span>dataset_count</span></a></h3>
<p style="margin-left: 2em;">Number of datasets. --> <code style="text-indent: 0em;">int</code></p>
<h3 id="dataset-names" tabindex="-1"><a class="header-anchor" href="#dataset-names"><span>dataset_names</span></a></h3>
<p style="margin-left: 2em;">Names of datasets. --> <code style="text-indent: 0em;">list[str]</code></p>
<h3 id="driver" tabindex="-1"><a class="header-anchor" href="#driver"><span>driver</span></a></h3>
<p style="margin-left: 2em;">Database driver. --> <code style="text-indent: 0em;">VectorDriver/RasterDriver</code></p>
<h3 id="files" tabindex="-1"><a class="header-anchor" href="#files"><span>files</span></a></h3>
<p style="margin-left: 2em;">GeoDatabase associated files. --> <code style="text-indent: 0em;">list[str]</code></p>
<h3 id="info" tabindex="-1"><a class="header-anchor" href="#info"><span>info</span></a></h3>
<p style="margin-left: 2em;">Source metadata. --> <code style="text-indent: 0em;">dict</code></p>
<h3 id="layer-count" tabindex="-1"><a class="header-anchor" href="#layer-count"><span>layer_count</span></a></h3>
<p style="margin-left: 2em;">Number of layers. --> <code style="text-indent: 0em;">int</code></p>
<h3 id="layer-names" tabindex="-1"><a class="header-anchor" href="#layer-names"><span>layer_names</span></a></h3>
<p style="margin-left: 2em;">Name of Layers. --> <code style="text-indent: 0em;">list[str]</code></p>
<h3 id="link" tabindex="-1"><a class="header-anchor" href="#link"><span>link</span></a></h3>
<p style="margin-left: 2em;">GeoDatabase path link. --> <code style="text-indent: 0em;">str</code></p>
<h3 id="name" tabindex="-1"><a class="header-anchor" href="#name"><span>name</span></a></h3>
<p style="margin-left: 2em;">GeoDatabase Name. --> <code style="text-indent: 0em;">str</code></p>
</div></template>


