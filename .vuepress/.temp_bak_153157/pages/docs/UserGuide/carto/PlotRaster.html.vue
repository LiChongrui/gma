<template><div><p style="font-size: 120%;font-weight: bold;">gma.carto.raster.PlotRaster</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">PlotRaster</span><span style="font-style: italic; color: black;font-size: 130%;">(raster, map_frame, bands = <span style="color:#48566B">None</span>):</span></span>
<p>Add a discrete dataset to the map frame.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>raster</b>: <code style="text-indent: 0em;">A gma Dataset</code>. </p>
<p style="margin-left: 4em;">A raster object to be added to this map frame.</p>
<p style="margin-left: 2em;"><b>map_frame</b>: <code style="text-indent: 0em;">A gma MapFframe</code>. </p>
<p style="margin-left: 4em;">A MapFframe object to plot.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>bands</b> = <code style="text-indent: 0em;">int, list or None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The band ID to be plotted. For multi-band data, only 1, 3 (RGB), and 4 (RGBA) bands are</p>
<p style="margin-left: 4em;">supported for selection. Duplicate bands will only keep one. Default is the first four bands.</p>
<h2 id="method" tabindex="-1"><a class="header-anchor" href="#method"><span>Method</span></a></h2>
<h3 id="plot-cmap-none" tabindex="-1"><a class="header-anchor" href="#plot-cmap-none"><span>plot<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(cmap = None)</span></span></a></h3>
<p>Add a discrete dataset to the map frame.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
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
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">matplotlib.image.AxesImage</code>. </p>
<h3 id="add-legend-loc-0-0-xsize-0-1-ysize-0-4-title-none" tabindex="-1"><a class="header-anchor" href="#add-legend-loc-0-0-xsize-0-1-ysize-0-4-title-none"><span>add_legend<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(loc = (0, 0), xsize = 0.1, ysize = 0.4, title = None)</span></span></a></h3>
<p>Place a legend of the raster on the map frame.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>loc</b> = <code style="text-indent: 0em;">tuple of float</code>. <span style="color:#48566B;"> Default (0, 0)</span>. </p>
<p style="margin-left: 4em;">Legend location in map frame, (x, y) ranging from 0 to 1</p>
<p style="margin-left: 2em;"><b>xsize</b> = <code style="text-indent: 0em;">float</code>. <span style="color:#48566B;"> Default 0.1</span>. </p>
<p style="margin-left: 4em;">Legend width in map frame.</p>
<p style="margin-left: 2em;"><b>ysize</b> = <code style="text-indent: 0em;">float</code>. <span style="color:#48566B;"> Default 0.4</span>. </p>
<p style="margin-left: 4em;">Legend height in map frame.</p>
<p style="margin-left: 2em;"><b>title</b> = <code style="text-indent: 0em;">str or None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Legend Name. Default(None) raster's name.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to matplotlib.colorbar.Colorbar.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">matplotlib.colorbar.Colorbar</code>. </p>
</div></template>


