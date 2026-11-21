<template><div><p style="font-size: 120%;font-weight: bold;">gma.carto.layout.MapFrame</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">MapFrame</span><span style="font-style: italic; color: black;font-size: 130%;">(ax = <span style="color:#48566B">None</span>, crs = <span style="color:#48566B">"WGS84"</span>, bounds = <span style="color:#48566B">None</span>):</span></span>
<p>Main entry of cartography: <code>from gma.carto.plot import MapFrame</code>.</p>
<p>Initialize a map frame for plotting a map!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>ax</b> = <code style="text-indent: 0em;">None or matplotlib.~.AxesSubplot</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">A matplotlib subplot. If None, a default axes will be created.</p>
<p style="margin-left: 2em;"><b>crs</b> = <code style="text-indent: 0em;">str, int or a class of SpatRef/SpatialReference</code>. <span style="color:#48566B;"> Default 'WGS84'</span>. </p>
<p style="margin-left: 4em;">Base map coordinate system. All data that added to this frame will be reprojected</p>
<p style="margin-left: 4em;">to this coordinate system. Can be EPSG, WKT, Proj4 and other types of coordinate</p>
<p style="margin-left: 4em;">characters or SpatRef/SpatialReference class.</p>
<p style="margin-left: 2em;"><b>bounds</b> = <code style="text-indent: 0em;">list or None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Plot [left, bottom, right, top] extent(In WGS84). All data that added to this map</p>
<p style="margin-left: 4em;">frame will be clipped to this extent. Default(None) is the maximum extent supported</p>
<p style="margin-left: 4em;">by the base map coordinate system.</p>
<h2 id="method" tabindex="-1"><a class="header-anchor" href="#method"><span>Method</span></a></h2>
<h3 id="add-appearance-map-app-compassnormal1-loc-0-0-size-0-3" tabindex="-1"><a class="header-anchor" href="#add-appearance-map-app-compassnormal1-loc-0-0-size-0-3"><span>add_appearance<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(map_app = &quot;CompassNormal1&quot;, loc = (0, 0), size = 0.3)</span></span></a></h3>
<p>Add a map appearance to this map frame.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>map_app</b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'CompassNormal1'</span>. </p>
<p style="margin-left: 4em;">Map appearance type. For more, see ~.appearance.MapAppearance.</p>
<p style="margin-left: 2em;"><b>loc</b> = <code style="text-indent: 0em;">tuple</code>. <span style="color:#48566B;"> Default (0, 0)</span>. </p>
<p style="margin-left: 4em;">The location of the map appearance. The coordinate system is the same as the map frame.</p>
<p style="margin-left: 2em;"><b>size</b> = <code style="text-indent: 0em;">float</code>. <span style="color:#48566B;"> Default 0.3</span>. </p>
<p style="margin-left: 4em;">The size of the map appearance. The unit is the same as the map frame.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to ~.appearance.MapAppearance.plot.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">~.appearance.MapAppearance</code>. </p>
<h3 id="add-graticule-lon-range-range-180-180-30-lat-range-range-90-90-15" tabindex="-1"><a class="header-anchor" href="#add-graticule-lon-range-range-180-180-30-lat-range-range-90-90-15"><span>add_graticule<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(lon_range = range(-180, 180, 30), lat_range = range(-90, 90, 15))</span></span></a></h3>
<p>Add longitude and latitude grid.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>lon_range</b> = <code style="text-indent: 0em;">list or range</code>. <span style="color:#48566B;"> Default range(-180, 180, 30)</span>. </p>
<p style="margin-left: 4em;">Grid longitude value.</p>
<p style="margin-left: 2em;"><b>lat_range</b> = <code style="text-indent: 0em;">list or range</code>. <span style="color:#48566B;"> Default range(-90, 90, 15)</span>. </p>
<p style="margin-left: 4em;">Grid latitude value.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to matplotlib.collections.Collections.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">~appearances.Graticule</code>. </p>
<h3 id="add-vector-vector-facecolors-bed2ff-edgecolors-b2b2b2-hatchs-none-hatchs-linewidths-none-linewidths-none-linestyles-solid-pointmarkers-o-pointsizes-none" tabindex="-1"><a class="header-anchor" href="#add-vector-vector-facecolors-bed2ff-edgecolors-b2b2b2-hatchs-none-hatchs-linewidths-none-linewidths-none-linestyles-solid-pointmarkers-o-pointsizes-none"><span>add_vector<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(vector, facecolors = &quot;#BED2FF&quot;, edgecolors = &quot;#B2B2B2&quot;, hatchs = None, hatchs_linewidths = None, linewidths = None, linestyles = &quot;solid&quot;, pointmarkers = &quot;o&quot;, pointsizes = None)</span></span></a></h3>
<p>Add a map vector(Layer/Feature/Geometry) to this map frame.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>vector</b>: <code style="text-indent: 0em;">Layer, Feature or Geometry</code>. </p>
<p style="margin-left: 4em;">A vector object to be added to this map frame.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>facecolors</b> = <code style="text-indent: 0em;">str, tuplt, list</code>. <span style="color:#48566B;"> Default '#BED2FF'</span>. </p>
<p style="margin-left: 4em;">Polygon fill color. Only for 'Polygon' or 'Point' geometries. If it is a list,</p>
<p style="margin-left: 4em;">assign a different color to each feature's geometry. For more, matplotlib.colors.</p>
<p style="margin-left: 2em;"><b>edgecolors</b> = <code style="text-indent: 0em;">str, tuplt, list</code>. <span style="color:#48566B;"> Default '#B2B2B2'</span>. </p>
<p style="margin-left: 4em;">The edge or line color. If it is a list, assign a different color to each feature's geometry.</p>
<p style="margin-left: 4em;">For more, matplotlib.colors.</p>
<p style="margin-left: 2em;"><b>hatchs</b> = <code style="text-indent: 0em;">str, list or None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Polygon fill style. Only for 'Polygon' geometries. May be {'/', '\', '|', '-', '+', 'x', 'o', 'O', '.', '*'}</p>
<p style="margin-left: 4em;">or a combination thereof. Default(None) no filling style. If it is a list, assign a different hatch to</p>
<p style="margin-left: 4em;">each feature. For more, see matplotlib.hatch.</p>
<p style="margin-left: 2em;"><b>hatchs_linewidths</b> = <code style="text-indent: 0em;">str, list or None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Hatch line width. Only for 'Polygon' geometries. If it is a list, assign a different line width to each hatch.</p>
<p style="margin-left: 2em;"><b>linewidths</b> = <code style="text-indent: 0em;">float or list</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The edge or line width. If it is a list, assign a different line width to each feature's geometry.</p>
<p style="margin-left: 2em;"><b>linestyles</b> = <code style="text-indent: 0em;">str, list or tuple</code>. <span style="color:#48566B;"> Default 'solid'</span>. </p>
<p style="margin-left: 4em;">The edge or line style. Only for 'Polygon' or 'Line' geometries. May be {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}. If it is a list,</p>
<p style="margin-left: 4em;">assign a different line style to each feature's geometry. For more, see matplotlib.lines.lineStyles.</p>
<p style="margin-left: 2em;"><b>pointmarkers</b> = <code style="text-indent: 0em;">str, list</code>. <span style="color:#48566B;"> Default 'o'</span>. </p>
<p style="margin-left: 4em;">The point marker. Only for 'Point' geometries. May be {'.', ',', 'o', 'v', '^', '&lt;', '&gt;', '1', '2',</p>
<p style="margin-left: 4em;">'3', '4', '8', 's', 'p', 'P', '*', 'h', 'H', '+', 'x', 'X', 'D', 'd', '|', '_', 0, 1, 2, 3, 4,</p>
<p style="margin-left: 4em;">5, 6, 7, 8, 9, 10, 11, 'None', ' ', '', '$...$', Path, ...}. If it is a list, assign a different</p>
<p style="margin-left: 4em;">marker to each feature's geometry. For more, see matplotlib.lines.lineMarkers.</p>
<p style="margin-left: 2em;"><b>pointsizes</b> = <code style="text-indent: 0em;">float, list or None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The point size. Only for 'Point' geometries. If it is a list, assign a different size to each feature's geometry.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to matplotlib.collections.Collections.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">~.vector.PlotVector</code>. </p>
<h3 id="add-raster-raster-bands-none-cmap-none" tabindex="-1"><a class="header-anchor" href="#add-raster-raster-bands-none-cmap-none"><span>add_raster<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(raster, bands = None, cmap = None)</span></span></a></h3>
<p>Add a discrete dataset to the map frame.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>raster</b>: <code style="text-indent: 0em;">A gma Dataset</code>. </p>
<p style="margin-left: 4em;">A raster object to be added to this map frame.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>bands</b> = <code style="text-indent: 0em;">int, list or None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The band ID to be plotted. For multi-band data, only 1, 3 (RGB), and 4 (RGBA) bands are</p>
<p style="margin-left: 4em;">supported for selection. Duplicate bands will only keep one. Default is the first four bands.</p>
<p style="margin-left: 2em;"><b>cmap</b> = <code style="text-indent: 0em;">str, list, matplotlib.color.Colormap or None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">color map. For more, see matplotlib.color.Colormap.</p>
<p style="margin-left: 4em;">*Note:</p>
<p style="margin-left: 4em;">1. If CMap is a list, the list must be in the format (R, G, B),(R, G, B, A) or HEX colors!</p>
<p style="margin-left: 4em;">Otherwise, create your own matplotlib cmap!</p>
<p style="margin-left: 4em;">2. If the input dataset has a color table, do not configure CMap, otherwise the dataset</p>
<p style="margin-left: 4em;">color table will be ignored. Color priority: CMap &gt; ColorTable.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to matplotlib.image.AxesImage.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">~.raster.PlotRaster</code>. </p>
<p>Inherits all methods from <code>MapFrameBase</code>.</p></div></template>


