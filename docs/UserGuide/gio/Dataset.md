---
title: Dataset
date: 2026-08-15
sidebar: true
---
<span style="font-size: 120%;font-weight: bold;">gma.gio.Dataset</span>


<span style="background-color:#EFF0FC;display: block;line-height:1.5"><span style="color: gray;font-size:90%;">class</span> <span style="color: #616AE5; font-weight: bold;font-size: 150%;">Dataset</span><span style="font-style: italic; color: black;font-size: 130%;">(data = <span style="color:#48566B">None</span>, shape = <span style="color:#48566B">None</span>, crs = <span style="color:#48566B">None</span>, geo_transform = <span style="color:#48566B">None</span>, dtype = <span style="color:#48566B">None</span>, nodata = <span style="color:#48566B">None</span>, metadata = <span style="color:#48566B">{}</span>, **kwargs):</span></span>

A gma Dataset object. Create a Dataset object!

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>data  = </b> <code style="text-indent: 0">Dataset||ndarray||list||tuple||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">Input data source. Can be a Dataset object, or a NumPy ndarray, list, tuple.</p><p style="padding-left: 1em;text-indent: 1em;">If data is None, a new Dataset will be created according to the shape parameter.</p><p style="text-indent: 1em;"><b>shape  = </b> <code style="text-indent: 0">tuple||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">Shape of the new Dataset. If shape is a 2-tuple, it represents (rows, columns), and the number of bands is 1. If shape is a 3-tuple, it represents (bands, rows, columns).</p><p style="padding-left: 1em;text-indent: 1em;">If shape is None, data must be set.</p><p style="text-indent: 1em;"><b>crs  = </b> <code style="text-indent: 0">str||int||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">The output coordinate system. Can be EPSG, WKT, Proj4, and other types of coordinate characters. Default(None) no coordinate system!</p><p style="text-indent: 1em;"><b>geo_transform  = </b> <code style="text-indent: 0">tuple||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">Geo transformation of the output raster. The affine transformation is not specified by default (None).</p><p style="text-indent: 1em;"><b>dtype  = </b> <code style="text-indent: 0">str||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">A code or string tag for the output raster data type.</p><p style="padding-left: 1em;text-indent: 1em;">Supported data types include: 'Unknown', 'Byte', 'UInt16', 'Int16', 'UInt32', 'Int32','Float32', 'Float64', 'CInt16', 'CInt32', 'CFloat32', 'CFloat64', ...</p><p style="padding-left: 1em;text-indent: 1em;">for more, see const.RaDT_*.</p><p style="padding-left: 1em;text-indent: 1em;">If dtype is None, the data type is determined by the data parameter.</p><p style="text-indent: 1em;"><b>nodata  = </b> <code style="text-indent: 0">float||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Invalid value for output raster. The default is not specified (None).    </p><p style="text-indent: 1em;"><b>metadata  = </b> <code style="text-indent: 0">dict</code>. <span style="color:#48566B;">Default {}.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Metadata to be added.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.dataset.raster_translate.</p>

---

## Methods 



### algebraic




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">algebraic</span><span style="font-style: italic; color: black;font-size: 120%;">(agg_fun, block = <span style="color:#48566B">(None, 2048, 2048)</span>, sel_bands = <span style="color:#48566B">None</span>, scr_nodata = <span style="color:#48566B">None</span>, dst_nodata = <span style="color:#48566B">None</span>, **kwargs):</span></span>


Perform algebraic operations on Dataset.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>agg_fun: </b> <code style="text-indent: 0">def</code>.</p><p style="padding-left: 1em;text-indent: 1em;">Calculate functions. For Example: def calFun(in_ar): return in_ar[0] * 2.1 agg_fun = calFun in_ar: Input NumPy arrays with block`s shape.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>block  = </b> <code style="text-indent: 0">tuple</code>. <span style="color:#48566B;">Default (None, 2048, 2048).</span></p><p style="padding-left: 1em;text-indent: 1em;">    Block sizes for bands, rows, and columns. Use None to represent all.</p><p style="text-indent: 1em;"><b>sel_bands  = </b> <code style="text-indent: 0">list||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">Extract band numbers. Selecting a subset of bands can reduce memory usage.</p><p style="padding-left: 1em;text-indent: 1em;">The default (None) is all bands.</p><p style="text-indent: 1em;"><b>scr_nodata  = </b> <code style="text-indent: 0">float</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Input nodata value. The default is not specified (None).</p><p style="text-indent: 1em;"><b>dst_nodata  = </b> <code style="text-indent: 0">float</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Output nodata value. The default is scr_nodata (None).</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to driver.RasterDriver.create.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Dataset</code>.</p>

---

### clip




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">clip</span><span style="font-style: italic; color: black;font-size: 120%;">(layer, **kwargs):</span></span>


Clip off areas that are not covered by the method layer.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>layer: </b> <code style="text-indent: 0">Layer||Feature||Geometry||str</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    A GMA item use for cliping!</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.dataset.raster_translate</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Dataset</code>.</p>

---

### extent




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">extent</span><span style="font-style: italic; color: black;font-size: 120%;">(**kwargs):</span></span>


The extent of a geometry is the bounding rectangle.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _aio.Layer.Layer.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### gen_lonlat




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">gen_lonlat</span><span style="font-style: italic; color: black;font-size: 120%;">(**kwargs):</span></span>


Generate latitude and longitude raster.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Dataset</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Band 1 is longitude, Band 2 is latitude.</p>

---

### get_palette




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">get_palette</span><span style="font-style: italic; color: black;font-size: 120%;">(bid = <span style="color:#48566B">1</span>):</span></span>


Get palette of the band.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>bid  = </b> <code style="text-indent: 0">int</code>. <span style="color:#48566B;">Default 1.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Number of the element calculation band. Start with 1.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">matplotlib.colors.ListedColormap||None</code>.</p>

---

### isopleth




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">isopleth</span><span style="font-style: italic; color: black;font-size: 120%;">(interval = <span style="color:#48566B">50</span>, base = <span style="color:#48566B">0</span>, band = <span style="color:#48566B">1</span>, **kwargs):</span></span>


Generate a smooth curve formed by connecting points with equal quantity index values.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>interval  = </b> <code style="text-indent: 0">float</code>. <span style="color:#48566B;">Default 50.0.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Isopleth interval.</p><p style="text-indent: 1em;"><b>base  = </b> <code style="text-indent: 0">float</code>. <span style="color:#48566B;">Default 0.0.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The offset from the zero point of the start of the interval.</p><p style="text-indent: 1em;"><b>band  = </b> <code style="text-indent: 0">int</code>. <span style="color:#48566B;">Default 1.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The number of the band to be calculated starts from 1.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _aio.layer.Layer.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### plot




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">plot</span><span style="font-style: italic; color: black;font-size: 120%;">(ax = <span style="color:#48566B">None</span>, bands = <span style="color:#48566B">None</span>, **kwargs):</span></span>


Make plots of Dataset.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>ax  = </b> <code style="text-indent: 0">None||matplotlib.~.AxesSubplot</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    A matplotlib subplot. If None, a default axes will be created. </p><p style="text-indent: 1em;"><b>bands  = </b> <code style="text-indent: 0">int||list||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">The band ID to be plotted. For multi-band data, only 1, 3 (RGB), and 4 (RGBA) bands are supported for selection. Duplicate bands will only keep one. Default is the first four bands.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to matplotlib.image.AxesImage.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>matplotlib.~.AxesSubplot</b>.</p>

---

### reclassify




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">reclassify</span><span style="font-style: italic; color: black;font-size: 120%;">(remap, method = <span style="color:#48566B">"Range"</span>, **kwargs):</span></span>


Reclassifies (or changes) the values in a raster.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>remap: </b> <code style="text-indent: 0">dict</code>.</p><p style="padding-left: 1em;text-indent: 1em;">Remap object. Used to remap an input value or range definition to a new value.</p><p style="padding-left: 1em;text-indent: 1em;">The format is {mapping1: value1, mapping2: value2, ...}.</p><p style="padding-left: 1em;text-indent: 1em;">Note: Items containing NAN will be rejected directly.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>method  = </b> <code style="text-indent: 0">str</code>. <span style="color:#48566B;">Default 'Range'.</span></p><p style="padding-left: 1em;text-indent: 1em;">Specifies how to reclassify the values of the input raster. May be: 'Range' or 'Unique'.</p><p style="padding-left: 1em;text-indent: 1em;">'Range': The data in the range will be mapped.</p><p style="padding-left: 1em;text-indent: 1em;">'Unique': Mapped strictly on a one-to-one basis.</p><p style="padding-left: 1em;text-indent: 1em;">For example: Remap = {1000: 1, 2000: 2, 3000: 3} 1. ReClaMethod = 'Range'.</p><p style="padding-left: 1em;text-indent: 1em;">Data <= 1000: --> 1 1000 < Data <= 1000: --> 2 2000 < Data <= 3000: --> 3 Data > 3000: --> NoData 2. ReClaMethod = 'Unique'.</p><p style="padding-left: 1em;text-indent: 1em;">Data == 1000: --> 1 Data == 2000: --> 2 Data == 3000: --> 3 Other values: --> NoData</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.dataset.raster_translate</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Dataset</code>.</p>

---

### resample




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">resample</span><span style="font-style: italic; color: black;font-size: 120%;">(resolution, method = <span style="color:#48566B">"Nearest"</span>, **kwargs):</span></span>


Change the spatial resolution of the Dataset.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>resolution: </b> <code style="text-indent: 0">float||list</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Resampling resolution(X, Y).</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>method  = </b> <code style="text-indent: 0">str</code>. <span style="color:#48566B;">Default 'Nearest'.</span></p><p style="padding-left: 1em;text-indent: 1em;">Resampling method. Supported resampling methods include: 'Nearest', 'Bilinear', 'Cubic', 'CubicSpline', 'Lanczos', 'Average', 'RMS', 'Mode'.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.dataset.raster_translate</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Dataset</code>.</p>

---

### set_crs




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">set_crs</span><span style="font-style: italic; color: black;font-size: 120%;">(crs):</span></span>


Set dataset's crs!

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>crs: </b> <code style="text-indent: 0">str||int||None</code>.</p><p style="padding-left: 1em;text-indent: 1em;">The output coordinate system. Can be EPSG, WKT, Proj4, and other types of coordinate characters.  Default(None) no coordinate system!</p>

---

### set_gcps




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">set_gcps</span><span style="font-style: italic; color: black;font-size: 120%;">(gcps = <span style="color:#48566B">[(0, 0, 0, 0, 0, '', '')]</span>, crs = <span style="color:#48566B">None</span>):</span></span>


Set GCPs.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>gcps  = </b> <code style="text-indent: 0">list[tuple]</code>. <span style="color:#48566B;">Default [(0, 0, 0, 0, 0, '', '')].</span></p><p style="padding-left: 1em;text-indent: 1em;">list(4 foloat + 2str) of gcps values.</p><p style="padding-left: 1em;text-indent: 1em;">format: [(x(float), y(float), z(float), pixel(float), line(float), info(str, opt), id(str, opt)), ...]</p><p style="text-indent: 1em;"><b>crs  = </b> <code style="text-indent: 0">str||int||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">The gcps' coordinate system. Can be EPSG, WKT, Proj4, and other types of coordinate characters.  Default(None) no coordinate system!</p>

---

### set_geo_transform




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">set_geo_transform</span><span style="font-style: italic; color: black;font-size: 120%;">(geo_transform):</span></span>


Set dataset's geo transform!

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>geo_transform: </b> <code style="text-indent: 0">tuple</code>.</p><p style="padding-left: 1em;text-indent: 1em;">Geo transformation of the output raster(6 float of tuple). format: [x min, x resolution, x rotation, y max, y rotation, y resolution]</p>

---

### set_metadata




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">set_metadata</span><span style="font-style: italic; color: black;font-size: 120%;">(metadata):</span></span>


Set dataset's metadata!

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>metadata: </b> <code style="text-indent: 0">dict</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Metadata to be added. </p>

---

### set_nodata




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">set_nodata</span><span style="font-style: italic; color: black;font-size: 120%;">(nodata, bids = <span style="color:#48566B">None</span>):</span></span>


Set dataset's nodata value of band!

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>nodata: </b> <code style="text-indent: 0">float</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Invalid value for output raster.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>bids  = </b> <code style="text-indent: 0">int||lintofint||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Number of the element calculation band. Start with 1. None for all bands.</p>

---

### set_palette




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">set_palette</span><span style="font-style: italic; color: black;font-size: 120%;">(palette):</span></span>


Set dataset's palette of band!

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>palette: </b> <code style="text-indent: 0">dict||matplotlib.~.cmap||alistofthem</code>.</p><p style="padding-left: 1em;text-indent: 1em;">Palette(color table) of raster bands.</p><p style="padding-left: 1em;text-indent: 1em;">For example: 1.dict({value: (R,G,B,A)}): palette = {10:(200,50,100,255), 20:(200,50,100,255)}.</p><p style="padding-left: 1em;text-indent: 1em;">2.camp: import matplotlib.colors as cor palette = cor.ListedColormap(['r', 'g', 'b'], N = 256)</p>

---

### set_statistics




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">set_statistics</span><span style="font-style: italic; color: black;font-size: 120%;">(statistics, bids = <span style="color:#48566B">None</span>):</span></span>


Set dataset's statistics of band!

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>statistics: </b> <code style="text-indent: 0">None||listoftuple(vmin||vmax||vmean||vstddev)</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Statistics values. None for automatically compute statistics.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>bids  = </b> <code style="text-indent: 0">int||lintofint||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Number of the element calculation band. Start with 1. None for all bands.</p>

---

### shift




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">shift</span><span style="font-style: italic; color: black;font-size: 120%;">(distance = <span style="color:#48566B">1</span>):</span></span>


Shift a distance of the dataset. **Warining: This method will modify the original data.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>distance  = </b> <code style="text-indent: 0">float||list</code>. <span style="color:#48566B;">Default 1.</span></p><p style="padding-left: 1em;text-indent: 1em;">    X, Y shift distance. If a single value is provided, it is assumed that X = Y.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Dataset</code>.</p>

---

### to_bytearray




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">to_bytearray</span><span style="font-style: italic; color: black;font-size: 120%;">(row_off = <span style="color:#48566B">0</span>, column_off = <span style="color:#48566B">0</span>, row_size = <span style="color:#48566B">None</span>, column_size = <span style="color:#48566B">None</span>, sel_bands = <span style="color:#48566B">None</span>):</span></span>


Reads the raster dataset as a bytearray.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>row_off  = </b> <code style="text-indent: 0">int</code>. <span style="color:#48566B;">Default 0.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The starting row of the data to be read.</p><p style="text-indent: 1em;"><b>column_off  = </b> <code style="text-indent: 0">int</code>. <span style="color:#48566B;">Default 0.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The starting column of the data to be read.</p><p style="text-indent: 1em;"><b>row_size  = </b> <code style="text-indent: 0">int</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The number of rows to read from the start row (the row width of the data window). The default (None) is all rows from the start row.</p><p style="text-indent: 1em;"><b>column_size  = </b> <code style="text-indent: 0">int</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The number of columns to read from the start column (the column width of the data window). Default (None) All columns from the start column.</p><p style="text-indent: 1em;"><b>sel_bands  = </b> <code style="text-indent: 0">int||list</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The band number or list of band numbers to be read. Default (None) All bands (numbering starts from 1).</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">bytearray</code>.</p>

---

### to_crs




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">to_crs</span><span style="font-style: italic; color: black;font-size: 120%;">(crs, **kwargs):</span></span>


Reproject to another coordinate system.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>crs: </b> <code style="text-indent: 0">str||int</code>.</p><p style="padding-left: 1em;text-indent: 1em;">The output coordinate system. Can be EPSG, WKT, Proj4, and other types of coordinate characters.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.dataset.raster_translate</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Dataset</code>.</p>

---

### to_dtype




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">to_dtype</span><span style="font-style: italic; color: black;font-size: 120%;">(dtype, **kwargs):</span></span>


Convert the data type of raster.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>dtype: </b> <code style="text-indent: 0">str</code>.</p><p style="padding-left: 1em;text-indent: 1em;">A code or string tag for the output raster data type.</p><p style="padding-left: 1em;text-indent: 1em;">Supported data types include: 'Unknown', 'Byte', 'UInt16', 'Int16', 'UInt32', 'Int32','Float32', 'Float64', 'CInt16', 'CInt32', 'CFloat32', 'CFloat64', ...</p><p style="padding-left: 1em;text-indent: 1em;">for more, see const.RaDT_*.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.dataset.raster_translate</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Dataset</code>.</p>

---

### to_file




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">to_file</span><span style="font-style: italic; color: black;font-size: 120%;">(out_dst, driver = <span style="color:#48566B">"GTiff"</span>, **kwargs):</span></span>


Save Dataset as a raster file.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>out_dst: </b> <code style="text-indent: 0">str</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    The output raster file path.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>driver  = </b> <code style="text-indent: 0">str</code>. <span style="color:#48566B;">Default 'GTiff'.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Output file driver. For other drivers, see gft.RasterSummary().CreatableFormats.    </p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.dataset.raster_translate.</p>

---

### to_layer




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">to_layer</span><span style="font-style: italic; color: black;font-size: 120%;">(field = <span style="color:#48566B">None</span>, band = <span style="color:#48566B">1</span>, gtype = <span style="color:#48566B">"Polygon"</span>, mask = <span style="color:#48566B">False</span>, **kwargs):</span></span>


Translate Dataset to Layer!

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>field  = </b> <code style="text-indent: 0">str</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The name of the output vector field. None for band.</p><p style="text-indent: 1em;"><b>band  = </b> <code style="text-indent: 0">int</code>. <span style="color:#48566B;">Default 1.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Number of the element calculation band. Start with 1.</p><p style="text-indent: 1em;"><b>gtype  = </b> <code style="text-indent: 0">str</code>. <span style="color:#48566B;">Default 'Polygon'.</span></p><p style="padding-left: 1em;text-indent: 1em;">Geometry type! Can be 'Point', 'MultiPoint', 'Line', 'MultiLine', 'MultiPolygon' or 'Polygon'. The default (None) is the automatic geometry type.</p><p style="text-indent: 1em;"><b>mask  = </b> <code style="text-indent: 0">bool</code>. <span style="color:#48566B;">Default False.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Whether to build mask layer(nodata:0, other:1).</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.Layer.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### to_numpy




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">to_numpy</span><span style="font-style: italic; color: black;font-size: 120%;">(row_off = <span style="color:#48566B">0</span>, column_off = <span style="color:#48566B">0</span>, row_size = <span style="color:#48566B">None</span>, column_size = <span style="color:#48566B">None</span>, sel_bands = <span style="color:#48566B">None</span>, mask_nodata = <span style="color:#48566B">False</span>):</span></span>


Reads the raster dataset as a 3-ndim Numpy array.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>row_off  = </b> <code style="text-indent: 0">int</code>. <span style="color:#48566B;">Default 0.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The starting row of the data to be read.</p><p style="text-indent: 1em;"><b>column_off  = </b> <code style="text-indent: 0">int</code>. <span style="color:#48566B;">Default 0.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The starting column of the data to be read.</p><p style="text-indent: 1em;"><b>row_size  = </b> <code style="text-indent: 0">int</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The number of rows to read from the start row (the row width of the data window). The default (None) is all rows from the start row.</p><p style="text-indent: 1em;"><b>column_size  = </b> <code style="text-indent: 0">int</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The number of columns to read from the start column (the column width of the data window). Default (None) All columns from the start column.</p><p style="text-indent: 1em;"><b>sel_bands  = </b> <code style="text-indent: 0">int||list</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The band number or list of band numbers to be read. Default (None) All bands (numbering starts from 1).</p><p style="text-indent: 1em;"><b>mask_nodata  = </b> <code style="text-indent: 0">bool</code>. <span style="color:#48566B;">Default False.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Whether to mask array with nodata value.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">array</code>.</p>

---

### write_array




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">write_array</span><span style="font-style: italic; color: black;font-size: 120%;">(ar, row_off = <span style="color:#48566B">0</span>, column_off = <span style="color:#48566B">0</span>, sel_bands = <span style="color:#48566B">None</span>):</span></span>


Write array to dataset.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>ar: </b> <code style="text-indent: 0">np.ndarray</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    The NumPy array that needs to be set.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>row_off  = </b> <code style="text-indent: 0">int</code>. <span style="color:#48566B;">Default 0.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The starting row of the data to be read.</p><p style="text-indent: 1em;"><b>column_off  = </b> <code style="text-indent: 0">int</code>. <span style="color:#48566B;">Default 0.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The starting column of the data to be read.</p><p style="text-indent: 1em;"><b>sel_bands  = </b> <code style="text-indent: 0">int||list</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The band number or list of band numbers to be read. Default (None) All bands (numbering starts from 1).</p>

---

## Property 



### blocks


<p style="text-indent: 1em;">Fetch the natural block size of this band. --> <code style="text-indent: 0em;"> list(x and y dimensions of block)</code></p>



---

### bounds


<p style="text-indent: 1em;">Bounds. --> <code style="text-indent: 0em;"> tuple</code></p>



---

### compression


<p style="text-indent: 1em;">Raster compression. --> <code style="text-indent: 0em;"> str</code></p>



---

### crs


Raster coordinate reference system. -> CoordinateReferenceSystem



---

### driver


<p style="text-indent: 1em;">Raster driver. --> <code style="text-indent: 0em;"> RasterDriver</code></p>



---

### dtype


<p style="text-indent: 1em;">Raster data type. --> <code style="text-indent: 0em;"> str</code></p>



---

### gcps


<p style="text-indent: 1em;">Raster GCPs. --> <code style="text-indent: 0em;"> tuple</code></p>



---

### geo_transform


<p style="text-indent: 1em;">Raster geo transform. --> <code style="text-indent: 0em;"> tuple</code></p>



---

### link


<p style="text-indent: 1em;">Layer path link. --> <code style="text-indent: 0em;"> str</code></p>



---

### metadata


<p style="text-indent: 1em;">metadata. --> <code style="text-indent: 0em;"> dict</code></p>



---

### name


<p style="text-indent: 1em;">Raster Name. --> <code style="text-indent: 0em;"> str</code></p>



---

### nodata


<p style="text-indent: 1em;">Raster nodata values. --> <code style="text-indent: 0em;"> float</code></p>



---

### resolution


<p style="text-indent: 1em;">X, Y resolution. --> <code style="text-indent: 0em;"> tuple</code></p>



---

### shape


<p style="text-indent: 1em;">Raster shape. --> <code style="text-indent: 0em;"> tuple(band, rows, columns)</code></p>



---

### stats


<p style="text-indent: 1em;">Get stats of all bands. --> <code style="text-indent: 0em;"> dict</code></p>



---