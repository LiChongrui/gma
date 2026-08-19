---
title: hillshade
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.etools.hillshade</p><span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[function] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">hillshade</span><span style="font-style: italic; color: black;font-size: 120%;">(in_src, out_dst, compute_edges = <span style="color:#48566B">None</span>, band = <span style="color:#48566B">1</span>, z_factor = <span style="color:#48566B">1.0</span>, scale = <span style="color:#48566B">1.0</span>, azimuth = <span style="color:#48566B">315.0</span>, altitude = <span style="color:#48566B">45.0</span>, combined = <span style="color:#48566B">False</span>, algos = <span style="color:#48566B">"Horn"</span>, **kwargs):</span></span>

<p>Calculate hillshade from any supported DEM raster file!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>in_src</b>: <code style="text-indent: 0em;">str</code>. </p>
<p style="margin-left: 4em;">The input raster file path.</p>
<p style="margin-left: 2em;"><b>out_dst</b>: <code style="text-indent: 0em;">str</code>. </p>
<p style="margin-left: 4em;">The output raster file path.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>compute_edges </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default True</span>. </p>
<p style="margin-left: 4em;">Whether to compute raster edge data and data near no data values.</p>
<p style="margin-left: 4em;">Setting values that are not True are treated as False.</p>
<p style="margin-left: 2em;"><b>band </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 1</span>. </p>
<p style="margin-left: 4em;">Number of the element calculation band. Start with 1.</p>
<p style="margin-left: 2em;"><b>z_factor </b> = <code style="text-indent: 0em;">float</code>. <span style="color:#48566B;"> Default 1.0</span>. </p>
<p style="margin-left: 4em;">Vertical exaggeration.</p>
<p style="margin-left: 2em;"><b>scale </b> = <code style="text-indent: 0em;">float</code>. <span style="color:#48566B;"> Default 1.0</span>. </p>
<p style="margin-left: 4em;">The ratio of vertical units to horizontal. If the vertical unit is m and the horizontal unit is бу, you can set Scale = 111120.</p>
<p style="margin-left: 2em;"><b>azimuth </b> = <code style="text-indent: 0em;">float</code>. <span style="color:#48566B;"> Default 315.0</span>. </p>
<p style="margin-left: 4em;">Azimuth of the light(бу).</p>
<p style="margin-left: 2em;"><b>altitude </b> = <code style="text-indent: 0em;">float</code>. <span style="color:#48566B;"> Default 45.0</span>. </p>
<p style="margin-left: 4em;">Altitude of the light(бу).</p>
<p style="margin-left: 2em;"><b>combined </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Whether to compute blended shadows. Setting values that are not True are treated as False.</p>
<p style="margin-left: 2em;"><b>algos </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'Horn'</span>. </p>
<p style="margin-left: 4em;">Surface algorithm. May be 'Horn' or 'ZevenbergenThorne'.</p>
<p style="margin-left: 2em;"><b>OutFormat </b> = <code style="text-indent: 0em;">str||a class of gma RasterFormat</code>. <span style="color:#48566B;"> Default 'GTiff'</span>. </p>
<p style="margin-left: 4em;">Output file format. For more, see rasp.Basic.ToOtherFormat.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">DataSet</code>. </p>
