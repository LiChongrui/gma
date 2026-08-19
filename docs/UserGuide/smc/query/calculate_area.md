---
title: calculate_area
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.smc.query.calculate_area</p><span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[function] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">calculate_area</span><span style="font-style: italic; color: black;font-size: 120%;">(points, in_crs = <span style="color:#48566B">"WGS84"</span>, unit = <span style="color:#48566B">"square meter"</span>):</span></span>

<p>Calculate the area of the polygon formed by the input multipoints.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>points</b>: <code style="text-indent: 0em;">list||tuple||array</code>. </p>
<p style="margin-left: 4em;">The X (longitude), Y (latitude) coordinates of the vertices of the polygon need to be calculated.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>in_crs </b> = <code style="text-indent: 0em;">str||int||CoordinateReferenceSystem</code>. <span style="color:#48566B;"> Default 'WGS84'</span>. </p>
<p style="margin-left: 4em;">Coordinate system. Can be EPSG, WKT, Proj4, and other types of coordinate characters or CoordinateReferenceSystem class.</p>
<p style="margin-left: 2em;"><b>unit </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'square meter'</span>. </p>
<p style="margin-left: 4em;">The unit in which to calculate the area result.</p>
<p style="margin-left: 4em;">Other supported units: 'square meter', 'square millimeter', 'square centimeter', 'square decimeter', 'square kilometer', 'hectare', 'acre', 'mu'.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">array</code>. </p>
