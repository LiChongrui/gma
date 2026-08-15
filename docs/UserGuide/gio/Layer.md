---
title: Layer
date: 2026-08-15
sidebar: true
---
<span style="font-size: 120%;font-weight: bold;">gma.gio.Layer</span>


<span style="background-color:#EFF0FC;display: block;line-height:1.5"><span style="color: gray;font-size:90%;">class</span> <span style="color: #616AE5; font-weight: bold;font-size: 150%;">Layer</span><span style="font-style: italic; color: black;font-size: 130%;">(data = <span style="color:#48566B">None</span>, name = <span style="color:#48566B">None</span>, gtype = <span style="color:#48566B">None</span>, ftypes = <span style="color:#48566B">None</span>, crs = <span style="color:#48566B">None</span>, **kwargs):</span></span>

GMA Layer class. Initialize a Layer object.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>data: </b> <code style="text-indent: 0">Layer||Geometry||Feature||list||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">The data source to create the Layer. It can be: 1) Another GMA Layer object.</p><p style="padding-left: 1em;text-indent: 1em;">2) A Geometry object or a Feature object, or a list of Geometry/Features.</p><p style="padding-left: 1em;text-indent: 1em;">3) None, create an empty Layer.</p><p style="text-indent: 1em;"><b>name: </b> <code style="text-indent: 0">str||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The name of the Layer. If data is a Layer, name can not be set.</p><p style="text-indent: 1em;"><b>gtype: </b> <code style="text-indent: 0">str||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">The geometry type of the Layer. Supported geometry type include: 'Point', 'MultiPoint', 'Line', 'MultiLine', 'Polygon', 'MultiPolygon'.</p><p style="padding-left: 1em;text-indent: 1em;">If data is a Layer, gtype can not be set.</p><p style="text-indent: 1em;"><b>ftypes: </b> <code style="text-indent: 0">FieldType||list||dict||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">The field types of the Layer. It can be: 1) A FieldType object.</p><p style="padding-left: 1em;text-indent: 1em;">2) A list of FieldType objects.</p><p style="padding-left: 1em;text-indent: 1em;">3) A dict of field name and field type.</p><p style="padding-left: 1em;text-indent: 1em;">If data is a Layer, ftypes can not be set.</p><p style="text-indent: 1em;"><b>crs: </b> <code style="text-indent: 0">str||int||class||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">The coordinate system of the Layer. Can be EPSG, WKT, Proj4, and other types of coordinate characters. If data is a Layer, crs can not be set.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geodatabase.GeoDatabase.</p>

---

## Methods 



### add_feature




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">add_feature</span><span style="font-style: italic; color: black;font-size: 120%;">(*features):</span></span>


Add features to Layer.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>*feature: </b> <code style="text-indent: 0">Feature</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    One or more vector features.</p>

---

### add_field




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">add_field</span><span style="font-style: italic; color: black;font-size: 120%;">(name = <span style="color:#48566B">None</span>, dtype = <span style="color:#48566B">"UNKNOWN"</span>):</span></span>


Add a field to Layer.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>name: </b> <code style="text-indent: 0">str</code>. <span style="color:#48566B;">Default = None</span></p><p style="padding-left: 1em;text-indent: 1em;">    The name of the field. None for dtype name.</p><p style="text-indent: 1em;"><b>dtype: </b> <code style="text-indent: 0">str</code>. <span style="color:#48566B;">Default = 'UNKNOWN'</span></p><p style="padding-left: 1em;text-indent: 1em;">    The data type of the field. See `dtypes.DefinedFieldDataTypes` for valid types.</p>

---

### boundary




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">boundary</span><span style="font-style: italic; color: black;font-size: 120%;">(**kwargs):</span></span>


Creates buffer polygons around input features to a specified distance. **kwargs:     Other parameters passed to _algos.geo.layer.vector_translate.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### buffer




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">buffer</span><span style="font-style: italic; color: black;font-size: 120%;">(distance = <span style="color:#48566B">10</span>, side = <span style="color:#48566B">"Both"</span>, dissolve = <span style="color:#48566B">False</span>, **kwargs):</span></span>


Creates buffer polygons around input features to a specified distance.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>distance  = </b> <code style="text-indent: 0">float</code>. <span style="color:#48566B;">Default 10.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The distance around the input features that will be buffered.</p><p style="text-indent: 1em;"><b>side  = </b> <code style="text-indent: 0">str</code>. <span style="color:#48566B;">Default 'Both'.</span></p><p style="padding-left: 1em;text-indent: 1em;">Specifies the sides of the input features that will be buffered. May be 'Both', 'Left' or 'Right'. 'Both' is only supported for Polygon.</p><p style="text-indent: 1em;"><b>dissolve  = </b> <code style="text-indent: 0">bool</code>. <span style="color:#48566B;">Default False.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Whether to dissolve the buffers into one feature.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### calculate_geometry




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">calculate_geometry</span><span style="font-style: italic; color: black;font-size: 120%;">(area = <span style="color:#48566B">False</span>, length = <span style="color:#48566B">False</span>, gtype = <span style="color:#48566B">False</span>, circularity = <span style="color:#48566B">False</span>, num_points = <span style="color:#48566B">False</span>, num_geometries = <span style="color:#48566B">False</span>, ellipsoid_area = <span style="color:#48566B">False</span>, ellipsoid_length = <span style="color:#48566B">False</span>, keep_fields = <span style="color:#48566B">False</span>, keep_geom = <span style="color:#48566B">True</span>, **kwargs):</span></span>


Calculate geometry attribute.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>area  = </b> <code style="text-indent: 0">bool||str</code>. <span style="color:#48566B;">Default False.</span></p><p style="padding-left: 1em;text-indent: 1em;">Whether to calculate the area of the polygon. GeoGCS: deg2; ProjCS:m2.</p><p style="padding-left: 1em;text-indent: 1em;">If str, it will be the new name of the output result.</p><p style="text-indent: 1em;"><b>length  = </b> <code style="text-indent: 0">bool||str</code>. <span style="color:#48566B;">Default False.</span></p><p style="padding-left: 1em;text-indent: 1em;">Whether to calculate the length of a line. GeoGCS: deg; ProjCS:m.</p><p style="padding-left: 1em;text-indent: 1em;">If str, it will be the new name of the output result.</p><p style="text-indent: 1em;"><b>gtype  = </b> <code style="text-indent: 0">bool||str</code>. <span style="color:#48566B;">Default False.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Whether to get the type of the geometry. If str, it will be the new name of the output result.</p><p style="text-indent: 1em;"><b>circularity  = </b> <code style="text-indent: 0">bool||str</code>. <span style="color:#48566B;">Default False.</span></p><p style="padding-left: 1em;text-indent: 1em;">Whether to computes the Circularity Index from the given Geometry.</p><p style="padding-left: 1em;text-indent: 1em;">If str, it will be the new name of the output result.</p><p style="text-indent: 1em;"><b>num_points  = </b> <code style="text-indent: 0">bool||str</code>. <span style="color:#48566B;">Default False.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Whether to count the number of inflection points. If str, it will be the new name of the output result.</p><p style="text-indent: 1em;"><b>NumGeometries  = </b> <code style="text-indent: 0">bool||str</code>. <span style="color:#48566B;">Default False.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Whether to count the number of geometries. If str, it will be the new name of the output result.</p><p style="text-indent: 1em;"><b>ellipsoid_area  = </b> <code style="text-indent: 0">bool||str</code>. <span style="color:#48566B;">Default False.</span></p><p style="padding-left: 1em;text-indent: 1em;">Whether to calculate the area of the polygon using crs's ellipsoid. Unit: m2.</p><p style="padding-left: 1em;text-indent: 1em;">If str, it will be the new name of the output result.</p><p style="text-indent: 1em;"><b>ellipsoid_length  = </b> <code style="text-indent: 0">bool||str</code>. <span style="color:#48566B;">Default False.</span></p><p style="padding-left: 1em;text-indent: 1em;">Whether to calculate the length of a line using crs's ellipsoid. Unit: m.</p><p style="padding-left: 1em;text-indent: 1em;">If str, it will be the new name of the output result.</p><p style="text-indent: 1em;"><b>keep_fields  = </b> <code style="text-indent: 0">bool||list</code>. <span style="color:#48566B;">Default False.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Whether to retain attribute table fields. If list, it specifies the field names to be retained.</p><p style="text-indent: 1em;"><b>keep_geom  = </b> <code style="text-indent: 0">bool</code>. <span style="color:#48566B;">Default True.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Whether to retain geometry field.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### calculate_statistics




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">calculate_statistics</span><span style="font-style: italic; color: black;font-size: 120%;">(statistics, case = <span style="color:#48566B">None</span>, where = <span style="color:#48566B">None</span>, **kwargs):</span></span>


Calculates summary statistics for fields in a table.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>statistics: </b> <code style="text-indent: 0">dict||list||str</code>.</p><p style="padding-left: 1em;text-indent: 1em;">Conduct statistical analysis on selected fields according to the predefined statistical methods.</p><p style="padding-left: 1em;text-indent: 1em;">Format 1: Statistics = {Method: [Field0, Field1, ...]} All fields will undergo Method(Field) and will be stored in Field_Method field.</p><p style="padding-left: 1em;text-indent: 1em;">Example: Statistics = {'sum': ['field0', 'field1']} Format 2: Statistics = {Method: {Field0: NewName0, Field1: NewName1, ...}} All fields will undergo Method(Field) and will be stored in NewName field.</p><p style="padding-left: 1em;text-indent: 1em;">Example: Statistics = {'sum': {'field0': 'NewName0sum', 'field1': 'NewName1sum'}} Format 3: Statistics = 'Field0 + Field1 AS sum_result' Calculate the sum of Field0 and Field1 as "sum_result".</p><p style="padding-left: 1em;text-indent: 1em;">If it is a list, it must be a list of str in the format 3.</p><p style="padding-left: 1em;text-indent: 1em;">Including statistics types: 'min', 'max', 'sum', 'avg', 'count', 'total', ...</p><p style="padding-left: 1em;text-indent: 1em;">For more, see SQLite grammar.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>case  = </b> <code style="text-indent: 0">str||list||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">The field or fields in the input that will be used to calculate statistics separately for each unique attribute value (or combination of attribute values when multiple fields are specified).</p><p style="text-indent: 1em;"><b>where  = </b> <code style="text-indent: 0">str||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">The SQL query string expressions to evaluate. For example: Where = 'ROWID = 1 OR Name IN ("GMA", "Layer")' 'ROWID' and 'Name' are the Layer field names.</p><p style="padding-left: 1em;text-indent: 1em;">Supported Rules: Comparison Operators: =, !=, <>, <, >, <=, >= Logical Operators: AND, OR, NOT Wildcard Search Symbols: LIKE Range Condition: BETWEEN, IN, NOT IN Null-Value Check Operators: IS NULL, IS NOT NULL Regular expression matching: REGEXP</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### centroid




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">centroid</span><span style="font-style: italic; color: black;font-size: 120%;">(**kwargs):</span></span>


The points representing the centroid of each geometry.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### clip




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">clip</span><span style="font-style: italic; color: black;font-size: 120%;">(other, **kwargs):</span></span>


Clip off areas that are not covered by the method layer.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to io.CreateLayer.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### closest_point




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">closest_point</span><span style="font-style: italic; color: black;font-size: 120%;">(other, **kwargs):</span></span>


Calculate the closest point on the tow layer.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>other: </b> <code style="text-indent: 0">Layer</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Another GMA Layer!</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### collect




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">collect</span><span style="font-style: italic; color: black;font-size: 120%;">(use_field = <span style="color:#48566B">None</span>, keep_fields = <span style="color:#48566B">True</span>, **kwargs):</span></span>


Collect features based on field values.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>use_field  = </b> <code style="text-indent: 0">str||list||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The field name(s) used to merge Features! If it's None, then dissolve all features.</p><p style="text-indent: 1em;"><b>keep_fields  = </b> <code style="text-indent: 0">bool||list</code>. <span style="color:#48566B;">Default False.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Whether to retain attribute table fields. If list, it specifies the field names to be retained.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### concave_hull




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">concave_hull</span><span style="font-style: italic; color: black;font-size: 120%;">(**kwargs):</span></span>


The concave hull of a geometry is the smallest concave Polygon containing all the points in each geometry.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### convex_hull




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">convex_hull</span><span style="font-style: italic; color: black;font-size: 120%;">(**kwargs):</span></span>


The convex hull of a geometry is the smallest convex Polygon containing all the points in each geometry.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### copy




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">copy</span><span style="font-style: italic; color: black;font-size: 120%;">(**kwargs):</span></span>


Copy replica to default driver.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### delaunay_triangulation




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">delaunay_triangulation</span><span style="font-style: italic; color: black;font-size: 120%;">(edges_only = <span style="color:#48566B">False</span>, tolerance = <span style="color:#48566B">0</span>, **kwargs):</span></span>


Return a Delaunay triangulation of the vertices of the geometry.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>tolerance  = </b> <code style="text-indent: 0">float</code>. <span style="color:#48566B;">Default 0.0.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Snapping tolerance to use for improved robustness.</p><p style="text-indent: 1em;"><b>edges_only  = </b> <code style="text-indent: 0">bool</code>. <span style="color:#48566B;">Default False.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Whether the output geometry should be filled polygons(False) or just boundary lines(True).</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### dissolve




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">dissolve</span><span style="font-style: italic; color: black;font-size: 120%;">(use_field = <span style="color:#48566B">None</span>, keep_fields = <span style="color:#48566B">True</span>, **kwargs):</span></span>


Dissolve features based on field values.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>use_field  = </b> <code style="text-indent: 0">str||list||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The field name(s) used to dissolve Features! If it's None, then dissolve all features.</p><p style="text-indent: 1em;"><b>keep_fields  = </b> <code style="text-indent: 0">bool||list</code>. <span style="color:#48566B;">Default False.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Whether to retain attribute table fields. If list, it specifies the field names to be retained.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### distance




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">distance</span><span style="font-style: italic; color: black;font-size: 120%;">(other, method = <span style="color:#48566B">None</span>, densify_fract = <span style="color:#48566B">0.1</span>, **kwargs):</span></span>


Calculates the distance between all geometric shapes within two Layers.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>other: </b> <code style="text-indent: 0">Layer</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Another GMA Layer!</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>method  = </b> <code style="text-indent: 0">str||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Calculate method. May be None(normal distance), 'Hausdorff' or 'Frechet'.</p><p style="text-indent: 1em;"><b>densify_fract  = </b> <code style="text-indent: 0">float</code>. <span style="color:#48566B;">Default 0.1.</span></p><p style="padding-left: 1em;text-indent: 1em;">A value between 0 and 1, that splits each subsegment of a line string into equal length segments, making the approximation less coarse.</p><p style="padding-left: 1em;text-indent: 1em;">A densify value of 0.5 will add a point halfway between each pair of points. A densify value of 0.25 will add a point every quarter of the way between each pair of points.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### drop




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">drop</span><span style="font-style: italic; color: black;font-size: 120%;">(rows = <span style="color:#48566B">None</span>, fields = <span style="color:#48566B">None</span>):</span></span>


Drop specified features or fields.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>rows  = </b> <code style="text-indent: 0">int||list||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    List of FIDs to be deleted.</p><p style="text-indent: 1em;"><b>fields  = </b> <code style="text-indent: 0">str||list||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    List of field names to be deleted.</p>

---

### envelope




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">envelope</span><span style="font-style: italic; color: black;font-size: 120%;">(union = <span style="color:#48566B">False</span>, **kwargs):</span></span>


The envelope of a geometry is the bounding rectangle.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>union  = </b> <code style="text-indent: 0">bool</code>. <span style="color:#48566B;">Default True.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Whether to first integrate all elements before calculating.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### erase




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">erase</span><span style="font-style: italic; color: black;font-size: 120%;">(other, **kwargs):</span></span>


Remove areas that are covered by the method layer.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>other: </b> <code style="text-indent: 0">Layer</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Another GMA Layer!</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to io.CreateLayer.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### explode




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">explode</span><span style="font-style: italic; color: black;font-size: 120%;">(**kwargs):</span></span>


Separate a selected multipart feature into its individual.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### extent




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">extent</span><span style="font-style: italic; color: black;font-size: 120%;">(**kwargs):</span></span>


The extent of a geometry is the bounding rectangle.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### exterior_ring




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">exterior_ring</span><span style="font-style: italic; color: black;font-size: 120%;">(**kwargs):</span></span>




<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### find_overlaps




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">find_overlaps</span><span style="font-style: italic; color: black;font-size: 120%;">(**kwargs):</span></span>


Find overlapping features in Layer.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.   </p>

---

### fix_geometry




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">fix_geometry</span><span style="font-style: italic; color: black;font-size: 120%;">(**kwargs):</span></span>


Fix invalid geometric features in Layer.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### gen_grid




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">gen_grid</span><span style="font-style: italic; color: black;font-size: 120%;">(grid_type = <span style="color:#48566B">"Square"</span>, size = <span style="color:#48566B">1</span>, **kwargs):</span></span>


Gen a grid of cells (having the edge length of size) precisely covering the input Layer.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>grid_type  = </b> <code style="text-indent: 0">str</code>. <span style="color:#48566B;">Default 'Square'.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Grid type.Can be 'Square', 'Triangular', 'Hexagonal'.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### geom_self_test




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">geom_self_test</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>


Geometry self-test. Include: Empty, Simple, Valid, 3D, Measured, Valid Reason, Polygon Clockwise Rule(Counter-Clockwise Rule).

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p><p style="padding-left: 1em;text-indent: 1em;">In this context, 0 indicates False, 1 indicates True, -1 indicates that the input geometry object is not of the required type.</p>

---

### geom_to_str




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">geom_to_str</span><span style="font-style: italic; color: black;font-size: 120%;">(wkt = <span style="color:#48566B">True</span>, gml = <span style="color:#48566B">False</span>, kml = <span style="color:#48566B">False</span>, json = <span style="color:#48566B">False</span>, ewkb = <span style="color:#48566B">False</span>, ewkt = <span style="color:#48566B">False</span>, svg = <span style="color:#48566B">False</span>, **kwargs):</span></span>


Converts geometry to string.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>wkt  = </b> <code style="text-indent: 0">bool</code>. <span style="color:#48566B;">Default True.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Whether to convert to WTK string.</p><p style="text-indent: 1em;"><b>gml  = </b> <code style="text-indent: 0">bool</code>. <span style="color:#48566B;">Default False.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Whether to convert to Gml string.</p><p style="text-indent: 1em;"><b>kml  = </b> <code style="text-indent: 0">bool</code>. <span style="color:#48566B;">Default False.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Whether to convert to Kml string.</p><p style="text-indent: 1em;"><b>json  = </b> <code style="text-indent: 0">bool</code>. <span style="color:#48566B;">Default False.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Whether to convert to GeoJSON string.</p><p style="text-indent: 1em;"><b>ewkb  = </b> <code style="text-indent: 0">bool</code>. <span style="color:#48566B;">Default False.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Whether to convert to EWKB string.</p><p style="text-indent: 1em;"><b>ewkt  = </b> <code style="text-indent: 0">bool</code>. <span style="color:#48566B;">Default False.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Whether to convert to EWKT string.</p><p style="text-indent: 1em;"><b>svg  = </b> <code style="text-indent: 0">bool</code>. <span style="color:#48566B;">Default False.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Whether to convert to SVG string.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### get_feature




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">get_feature</span><span style="font-style: italic; color: black;font-size: 120%;">(row_num = <span style="color:#48566B">0</span>):</span></span>


Fetch a feature by its identifier.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>row_num  = </b> <code style="text-indent: 0">int</code>. <span style="color:#48566B;">Default 0.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The feature number of the feature to read.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Feature:</b></p><p style="padding-left: 1em;text-indent: 1em;">    A new feature now owned by the caller</p>

---

### identity




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">identity</span><span style="font-style: italic; color: black;font-size: 120%;">(other, o_prefix = <span style="color:#48566B">"L1_"</span>, **kwargs):</span></span>


Identify the features of this layer with the ones from the identity layer.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>other: </b> <code style="text-indent: 0">Layer</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Another GMA Layer!</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>o_prefix  = </b> <code style="text-indent: 0">str</code>. <span style="color:#48566B;">Default 'L1_'.</span></p><p style="padding-left: 1em;text-indent: 1em;">Set a prefix for the field names that will be created from the fields of the method layer.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to io.CreateLayer.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### interior_ring




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">interior_ring</span><span style="font-style: italic; color: black;font-size: 120%;">(n = <span style="color:#48566B">1</span>, **kwargs):</span></span>




<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>n  = </b> <code style="text-indent: 0">int</code>. <span style="color:#48566B;">Default 1.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Extracted inner ring index (starting from 1).</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### interpolation




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">interpolation</span><span style="font-style: italic; color: black;font-size: 120%;">(v_field, bounds = <span style="color:#48566B">None</span>, resolution = <span style="color:#48566B">None</span>, method = <span style="color:#48566B">"idw"</span>, ipt_opts = <span style="color:#48566B">{}</span>, **kwargs):</span></span>


Interpolate points into raster dataset.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>v_field: </b> <code style="text-indent: 0">str</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    The field to be interpolated.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>bounds  = </b> <code style="text-indent: 0">tuple</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">The four boundaries of the interpolation result are the minimum longitude (left), the minimum latitude (bottom), the maximum longitude (right), and the maximum latitude (top). The default (None) is to extract the range from the input coordinate points.</p><p style="text-indent: 1em;"><b>resolution  = </b> <code style="text-indent: 0">float</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">The resolution of the interpolation result. The default (None) is 1/10 of the minimum bounds X and Y difference.</p><p style="text-indent: 1em;"><b>method  = </b> <code style="text-indent: 0">str</code>. <span style="color:#48566B;">Default 'idw'.</span></p><p style="padding-left: 1em;text-indent: 1em;">Interpolation method. Can be 'b_spline', 'idw', 'kriging', 'natural_neighbor', 'nearest', 'rbf' and 'trend'. For more, see smc.interp.</p><p style="text-indent: 1em;"><b>ipt_opts  = </b> <code style="text-indent: 0">dict</code>. <span style="color:#48566B;">Default {}.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Interpolation parameters. Corresponding to the interpolation method.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.dataset.raster_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Dataset||dict</code>.</p><p style="padding-left: 1em;text-indent: 1em;">Contains the raster dataset and other interpolation results. The keys are the names of the results, and the values are the corresponding raster datasets or other results.</p>

---

### intersection




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">intersection</span><span style="font-style: italic; color: black;font-size: 120%;">(other, o_prefix = <span style="color:#48566B">"L1_"</span>, **kwargs):</span></span>


Intersection of two layers.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>other: </b> <code style="text-indent: 0">Layer</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Another GMA Layer!</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>o_prefix  = </b> <code style="text-indent: 0">str</code>. <span style="color:#48566B;">Default 'L1_'.</span></p><p style="padding-left: 1em;text-indent: 1em;">Set a prefix for the field names that will be created from the fields of the method layer.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to io.CreateLayer.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### join




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">join</span><span style="font-style: italic; color: black;font-size: 120%;">(other, spatial_join = <span style="color:#48566B">None</span>, left_on = <span style="color:#48566B">None</span>, right_on = <span style="color:#48566B">None</span>, one_to_one = <span style="color:#48566B">True</span>, suffixes = <span style="color:#48566B">""</span>, ext_cond = <span style="color:#48566B">None</span>, **kwargs):</span></span>


Join the attribute table of RLayer into the first Layer.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>other: </b> <code style="text-indent: 0">Layer</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Another GMA Layer!</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>spatial_join  = </b> <code style="text-indent: 0">str</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">Spatial join method. Supported 'Intersects', 'Disjoint', 'Within', 'Equals', 'Touches'.</p><p style="padding-left: 1em;text-indent: 1em;">Default(None) no spatial join.</p><p style="text-indent: 1em;"><b>left_on  = </b> <code style="text-indent: 0">str||list||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">Feild names to join on in the self Layer. Can also be a list of the length of the self Layer. Default(None) using self FID column if spatial_join is None.</p><p style="text-indent: 1em;"><b>right_on  = </b> <code style="text-indent: 0">str||list||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">Feild names to join on in the other Layer. Can also be a list of the length of the other Layer. Default(None) using other FID column if spatial_join is None.</p><p style="text-indent: 1em;"><b>one_to_one  = </b> <code style="text-indent: 0">bool</code>. <span style="color:#48566B;">Default False.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Whether to keep only one feature in the second layer for each feature in the first layer.</p><p style="text-indent: 1em;"><b>suffixes  = </b> <code style="text-indent: 0">str</code>. <span style="color:#48566B;">Default ''.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Extended character used to mark the second layer column.</p><p style="text-indent: 1em;"><b>ext_cond  = </b> <code style="text-indent: 0">str||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">Additional SQL conditions for joining the two layers. For example: ext_cond = 'a0.field0 > 10 AND a1.field1 < 20'.</p><p style="padding-left: 1em;text-indent: 1em;">a0 and a1 are the aliases of the self and other layers, respectively.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### line_equidistant_points




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">line_equidistant_points</span><span style="font-style: italic; color: black;font-size: 120%;">(length, keep_fields = <span style="color:#48566B">True</span>, **kwargs):</span></span>


Generate equidistant points along the line geometry.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>length: </b> <code style="text-indent: 0">float</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Distance between points.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>keep_fields  = </b> <code style="text-indent: 0">bool</code>. <span style="color:#48566B;">Default True.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Whether to retain attribute table fields.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### merge




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">merge</span><span style="font-style: italic; color: black;font-size: 120%;">(*others, **kwargs):</span></span>


Merge all layers.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>*others: </b> <code style="text-indent: 0">Layer||listofLayer</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Other GMA Layers!</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### min_bounding_circle




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">min_bounding_circle</span><span style="font-style: italic; color: black;font-size: 120%;">(**kwargs):</span></span>


Constructs the Minimum Bounding Circle for a generic geometry.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### min_rotated_rectangle




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">min_rotated_rectangle</span><span style="font-style: italic; color: black;font-size: 120%;">(**kwargs):</span></span>


Calculate the minimum rotated rectangular polygon which encloses the input geometry.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### min_width




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">min_width</span><span style="font-style: italic; color: black;font-size: 120%;">(**kwargs):</span></span>


Calculate the LINESTRING geometry which represents the minimum diameter of the geometry.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### multi




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">multi</span><span style="font-style: italic; color: black;font-size: 120%;">(**kwargs):</span></span>


Make single part geometry into their multi counterpart.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### order_by




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">order_by</span><span style="font-style: italic; color: black;font-size: 120%;">(fields, ascending = <span style="color:#48566B">True</span>, **kwargs):</span></span>


Sort by field.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>fields: </b> <code style="text-indent: 0">str||list</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Fields or list of fields to be sorted.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>ascending  = </b> <code style="text-indent: 0">bool||list</code>. <span style="color:#48566B;">Default True.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Sort order, which can be True(ascending) or False(descending).</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.  </p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### plot




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">plot</span><span style="font-style: italic; color: black;font-size: 120%;">(ax = <span style="color:#48566B">None</span>, **kwargs):</span></span>


Make plots of Layer.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>ax  = </b> <code style="text-indent: 0">None||matplotlib.~.AxesSubplot</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    A matplotlib subplot. If None, a default axes will be created. </p><p style="text-indent: 1em;"><b>**kwargs</b>.</p><p style="padding-left: 1em;text-indent: 1em;">Other plotting parameters. For more, see: ~.carto.utils.PolyCollection/LineCollection/PointCollection.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>matplotlib.~.AxesSubplot</b>.</p>

---

### point_on_surface




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">point_on_surface</span><span style="font-style: italic; color: black;font-size: 120%;">(**kwargs):</span></span>


Computes a point guaranteed to lie in a polygon, or on a geometry.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### query




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">query</span><span style="font-style: italic; color: black;font-size: 120%;">(expr, tran_opts = <span style="color:#48566B">{}</span>, **kwargs):</span></span>


Query the data with a full SpatiaLite SQL expression.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>expr: </b> <code style="text-indent: 0">str</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    The query string to evaluate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>tran_opts  = </b> <code style="text-indent: 0">dict</code>. <span style="color:#48566B;">Default {}.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Vector translate options. For more, see _algos.geo.layer.vector_translate.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to ._algos.geo.vrt.VRTGeoDatabase.add_layer.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### rotate




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">rotate</span><span style="font-style: italic; color: black;font-size: 120%;">(angle = <span style="color:#48566B">90</span>, **kwargs):</span></span>


Rotate an angle of the layer.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>Angle  = </b> <code style="text-indent: 0">float</code>. <span style="color:#48566B;">Default 90.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Rotation angle (In Degrees) with the point [0, 0] as the origin.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### sanitize




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">sanitize</span><span style="font-style: italic; color: black;font-size: 120%;">(**kwargs):</span></span>


Sanitize geometry. Including removing duplicate points and ensuring closed rings.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### scale




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">scale</span><span style="font-style: italic; color: black;font-size: 120%;">(factor = <span style="color:#48566B">1</span>, **kwargs):</span></span>


Select the intersecting features.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>factor  = </b> <code style="text-indent: 0">float||list</code>. <span style="color:#48566B;">Default 1.</span></p><p style="padding-left: 1em;text-indent: 1em;">    X, Y scale factors. If a single value is provided, it is assumed that X = Y.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### select




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">select</span><span style="font-style: italic; color: black;font-size: 120%;">(where = <span style="color:#48566B">""</span>, keep_fields = <span style="color:#48566B">True</span>, keep_geom = <span style="color:#48566B">True</span>, **kwargs):</span></span>


Using SQL WHERE expressions to filter features by attribute table fields.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>where  = </b> <code style="text-indent: 0">str</code>. <span style="color:#48566B;">Default ''.</span></p><p style="padding-left: 1em;text-indent: 1em;">The SQL query string expressions to evaluate. For example: Where = 'ROWID = 1 OR Name IN ("GMA", "Layer")' 'ROWID' and 'Name' are the Layer field names.</p><p style="padding-left: 1em;text-indent: 1em;">Supported Rules: Comparison Operators: =, !=, <>, <, >, <=, >= Logical Operators: AND, OR, NOT Wildcard Search Symbols: LIKE Range Condition: BETWEEN, IN, NOT IN Null-Value Check Operators: IS NULL, IS NOT NULL Regular expression matching: REGEXP</p><p style="text-indent: 1em;"><b>keep_fields  = </b> <code style="text-indent: 0">bool||list</code>. <span style="color:#48566B;">Default False.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Whether to retain attribute table fields. If list, it specifies the field names to be retained.</p><p style="text-indent: 1em;"><b>keep_geom  = </b> <code style="text-indent: 0">bool</code>. <span style="color:#48566B;">Default True.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Whether to retain geometry field.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### select_overlay




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">select_overlay</span><span style="font-style: italic; color: black;font-size: 120%;">(other, method = <span style="color:#48566B">"Intersects"</span>, **kwargs):</span></span>


Select features that conform to the overlay rule.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>other: </b> <code style="text-indent: 0">Layer</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Another GMA Layer!</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>method  = </b> <code style="text-indent: 0">str</code>. <span style="color:#48566B;">Default 'Intersects'.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Overlay method. Supported methods include: 'Intersects', 'Disjoint', 'Within', 'Equals', 'Touches'.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### set_feature




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">set_feature</span><span style="font-style: italic; color: black;font-size: 120%;">(feature, fid = <span style="color:#48566B">None</span>):</span></span>


Rewrite an existing feature. To set a feature, but create it if it doesn't exist.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>feature: </b> <code style="text-indent: 0">Feature</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    A vector feature.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>fid  = </b> <code style="text-indent: 0">int||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The FID added to the layer. Defaults to the feature's FID.</p>

---

### set_spatial_filter




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">set_spatial_filter</span><span style="font-style: italic; color: black;font-size: 120%;">(geom = <span style="color:#48566B">None</span>):</span></span>




---

### shared_paths




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">shared_paths</span><span style="font-style: italic; color: black;font-size: 120%;">(other, **kwargs):</span></span>


Calculate the shared paths between two layers.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>other: </b> <code style="text-indent: 0">Layer</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Another GMA Layer!</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### shift




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">shift</span><span style="font-style: italic; color: black;font-size: 120%;">(distance = <span style="color:#48566B">1</span>, **kwargs):</span></span>


Shilf a distance of the layer.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>distance  = </b> <code style="text-indent: 0">float||list</code>. <span style="color:#48566B;">Default 1.</span></p><p style="padding-left: 1em;text-indent: 1em;">    X, Y shift distance. If a single value is provided, it is assumed that X = Y.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### shortest_line




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">shortest_line</span><span style="font-style: italic; color: black;font-size: 120%;">(other, **kwargs):</span></span>


Calculate the shortest line between the geometries of tow layers.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>other: </b> <code style="text-indent: 0">Layer</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Another GMA Layer!</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### simplify




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">simplify</span><span style="font-style: italic; color: black;font-size: 120%;">(tolerance = <span style="color:#48566B">0</span>, preserve_topology = <span style="color:#48566B">False</span>, **kwargs):</span></span>


Simplify geometries in the Layer.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>tolerance  = </b> <code style="text-indent: 0">float</code>. <span style="color:#48566B;">Default 0.0.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Tolerance allowed when simplifying geometric features.</p><p style="text-indent: 1em;"><b>preserve_topology  = </b> <code style="text-indent: 0">bool</code>. <span style="color:#48566B;">Default False.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Simplify the geometry while preserving topology.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### snap




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">snap</span><span style="font-style: italic; color: black;font-size: 120%;">(other = <span style="color:#48566B">None</span>, tolerance = <span style="color:#48566B">0</span>, **kwargs):</span></span>


Snap vertices to the nearest vertices of another geometry.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>other  = </b> <code style="text-indent: 0">None||Layer</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Another GMA Layer! If None, snap to the grid.</p><p style="text-indent: 1em;"><b>tolerance  = </b> <code style="text-indent: 0">float</code>. <span style="color:#48566B;">Default 0.0.</span></p><p style="padding-left: 1em;text-indent: 1em;">Tolerance allowed when processing features. If snapped to the grid, this parameter represents the size of the grid. All points and vertices will be aligned to a grid defined by its origin and size.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### sym_difference




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">sym_difference</span><span style="font-style: italic; color: black;font-size: 120%;">(other, o_prefix = <span style="color:#48566B">"L1_"</span>, **kwargs):</span></span>


Symmetrical difference of two layers.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>other: </b> <code style="text-indent: 0">Layer</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Another GMA Layer!</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>o_prefix  = </b> <code style="text-indent: 0">str</code>. <span style="color:#48566B;">Default 'L1_'.</span></p><p style="padding-left: 1em;text-indent: 1em;">Set a prefix for the field names that will be created from the fields of the method layer.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to io.CreateLayer.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### to_bytearray




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">to_bytearray</span><span style="font-style: italic; color: black;font-size: 120%;">(keep_geom = <span style="color:#48566B">False</span>, keep_fields = <span style="color:#48566B">True</span>):</span></span>


Read vector attribute table to a bytearray.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>keep_geom  = </b> <code style="text-indent: 0">bool</code>. <span style="color:#48566B;">Default False.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Whether to export the geometry in WKT format!</p><p style="text-indent: 1em;"><b>keep_fields  = </b> <code style="text-indent: 0">bool||list</code>. <span style="color:#48566B;">Default False.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Whether to retain attribute table fields. If list, it specifies the field names to be retained.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">bytearray</code>.</p>

---

### to_crs




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">to_crs</span><span style="font-style: italic; color: black;font-size: 120%;">(crs = <span style="color:#48566B">"WGS84"</span>, **kwargs):</span></span>


Reproject to another coordinate system.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>crs  = </b> <code style="text-indent: 0">str||int||class</code>. <span style="color:#48566B;">Default 'WGS84'.</span></p><p style="padding-left: 1em;text-indent: 1em;">The output coordinate system. Can be EPSG, WKT, Proj4, and other types of coordinate characters.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### to_dataset




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">to_dataset</span><span style="font-style: italic; color: black;font-size: 120%;">(resolution = <span style="color:#48566B">1</span>, field = <span style="color:#48566B">None</span>, bounds = <span style="color:#48566B">None</span>, nodata = <span style="color:#48566B">None</span>, **kwargs):</span></span>


Translate Layer to DataSet!

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>resolution  = </b> <code style="text-indent: 0">float</code>. <span style="color:#48566B;">Default 1.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Resolution of the DataSet.</p><p style="text-indent: 1em;"><b>field  = </b> <code style="text-indent: 0">str||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The field to be translated. By default (None), the DataSet will be generated with 0 and 1.</p><p style="text-indent: 1em;"><b>bounds  = </b> <code style="text-indent: 0">tuple</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">The four boundaries of the interpolation result are the minimum longitude (left), the minimum latitude (bottom), the maximum longitude (right), and the maximum latitude (top). The default (None) is the bounds of the input Layer.</p><p style="text-indent: 1em;"><b>nodata  = </b> <code style="text-indent: 0">float||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The output DataSet nodata value. By default (None), the nodata value is automatically calculated.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to algos.dataio.utils.CreateRasterEx. </p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">DataSet</code>.</p>

---

### to_dim




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">to_dim</span><span style="font-style: italic; color: black;font-size: 120%;">(dim = <span style="color:#48566B">"XY"</span>, z = <span style="color:#48566B">None</span>, m = <span style="color:#48566B">None</span>, **kwargs):</span></span>


Casting space dimension of Layer.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>dim  = </b> <code style="text-indent: 0">str</code>. <span style="color:#48566B;">Default 'XY'.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Space dimensions. Can be 'XY', 'XYZ', 'XYM' or 'XYZM'.</p><p style="text-indent: 1em;"><b>z  = </b> <code style="text-indent: 0">float||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Z value. Only valid when SDIM is in 'XYZ', 'ZYZM' and layer SDIM is 'XY'.</p><p style="text-indent: 1em;"><b>m  = </b> <code style="text-indent: 0">float||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    M value. Only valid when SDIM is in 'XYM', 'ZYZM' and layer SDIM is 'XY'.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### to_file




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">to_file</span><span style="font-style: italic; color: black;font-size: 120%;">(out_dst, driver = <span style="color:#48566B">"ESRI Shapefile"</span>, layer_name = <span style="color:#48566B">None</span>, mode = <span style="color:#48566B">None</span>, **kwargs):</span></span>


in_src, out_dst = None, driver = None, optional Save Layer as a vector file.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>out_dst: </b> <code style="text-indent: 0">str</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    The output vector file path.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>driver  = </b> <code style="text-indent: 0">str</code>. <span style="color:#48566B;">Default 'ESRI Shapefile'.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Output file driver. For other drivers, see ._algos.geo.driver.DriveStatistics().vectors.</p><p style="text-indent: 1em;"><b>layer_name  = </b> <code style="text-indent: 0">str||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Output layer name. Default(None) is the self name.</p><p style="text-indent: 1em;"><b>mode  = </b> <code style="text-indent: 0">str||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">Access mode. Default(None) is 'creation'. Other supported mode include: 'update', 'append', 'upsert' and 'overwrite'.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p>

---

### to_gtype




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">to_gtype</span><span style="font-style: italic; color: black;font-size: 120%;">(gtype = <span style="color:#48566B">"MultiPolygon"</span>, **kwargs):</span></span>


Change the geometric type of Layer.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>gtype  = </b> <code style="text-indent: 0">str</code>. <span style="color:#48566B;">Default 'MultiPolygon'.</span></p><p style="padding-left: 1em;text-indent: 1em;">Output geometry type. Supported geometry type include: 'Point', 'MultiPoint', 'Line', 'MultiLine', 'Polygon', 'MultiPolygon'.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### to_pandas




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">to_pandas</span><span style="font-style: italic; color: black;font-size: 120%;">(keep_geom = <span style="color:#48566B">False</span>, keep_fields = <span style="color:#48566B">True</span>, **kwargs):</span></span>


Read vector attribute table to a pandas DataFrame.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>keep_geom  = </b> <code style="text-indent: 0">bool</code>. <span style="color:#48566B;">Default False.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Whether to export the geometry in WKT format!</p><p style="text-indent: 1em;"><b>keep_fields  = </b> <code style="text-indent: 0">bool||list</code>. <span style="color:#48566B;">Default False.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Whether to retain attribute table fields. If list, it specifies the field names to be retained.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to pd.read_csv.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">DataFrame</code>.</p>

---

### union




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">union</span><span style="font-style: italic; color: black;font-size: 120%;">(other, o_prefix = <span style="color:#48566B">"L1_"</span>, **kwargs):</span></span>


Union of two layers.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>other: </b> <code style="text-indent: 0">Layer</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Another GMA Layer!</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>o_prefix  = </b> <code style="text-indent: 0">str</code>. <span style="color:#48566B;">Default 'L1_'.</span></p><p style="padding-left: 1em;text-indent: 1em;">Set a prefix for the field names that will be created from the fields of the method layer.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to io.CreateLayer.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### update




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">update</span><span style="font-style: italic; color: black;font-size: 120%;">(other, **kwargs):</span></span>


Update this layer with features from the update layer.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>other: </b> <code style="text-indent: 0">Layer</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Another GMA Layer!</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to io.CreateLayer.    </p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### vertices_to_points




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">vertices_to_points</span><span style="font-style: italic; color: black;font-size: 120%;">(**kwargs):</span></span>


Creates points generated from specified vertices or locations.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate. </p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### voronoj_diagram




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">voronoj_diagram</span><span style="font-style: italic; color: black;font-size: 120%;">(ext_frame_size = <span style="color:#48566B">5</span>, edges_only = <span style="color:#48566B">False</span>, **kwargs):</span></span>


Return a geometric object representing the Voronoj Diagram corresponding to the input Geometry.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>ext_frame_size  = </b> <code style="text-indent: 0">float</code>. <span style="color:#48566B;">Default 5(%).</span></p><p style="padding-left: 1em;text-indent: 1em;">    Allows to arbitrarily set the percent extension of the bounding frame.</p><p style="text-indent: 1em;"><b>edges_only  = </b> <code style="text-indent: 0">bool</code>. <span style="color:#48566B;">Default False.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Whether the output geometry should be filled polygons(False) or just boundary lines(True).</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

### xy_table_to_point




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">xy_table_to_point</span><span style="font-style: italic; color: black;font-size: 120%;">(x_field, y_field, crs = <span style="color:#48566B">"WGS84"</span>, **kwargs):</span></span>


Creates a point Layer based on X, Y-coordinates from a table.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>x_field: </b> <code style="text-indent: 0">str</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    The field in the input table that contains the x-coordinates (or longitude).</p><p style="text-indent: 1em;"><b>y_field: </b> <code style="text-indent: 0">str</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    The field in the input table that contains the y-coordinates (or latitude).</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>crs  = </b> <code style="text-indent: 0">str||int||class||None</code>. <span style="color:#48566B;">Default 'WGS84'.</span></p><p style="padding-left: 1em;text-indent: 1em;">The output coordinate system. Can be EPSG, WKT, Proj4, and other types of coordinate characters.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to _algos.geo.layer.vector_translate.  </p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code style="text-indent: 0">Layer</code>.</p>

---

## Property 



### bounds


<p style="text-indent: 1em;">Layer bounds(left, bottom, right, top). --> <code style="text-indent: 0em;"> tuple</code></p>



---

### crs


<p style="text-indent: 1em;">Layer coordinate reference system. --> <code style="text-indent: 0em;"> CoordinateReferenceSystem</code></p>



---

### driver


<p style="text-indent: 1em;">Layer driver. --> <code style="text-indent: 0em;"> VectorDriver</code></p>



---

### fid_col


<p style="text-indent: 1em;">FID field name. --> <code style="text-indent: 0em;"> str</code></p>



---

### ftypes


<p style="text-indent: 1em;">Field definitions. --> <code style="text-indent: 0em;"> FieldTypes</code></p>



---

### geom_col


<p style="text-indent: 1em;">Geometry field name. --> <code style="text-indent: 0em;"> str</code></p>



---

### gtype


<p style="text-indent: 1em;">Layer geometry type. --> <code style="text-indent: 0em;"> GMADataType</code></p>



---

### link


<p style="text-indent: 1em;">Layer path link. --> <code style="text-indent: 0em;"> str</code></p>



---

### name




---

### spatial_filter




---

### tb




---