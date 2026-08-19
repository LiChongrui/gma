---
title: calculate_distance
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.smc.query.calculate_distance</p><span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[function] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">calculate_distance</span><span style="font-style: italic; color: black;font-size: 120%;">(points, in_crs = <span style="color:#48566B">"WGS84"</span>, unit = <span style="color:#48566B">"meter"</span>):</span></span>

<p>Calculate the distance between two or more input points.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>points</b>: <code style="text-indent: 0em;">list||tuple||array</code>. </p>
<p style="margin-left: 4em;">The X (longitude), Y (latitude) coordinates of two points (or multiple points) for which distances need to be calculated.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>in_crs </b> = <code style="text-indent: 0em;">str||int||CoordinateReferenceSystem</code>. <span style="color:#48566B;"> Default 'WGS84'</span>. </p>
<p style="margin-left: 4em;">Coordinate system. Can be EPSG, WKT, Proj4, and other types of coordinate characters or CoordinateReferenceSystem class.</p>
<p style="margin-left: 2em;"><b>unit </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'meter'</span>. </p>
<p style="margin-left: 4em;">The unit in which to calculate the distance result.</p>
<p style="margin-left: 4em;">Other supported units: 'decimeter', 'centimeter', 'millimeter', 'micron', 'picometer', 'fermi', 'kilometer', 'inch', 'foot', 'yard', 'mile', 'mil', 'point', 'survey foot', 'survey mile', 'nautical mile', 'angstrom', 'astronomical unit', 'light year', 'parsec'.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">array</code>. </p>
