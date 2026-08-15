---
title: CoordinateReferenceSystem
date: 2026-08-15
sidebar: true
---
<span style="font-size: 120%;font-weight: bold;">gma.crs.CoordinateReferenceSystem</span>


<span style="background-color:#EFF0FC;display: block;line-height:1.5"><span style="color: gray;font-size:90%;">class</span> <span style="color: #616AE5; font-weight: bold;font-size: 150%;">CoordinateReferenceSystem</span><span style="font-style: italic; color: black;font-size: 130%;">(crs = <span style="color:#48566B">"WGS84"</span>):</span></span>

Coordinate reference system object Coordinate system!

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>crs  = </b> <code style="text-indent: 0">str||int||aclassofgmaCoordinateReferenceSystem</code>. <span style="color:#48566B;">Default 'WGS84'.</span></p><p style="padding-left: 1em;text-indent: 1em;">Coordinate system. Can be EPSG, WKT, Proj4, and other types of coordinate characters or CoordinateReferenceSystem class.</p>

---

## Methods 



### copy




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">copy</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>


<p style="text-indent: 1em;">Clone crs. --> <code style="text-indent: 0em;"> CoordinateReferenceSystem</code></p>



---

### get_proj_parms




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">get_proj_parms</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>


Get projection parameters.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">dict</code>.</p>

---

### plot




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">plot</span><span style="font-style: italic; color: black;font-size: 120%;">(ax = <span style="color:#48566B">None</span>, **kwargs):</span></span>


Make area of use of the CoordinateReferenceSystem in world.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>ax  = </b> <code style="text-indent: 0">None||matplotlib.~.AxesSubplot</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    A matplotlib subplot. If None, a default axes will be created. </p><p style="text-indent: 1em;"><b>**kwargs</b>.</p><p style="padding-left: 1em;text-indent: 1em;">Other plotting parameters of CoordinateReferenceSystem's geometry. For more, see: ~.carto.utils.PolyCollection.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">matplotlib.~.AxesSubplot</code>.</p>

---

### to_dict




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">to_dict</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>


Export projection to dict(json).

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">dict</code>.</p>

---

### to_list




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">to_list</span><span style="font-style: italic; color: black;font-size: 120%;">(ctype = <span style="color:#48566B">"PCI"</span>):</span></span>


Export projection to list.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>ctype  = </b> <code style="text-indent: 0">str</code>. <span style="color:#48566B;">Default 'PCI'.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Export format. Can be 'PCI', 'USGS'.   </p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">list</code>.</p>

---

### to_str




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">to_str</span><span style="font-style: italic; color: black;font-size: 120%;">(ctype = <span style="color:#48566B">"Wkt"</span>):</span></span>


Export projection to string.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>ctype  = </b> <code style="text-indent: 0">str</code>. <span style="color:#48566B;">Default 'Wkt'.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Export format. Can be 'MICoordSys', 'PrettyWkt', 'Proj4', 'Wkt', 'XML'.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">str</code>.</p>

---

## Property 



### WKID


<p style="text-indent: 1em;">Well-known ID Code and name. --> <code style="text-indent: 0em;"> tuple(float, str)</code></p>



---

### angular_units


<p style="text-indent: 1em;">Angular units. --> <code style="text-indent: 0em;"> tuple(float, str)</code></p>



---

### area_of_interest


<p style="text-indent: 1em;">The area of use's geometry of the crs in WGS84. --> <code style="text-indent: 0em;"> Geometry.</code></p>



---

### area_of_use


<p style="text-indent: 1em;">Get the area where the coordinate system is used. --> <code style="text-indent: 0em;"> tuple(West, South, East, North in degree).</code></p>



---

### axes_count


<p style="text-indent: 1em;">Number of coordinate axes. --> <code style="text-indent: 0em;"> int</code></p>



---

### central_longitude


<p style="text-indent: 1em;">Get the longitude of the central meridian. --> <code style="text-indent: 0em;"> float</code></p>



---

### change_longitude


<p style="text-indent: 1em;">Date Line --> <code style="text-indent: 0em;"> float</code></p>



---

### datum_name


<p style="text-indent: 1em;">Datum name. --> <code style="text-indent: 0em;"> str</code></p>



---

### gcs


<p style="text-indent: 1em;">Get projection parameters. --> <code style="text-indent: 0em;"> CoordinateReferenceSystem</code></p>



---

### inv_flattening


<p style="text-indent: 1em;">Inverse flattening. --> <code style="text-indent: 0em;"> float</code></p>



---

### linear_units


<p style="text-indent: 1em;">Linear units and name. --> <code style="text-indent: 0em;"> tuple(float, str).</code></p>



---

### name


<p style="text-indent: 1em;">Name of the coordinate system. --> <code style="text-indent: 0em;"> str</code></p>



---

### planet


<p style="text-indent: 1em;">The planet of the coordinate system. --> <code style="text-indent: 0em;"> str</code></p>



---

### primem


<p style="text-indent: 1em;">The prime meridian and name. --> <code style="text-indent: 0em;"> tuple(float, str)</code></p>



---

### proj_method


<p style="text-indent: 1em;">The project method name. --> <code style="text-indent: 0em;"> str</code></p>



---

### radius


<p style="text-indent: 1em;">Ellipsoid radius. --> <code style="text-indent: 0em;"> float</code></p>



---

### semi_major


<p style="text-indent: 1em;">Semi-major axis. --> <code style="text-indent: 0em;"> float</code></p>



---

### semi_minor


<p style="text-indent: 1em;">Semi-minor axis. --> <code style="text-indent: 0em;"> float</code></p>



---

### spheroid_name


<p style="text-indent: 1em;">Spheroid name. --> <code style="text-indent: 0em;"> str</code></p>



---

### type


<p style="text-indent: 1em;">Space Reference Type. --> <code style="text-indent: 0em;"> str</code></p>



---