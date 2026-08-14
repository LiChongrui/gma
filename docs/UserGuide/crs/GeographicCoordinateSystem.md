---
title: GeographicCoordinateSystem
date: 2026-08-14
sidebar: true
---
# gma.crs.GeographicCoordinateSystem


<span style="background-color:#EFF0FC;display: block;line-height:1.5"><span style="color: gray;font-size:90%;">class</span> <span style="color: #616AE5; font-weight: bold;font-size: 150%;">GeographicCoordinateSystem</span><span style="font-style: italic; color: black;font-size: 130%;">(name = <span style="color:#48566B">"GMA GCS"</span>, angular_unit = <span style="color:#48566B">"degree"</span>, primem = <span style="color:#48566B">"Greenwich"</span>, ellipsoid = <span style="color:#48566B">"WGS_84"</span>, datum = <span style="color:#48566B">None</span>):</span></span>

geographic coordinate system Create a geographic coordinate system!

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>name  = </b> <code>str</code>. <span style="color:#48566B;">Default 'GMA GCS'.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Name of the new geographical coordinate system.</p><p style="text-indent: 1em;"><b>angular_unit  = </b> <code>float||str</code>. <span style="color:#48566B;">Default 'Degree'.</span></p><p style="padding-left: 1em;text-indent: 1em;">Angular unit value. See more default angular units: AngularUnits class! If you need to customize the angle unit, you can enter a real number.</p><p style="text-indent: 1em;"><b>primem  = </b> <code>float||str</code>. <span style="color:#48566B;">Default 'Greenwich'.</span></p><p style="padding-left: 1em;text-indent: 1em;">Prime meridian. See more default prime meridians: PRIMEMs class! If you need to customize the prime meridian, you can enter a real number.</p><p style="text-indent: 1em;"><b>ellipsoid  = </b> <code>str||aclassofEllipsoid</code>. <span style="color:#48566B;">Default 'WGS84'.</span></p><p style="padding-left: 1em;text-indent: 1em;">Ellipsoid. See more default prime ellipsoids: Ellips class! If you need to customize the ellipsoid, please use the Ellipsoid class to initialize.</p><p style="text-indent: 1em;"><b>datum  = </b> <code>None||aclassofDatum</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">Datum. If None, the ellipsoid is automatically configured based on the datum.</p><p style="padding-left: 1em;text-indent: 1em;">If it is a class of Datum, the parameter of Ellipsoid will be ignored.</p>

---

## Methods 



### copy




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">copy</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>


Clone crs. --> <code> CoordinateReferenceSystem</code>



---

### get_proj_parms




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">get_proj_parms</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>


Get projection parameters.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code>dict</code>.</p>

---

### plot




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">plot</span><span style="font-style: italic; color: black;font-size: 120%;">(ax = <span style="color:#48566B">None</span>, **kwargs):</span></span>


Make area of use of the CoordinateReferenceSystem in world.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>ax  = </b> <code>None||matplotlib.~.AxesSubplot</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    A matplotlib subplot. If None, a default axes will be created. </p><p style="text-indent: 1em;"><b>**kwargs</b>.</p><p style="padding-left: 1em;text-indent: 1em;">Other plotting parameters of CoordinateReferenceSystem's geometry. For more, see: ~.carto.utils.PolyCollection.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code>matplotlib.~.AxesSubplot</code>.</p>

---

### to_dict




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">to_dict</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>


Export projection to dict(json).

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code>dict</code>.</p>

---

### to_list




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">to_list</span><span style="font-style: italic; color: black;font-size: 120%;">(ctype = <span style="color:#48566B">"PCI"</span>):</span></span>


Export projection to list.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>ctype  = </b> <code>str</code>. <span style="color:#48566B;">Default 'PCI'.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Export format. Can be 'PCI', 'USGS'.   </p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code>list</code>.</p>

---

### to_str




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">to_str</span><span style="font-style: italic; color: black;font-size: 120%;">(ctype = <span style="color:#48566B">"Wkt"</span>):</span></span>


Export projection to string.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>ctype  = </b> <code>str</code>. <span style="color:#48566B;">Default 'Wkt'.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Export format. Can be 'MICoordSys', 'PrettyWkt', 'Proj4', 'Wkt', 'XML'.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code>str</code>.</p>

---

## Property 



### WKID


Well-known ID Code and name. --> <code> tuple(float, str)</code>



---

### angular_units


Angular units. --> <code> tuple(float, str)</code>



---

### area_of_interest


The area of use's geometry of the crs in WGS84. --> <code> Geometry.</code>



---

### area_of_use


Get the area where the coordinate system is used. --> <code> tuple(West, South, East, North in degree).</code>



---

### axes_count


Number of coordinate axes. --> <code> int</code>



---

### central_longitude


Get the longitude of the central meridian. --> <code> float</code>



---

### change_longitude


Date Line --> <code> float</code>



---

### datum_name


Datum name. --> <code> str</code>



---

### gcs


Get projection parameters. --> <code> CoordinateReferenceSystem</code>



---

### inv_flattening


Inverse flattening. --> <code> float</code>



---

### linear_units


Linear units and name. --> <code> tuple(float, str).</code>



---

### name


Name of the coordinate system. --> <code> str</code>



---

### planet


The planet of the coordinate system. --> <code> str</code>



---

### primem


The prime meridian and name. --> <code> tuple(float, str)</code>



---

### proj_method


The project method name. --> <code> str</code>



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


Space Reference Type. --> <code> str</code>



---