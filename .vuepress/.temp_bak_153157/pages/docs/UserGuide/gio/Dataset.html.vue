<template><div><p style="font-size: 120%;font-weight: bold;">gma.gio.Dataset</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">Dataset</span><span style="font-style: italic; color: black;font-size: 130%;">(data = <span style="color:#48566B">None</span>, shape = <span style="color:#48566B">None</span>, crs = <span style="color:#48566B">None</span>, geo_transform = <span style="color:#48566B">None</span>, dtype = <span style="color:#48566B">None</span>, nodata = <span style="color:#48566B">None</span>, metadata = <span style="color:#48566B">{}</span>, **kwargs):</span></span>
<p>Create a Dataset object!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>data </b> = <code style="text-indent: 0em;">Dataset||ndarray||list||tuple||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Input data source. Can be a Dataset object, or a NumPy ndarray, list, tuple.</p>
<p style="margin-left: 4em;">If data is None, a new Dataset will be created according to the shape parameter.</p>
<p style="margin-left: 2em;"><b>shape </b> = <code style="text-indent: 0em;">tuple||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Shape of the new Dataset. If shape is a 2-tuple, it represents (rows, columns), and the number of bands is 1. If shape is a 3-tuple, it represents (bands, rows, columns).</p>
<p style="margin-left: 4em;">If shape is None, data must be set.</p>
<p style="margin-left: 2em;"><b>crs </b> = <code style="text-indent: 0em;">str||int||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The output coordinate system. Can be EPSG, WKT, Proj4, and other types of coordinate characters. Default(None) no coordinate system!</p>
<p style="margin-left: 2em;"><b>geo_transform </b> = <code style="text-indent: 0em;">tuple||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Geo transformation of the output raster. The affine transformation is not specified by default (None).</p>
<p style="margin-left: 2em;"><b>dtype </b> = <code style="text-indent: 0em;">str||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">A code or string tag for the output raster data type.</p>
<p style="margin-left: 4em;">Supported data types include:</p>
<p style="margin-left: 6em;">'Unknown', 'Byte', 'UInt16', 'Int16', 'UInt32', 'Int32','Float32', 'Float64', 'CInt16', 'CInt32', 'CFloat32', 'CFloat64', ...</p>
<p style="margin-left: 4em;">For more, see const.RaDT_*.</p>
<p style="margin-left: 4em;">If dtype is None, the data type is determined by the data parameter.</p>
<p style="margin-left: 2em;"><b>nodata </b> = <code style="text-indent: 0em;">float||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Invalid value for output raster. The default is not specified (None).</p>
<p style="margin-left: 2em;"><b>metadata </b> = <code style="text-indent: 0em;">dict</code>. <span style="color:#48566B;"> Default {}</span>. </p>
<p style="margin-left: 4em;">Metadata to be added.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.dataset.raster_translate.</p>
<h2 id="method" tabindex="-1"><a class="header-anchor" href="#method"><span>Method</span></a></h2>
<h3 id="algebraic-agg-fun-block-none-2048-2048-sel-bands-none-scr-nodata-none-dst-nodata-none-kwargs" tabindex="-1"><a class="header-anchor" href="#algebraic-agg-fun-block-none-2048-2048-sel-bands-none-scr-nodata-none-dst-nodata-none-kwargs"><span>algebraic<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(agg_fun, block = (None, 2048, 2048), sel_bands = None, scr_nodata = None, dst_nodata = None, **kwargs)</span></span></a></h3>
<p>Perform algebraic operations on Dataset.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>agg_fun</b>: <code style="text-indent: 0em;">def</code>. </p>
<p style="margin-left: 4em;">Calculate functions. For Example:</p>
<div class="language-python line-numbers-mode" data-highlighter="prismjs" data-ext="py" data-title="py"><pre v-pre><code><span class="line"><span class="token keyword">def</span> <span class="token function">func</span><span class="token punctuation">(</span>in_ar<span class="token punctuation">)</span><span class="token punctuation">:</span></span>
<span class="line">    <span class="token keyword">return</span> in_ar<span class="token punctuation">[</span><span class="token number">0</span><span class="token punctuation">]</span> <span class="token operator">*</span> <span class="token number">2.1</span></span>
<span class="line">agg_fun <span class="token operator">=</span> func</span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p style="margin-left: 4em;">in_ar: Input NumPy arrays with block`s shape.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>block </b> = <code style="text-indent: 0em;">tuple</code>. <span style="color:#48566B;"> Default (None, 2048, 2048)</span>. </p>
<p style="margin-left: 4em;">Block sizes for bands, rows, and columns. Use None to represent all.</p>
<p style="margin-left: 2em;"><b>sel_bands </b> = <code style="text-indent: 0em;">list||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Extract band numbers. Selecting a subset of bands can reduce memory usage.</p>
<p style="margin-left: 4em;">The default (None) is all bands.</p>
<p style="margin-left: 2em;"><b>scr_nodata </b> = <code style="text-indent: 0em;">float</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Input nodata value. The default is not specified (None).</p>
<p style="margin-left: 2em;"><b>dst_nodata </b> = <code style="text-indent: 0em;">float</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Output nodata value. The default is scr_nodata (None).</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to driver.RasterDriver.create.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Dataset</code>. </p>
<h3 id="clip-layer-kwargs" tabindex="-1"><a class="header-anchor" href="#clip-layer-kwargs"><span>clip<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(layer, **kwargs)</span></span></a></h3>
<p>Clip off areas that are not covered by the method layer.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>layer</b>: <code style="text-indent: 0em;">Layer||Feature||Geometry||str</code>. </p>
<p style="margin-left: 4em;">A GMA item use for cliping!</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.dataset.raster_translate</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Dataset</code>. </p>
<h3 id="extent-kwargs" tabindex="-1"><a class="header-anchor" href="#extent-kwargs"><span>extent<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(**kwargs)</span></span></a></h3>
<p>The extent of a geometry is the bounding rectangle.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _aio.Layer.Layer.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="gen-lonlat-kwargs" tabindex="-1"><a class="header-anchor" href="#gen-lonlat-kwargs"><span>gen_lonlat<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(**kwargs)</span></span></a></h3>
<p>Generate latitude and longitude raster.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Dataset</code>. </p>
<p style="margin-left: 4em;">Band 1 is longitude, Band 2 is latitude.</p>
<h3 id="get-palette-bid-1" tabindex="-1"><a class="header-anchor" href="#get-palette-bid-1"><span>get_palette<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(bid = 1)</span></span></a></h3>
<p>Get palette of the band.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>bid </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 1</span>. </p>
<p style="margin-left: 4em;">Number of the element calculation band. Start with 1.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">matplotlib</code>. <span style="color:#48566B;">colors.ListedColormap or None</span>. </p>
<h3 id="isopleth-interval-50-base-0-band-1-kwargs" tabindex="-1"><a class="header-anchor" href="#isopleth-interval-50-base-0-band-1-kwargs"><span>isopleth<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(interval = 50, base = 0, band = 1, **kwargs)</span></span></a></h3>
<p>Generate a smooth curve formed by connecting points with equal quantity index values.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>interval </b> = <code style="text-indent: 0em;">float</code>. <span style="color:#48566B;"> Default 50.0</span>. </p>
<p style="margin-left: 4em;">Isopleth interval.</p>
<p style="margin-left: 2em;"><b>base </b> = <code style="text-indent: 0em;">float</code>. <span style="color:#48566B;"> Default 0.0</span>. </p>
<p style="margin-left: 4em;">The offset from the zero point of the start of the interval.</p>
<p style="margin-left: 2em;"><b>band </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 1</span>. </p>
<p style="margin-left: 4em;">The number of the band to be calculated starts from 1.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _aio.layer.Layer.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="plot-ax-none-bands-none-kwargs" tabindex="-1"><a class="header-anchor" href="#plot-ax-none-bands-none-kwargs"><span>plot<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(ax = None, bands = None, **kwargs)</span></span></a></h3>
<p>Make plots of Dataset.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>ax </b> = <code style="text-indent: 0em;">None||matplotlib</code>. <span style="color:#48566B;">~.AxesSubplot. Default None</span>. </p>
<p style="margin-left: 4em;">A matplotlib subplot. If None, a default axes will be created.</p>
<p style="margin-left: 2em;"><b>bands </b> = <code style="text-indent: 0em;">int||list||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The band ID to be plotted. For multi-band data, only 1, 3 (RGB), and 4 (RGBA) bands are supported for selection. Duplicate bands will only keep one. Default is the first four bands.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to matplotlib.image.AxesImage.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>matplotlib.~.AxesSubplot</b></p>
<h3 id="reclassify-remap-method-range-kwargs" tabindex="-1"><a class="header-anchor" href="#reclassify-remap-method-range-kwargs"><span>reclassify<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(remap, method = &quot;Range&quot;, **kwargs)</span></span></a></h3>
<p>Reclassifies (or changes) the values in a raster.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>remap</b>: <code style="text-indent: 0em;">dict</code>. </p>
<p style="margin-left: 4em;">Remap object. Used to remap an input value or range definition to a new value.</p>
<p style="margin-left: 4em;">The format is {mapping1: value1, mapping2: value2, ...}.</p>
<p style="margin-left: 4em;">Note: Items containing NAN will be rejected directly.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>method </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'Range'</span>. </p>
<p style="margin-left: 4em;">Specifies how to reclassify the values of the input raster. May be: 'Range' or 'Unique'.</p>
<p style="margin-left: 4em;">'Range': The data in the range will be mapped.</p>
<p style="margin-left: 4em;">'Unique': Mapped strictly on a one-to-one basis.</p>
<p style="margin-left: 4em;">For example:</p>
<p style="margin-left: 6em;">Remap = {1000: 1, 2000: 2, 3000: 3} 1. ReClaMethod = 'Range'.</p>
<p style="margin-left: 2em;">Data <= 1000: --> <code style="text-indent: 0em;">1</code></p>
<p style="margin-left: 2em;">1000 < Data <= 1000: --> <code style="text-indent: 0em;">2</code></p>
<p style="margin-left: 2em;">2000 < Data <= 3000: --> <code style="text-indent: 0em;">3</code></p>
<p style="margin-left: 2em;">Data > 3000: --> <code style="text-indent: 0em;">NoData</code></p>
<p style="margin-left: 6em;">2. ReClaMethod = 'Unique'.</p>
<p style="margin-left: 2em;">Data == 1000: --> <code style="text-indent: 0em;">1</code></p>
<p style="margin-left: 2em;">Data == 2000: --> <code style="text-indent: 0em;">2</code></p>
<p style="margin-left: 2em;">Data == 3000: --> <code style="text-indent: 0em;">3</code></p>
<p style="margin-left: 2em;">Other values: --> <code style="text-indent: 0em;">NoData</code></p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.dataset.raster_translate</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Dataset</code>. </p>
<h3 id="resample-resolution-method-nearest-kwargs" tabindex="-1"><a class="header-anchor" href="#resample-resolution-method-nearest-kwargs"><span>resample<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(resolution, method = &quot;Nearest&quot;, **kwargs)</span></span></a></h3>
<p>Change the spatial resolution of the Dataset.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>resolution</b>: <code style="text-indent: 0em;">float||list</code>. </p>
<p style="margin-left: 4em;">Resampling resolution(X, Y).</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>method </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'Nearest'</span>. </p>
<p style="margin-left: 4em;">Resampling method. Supported resampling methods include:</p>
<p style="margin-left: 4em;">'Nearest', 'Bilinear', 'Cubic', 'CubicSpline', 'Lanczos', 'Average', 'RMS', 'Mode'.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.dataset.raster_translate</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Dataset</code>. </p>
<h3 id="set-crs-crs" tabindex="-1"><a class="header-anchor" href="#set-crs-crs"><span>set_crs<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(crs)</span></span></a></h3>
<p>Set dataset's crs!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>crs</b>: <code style="text-indent: 0em;">str||int||None</code>. </p>
<p style="margin-left: 4em;">The output coordinate system. Can be EPSG, WKT, Proj4, and other types of coordinate characters.  Default(None) no coordinate system!</p>
<h3 id="set-gcps-gcps-0-0-0-0-0-crs-none" tabindex="-1"><a class="header-anchor" href="#set-gcps-gcps-0-0-0-0-0-crs-none"><span>set_gcps<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(gcps = [(0, 0, 0, 0, 0, '', '')], crs = None)</span></span></a></h3>
<p>Set GCPs.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>gcps </b> = <code style="text-indent: 0em;">list[tuple]</code>. <span style="color:#48566B;"> Default [(0, 0, 0, 0, 0, '', '')]</span>. </p>
<p style="margin-left: 4em;">list(4 foloat + 2str) of gcps values.</p>
<p style="margin-left: 4em;">format:</p>
<p style="margin-left: 6em;">[(x(float), y(float), z(float), pixel(float), line(float), info(str, opt), id(str, opt)), ...]</p>
<p style="margin-left: 2em;"><b>crs </b> = <code style="text-indent: 0em;">str||int||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The gcps' coordinate system. Can be EPSG, WKT, Proj4, and other types of coordinate characters.  Default(None) no coordinate system!</p>
<h3 id="set-geo-transform-geo-transform" tabindex="-1"><a class="header-anchor" href="#set-geo-transform-geo-transform"><span>set_geo_transform<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(geo_transform)</span></span></a></h3>
<p>Set dataset's geo transform!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>geo_transform</b>: <code style="text-indent: 0em;">tuple</code>. </p>
<p style="margin-left: 4em;">Geo transformation of the output raster(6 float of tuple). format:</p>
<p style="margin-left: 6em;">[x min, x resolution, x rotation, y max, y rotation, y resolution]</p>
<h3 id="set-metadata-metadata" tabindex="-1"><a class="header-anchor" href="#set-metadata-metadata"><span>set_metadata<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(metadata)</span></span></a></h3>
<p>Set dataset's metadata!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>metadata</b>: <code style="text-indent: 0em;">dict</code>. </p>
<p style="margin-left: 4em;">Metadata to be added.</p>
<h3 id="set-nodata-nodata-bids-none" tabindex="-1"><a class="header-anchor" href="#set-nodata-nodata-bids-none"><span>set_nodata<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(nodata, bids = None)</span></span></a></h3>
<p>Set dataset's nodata value of band!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>nodata</b>: <code style="text-indent: 0em;">float</code>. </p>
<p style="margin-left: 4em;">Invalid value for output raster.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>bids </b> = <code style="text-indent: 0em;">int||lint of int||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Number of the element calculation band. Start with 1. None for all bands.</p>
<h3 id="set-palette-palette" tabindex="-1"><a class="header-anchor" href="#set-palette-palette"><span>set_palette<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(palette)</span></span></a></h3>
<p>Set dataset's palette of band!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>palette</b>: <code style="text-indent: 0em;">dict||matplotlib</code>. <span style="color:#48566B;">~.cmap or a list of them</span>. </p>
<p style="margin-left: 4em;">Palette(color table) of raster bands.</p>
<p style="margin-left: 4em;">For example:</p>
<p style="margin-left: 6em;">1.dict({value: (R,G,B,A)}):</p>
<p style="margin-left: 8em;">palette = {10:(200,50,100,255), 20:(200,50,100,255)}.</p>
<p style="margin-left: 6em;">2.camp:</p>
<p style="margin-left: 8em;">import matplotlib.colors as cor palette = cor.ListedColormap(['r', 'g', 'b'], N = 256)</p>
<h3 id="set-statistics-statistics-bids-none" tabindex="-1"><a class="header-anchor" href="#set-statistics-statistics-bids-none"><span>set_statistics<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(statistics, bids = None)</span></span></a></h3>
<p>Set dataset's statistics of band!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>statistics</b>: <code style="text-indent: 0em;">None||list of tuple(vmin||vmax||vmean||vstddev)</code>. </p>
<p style="margin-left: 4em;">Statistics values. None for automatically compute statistics.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>bids </b> = <code style="text-indent: 0em;">int||lint of int||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Number of the element calculation band. Start with 1. None for all bands.</p>
<h3 id="shift-distance-1" tabindex="-1"><a class="header-anchor" href="#shift-distance-1"><span>shift<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(distance = 1)</span></span></a></h3>
<p>Shift a distance of the dataset. **Warining: This method will modify the original data.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>distance </b> = <code style="text-indent: 0em;">float||list</code>. <span style="color:#48566B;"> Default 1</span>. </p>
<p style="margin-left: 4em;">X, Y shift distance. If a single value is provided, it is assumed that X = Y.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Dataset</code>. </p>
<h3 id="to-bytearray-row-off-0-column-off-0-row-size-none-column-size-none-sel-bands-none" tabindex="-1"><a class="header-anchor" href="#to-bytearray-row-off-0-column-off-0-row-size-none-column-size-none-sel-bands-none"><span>to_bytearray<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(row_off = 0, column_off = 0, row_size = None, column_size = None, sel_bands = None)</span></span></a></h3>
<p>Reads the raster dataset as a bytearray.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>row_off </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 0</span>. </p>
<p style="margin-left: 4em;">The starting row of the data to be read.</p>
<p style="margin-left: 2em;"><b>column_off </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 0</span>. </p>
<p style="margin-left: 4em;">The starting column of the data to be read.</p>
<p style="margin-left: 2em;"><b>row_size </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The number of rows to read from the start row (the row width of the data window). The default (None) is all rows from the start row.</p>
<p style="margin-left: 2em;"><b>column_size </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The number of columns to read from the start column (the column width of the data window). Default (None) All columns from the start column.</p>
<p style="margin-left: 2em;"><b>sel_bands </b> = <code style="text-indent: 0em;">int||list</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The band number or list of band numbers to be read. Default (None) All bands (numbering starts from 1).</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">bytearray</code>. </p>
<h3 id="to-crs-crs-kwargs" tabindex="-1"><a class="header-anchor" href="#to-crs-crs-kwargs"><span>to_crs<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(crs, **kwargs)</span></span></a></h3>
<p>Reproject to another coordinate system.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>crs</b>: <code style="text-indent: 0em;">str||int</code>. </p>
<p style="margin-left: 4em;">The output coordinate system. Can be EPSG, WKT, Proj4, and other types of coordinate characters.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.dataset.raster_translate</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Dataset</code>. </p>
<h3 id="to-dtype-dtype-kwargs" tabindex="-1"><a class="header-anchor" href="#to-dtype-dtype-kwargs"><span>to_dtype<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(dtype, **kwargs)</span></span></a></h3>
<p>Convert the data type of raster.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>dtype</b>: <code style="text-indent: 0em;">str</code>. </p>
<p style="margin-left: 4em;">A code or string tag for the output raster data type.</p>
<p style="margin-left: 4em;">Supported data types include:</p>
<p style="margin-left: 4em;">'Unknown', 'Byte', 'UInt16', 'Int16', 'UInt32', 'Int32','Float32', 'Float64', 'CInt16', 'CInt32', 'CFloat32', 'CFloat64', ...</p>
<p style="margin-left: 4em;">for more, see const.RaDT_*.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.dataset.raster_translate</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Dataset</code>. </p>
<h3 id="to-file-out-dst-driver-gtiff-kwargs" tabindex="-1"><a class="header-anchor" href="#to-file-out-dst-driver-gtiff-kwargs"><span>to_file<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(out_dst, driver = &quot;GTiff&quot;, **kwargs)</span></span></a></h3>
<p>Save Dataset as a raster file.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>out_dst</b>: <code style="text-indent: 0em;">str</code>. </p>
<p style="margin-left: 4em;">The output raster file path.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>driver </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'GTiff'</span>. </p>
<p style="margin-left: 4em;">Output file driver. For other drivers, see gft.RasterSummary().CreatableFormats.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.dataset.raster_translate.</p>
<h3 id="to-layer-field-none-band-1-gtype-polygon-mask-false-kwargs" tabindex="-1"><a class="header-anchor" href="#to-layer-field-none-band-1-gtype-polygon-mask-false-kwargs"><span>to_layer<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(field = None, band = 1, gtype = &quot;Polygon&quot;, mask = False, **kwargs)</span></span></a></h3>
<p>Translate Dataset to Layer!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>field </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The name of the output vector field. None for band.</p>
<p style="margin-left: 2em;"><b>band </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 1</span>. </p>
<p style="margin-left: 4em;">Number of the element calculation band. Start with 1.</p>
<p style="margin-left: 2em;"><b>gtype </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'Polygon'</span>. </p>
<p style="margin-left: 4em;">Geometry type! Can be 'Point', 'MultiPoint', 'Line', 'MultiLine', 'MultiPolygon' or 'Polygon'. The default (None) is the automatic geometry type.</p>
<p style="margin-left: 2em;"><b>mask </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Whether to build mask layer(nodata:0, other:1).</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.Layer.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="to-numpy-row-off-0-column-off-0-row-size-none-column-size-none-sel-bands-none-mask-nodata-false" tabindex="-1"><a class="header-anchor" href="#to-numpy-row-off-0-column-off-0-row-size-none-column-size-none-sel-bands-none-mask-nodata-false"><span>to_numpy<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(row_off = 0, column_off = 0, row_size = None, column_size = None, sel_bands = None, mask_nodata = False)</span></span></a></h3>
<p>Reads the raster dataset as a 3-ndim Numpy array.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>row_off </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 0</span>. </p>
<p style="margin-left: 4em;">The starting row of the data to be read.</p>
<p style="margin-left: 2em;"><b>column_off </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 0</span>. </p>
<p style="margin-left: 4em;">The starting column of the data to be read.</p>
<p style="margin-left: 2em;"><b>row_size </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The number of rows to read from the start row (the row width of the data window). The default (None) is all rows from the start row.</p>
<p style="margin-left: 2em;"><b>column_size </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The number of columns to read from the start column (the column width of the data window). Default (None) All columns from the start column.</p>
<p style="margin-left: 2em;"><b>sel_bands </b> = <code style="text-indent: 0em;">int||list</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The band number or list of band numbers to be read. Default (None) All bands (numbering starts from 1).</p>
<p style="margin-left: 2em;"><b>mask_nodata </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Whether to mask array with nodata value.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">array</code>. </p>
<h3 id="write-array-ar-row-off-0-column-off-0-sel-bands-none" tabindex="-1"><a class="header-anchor" href="#write-array-ar-row-off-0-column-off-0-sel-bands-none"><span>write_array<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(ar, row_off = 0, column_off = 0, sel_bands = None)</span></span></a></h3>
<p>Write array to dataset.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>ar</b>: <code style="text-indent: 0em;">np</code>. <span style="color:#48566B;">ndarray</span>. </p>
<p style="margin-left: 4em;">The NumPy array that needs to be set.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>row_off </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 0</span>. </p>
<p style="margin-left: 4em;">The starting row of the data to be read.</p>
<p style="margin-left: 2em;"><b>column_off </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 0</span>. </p>
<p style="margin-left: 4em;">The starting column of the data to be read.</p>
<p style="margin-left: 2em;"><b>sel_bands </b> = <code style="text-indent: 0em;">int||list</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The band number or list of band numbers to be read. Default (None) All bands (numbering starts from 1).</p>
<h2 id="property" tabindex="-1"><a class="header-anchor" href="#property"><span>Property</span></a></h2>
<h3 id="blocks" tabindex="-1"><a class="header-anchor" href="#blocks"><span>blocks</span></a></h3>
<p style="margin-left: 2em;">Fetch the natural block size of this band. --> <code style="text-indent: 0em;">list(x and y dimensions of block)</code></p>
<h3 id="bounds" tabindex="-1"><a class="header-anchor" href="#bounds"><span>bounds</span></a></h3>
<p style="margin-left: 2em;">Bounds. --> <code style="text-indent: 0em;">tuple</code></p>
<h3 id="compression" tabindex="-1"><a class="header-anchor" href="#compression"><span>compression</span></a></h3>
<p style="margin-left: 2em;">Raster compression. --> <code style="text-indent: 0em;">str</code></p>
<h3 id="crs" tabindex="-1"><a class="header-anchor" href="#crs"><span>crs</span></a></h3>
<p style="margin-left: 2em;">Raster coordinate reference system. --> <code style="text-indent: 0em;">CoordinateReferenceSystem</code></p>
<h3 id="driver" tabindex="-1"><a class="header-anchor" href="#driver"><span>driver</span></a></h3>
<p style="margin-left: 2em;">Raster driver. --> <code style="text-indent: 0em;">RasterDriver</code></p>
<h3 id="dtype" tabindex="-1"><a class="header-anchor" href="#dtype"><span>dtype</span></a></h3>
<p style="margin-left: 2em;">Raster data type. --> <code style="text-indent: 0em;">str</code></p>
<h3 id="gcps" tabindex="-1"><a class="header-anchor" href="#gcps"><span>gcps</span></a></h3>
<p style="margin-left: 2em;">Raster GCPs. --> <code style="text-indent: 0em;">tuple</code></p>
<h3 id="geo-transform" tabindex="-1"><a class="header-anchor" href="#geo-transform"><span>geo_transform</span></a></h3>
<p style="margin-left: 2em;">Raster geo transform. --> <code style="text-indent: 0em;">tuple</code></p>
<h3 id="link" tabindex="-1"><a class="header-anchor" href="#link"><span>link</span></a></h3>
<p style="margin-left: 2em;">Layer path link. --> <code style="text-indent: 0em;">str</code></p>
<h3 id="metadata" tabindex="-1"><a class="header-anchor" href="#metadata"><span>metadata</span></a></h3>
<p style="margin-left: 2em;">metadata. --> <code style="text-indent: 0em;">dict</code></p>
<h3 id="name" tabindex="-1"><a class="header-anchor" href="#name"><span>name</span></a></h3>
<p style="margin-left: 2em;">Raster Name. --> <code style="text-indent: 0em;">str</code></p>
<h3 id="nodata" tabindex="-1"><a class="header-anchor" href="#nodata"><span>nodata</span></a></h3>
<p style="margin-left: 2em;">Raster nodata values. --> <code style="text-indent: 0em;">float</code></p>
<h3 id="resolution" tabindex="-1"><a class="header-anchor" href="#resolution"><span>resolution</span></a></h3>
<p style="margin-left: 2em;">X, Y resolution. --> <code style="text-indent: 0em;">tuple</code></p>
<h3 id="shape" tabindex="-1"><a class="header-anchor" href="#shape"><span>shape</span></a></h3>
<p style="margin-left: 2em;">Raster shape. --> <code style="text-indent: 0em;">tuple(band, rows, columns)</code></p>
<h3 id="stats" tabindex="-1"><a class="header-anchor" href="#stats"><span>stats</span></a></h3>
<p style="margin-left: 2em;">Get stats of all bands. --> <code style="text-indent: 0em;">dict</code></p>
<h2 id="example" tabindex="-1"><a class="header-anchor" href="#example"><span>Example</span></a></h2>
<div class="language-python line-numbers-mode" data-highlighter="prismjs" data-ext="py" data-title="py"><pre v-pre><code><span class="line"><span class="token keyword">from</span> gma <span class="token keyword">import</span> io</span>
<span class="line"></span>
<span class="line"><span class="token comment"># Open a raster dataset</span></span>
<span class="line">ds <span class="token operator">=</span> io<span class="token punctuation">.</span>Dataset<span class="token punctuation">(</span><span class="token string">'demo.tif'</span><span class="token punctuation">)</span></span>
<span class="line"></span>
<span class="line"><span class="token comment"># Save it to a new file (GeoTIFF by default)</span></span>
<span class="line">ds<span class="token punctuation">.</span>to_file<span class="token punctuation">(</span><span class="token string">'result.tif'</span><span class="token punctuation">)</span></span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div></div></template>


