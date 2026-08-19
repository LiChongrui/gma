---
title: Feature
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.gio.Feature</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">Feature</span><span style="font-style: italic; color: black;font-size: 130%;">(geom = <span style="color:#48566B">None</span>, values = <span style="color:#48566B">[]</span>, gtype = <span style="color:#48566B">None</span>, ftypes = <span style="color:#48566B">None</span>, crs = <span style="color:#48566B">None</span>):</span></span>

<p>Create a Feature object.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>geom </b> = <code style="text-indent: 0em;">None||Geometry</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The geometry of the feature. If None, create an empty geometry.</p>
<p style="margin-left: 2em;"><b>values </b> = <code style="text-indent: 0em;">list</code>. <span style="color:#48566B;"> Default []</span>. </p>
<p style="margin-left: 4em;">The field values of the feature.</p>
<p style="margin-left: 2em;"><b>gtype </b> = <code style="text-indent: 0em;">str||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The geometry type of the feature. See `dtypes.DefinedGeomTypes` for valid types. If None, use the geometry type of `geom`.</p>
<p style="margin-left: 2em;"><b>ftypes </b> = <code style="text-indent: 0em;">None||list of FieldType</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The FieldTypes of the feature. If None, create an empty FieldTypes.</p>
<p style="margin-left: 2em;"><b>crs </b> = <code style="text-indent: 0em;">str||int||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The projection of the geometry. If None, no projection is set.</p>

## Method

### copy
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.copy</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>

<p style="margin-left: 2em;">copy self. --> <code style="text-indent: 0em;">Feature</code></p>

### plot
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.plot</span><span style="font-style: italic; color: black;font-size: 120%;">(ax = <span style="color:#48566B">None</span>, **kwargs):</span></span>

<p>Make plots of Geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>ax </b> = <code style="text-indent: 0em;">None||matplotlib</code>. <span style="color:#48566B;">~.AxesSubplot. Default None</span>. </p>
<p style="margin-left: 4em;">A matplotlib subplot. If None, a default axes will be created.</p>
<p style="margin-left: 2em;"><b>**kwargs</b></p>
<p style="margin-left: 4em;">Other plotting parameters. For more, see:</p>
<p style="margin-left: 6em;">~.carto.utils.PolyCollection/LineCollection/PointCollection.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>matplotlib.~.AxesSubplot</b></p>

### set_fid
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.set_fid</span><span style="font-style: italic; color: black;font-size: 120%;">(fid):</span></span>

<p>Set the feature identifier.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>fid</b>: <code style="text-indent: 0em;">int</code>. </p>
<p style="margin-left: 4em;">the new feature identifier value to assign.</p>

### set_geom
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.set_geom</span><span style="font-style: italic; color: black;font-size: 120%;">(geom):</span></span>

<p>Set feature geometry. This function updates the features geometry, except that this function does not assume ownership of the passed geometry, but instead makes a copy of it.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>geom</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">new geometry to apply to feature.</p>

### update
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.update</span><span style="font-style: italic; color: black;font-size: 120%;">(other):</span></span>

<p>Set one feature from another. Overwrite the contents of this feature from the geometry and attributes of another.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Feature</code>. </p>
<p style="margin-left: 4em;">feature from which geometry and field values will be copied.</p>

## Property

### crs
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.crs</span><span style=""></span></span>

<p style="margin-left: 2em;">Get coordinate reference system. --> <code style="text-indent: 0em;">CoordinateReferenceSystem</code></p>

### fid
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.fid</span><span style=""></span></span>

<p style="margin-left: 2em;">Get feature identifier. --> <code style="text-indent: 0em;">int</code></p>

### fields
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.fields</span><span style=""></span></span>

<p style="margin-left: 2em;">Get fields for feature. --> <code style="text-indent: 0em;">dict</code></p>

### ftypes
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.ftypes</span><span style=""></span></span>

<p style="margin-left: 2em;">Get field types for feature. --> <code style="text-indent: 0em;">FieldTypes</code></p>

### geom
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.geom</span><span style=""></span></span>

<p style="margin-left: 2em;">Get geometry for feature. --> <code style="text-indent: 0em;">Geometry</code></p>
