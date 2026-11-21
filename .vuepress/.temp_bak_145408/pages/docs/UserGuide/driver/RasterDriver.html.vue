<template><div><p style="font-size: 120%;font-weight: bold;">gma.driver.RasterDriver</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">RasterDriver</span><span style="font-style: italic; color: black;font-size: 130%;">(name = <span style="color:#48566B">"GTiff"</span>):</span></span>
<p>Create a raster driver object.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>name </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'GTiff'</span>. </p>
<p style="margin-left: 4em;">A raster driver name.</p>
<h2 id="method" tabindex="-1"><a class="header-anchor" href="#method"><span>Method</span></a></h2>
<h3 id="create-out-dst-bands-ysize-xsize-dtype-float32" tabindex="-1"><a class="header-anchor" href="#create-out-dst-bands-ysize-xsize-dtype-float32"><span>create<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(out_dst, bands, ysize, xsize, dtype = &quot;Float32&quot;)</span></span></a></h3>
<p>Create a new Dataset with this driver.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>out_dst</b>: <code style="text-indent: 0em;">str</code>. </p>
<p style="margin-left: 4em;">Path of the dataset to create. None for memory.</p>
<p style="margin-left: 2em;"><b>xsize</b>: <code style="text-indent: 0em;">int</code>. </p>
<p style="margin-left: 4em;">Width of created raster in pixels.</p>
<p style="margin-left: 2em;"><b>ysize</b>: <code style="text-indent: 0em;">int</code>. </p>
<p style="margin-left: 4em;">Height of created raster in pixels.</p>
<p style="margin-left: 2em;"><b>bands</b>: <code style="text-indent: 0em;">int</code>. </p>
<p style="margin-left: 4em;">Number of bands.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>dtype</b>: <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> str or RaterDataType, Default 'Float32'</span>. </p>
<p style="margin-left: 4em;">Raster data type. Set to `dtypes.DefinedRaterDataTypes` for raster datasets.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Dataset</b></p>
<h3 id="open-in-src-sibling-files" tabindex="-1"><a class="header-anchor" href="#open-in-src-sibling-files"><span>open<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(in_src, sibling_files = [])</span></span></a></h3>
<p>Open a raster file of this driver as a Dataset.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>in_src</b>: <code style="text-indent: 0em;">str</code>. </p>
<p style="margin-left: 4em;">name of the file to open</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>sibling_files</b>: <code style="text-indent: 0em;">list||Default None</code>. </p>
<p style="margin-left: 4em;">A list of filenames that are auxiliary to the main filename.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Dataset</b></p>
<h3 id="set-creation-options-kwargs" tabindex="-1"><a class="header-anchor" href="#set-creation-options-kwargs"><span>set_creation_options<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(**kwargs)</span></span></a></h3>
<p>Set create options! For more, see ~.creation_options_info!</p>
<h3 id="set-open-options-kwargs" tabindex="-1"><a class="header-anchor" href="#set-open-options-kwargs"><span>set_open_options<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(**kwargs)</span></span></a></h3>
<p>Set open options! For more, see ~.open_options_info!</p>
<h2 id="property" tabindex="-1"><a class="header-anchor" href="#property"><span>Property</span></a></h2>
<h3 id="category" tabindex="-1"><a class="header-anchor" href="#category"><span>category</span></a></h3>
<p style="margin-left: 2em;">Driver category. --> <code style="text-indent: 0em;">str</code></p>
<h3 id="compress-modes" tabindex="-1"><a class="header-anchor" href="#compress-modes"><span>compress_modes</span></a></h3>
<p style="margin-left: 2em;">The compression methods supported by the raster driver. --> <code style="text-indent: 0em;">list</code></p>
<h3 id="coordinate-epoch" tabindex="-1"><a class="header-anchor" href="#coordinate-epoch"><span>coordinate_epoch</span></a></h3>
<p style="margin-left: 2em;">Whether the raster driver supports georeferencing. --> <code style="text-indent: 0em;">bool</code></p>
<h3 id="copyable" tabindex="-1"><a class="header-anchor" href="#copyable"><span>copyable</span></a></h3>
<p style="margin-left: 2em;">Whether the target drive supports copy. --> <code style="text-indent: 0em;">bool</code></p>
<h3 id="creatable" tabindex="-1"><a class="header-anchor" href="#creatable"><span>creatable</span></a></h3>
<p style="margin-left: 2em;">Whether the target drive supports creation. --> <code style="text-indent: 0em;">bool</code></p>
<h3 id="creation-dtypes" tabindex="-1"><a class="header-anchor" href="#creation-dtypes"><span>creation_dtypes</span></a></h3>
<p style="margin-left: 2em;">Supported data storage types. --> <code style="text-indent: 0em;">list</code></p>
<h3 id="creation-options" tabindex="-1"><a class="header-anchor" href="#creation-options"><span>creation_options</span></a></h3>
<p style="margin-left: 2em;">Creation options. --> <code style="text-indent: 0em;">dict</code></p>
<h3 id="creation-options-info" tabindex="-1"><a class="header-anchor" href="#creation-options-info"><span>creation_options_info</span></a></h3>
<p style="margin-left: 2em;">creation options. --> <code style="text-indent: 0em;">list</code></p>
<h3 id="extension" tabindex="-1"><a class="header-anchor" href="#extension"><span>extension</span></a></h3>
<p style="margin-left: 2em;">Driver extension. --> <code style="text-indent: 0em;">str</code></p>
<h3 id="extensions" tabindex="-1"><a class="header-anchor" href="#extensions"><span>extensions</span></a></h3>
<p style="margin-left: 2em;">Driver extensions. --> <code style="text-indent: 0em;">list</code></p>
<h3 id="is-raster" tabindex="-1"><a class="header-anchor" href="#is-raster"><span>is_raster</span></a></h3>
<p style="margin-left: 2em;">Is a raster driver. --> <code style="text-indent: 0em;">bool</code></p>
<h3 id="is-vector" tabindex="-1"><a class="header-anchor" href="#is-vector"><span>is_vector</span></a></h3>
<p style="margin-left: 2em;">Is a vector driver. --> <code style="text-indent: 0em;">bool</code></p>
<h3 id="long-name" tabindex="-1"><a class="header-anchor" href="#long-name"><span>long_name</span></a></h3>
<p style="margin-left: 2em;">Driver long name. --> <code style="text-indent: 0em;">str</code></p>
<h3 id="name" tabindex="-1"><a class="header-anchor" href="#name"><span>name</span></a></h3>
<p style="margin-left: 2em;">Driver name. --> <code style="text-indent: 0em;">str</code></p>
<h3 id="open-options" tabindex="-1"><a class="header-anchor" href="#open-options"><span>open_options</span></a></h3>
<p style="margin-left: 2em;">Open options. --> <code style="text-indent: 0em;">dict</code></p>
<h3 id="open-options-info" tabindex="-1"><a class="header-anchor" href="#open-options-info"><span>open_options_info</span></a></h3>
<p style="margin-left: 2em;">open options. --> <code style="text-indent: 0em;">list</code></p>
<h3 id="sub-datasets" tabindex="-1"><a class="header-anchor" href="#sub-datasets"><span>sub_datasets</span></a></h3>
<p style="margin-left: 2em;">Whether the raster driver supports sub dataset. --> <code style="text-indent: 0em;">bool</code></p>
<h3 id="transformable" tabindex="-1"><a class="header-anchor" href="#transformable"><span>transformable</span></a></h3>
<p style="margin-left: 2em;">Whether the raster driver supports transformable. --> <code style="text-indent: 0em;">bool</code></p>
<h3 id="updatable" tabindex="-1"><a class="header-anchor" href="#updatable"><span>updatable</span></a></h3>
<p style="margin-left: 2em;">Whether the target driver can be modified/updated. --> <code style="text-indent: 0em;">bool</code></p>
<h3 id="virtualio" tabindex="-1"><a class="header-anchor" href="#virtualio"><span>virtualio</span></a></h3>
<p style="margin-left: 2em;">Whether the raster driver supports virtual dataset. --> <code style="text-indent: 0em;">bool</code></p>
</div></template>


