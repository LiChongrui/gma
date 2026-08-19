---
title: VirtualRasterDataset
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.gio.VirtualRasterDataset</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">VirtualRasterDataset</span><span style="font-style: italic; color: black;font-size: 130%;">(gma_dses, **kwargs):</span></span>

<p>Create a VRT Dataset object!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>gma_dses</b>: <code style="text-indent: 0em;">str||list[str/Dataset]</code>. </p>
<p style="margin-left: 4em;">Datasets or raster file paths.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.dataset.raster_translate.</p>

## Method

### algebraic
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.algebraic</span><span style="font-style: italic; color: black;font-size: 120%;">(agg_fun, block = <span style="color:#48566B">(None, 2048, 2048)</span>, sel_bands = <span style="color:#48566B">None</span>, scr_nodata = <span style="color:#48566B">None</span>, dst_nodata = <span style="color:#48566B">None</span>, **kwargs):</span></span>

<p>Perform algebraic operations on Dataset.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>agg_fun</b>: <code style="text-indent: 0em;">def</code>. </p>
<p style="margin-left: 4em;">Calculate functions. For Example:</p>

```python
def func(in_ar):
    return in_ar[0] * 2.1
agg_fun = func
```

<p style="margin-left: 4em;">in_ar: Input NumPy arrays with block`s shape.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
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

### clip
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.clip</span><span style="font-style: italic; color: black;font-size: 120%;">(layer, **kwargs):</span></span>

<p>Clip off areas that are not covered by the method layer.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>layer</b>: <code style="text-indent: 0em;">Layer||Feature||Geometry||str</code>. </p>
<p style="margin-left: 4em;">A GMA item use for cliping!</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.dataset.raster_translate</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Dataset</code>. </p>

### extent
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.extent</span><span style="font-style: italic; color: black;font-size: 120%;">(**kwargs):</span></span>

<p>The extent of a geometry is the bounding rectangle.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _aio.Layer.Layer.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>

### gen_lonlat
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.gen_lonlat</span><span style="font-style: italic; color: black;font-size: 120%;">(**kwargs):</span></span>

<p>Generate latitude and longitude raster.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Dataset</code>. </p>
<p style="margin-left: 4em;">Band 1 is longitude, Band 2 is latitude.</p>

### get_palette
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.get_palette</span><span style="font-style: italic; color: black;font-size: 120%;">(bid = <span style="color:#48566B">1</span>):</span></span>

<p>Get palette of the band.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>bid </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 1</span>. </p>
<p style="margin-left: 4em;">Number of the element calculation band. Start with 1.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">matplotlib</code>. <span style="color:#48566B;">colors.ListedColormap or None</span>. </p>

### isopleth
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.isopleth</span><span style="font-style: italic; color: black;font-size: 120%;">(interval = <span style="color:#48566B">50</span>, base = <span style="color:#48566B">0</span>, band = <span style="color:#48566B">1</span>, **kwargs):</span></span>

<p>Generate a smooth curve formed by connecting points with equal quantity index values.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
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

### plot
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.plot</span><span style="font-style: italic; color: black;font-size: 120%;">(ax = <span style="color:#48566B">None</span>, bands = <span style="color:#48566B">None</span>, **kwargs):</span></span>

<p>Make plots of Dataset.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>ax </b> = <code style="text-indent: 0em;">None||matplotlib</code>. <span style="color:#48566B;">~.AxesSubplot. Default None</span>. </p>
<p style="margin-left: 4em;">A matplotlib subplot. If None, a default axes will be created.</p>
<p style="margin-left: 2em;"><b>bands </b> = <code style="text-indent: 0em;">int||list||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The band ID to be plotted. For multi-band data, only 1, 3 (RGB), and 4 (RGBA) bands are supported for selection. Duplicate bands will only keep one. Default is the first four bands.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to matplotlib.image.AxesImage.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>matplotlib.~.AxesSubplot</b></p>

### reclassify
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.reclassify</span><span style="font-style: italic; color: black;font-size: 120%;">(remap, method = <span style="color:#48566B">"Range"</span>, **kwargs):</span></span>

<p>Reclassifies (or changes) the values in a raster.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>remap</b>: <code style="text-indent: 0em;">dict</code>. </p>
<p style="margin-left: 4em;">Remap object. Used to remap an input value or range definition to a new value.</p>
<p style="margin-left: 4em;">The format is {mapping1: value1, mapping2: value2, ...}.</p>
<p style="margin-left: 4em;">Note: Items containing NAN will be rejected directly.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
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

### resample
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.resample</span><span style="font-style: italic; color: black;font-size: 120%;">(resolution, method = <span style="color:#48566B">"Nearest"</span>, **kwargs):</span></span>

<p>Change the spatial resolution of the Dataset.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>resolution</b>: <code style="text-indent: 0em;">float||list</code>. </p>
<p style="margin-left: 4em;">Resampling resolution(X, Y).</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>method </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'Nearest'</span>. </p>
<p style="margin-left: 4em;">Resampling method. Supported resampling methods include:</p>
<p style="margin-left: 4em;">'Nearest', 'Bilinear', 'Cubic', 'CubicSpline', 'Lanczos', 'Average', 'RMS', 'Mode'.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.dataset.raster_translate</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Dataset</code>. </p>

### set_crs
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.set_crs</span><span style="font-style: italic; color: black;font-size: 120%;">(crs):</span></span>

<p>Set dataset's crs!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>crs</b>: <code style="text-indent: 0em;">str||int||None</code>. </p>
<p style="margin-left: 4em;">The output coordinate system. Can be EPSG, WKT, Proj4, and other types of coordinate characters.  Default(None) no coordinate system!</p>

### set_gcps
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.set_gcps</span><span style="font-style: italic; color: black;font-size: 120%;">(gcps = <span style="color:#48566B">[(0, 0, 0, 0, 0, '', '')]</span>, crs = <span style="color:#48566B">None</span>):</span></span>

<p>Set GCPs.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>gcps </b> = <code style="text-indent: 0em;">list[tuple]</code>. <span style="color:#48566B;"> Default [(0, 0, 0, 0, 0, '', '')]</span>. </p>
<p style="margin-left: 4em;">list(4 foloat + 2str) of gcps values.</p>
<p style="margin-left: 4em;">format:</p>
<p style="margin-left: 6em;">[(x(float), y(float), z(float), pixel(float), line(float), info(str, opt), id(str, opt)), ...]</p>
<p style="margin-left: 2em;"><b>crs </b> = <code style="text-indent: 0em;">str||int||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The gcps' coordinate system. Can be EPSG, WKT, Proj4, and other types of coordinate characters.  Default(None) no coordinate system!</p>

### set_geo_transform
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.set_geo_transform</span><span style="font-style: italic; color: black;font-size: 120%;">(geo_transform):</span></span>

<p>Set dataset's geo transform!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>geo_transform</b>: <code style="text-indent: 0em;">tuple</code>. </p>
<p style="margin-left: 4em;">Geo transformation of the output raster(6 float of tuple). format:</p>
<p style="margin-left: 6em;">[x min, x resolution, x rotation, y max, y rotation, y resolution]</p>

### set_metadata
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.set_metadata</span><span style="font-style: italic; color: black;font-size: 120%;">(metadata):</span></span>

<p>Set dataset's metadata!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>metadata</b>: <code style="text-indent: 0em;">dict</code>. </p>
<p style="margin-left: 4em;">Metadata to be added.</p>

### set_nodata
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.set_nodata</span><span style="font-style: italic; color: black;font-size: 120%;">(nodata, bids = <span style="color:#48566B">None</span>):</span></span>

<p>Set dataset's nodata value of band!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>nodata</b>: <code style="text-indent: 0em;">float</code>. </p>
<p style="margin-left: 4em;">Invalid value for output raster.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>bids </b> = <code style="text-indent: 0em;">int||lint of int||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Number of the element calculation band. Start with 1. None for all bands.</p>

### set_palette
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.set_palette</span><span style="font-style: italic; color: black;font-size: 120%;">(palette):</span></span>

<p>Set dataset's palette of band!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>palette</b>: <code style="text-indent: 0em;">dict||matplotlib</code>. <span style="color:#48566B;">~.cmap or a list of them</span>. </p>
<p style="margin-left: 4em;">Palette(color table) of raster bands.</p>
<p style="margin-left: 4em;">For example:</p>
<p style="margin-left: 6em;">1.dict({value: (R,G,B,A)}):</p>
<p style="margin-left: 8em;">palette = {10:(200,50,100,255), 20:(200,50,100,255)}.</p>
<p style="margin-left: 6em;">2.camp:</p>
<p style="margin-left: 8em;">import matplotlib.colors as cor palette = cor.ListedColormap(['r', 'g', 'b'], N = 256)</p>

### set_statistics
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.set_statistics</span><span style="font-style: italic; color: black;font-size: 120%;">(statistics, bids = <span style="color:#48566B">None</span>):</span></span>

<p>Set dataset's statistics of band!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>statistics</b>: <code style="text-indent: 0em;">None||list of tuple(vmin||vmax||vmean||vstddev)</code>. </p>
<p style="margin-left: 4em;">Statistics values. None for automatically compute statistics.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>bids </b> = <code style="text-indent: 0em;">int||lint of int||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Number of the element calculation band. Start with 1. None for all bands.</p>

### shift
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.shift</span><span style="font-style: italic; color: black;font-size: 120%;">(distance = <span style="color:#48566B">1</span>):</span></span>

<p>Shift a distance of the dataset. **Warining: This method will modify the original data.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>distance </b> = <code style="text-indent: 0em;">float||list</code>. <span style="color:#48566B;"> Default 1</span>. </p>
<p style="margin-left: 4em;">X, Y shift distance. If a single value is provided, it is assumed that X = Y.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Dataset</code>. </p>

### to_bytearray
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.to_bytearray</span><span style="font-style: italic; color: black;font-size: 120%;">(row_off = <span style="color:#48566B">0</span>, column_off = <span style="color:#48566B">0</span>, row_size = <span style="color:#48566B">None</span>, column_size = <span style="color:#48566B">None</span>, sel_bands = <span style="color:#48566B">None</span>):</span></span>

<p>Reads the raster dataset as a bytearray.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
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

### to_crs
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.to_crs</span><span style="font-style: italic; color: black;font-size: 120%;">(crs, **kwargs):</span></span>

<p>Reproject to another coordinate system.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>crs</b>: <code style="text-indent: 0em;">str||int</code>. </p>
<p style="margin-left: 4em;">The output coordinate system. Can be EPSG, WKT, Proj4, and other types of coordinate characters.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.dataset.raster_translate</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Dataset</code>. </p>

### to_dtype
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.to_dtype</span><span style="font-style: italic; color: black;font-size: 120%;">(dtype, **kwargs):</span></span>

<p>Convert the data type of raster.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>dtype</b>: <code style="text-indent: 0em;">str</code>. </p>
<p style="margin-left: 4em;">A code or string tag for the output raster data type.</p>
<p style="margin-left: 4em;">Supported data types include:</p>
<p style="margin-left: 4em;">'Unknown', 'Byte', 'UInt16', 'Int16', 'UInt32', 'Int32','Float32', 'Float64', 'CInt16', 'CInt32', 'CFloat32', 'CFloat64', ...</p>
<p style="margin-left: 4em;">for more, see const.RaDT_*.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.dataset.raster_translate</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Dataset</code>. </p>

### to_file
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.to_file</span><span style="font-style: italic; color: black;font-size: 120%;">(out_dst, driver = <span style="color:#48566B">"GTiff"</span>, **kwargs):</span></span>

<p>Save Dataset as a raster file.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>out_dst</b>: <code style="text-indent: 0em;">str</code>. </p>
<p style="margin-left: 4em;">The output raster file path.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>driver </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'GTiff'</span>. </p>
<p style="margin-left: 4em;">Output file driver. For other drivers, see gft.RasterSummary().CreatableFormats.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.dataset.raster_translate.</p>

### to_layer
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.to_layer</span><span style="font-style: italic; color: black;font-size: 120%;">(field = <span style="color:#48566B">None</span>, band = <span style="color:#48566B">1</span>, gtype = <span style="color:#48566B">"Polygon"</span>, mask = <span style="color:#48566B">False</span>, **kwargs):</span></span>

<p>Translate Dataset to Layer!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
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

### to_numpy
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.to_numpy</span><span style="font-style: italic; color: black;font-size: 120%;">(row_off = <span style="color:#48566B">0</span>, column_off = <span style="color:#48566B">0</span>, row_size = <span style="color:#48566B">None</span>, column_size = <span style="color:#48566B">None</span>, sel_bands = <span style="color:#48566B">None</span>, mask_nodata = <span style="color:#48566B">False</span>):</span></span>

<p>Reads the raster dataset as a 3-ndim Numpy array.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
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

### write_array
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.write_array</span><span style="font-style: italic; color: black;font-size: 120%;">(ar, row_off = <span style="color:#48566B">0</span>, column_off = <span style="color:#48566B">0</span>, sel_bands = <span style="color:#48566B">None</span>):</span></span>

<p>Write array to dataset.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>ar</b>: <code style="text-indent: 0em;">np</code>. <span style="color:#48566B;">ndarray</span>. </p>
<p style="margin-left: 4em;">The NumPy array that needs to be set.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>row_off </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 0</span>. </p>
<p style="margin-left: 4em;">The starting row of the data to be read.</p>
<p style="margin-left: 2em;"><b>column_off </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 0</span>. </p>
<p style="margin-left: 4em;">The starting column of the data to be read.</p>
<p style="margin-left: 2em;"><b>sel_bands </b> = <code style="text-indent: 0em;">int||list</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The band number or list of band numbers to be read. Default (None) All bands (numbering starts from 1).</p>

## Property

### blocks
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.blocks</span><span style=""></span></span>

<p style="margin-left: 2em;">Fetch the natural block size of this band. --> <code style="text-indent: 0em;">list(x and y dimensions of block)</code></p>

### bounds
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.bounds</span><span style=""></span></span>

<p style="margin-left: 2em;">Bounds. --> <code style="text-indent: 0em;">tuple</code></p>

### compression
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.compression</span><span style=""></span></span>

<p style="margin-left: 2em;">Raster compression. --> <code style="text-indent: 0em;">str</code></p>

### crs
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.crs</span><span style=""></span></span>

<p style="margin-left: 2em;">Raster coordinate reference system. --> <code style="text-indent: 0em;">CoordinateReferenceSystem</code></p>

### driver
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.driver</span><span style=""></span></span>

<p style="margin-left: 2em;">Raster driver. --> <code style="text-indent: 0em;">RasterDriver</code></p>

### dtype
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.dtype</span><span style=""></span></span>

<p style="margin-left: 2em;">Raster data type. --> <code style="text-indent: 0em;">str</code></p>

### gcps
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.gcps</span><span style=""></span></span>

<p style="margin-left: 2em;">Raster GCPs. --> <code style="text-indent: 0em;">tuple</code></p>

### geo_transform
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.geo_transform</span><span style=""></span></span>

<p style="margin-left: 2em;">Raster geo transform. --> <code style="text-indent: 0em;">tuple</code></p>

### link
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.link</span><span style=""></span></span>

<p style="margin-left: 2em;">Layer path link. --> <code style="text-indent: 0em;">str</code></p>

### metadata
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.metadata</span><span style=""></span></span>

<p style="margin-left: 2em;">metadata. --> <code style="text-indent: 0em;">dict</code></p>

### name
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.name</span><span style=""></span></span>

<p style="margin-left: 2em;">Raster Name. --> <code style="text-indent: 0em;">str</code></p>

### nodata
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.nodata</span><span style=""></span></span>

<p style="margin-left: 2em;">Raster nodata values. --> <code style="text-indent: 0em;">float</code></p>

### resolution
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.resolution</span><span style=""></span></span>

<p style="margin-left: 2em;">X, Y resolution. --> <code style="text-indent: 0em;">tuple</code></p>

### shape
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.shape</span><span style=""></span></span>

<p style="margin-left: 2em;">Raster shape. --> <code style="text-indent: 0em;">tuple(band, rows, columns)</code></p>

### stats
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.stats</span><span style=""></span></span>

<p style="margin-left: 2em;">Get stats of all bands. --> <code style="text-indent: 0em;">dict</code></p>
