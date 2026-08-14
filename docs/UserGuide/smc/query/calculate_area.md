---
title: calculate\_area
date: 2026-08-14
sidebar: true
---
# gma.smc.query.calculate_area


<span style="background-color:#EFF0FC;display: block;line-height:1.5"><span style="color: gray;font-size:90%;">function</span> <span style="color: #616AE5; font-weight: bold;font-size: 150%;">calculate_area</span><span style="font-style: italic; color: black;font-size: 130%;">(points, in_crs = <span style="color:#48566B">"WGS84"</span>, unit = <span style="color:#48566B">"square meter"</span>):</span></span>

Calculate the area of the polygon formed by the input multipoints.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>points: </b> <code>list||tuple||array</code>.</p><p style="padding-left: 1em;text-indent: 1em;">The X (longitude), Y (latitude) coordinates of the vertices of the polygon need to be calculated.</p><p style="padding-left: 1em;text-indent: 1em;">For example: points = [(130.1, 45.2), (131.5, 40.2), (131.5, 45.2)]</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>in_crs  = </b> <code>str||int||aclassofgmaCoordinateReferenceSystem</code>. <span style="color:#48566B;">Default 'WGS84'.</span></p><p style="padding-left: 1em;text-indent: 1em;">Coordinate system. Can be EPSG, WKT, Proj4, and other types of coordinate characters or CoordinateReferenceSystem class.</p><p style="text-indent: 1em;"><b>unit  = </b> <code>str</code>. <span style="color:#48566B;">Default 'square meter'.</span></p><p style="padding-left: 1em;text-indent: 1em;">The unit in which to calculate the area result.</p><p style="padding-left: 1em;text-indent: 1em;">Other supported units: 'square meter', 'square millimeter', 'square centimeter', 'square decimeter', 'square kilometer', 'hectare', 'acre', 'mu'.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code>array</code>.</p>

---