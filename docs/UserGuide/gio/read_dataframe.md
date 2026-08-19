---
title: read_dataframe
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.gio.read_dataframe</p><span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[function] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">read_dataframe</span><span style="font-style: italic; color: black;font-size: 120%;">(df, geom_col = <span style="color:#48566B">None</span>, crs = <span style="color:#48566B">"WGS84"</span>, encoding = <span style="color:#48566B">"WKT"</span>, gtype = <span style="color:#48566B">None</span>, **kwargs):</span></span>

<p>Read pandas DataFrame as gma Layer.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>df</b>: <code style="text-indent: 0em;">DataFrame</code>. </p>
<p style="margin-left: 4em;">The pandas DataFrame that needs to be read.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>geom_col </b> = <code style="text-indent: 0em;">str||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Geometry field name. If None, there is no geometry.</p>
<p style="margin-left: 2em;"><b>crs </b> = <code style="text-indent: 0em;">str||int||class</code>. <span style="color:#48566B;"> Default 'WGS84'</span>. </p>
<p style="margin-left: 4em;">The output coordinate system. Can be EPSG, WKT, Proj4, and other types of coordinate characters.</p>
<p style="margin-left: 2em;"><b>encoding </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'WKT'</span>. </p>
<p style="margin-left: 4em;">Type of geometry encoding. Can be Direct/WKT/WKB/PointFromColumns.</p>
<p style="margin-left: 4em;">If the encoding is "Direct" or not specified, then the field attribute must be set to the name of the source geometry field, if there are multiple source geometry fields. If neither encoding nor field are specified, it is assumed that the name of source geometry field is the value of the name attribute.</p>
<p style="margin-left: 4em;">If the encoding is "WKT" or "WKB" then the field attribute must be set to the name of the source field containing the WKT or WKB geometry.</p>
<p style="margin-left: 4em;">If the encoding is "PointFromColumns" then the x, y, z and m attributes must be set to the names of the columns to be used for the X, Y, Z and M coordinates in kwargs. The z and m attributes are optional.</p>
<p style="margin-left: 2em;"><b>gtype </b> = <code style="text-indent: 0em;">str||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Output geometry type. Supported geometry type include:</p>
<p style="margin-left: 6em;">'Point', 'MultiPoint', 'Line', 'MultiLine', 'Polygon', 'MultiPolygon'.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to geometry field. For more, see ogr OGRVRTLayer/GeometryField.</p>
<p style="margin-left: 4em;">(https://gdal.org/en/stable/drivers/vector/vrt.html).</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
