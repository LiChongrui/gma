---
title: GeometryStyles
date: 2026-11-20
---


<p style="font-size: 120%;font-weight: bold;">gma.carto.styles.GeometryStyles</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">GeometryStyles</span><span style="font-style: italic; color: black;font-size: 130%;">(pointmarkers = <span style="color:#48566B">"o"</span>, pointsizes = <span style="color:#48566B">None</span>, ax = <span style="color:#48566B">None</span>):</span></span>

<p>Passed to <code>PlotVector.plot(style=...)</code> to customize vector plotting styles.</p>
<p>Build point, line and polygon plotting styles for a vector.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>pointmarkers</b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'o'</span>. </p>
<p style="margin-left: 4em;">Marker style for point geometries. For more, see matplotlib.markers.</p>
<p style="margin-left: 2em;"><b>pointsizes</b> = <code style="text-indent: 0em;">float, list or None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Marker size for point geometries. Default(None) determined by the plotted data.</p>
<p style="margin-left: 2em;"><b>ax</b> = <code style="text-indent: 0em;">matplotlib.axes.Axes or None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The axes used for plotting. Default(None) the axes of the map frame.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">GeometryStyles</code>. </p>

## Method

### build_polygons<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span>

<p>构建图例 多边形</p>

### build_lines<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span>

<p>构建图例 线</p>

### build_points<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span>

<p>构建图例 点</p>
