---
title: ProjectedCoordinateSystem
date: 2026-08-14
sidebar: true
---
# gma.crs.ProjectedCoordinateSystem


<span style="background-color:#EFF0FC;display: block;line-height:1.5"><span style="color: gray;font-size:90%;">class</span> <span style="color: #616AE5; font-weight: bold;font-size: 150%;">ProjectedCoordinateSystem</span><span style="font-style: italic; color: black;font-size: 130%;">(name = <span style="color:#48566B">"GMA PCS"</span>, linear_unit = <span style="color:#48566B">"metre"</span>, proj_method = <span style="color:#48566B">"AlbersConicEqualArea"</span>, gcs = <span style="color:#48566B">"WGS84"</span>):</span></span>

projected coordinate system Create a projected coordinate system!

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>name  = </b> <code>str</code>. <span style="color:#48566B;">Default 'GMA PCS'.</span></p><p style="padding-left: 1em;text-indent: 1em;">    name of the new projected coordinate system.</p><p style="text-indent: 1em;"><b>linear_unit  = </b> <code>float||str</code>. <span style="color:#48566B;">Default 'metre'.</span></p><p style="padding-left: 1em;text-indent: 1em;">Linear unit value. See more default linear units: LinearUnits class! If you need to customize the linear unit, you can enter a real number.</p><p style="text-indent: 1em;"><b>proj_method  = </b> <code>aclassofadefaultprojectionmethod||str(classname)</code>. <span style="color:#48566B;">Default 'AlbersConicEqualArea'.</span></p><p style="padding-left: 1em;text-indent: 1em;">Projection method. If it is the name of a projection method class, it will refer to the default projection parameters of the projection method. See more projection method class: projection module!</p><p style="text-indent: 1em;"><b>gcs  = </b> <code>str||int||CoordinateReferenceSystem</code>. <span style="color:#48566B;">Default 'WGS84'.</span></p><p style="padding-left: 1em;text-indent: 1em;">Geographic coordinate system in the projected coordinate system. Can be EPSG, WKT, Proj4, and other types of coordinate characters or a CoordinateReferenceSystem class.</p>

---

## Methods 



### copy




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">copy</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>


Clone crs. --> <code> CoordinateReferenceSystem</code>



---

### get_proj_parms




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">get_proj_parms</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>


Get projection parameters.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>dict</b>.</p>

---

### plot




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">plot</span><span style="font-style: italic; color: black;font-size: 120%;">(ax = <span style="color:#48566B">None</span>, **kwargs):</span></span>


Make area of use of the CoordinateReferenceSystem in world.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>ax  = </b> <code>None||matplotlib.~.AxesSubplot</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    A matplotlib subplot. If None, a default axes will be created. </p><p style="text-indent: 1em;"><b>**kwargs</b>.</p><p style="padding-left: 1em;text-indent: 1em;">Other plotting parameters of CoordinateReferenceSystem's geometry. For more, see: ~.carto.utils.PolyCollection.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>matplotlib.~.AxesSubplot</b>.</p>

---

### to_dict




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">to_dict</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>


Export projection to dict(json).

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>dict</b>.</p>

---

### to_list




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">to_list</span><span style="font-style: italic; color: black;font-size: 120%;">(ctype = <span style="color:#48566B">"PCI"</span>):</span></span>


Export projection to list.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>ctype  = </b> <code>str</code>. <span style="color:#48566B;">Default 'PCI'.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Export format. Can be 'PCI', 'USGS'.   </p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>list</b>.</p>

---

### to_str




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">to_str</span><span style="font-style: italic; color: black;font-size: 120%;">(ctype = <span style="color:#48566B">"Wkt"</span>):</span></span>


Export projection to string.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>ctype  = </b> <code>str</code>. <span style="color:#48566B;">Default 'Wkt'.</span></p><p style="padding-left: 1em;text-indent: 1em;">Export format. Can be 'MICoordSys', 'PrettyWkt', 'Proj4', 'Wkt', 'XML'.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>str</b>.</p>

---

## Property 



### WKID


Well-known ID Code and name. -> tuple(float, str)



---

### angular_units


Angular units. --> <code> tuple(float, str)</code>



---

### area_of_interest


The area of use's geometry of the crs in WGS84. -> Geometry.



---

### area_of_use


Get the area where the coordinate system is used. -> tuple(West, South, East, North in degree).



---

### axes_count


Number of coordinate axes. --> <code> int</code>



---

### central_longitude


Get the longitude of the central meridian. -> float



---

### change_longitude


Date Line -> float



---

### datum_name


Datum name. --> <code> str</code>



---

### gcs


Get projection parameters. -> CoordinateReferenceSystem



---

### inv_flattening


Inverse flattening. --> <code> float</code>



---

### linear_units


Linear units and name. -> tuple(float, str).



---

### name


Name of the coordinate system. --> <code> str</code>



---

### planet


The planet of the coordinate system. -> str



---

### primem


The prime meridian and name. -> tuple(float, str)



---

### proj_method


The project method name. -> str



---

### radius


Ellipsoid radius. --> <code> float</code>



---

### semi_major


Semi-major axis. --> <code> float</code>



---

### semi_minor


Semi-minor axis. --> <code> float</code>



---

### spheroid_name


Spheroid name. --> <code> str</code>



---

### type


Space Reference Type. -> str



---