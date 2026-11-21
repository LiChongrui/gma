---
title: CoordinateReferenceSystem
date: 2026-11-20
---


<p style="font-size: 120%;font-weight: bold;">gma.crs.CoordinateReferenceSystem</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">CoordinateReferenceSystem</span><span style="font-style: italic; color: black;font-size: 130%;">(crs = <span style="color:#48566B">"WGS84"</span>):</span></span>

<p>Coordinate system!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>crs</b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'WGS84'</span>. </p>
<p style="margin-left: 4em;">Coordinate system. Can be EPSG, WKT, Proj4 and other types of coordinate characters, or a CoordinateReferenceSystem object.</p>

## Method

### copy<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span>

<p>Clone crs. --> <code style="text-indent: 0em;">CoordinateReferenceSystem</code></p>

### get_proj_parms<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span>

<p>Get projection parameters.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">dict</code>. </p>

### plot<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(ax = None)</span>

<p>Make area of use of the CoordinateReferenceSystem in world.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>ax</b> = <code style="text-indent: 0em;">None or matplotlib.~.AxesSubplot</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">A matplotlib subplot. If None, a default axes will be created.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other plotting parameters of CoordinateReferenceSystem's geometry. For more, see:</p>
<p style="margin-left: 4em;">~.carto.utils.PolyCollection.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">matplotlib.~.AxesSubplot</code>. </p>

### to_str<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(ctype = "Wkt")</span>

<p>Export projection to string.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>ctype</b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'Wkt'</span>. </p>
<p style="margin-left: 4em;">Export format. Can be 'MICoordSys', 'PrettyWkt',</p>
<p style="margin-left: 4em;">'Proj4', 'Wkt', 'XML'.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">str</code>. </p>

### to_list<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(ctype = "PCI")</span>

<p>Export projection to list.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>ctype</b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'PCI'</span>. </p>
<p style="margin-left: 4em;">Export format. Can be 'PCI', 'USGS'.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">list</code>. </p>

### to_dict<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span>

<p>Export projection to dict(json).</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">dict</code>. </p>


## Property

### angular_units

<p style="margin-left: 2em;">Angular units. --> <code style="text-indent: 0em;">tuple(float, str)</code></p>

### area_of_use

<p style="margin-left: 2em;">Get the area where the coordinate system is used. --> <code style="text-indent: 0em;">tuple(West, South, East, North in degree).</code></p>

### area_of_interest

<p style="margin-left: 2em;">The area of use's geometry of the crs in WGS84. --> <code style="text-indent: 0em;">Geometry.</code></p>

### axes_count

<p style="margin-left: 2em;">Number of coordinate axes. --> <code style="text-indent: 0em;">int</code></p>

### central_longitude

<p style="margin-left: 2em;">Get the longitude of the central meridian. --> <code style="text-indent: 0em;">float</code></p>

### change_longitude

<p style="margin-left: 2em;">Date Line --> <code style="text-indent: 0em;">float</code></p>

### datum_name

<p style="margin-left: 2em;">Datum name. --> <code style="text-indent: 0em;">str</code></p>

### gcs

<p style="margin-left: 2em;">Get projection parameters. --> <code style="text-indent: 0em;">CoordinateReferenceSystem</code></p>

### inv_flattening

<p style="margin-left: 2em;">Inverse flattening. --> <code style="text-indent: 0em;">float</code></p>

### linear_units

<p style="margin-left: 2em;">Linear units and name. --> <code style="text-indent: 0em;">tuple(float, str).</code></p>

### name

<p style="margin-left: 2em;">Name of the coordinate system. --> <code style="text-indent: 0em;">str</code></p>

### planet

<p style="margin-left: 2em;">The planet of the coordinate system. --> <code style="text-indent: 0em;">str</code></p>

### primem

<p style="margin-left: 2em;">The prime meridian and name. --> <code style="text-indent: 0em;">tuple(float, str)</code></p>

### proj_method

<p style="margin-left: 2em;">The project method name. --> <code style="text-indent: 0em;">str</code></p>

### radius

<p style="margin-left: 2em;">Ellipsoid radius. --> <code style="text-indent: 0em;">float</code></p>

### semi_major

<p style="margin-left: 2em;">Semi-major axis. --> <code style="text-indent: 0em;">float</code></p>

### semi_minor

<p style="margin-left: 2em;">Semi-minor axis. --> <code style="text-indent: 0em;">float</code></p>

### spheroid_name

<p style="margin-left: 2em;">Spheroid name. --> <code style="text-indent: 0em;">str</code></p>

### type

<p style="margin-left: 2em;">Space Reference Type. --> <code style="text-indent: 0em;">str</code></p>

### WKID

<p style="margin-left: 2em;">Well-known ID Code and name. --> <code style="text-indent: 0em;">tuple(float, str)</code></p>
