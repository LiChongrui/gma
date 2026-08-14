---
title: Feature
date: 2026-08-14
sidebar: true
---
# gma.gio.Feature


<span style="background-color:#EFF0FC;display: block;line-height:1.5"><span style="color: gray;font-size:90%;">class</span> <span style="color: #616AE5; font-weight: bold;font-size: 150%;">Feature</span><span style="font-style: italic; color: black;font-size: 130%;">(geom = <span style="color:#48566B">None</span>, values = <span style="color:#48566B">[]</span>, gtype = <span style="color:#48566B">None</span>, ftypes = <span style="color:#48566B">None</span>, crs = <span style="color:#48566B">None</span>):</span></span>

Feature object for vector data. Create a Feature object.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>geom: </b> <code>None||Geometry</code>. <span style="color:#48566B;">Default = None</span></p><p style="padding-left: 1em;text-indent: 1em;">    The geometry of the feature. If None, create an empty geometry. </p><p style="text-indent: 1em;"><b>values: </b> <code>list</code>. <span style="color:#48566B;">Default = []</span></p><p style="padding-left: 1em;text-indent: 1em;">    The field values of the feature.    </p><p style="text-indent: 1em;"><b>gtype: </b> <code>str</code>. <span style="color:#48566B;">Default = None</span></p><p style="padding-left: 1em;text-indent: 1em;">    The geometry type of the feature. See `dtypes.DefinedGeomTypes` for valid types. If None, use the geometry type of `geom`.  </p><p style="text-indent: 1em;"><b>ftypes: </b> <code>None||listofFieldType</code>. <span style="color:#48566B;">Default = None</span></p><p style="padding-left: 1em;text-indent: 1em;">    The FieldTypes of the feature. If None, create an empty FieldTypes.</p><p style="text-indent: 1em;"><b>crs: </b> <code>str</code>. <span style="color:#48566B;">Default = None</span></p><p style="padding-left: 1em;text-indent: 1em;">    The projection of the geometry. If None, no projection is set.</p>

---

## Methods 



### copy




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">copy</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>


copy self. --> <code> Feature</code>



---

### plot




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">plot</span><span style="font-style: italic; color: black;font-size: 120%;">(ax = <span style="color:#48566B">None</span>, **kwargs):</span></span>


Make plots of Geometry.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>ax  = </b> <code>None||matplotlib.~.AxesSubplot</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    A matplotlib subplot. If None, a default axes will be created. </p><p style="text-indent: 1em;"><b>**kwargs</b>.</p><p style="padding-left: 1em;text-indent: 1em;">Other plotting parameters. For more, see: ~.carto.utils.PolyCollection/LineCollection/PointCollection.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>matplotlib.~.AxesSubplot</b>.</p>

---

### set_fid




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">set_fid</span><span style="font-style: italic; color: black;font-size: 120%;">(fid):</span></span>


Set the feature identifier.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>fid: </b> <code>int</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    the new feature identifier value to assign.</p>

---

### set_geom




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">set_geom</span><span style="font-style: italic; color: black;font-size: 120%;">(geom):</span></span>


Set feature geometry. This function updates the features geometry, except that this function does not assume ownership of the passed geometry, but instead makes a copy of it.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>geom: </b> <code>Geometry</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    new geometry to apply to feature.</p>

---

### update




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">update</span><span style="font-style: italic; color: black;font-size: 120%;">(other):</span></span>


Set one feature from another. Overwrite the contents of this feature from the geometry and attributes of another.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>other: </b> <code>Feature</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    feature from which geometry and field values will be copied.</p>

---

## Property 



### crs


Get coordinate reference system. --> <code> CoordinateReferenceSystem</code>



---

### fid


Get feature identifier. --> <code> int</code>



---

### fields


Get fields for feature. --> <code> dict</code>



---

### ftypes


Get field types for feature. --> <code> FieldTypes</code>



---

### geom


Get geometry for feature. --> <code> Geometry</code>



---