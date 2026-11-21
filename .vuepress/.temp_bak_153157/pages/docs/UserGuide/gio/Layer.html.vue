<template><div><p style="font-size: 120%;font-weight: bold;">gma.gio.Layer</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">Layer</span><span style="font-style: italic; color: black;font-size: 130%;">(data = <span style="color:#48566B">None</span>, name = <span style="color:#48566B">None</span>, gtype = <span style="color:#48566B">None</span>, ftypes = <span style="color:#48566B">None</span>, crs = <span style="color:#48566B">None</span>, **kwargs):</span></span>
<p>Initialize a Layer object.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>data </b> = <code style="text-indent: 0em;">Layer||Geometry||Feature||list||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The data source to create the Layer. It can be:</p>
<p style="margin-left: 6em;">1) Another GMA Layer object.</p>
<p style="margin-left: 6em;">2) A Geometry object or a Feature object, or a list of Geometry/Features.</p>
<p style="margin-left: 6em;">3) None, create an empty Layer.</p>
<p style="margin-left: 2em;"><b>name </b> = <code style="text-indent: 0em;">str||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The name of the Layer. If data is a Layer, name can not be set.</p>
<p style="margin-left: 2em;"><b>gtype </b> = <code style="text-indent: 0em;">str||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The geometry type of the Layer. Supported geometry type include:</p>
<p style="margin-left: 6em;">'Point', 'MultiPoint', 'Line', 'MultiLine', 'Polygon', 'MultiPolygon'.</p>
<p style="margin-left: 4em;">If data is a Layer, gtype can not be set.</p>
<p style="margin-left: 2em;"><b>ftypes </b> = <code style="text-indent: 0em;">FieldType||list||dict||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The field types of the Layer. It can be:</p>
<p style="margin-left: 6em;">1) A FieldType object.</p>
<p style="margin-left: 6em;">2) A list of FieldType objects.</p>
<p style="margin-left: 6em;">3) A dict of field name and field type.</p>
<p style="margin-left: 4em;">If data is a Layer, ftypes can not be set.</p>
<p style="margin-left: 2em;"><b>crs </b> = <code style="text-indent: 0em;">str||int||class||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The coordinate system of the Layer. Can be EPSG, WKT, Proj4, and other types of coordinate characters. If data is a Layer, crs can not be set.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geodatabase.GeoDatabase.</p>
<h2 id="method" tabindex="-1"><a class="header-anchor" href="#method"><span>Method</span></a></h2>
<h3 id="add-feature-features" tabindex="-1"><a class="header-anchor" href="#add-feature-features"><span>add_feature<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(*features)</span></span></a></h3>
<p>Add features to Layer.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>*feature</b>: <code style="text-indent: 0em;">Feature</code>. </p>
<p style="margin-left: 4em;">One or more vector features.</p>
<h3 id="add-field-name-none-dtype-unknown" tabindex="-1"><a class="header-anchor" href="#add-field-name-none-dtype-unknown"><span>add_field<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(name = None, dtype = &quot;UNKNOWN&quot;)</span></span></a></h3>
<p>Add a field to Layer.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>name</b>: <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The name of the field. None for dtype name.</p>
<p style="margin-left: 2em;"><b>dtype</b>: <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'UNKNOWN'</span>. </p>
<p style="margin-left: 4em;">The data type of the field. See `dtypes.DefinedFieldDataTypes` for valid types.</p>
<h3 id="boundary-kwargs" tabindex="-1"><a class="header-anchor" href="#boundary-kwargs"><span>boundary<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(**kwargs)</span></span></a></h3>
<p>Creates buffer polygons around input features to a specified distance. **kwargs:</p>
<p style="margin-left: 2em;"><b>Other parameters passed to _algos.geo.layer.vector_translate.</b></p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="buffer-distance-10-side-both-dissolve-false-kwargs" tabindex="-1"><a class="header-anchor" href="#buffer-distance-10-side-both-dissolve-false-kwargs"><span>buffer<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(distance = 10, side = &quot;Both&quot;, dissolve = False, **kwargs)</span></span></a></h3>
<p>Creates buffer polygons around input features to a specified distance.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>distance </b> = <code style="text-indent: 0em;">float</code>. <span style="color:#48566B;"> Default 10</span>. </p>
<p style="margin-left: 4em;">The distance around the input features that will be buffered.</p>
<p style="margin-left: 2em;"><b>side </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'Both'</span>. </p>
<p style="margin-left: 4em;">Specifies the sides of the input features that will be buffered. May be 'Both', 'Left' or 'Right'. 'Both' is only supported for Polygon.</p>
<p style="margin-left: 2em;"><b>dissolve </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Whether to dissolve the buffers into one feature.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="calculate-geometry-area-false-length-false-gtype-false-circularity-false-num-points-false-num-geometries-false-ellipsoid-area-false-ellipsoid-length-false-keep-fields-false-keep-geom-true-kwargs" tabindex="-1"><a class="header-anchor" href="#calculate-geometry-area-false-length-false-gtype-false-circularity-false-num-points-false-num-geometries-false-ellipsoid-area-false-ellipsoid-length-false-keep-fields-false-keep-geom-true-kwargs"><span>calculate_geometry<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(area = False, length = False, gtype = False, circularity = False, num_points = False, num_geometries = False, ellipsoid_area = False, ellipsoid_length = False, keep_fields = False, keep_geom = True, **kwargs)</span></span></a></h3>
<p>Calculate geometry attribute.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>area </b> = <code style="text-indent: 0em;">bool||str</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Whether to calculate the area of the polygon. GeoGCS: deg2; ProjCS:m2.</p>
<p style="margin-left: 4em;">If str, it will be the new name of the output result.</p>
<p style="margin-left: 2em;"><b>length </b> = <code style="text-indent: 0em;">bool||str</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Whether to calculate the length of a line. GeoGCS: deg; ProjCS:m.</p>
<p style="margin-left: 4em;">If str, it will be the new name of the output result.</p>
<p style="margin-left: 2em;"><b>gtype </b> = <code style="text-indent: 0em;">bool||str</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Whether to get the type of the geometry. If str, it will be the new name of the output result.</p>
<p style="margin-left: 2em;"><b>circularity </b> = <code style="text-indent: 0em;">bool||str</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Whether to computes the Circularity Index from the given Geometry.</p>
<p style="margin-left: 4em;">If str, it will be the new name of the output result.</p>
<p style="margin-left: 2em;"><b>num_points </b> = <code style="text-indent: 0em;">bool||str</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Whether to count the number of inflection points. If str, it will be the new name of the output result.</p>
<p style="margin-left: 2em;"><b>NumGeometries </b> = <code style="text-indent: 0em;">bool||str</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Whether to count the number of geometries. If str, it will be the new name of the output result.</p>
<p style="margin-left: 2em;"><b>ellipsoid_area </b> = <code style="text-indent: 0em;">bool||str</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Whether to calculate the area of the polygon using crs's ellipsoid. Unit: m2.</p>
<p style="margin-left: 4em;">If str, it will be the new name of the output result.</p>
<p style="margin-left: 2em;"><b>ellipsoid_length </b> = <code style="text-indent: 0em;">bool||str</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Whether to calculate the length of a line using crs's ellipsoid. Unit: m.</p>
<p style="margin-left: 4em;">If str, it will be the new name of the output result.</p>
<p style="margin-left: 2em;"><b>keep_fields </b> = <code style="text-indent: 0em;">bool||list</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Whether to retain attribute table fields. If list, it specifies the field names to be retained.</p>
<p style="margin-left: 2em;"><b>keep_geom </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default True</span>. </p>
<p style="margin-left: 4em;">Whether to retain geometry field.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="calculate-statistics-statistics-case-none-where-none-kwargs" tabindex="-1"><a class="header-anchor" href="#calculate-statistics-statistics-case-none-where-none-kwargs"><span>calculate_statistics<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(statistics, case = None, where = None, **kwargs)</span></span></a></h3>
<p>Calculates summary statistics for fields in a table.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>statistics</b>: <code style="text-indent: 0em;">dict||list||str</code>. </p>
<p style="margin-left: 4em;">Conduct statistical analysis on selected fields according to the predefined statistical methods.</p>
<p style="margin-left: 4em;">Format 1: Statistics = {Method: [Field0, Field1, ...]}</p>
<p style="margin-left: 6em;">All fields will undergo Method(Field) and will be stored in Field_Method field.</p>
<p style="margin-left: 6em;">Example: Statistics = {'sum': ['field0', 'field1']}</p>
<p style="margin-left: 4em;">Format 2: Statistics = {Method: {Field0: NewName0, Field1: NewName1, ...}}</p>
<p style="margin-left: 6em;">All fields will undergo Method(Field) and will be stored in NewName field.</p>
<p style="margin-left: 6em;">Example: Statistics = {'sum': {'field0': 'NewName0sum', 'field1': 'NewName1sum'}}</p>
<p style="margin-left: 4em;">Format 3: Statistics = 'Field0 + Field1 AS sum_result'</p>
<p style="margin-left: 6em;">Calculate the sum of Field0 and Field1 as "sum_result".</p>
<p style="margin-left: 4em;">If it is a list, it must be a list of str in the format 3.</p>
<p style="margin-left: 4em;">Including statistics types: 'min', 'max', 'sum', 'avg', 'count', 'total', ...</p>
<p style="margin-left: 4em;">For more, see SQLite grammar.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>case </b> = <code style="text-indent: 0em;">str||list||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The field or fields in the input that will be used to calculate statistics separately for each unique attribute value (or combination of attribute values when multiple fields are specified).</p>
<p style="margin-left: 2em;"><b>where </b> = <code style="text-indent: 0em;">str||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The SQL query string expressions to evaluate. For example:</p>
<p style="margin-left: 6em;">Where = 'ROWID = 1 OR Name IN ("GMA", "Layer")' 'ROWID' and 'Name' are the Layer field names.</p>
<p style="margin-left: 4em;">Supported Rules:</p>
<p style="margin-left: 4em;">Comparison Operators: =, !=, <>, <, >, <=, >= Logical Operators: AND, OR, NOT Wildcard Search Symbols: LIKE Range Condition: BETWEEN, IN, NOT IN Null-Value Check Operators: IS NULL, IS NOT NULL Regular expression matching: REGEXP</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="centroid-kwargs" tabindex="-1"><a class="header-anchor" href="#centroid-kwargs"><span>centroid<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(**kwargs)</span></span></a></h3>
<p>The points representing the centroid of each geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="clip-other-kwargs" tabindex="-1"><a class="header-anchor" href="#clip-other-kwargs"><span>clip<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other, **kwargs)</span></span></a></h3>
<p>Clip off areas that are not covered by the method layer.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 4em;">other: Layer.</p>
<p style="margin-left: 4em;">Another GMA Layer!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to io.CreateLayer.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="closest-point-other-kwargs" tabindex="-1"><a class="header-anchor" href="#closest-point-other-kwargs"><span>closest_point<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other, **kwargs)</span></span></a></h3>
<p>Calculate the closest point on the tow layer.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<p style="margin-left: 4em;">Another GMA Layer!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="collect-use-field-none-keep-fields-true-kwargs" tabindex="-1"><a class="header-anchor" href="#collect-use-field-none-keep-fields-true-kwargs"><span>collect<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(use_field = None, keep_fields = True, **kwargs)</span></span></a></h3>
<p>Collect features based on field values.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>use_field </b> = <code style="text-indent: 0em;">str||list||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The field name(s) used to merge Features! If it's None, then dissolve all features.</p>
<p style="margin-left: 2em;"><b>keep_fields </b> = <code style="text-indent: 0em;">bool||list</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Whether to retain attribute table fields. If list, it specifies the field names to be retained.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="concave-hull-kwargs" tabindex="-1"><a class="header-anchor" href="#concave-hull-kwargs"><span>concave_hull<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(**kwargs)</span></span></a></h3>
<p>The concave hull of a geometry is the smallest concave Polygon containing all the points in each geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="convex-hull-kwargs" tabindex="-1"><a class="header-anchor" href="#convex-hull-kwargs"><span>convex_hull<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(**kwargs)</span></span></a></h3>
<p>The convex hull of a geometry is the smallest convex Polygon containing all the points in each geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="copy-kwargs" tabindex="-1"><a class="header-anchor" href="#copy-kwargs"><span>copy<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(**kwargs)</span></span></a></h3>
<p>Copy replica to default driver.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="delaunay-triangulation-edges-only-false-tolerance-0-kwargs" tabindex="-1"><a class="header-anchor" href="#delaunay-triangulation-edges-only-false-tolerance-0-kwargs"><span>delaunay_triangulation<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(edges_only = False, tolerance = 0, **kwargs)</span></span></a></h3>
<p>Return a Delaunay triangulation of the vertices of the geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>tolerance </b> = <code style="text-indent: 0em;">float</code>. <span style="color:#48566B;"> Default 0.0</span>. </p>
<p style="margin-left: 4em;">Snapping tolerance to use for improved robustness.</p>
<p style="margin-left: 2em;"><b>edges_only </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Whether the output geometry should be filled polygons(False) or just boundary lines(True).</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="dissolve-use-field-none-keep-fields-true-kwargs" tabindex="-1"><a class="header-anchor" href="#dissolve-use-field-none-keep-fields-true-kwargs"><span>dissolve<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(use_field = None, keep_fields = True, **kwargs)</span></span></a></h3>
<p>Dissolve features based on field values.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>use_field </b> = <code style="text-indent: 0em;">str||list||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The field name(s) used to dissolve Features! If it's None, then dissolve all features.</p>
<p style="margin-left: 2em;"><b>keep_fields </b> = <code style="text-indent: 0em;">bool||list</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Whether to retain attribute table fields. If list, it specifies the field names to be retained.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="distance-other-method-none-densify-fract-0-1-kwargs" tabindex="-1"><a class="header-anchor" href="#distance-other-method-none-densify-fract-0-1-kwargs"><span>distance<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other, method = None, densify_fract = 0.1, **kwargs)</span></span></a></h3>
<p>Calculates the distance between all geometric shapes within two Layers.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<p style="margin-left: 4em;">Another GMA Layer!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>method </b> = <code style="text-indent: 0em;">str||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Calculate method. May be None(normal distance), 'Hausdorff' or 'Frechet'.</p>
<p style="margin-left: 2em;"><b>densify_fract </b> = <code style="text-indent: 0em;">float</code>. <span style="color:#48566B;"> Default 0.1</span>. </p>
<p style="margin-left: 4em;">A value between 0 and 1, that splits each subsegment of a line string into equal length segments, making the approximation less coarse.</p>
<p style="margin-left: 4em;">A densify value of 0.5 will add a point halfway between each pair of points. A densify value of 0.25 will add a point every quarter of the way between each pair of points.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="drop-rows-none-fields-none" tabindex="-1"><a class="header-anchor" href="#drop-rows-none-fields-none"><span>drop<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(rows = None, fields = None)</span></span></a></h3>
<p>Drop specified features or fields.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>rows </b> = <code style="text-indent: 0em;">int||list||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">List of FIDs to be deleted.</p>
<p style="margin-left: 2em;"><b>fields </b> = <code style="text-indent: 0em;">str||list||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">List of field names to be deleted.</p>
<h3 id="envelope-union-false-kwargs" tabindex="-1"><a class="header-anchor" href="#envelope-union-false-kwargs"><span>envelope<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(union = False, **kwargs)</span></span></a></h3>
<p>The envelope of a geometry is the bounding rectangle.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>union </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default True</span>. </p>
<p style="margin-left: 4em;">Whether to first integrate all elements before calculating.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="erase-other-kwargs" tabindex="-1"><a class="header-anchor" href="#erase-other-kwargs"><span>erase<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other, **kwargs)</span></span></a></h3>
<p>Remove areas that are covered by the method layer.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<p style="margin-left: 4em;">Another GMA Layer!</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to io.CreateLayer.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="explode-kwargs" tabindex="-1"><a class="header-anchor" href="#explode-kwargs"><span>explode<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(**kwargs)</span></span></a></h3>
<p>Separate a selected multipart feature into its individual.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="extent-kwargs" tabindex="-1"><a class="header-anchor" href="#extent-kwargs"><span>extent<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(**kwargs)</span></span></a></h3>
<p>The extent of a geometry is the bounding rectangle.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="exterior-ring-kwargs" tabindex="-1"><a class="header-anchor" href="#exterior-ring-kwargs"><span>exterior_ring<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(**kwargs)</span></span></a></h3>
<p>Returns a of LinearRings representing the outer bounds of each polygon.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="find-overlaps-kwargs" tabindex="-1"><a class="header-anchor" href="#find-overlaps-kwargs"><span>find_overlaps<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(**kwargs)</span></span></a></h3>
<p>Find overlapping features in Layer.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<h3 id="fix-geometry-kwargs" tabindex="-1"><a class="header-anchor" href="#fix-geometry-kwargs"><span>fix_geometry<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(**kwargs)</span></span></a></h3>
<p>Fix invalid geometric features in Layer.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="gen-grid-grid-type-square-size-1-kwargs" tabindex="-1"><a class="header-anchor" href="#gen-grid-grid-type-square-size-1-kwargs"><span>gen_grid<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(grid_type = &quot;Square&quot;, size = 1, **kwargs)</span></span></a></h3>
<p>Gen a grid of cells (having the edge length of size) precisely covering the input Layer.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>grid_type </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'Square'</span>. </p>
<p style="margin-left: 4em;">Grid type.Can be 'Square', 'Triangular', 'Hexagonal'.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="geom-self-test" tabindex="-1"><a class="header-anchor" href="#geom-self-test"><span>geom_self_test<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span></span></a></h3>
<p>Geometry self-test. Include: Empty, Simple, Valid, 3D, Measured, Valid Reason, Polygon Clockwise Rule(Counter-Clockwise Rule).</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<p style="margin-left: 4em;">In this context, 0 indicates False, 1 indicates True, -1 indicates that the input geometry object is not of the required type.</p>
<h3 id="geom-to-str-wkt-true-gml-false-kml-false-json-false-ewkb-false-ewkt-false-svg-false-kwargs" tabindex="-1"><a class="header-anchor" href="#geom-to-str-wkt-true-gml-false-kml-false-json-false-ewkb-false-ewkt-false-svg-false-kwargs"><span>geom_to_str<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(wkt = True, gml = False, kml = False, json = False, ewkb = False, ewkt = False, svg = False, **kwargs)</span></span></a></h3>
<p>Converts geometry to string.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>wkt </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default True</span>. </p>
<p style="margin-left: 4em;">Whether to convert to WTK string.</p>
<p style="margin-left: 2em;"><b>gml </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Whether to convert to Gml string.</p>
<p style="margin-left: 2em;"><b>kml </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Whether to convert to Kml string.</p>
<p style="margin-left: 2em;"><b>json </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Whether to convert to GeoJSON string.</p>
<p style="margin-left: 2em;"><b>ewkb </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Whether to convert to EWKB string.</p>
<p style="margin-left: 2em;"><b>ewkt </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Whether to convert to EWKT string.</p>
<p style="margin-left: 2em;"><b>svg </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Whether to convert to SVG string.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="get-feature-row-num-0" tabindex="-1"><a class="header-anchor" href="#get-feature-row-num-0"><span>get_feature<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(row_num = 0)</span></span></a></h3>
<p>Fetch a feature by its identifier.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>row_num </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 0</span>. </p>
<p style="margin-left: 4em;">The feature number of the feature to read.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Feature</b>: </p>
<p style="margin-left: 4em;">A new feature now owned by the caller</p>
<h3 id="identity-other-o-prefix-l1-kwargs" tabindex="-1"><a class="header-anchor" href="#identity-other-o-prefix-l1-kwargs"><span>identity<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other, o_prefix = &quot;L1_&quot;, **kwargs)</span></span></a></h3>
<p>Identify the features of this layer with the ones from the identity layer.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<p style="margin-left: 4em;">Another GMA Layer!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>o_prefix </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'L1_'</span>. </p>
<p style="margin-left: 4em;">Set a prefix for the field names that will be created from the fields of the method layer.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to io.CreateLayer.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="interior-ring-n-1-kwargs" tabindex="-1"><a class="header-anchor" href="#interior-ring-n-1-kwargs"><span>interior_ring<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(n = 1, **kwargs)</span></span></a></h3>
<p>Returns a of LinearRings representing the inner bounds of each polygon.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>n </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 1</span>. </p>
<p style="margin-left: 4em;">Extracted inner ring index (starting from 1).</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="interpolation-v-field-bounds-none-resolution-none-method-idw-ipt-opts-kwargs" tabindex="-1"><a class="header-anchor" href="#interpolation-v-field-bounds-none-resolution-none-method-idw-ipt-opts-kwargs"><span>interpolation<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(v_field, bounds = None, resolution = None, method = &quot;idw&quot;, ipt_opts = {}, **kwargs)</span></span></a></h3>
<p>Interpolate points into raster dataset.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>v_field</b>: <code style="text-indent: 0em;">str</code>. </p>
<p style="margin-left: 4em;">The field to be interpolated.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>bounds </b> = <code style="text-indent: 0em;">tuple</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The four boundaries of the interpolation result are the minimum longitude (left), the minimum latitude (bottom), the maximum longitude (right), and the maximum latitude (top). The default (None) is to extract the range from the input coordinate points.</p>
<p style="margin-left: 2em;"><b>resolution </b> = <code style="text-indent: 0em;">float</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The resolution of the interpolation result. The default (None) is 1/10 of the minimum bounds X and Y difference.</p>
<p style="margin-left: 2em;"><b>method </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'idw'</span>. </p>
<p style="margin-left: 4em;">Interpolation method. Can be 'b_spline', 'idw', 'kriging', 'natural_neighbor', 'nearest', 'rbf' and 'trend'. For more, see smc.interp.</p>
<p style="margin-left: 2em;"><b>ipt_opts </b> = <code style="text-indent: 0em;">dict</code>. <span style="color:#48566B;"> Default {}</span>. </p>
<p style="margin-left: 4em;">Interpolation parameters. Corresponding to the interpolation method.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.dataset.raster_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Dataset||dict</code>. </p>
<p style="margin-left: 4em;">Contains the raster dataset and other interpolation results. The keys are the names of the results, and the values are the corresponding raster datasets or other results.</p>
<h3 id="intersection-other-o-prefix-l1-kwargs" tabindex="-1"><a class="header-anchor" href="#intersection-other-o-prefix-l1-kwargs"><span>intersection<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other, o_prefix = &quot;L1_&quot;, **kwargs)</span></span></a></h3>
<p>Intersection of two layers.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<p style="margin-left: 4em;">Another GMA Layer!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>o_prefix </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'L1_'</span>. </p>
<p style="margin-left: 4em;">Set a prefix for the field names that will be created from the fields of the method layer.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to io.CreateLayer.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="join-other-spatial-join-none-left-on-none-right-on-none-one-to-one-true-suffixes-ext-cond-none-kwargs" tabindex="-1"><a class="header-anchor" href="#join-other-spatial-join-none-left-on-none-right-on-none-one-to-one-true-suffixes-ext-cond-none-kwargs"><span>join<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other, spatial_join = None, left_on = None, right_on = None, one_to_one = True, suffixes = &quot;&quot;, ext_cond = None, **kwargs)</span></span></a></h3>
<p>Join the attribute table of RLayer into the first Layer.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<p style="margin-left: 4em;">Another GMA Layer!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>spatial_join </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Spatial join method. Supported 'Intersects', 'Disjoint', 'Within', 'Equals', 'Touches'.</p>
<p style="margin-left: 4em;">Default(None) no spatial join.</p>
<p style="margin-left: 2em;"><b>left_on </b> = <code style="text-indent: 0em;">str||list||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Feild names to join on in the self Layer. Can also be a list of the length of the self Layer. Default(None) using self FID column if spatial_join is None.</p>
<p style="margin-left: 2em;"><b>right_on </b> = <code style="text-indent: 0em;">str||list||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Feild names to join on in the other Layer. Can also be a list of the length of the other Layer. Default(None) using other FID column if spatial_join is None.</p>
<p style="margin-left: 2em;"><b>one_to_one </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Whether to keep only one feature in the second layer for each feature in the first layer.</p>
<p style="margin-left: 2em;"><b>suffixes </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default ''</span>. </p>
<p style="margin-left: 4em;">Extended character used to mark the second layer column.</p>
<p style="margin-left: 2em;"><b>ext_cond </b> = <code style="text-indent: 0em;">str||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Additional SQL conditions for joining the two layers. For example:</p>
<p style="margin-left: 6em;">ext_cond = 'a0.field0 > 10 AND a1.field1 < 20'.</p>
<p style="margin-left: 6em;">a0 and a1 are the aliases of the self and other layers, respectively.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="line-equidistant-points-length-keep-fields-true-kwargs" tabindex="-1"><a class="header-anchor" href="#line-equidistant-points-length-keep-fields-true-kwargs"><span>line_equidistant_points<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(length, keep_fields = True, **kwargs)</span></span></a></h3>
<p>Generate equidistant points along the line geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>length</b>: <code style="text-indent: 0em;">float</code>. </p>
<p style="margin-left: 4em;">Distance between points.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>keep_fields </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default True</span>. </p>
<p style="margin-left: 4em;">Whether to retain attribute table fields.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="merge-others-kwargs" tabindex="-1"><a class="header-anchor" href="#merge-others-kwargs"><span>merge<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(*others, **kwargs)</span></span></a></h3>
<p>Merge all layers.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>*others</b>: <code style="text-indent: 0em;">Layer||list of Layer</code>. </p>
<p style="margin-left: 4em;">Other GMA Layers!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="min-bounding-circle-kwargs" tabindex="-1"><a class="header-anchor" href="#min-bounding-circle-kwargs"><span>min_bounding_circle<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(**kwargs)</span></span></a></h3>
<p>Constructs the Minimum Bounding Circle for a generic geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="min-rotated-rectangle-kwargs" tabindex="-1"><a class="header-anchor" href="#min-rotated-rectangle-kwargs"><span>min_rotated_rectangle<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(**kwargs)</span></span></a></h3>
<p>Calculate the minimum rotated rectangular polygon which encloses the input geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="min-width-kwargs" tabindex="-1"><a class="header-anchor" href="#min-width-kwargs"><span>min_width<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(**kwargs)</span></span></a></h3>
<p>Calculate the LINESTRING geometry which represents the minimum diameter of the geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="multi-kwargs" tabindex="-1"><a class="header-anchor" href="#multi-kwargs"><span>multi<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(**kwargs)</span></span></a></h3>
<p>Make single part geometry into their multi counterpart.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="order-by-fields-ascending-true-kwargs" tabindex="-1"><a class="header-anchor" href="#order-by-fields-ascending-true-kwargs"><span>order_by<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(fields, ascending = True, **kwargs)</span></span></a></h3>
<p>Sort by field.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>fields</b>: <code style="text-indent: 0em;">str||list</code>. </p>
<p style="margin-left: 4em;">Fields or list of fields to be sorted.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>ascending </b> = <code style="text-indent: 0em;">bool||list</code>. <span style="color:#48566B;"> Default True</span>. </p>
<p style="margin-left: 4em;">Sort order, which can be True(ascending) or False(descending).</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="plot-ax-none-kwargs" tabindex="-1"><a class="header-anchor" href="#plot-ax-none-kwargs"><span>plot<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(ax = None, **kwargs)</span></span></a></h3>
<p>Make plots of Layer.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>ax </b> = <code style="text-indent: 0em;">None||matplotlib</code>. <span style="color:#48566B;">~.AxesSubplot. Default None</span>. </p>
<p style="margin-left: 4em;">A matplotlib subplot. If None, a default axes will be created.</p>
<p style="margin-left: 2em;"><b>**kwargs</b></p>
<p style="margin-left: 4em;">Other plotting parameters. For more, see:</p>
<p style="margin-left: 6em;">~.carto.utils.PolyCollection/LineCollection/PointCollection.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>matplotlib.~.AxesSubplot</b></p>
<h3 id="point-on-surface-kwargs" tabindex="-1"><a class="header-anchor" href="#point-on-surface-kwargs"><span>point_on_surface<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(**kwargs)</span></span></a></h3>
<p>Computes a point guaranteed to lie in a polygon, or on a geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="query-expr-tran-opts-kwargs" tabindex="-1"><a class="header-anchor" href="#query-expr-tran-opts-kwargs"><span>query<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(expr, tran_opts = {}, **kwargs)</span></span></a></h3>
<p>Query the data with a full SpatiaLite SQL expression.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>expr</b>: <code style="text-indent: 0em;">str</code>. </p>
<p style="margin-left: 4em;">The query string to evaluate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>tran_opts </b> = <code style="text-indent: 0em;">dict</code>. <span style="color:#48566B;"> Default {}</span>. </p>
<p style="margin-left: 4em;">Vector translate options. For more, see _algos.geo.layer.vector_translate.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to ._algos.geo.vrt.VRTGeoDatabase.add_layer.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="rotate-angle-90-kwargs" tabindex="-1"><a class="header-anchor" href="#rotate-angle-90-kwargs"><span>rotate<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(angle = 90, **kwargs)</span></span></a></h3>
<p>Rotate an angle of the layer.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>Angle </b> = <code style="text-indent: 0em;">float</code>. <span style="color:#48566B;"> Default 90</span>. </p>
<p style="margin-left: 4em;">Rotation angle (In Degrees) with the point [0, 0] as the origin.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="sanitize-kwargs" tabindex="-1"><a class="header-anchor" href="#sanitize-kwargs"><span>sanitize<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(**kwargs)</span></span></a></h3>
<p>Sanitize geometry. Including removing duplicate points and ensuring closed rings.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="scale-factor-1-kwargs" tabindex="-1"><a class="header-anchor" href="#scale-factor-1-kwargs"><span>scale<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(factor = 1, **kwargs)</span></span></a></h3>
<p>Select the intersecting features.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>factor </b> = <code style="text-indent: 0em;">float||list</code>. <span style="color:#48566B;"> Default 1</span>. </p>
<p style="margin-left: 4em;">X, Y scale factors. If a single value is provided, it is assumed that X = Y.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="select-where-keep-fields-true-keep-geom-true-kwargs" tabindex="-1"><a class="header-anchor" href="#select-where-keep-fields-true-keep-geom-true-kwargs"><span>select<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(where = &quot;&quot;, keep_fields = True, keep_geom = True, **kwargs)</span></span></a></h3>
<p>Using SQL WHERE expressions to filter features by attribute table fields.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>where </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default ''</span>. </p>
<p style="margin-left: 4em;">The SQL query string expressions to evaluate. For example:</p>
<p style="margin-left: 6em;">Where = 'ROWID = 1 OR Name IN ("GMA", "Layer")' 'ROWID' and 'Name' are the Layer field names.</p>
<p style="margin-left: 4em;">Supported Rules:</p>
<p style="margin-left: 4em;">Comparison Operators: =, !=, <>, <, >, <=, >= Logical Operators: AND, OR, NOT Wildcard Search Symbols: LIKE Range Condition: BETWEEN, IN, NOT IN Null-Value Check Operators: IS NULL, IS NOT NULL Regular expression matching: REGEXP</p>
<p style="margin-left: 2em;"><b>keep_fields </b> = <code style="text-indent: 0em;">bool||list</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Whether to retain attribute table fields. If list, it specifies the field names to be retained.</p>
<p style="margin-left: 2em;"><b>keep_geom </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default True</span>. </p>
<p style="margin-left: 4em;">Whether to retain geometry field.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="select-overlay-other-method-intersects-kwargs" tabindex="-1"><a class="header-anchor" href="#select-overlay-other-method-intersects-kwargs"><span>select_overlay<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other, method = &quot;Intersects&quot;, **kwargs)</span></span></a></h3>
<p>Select features that conform to the overlay rule.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<p style="margin-left: 4em;">Another GMA Layer!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>method </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'Intersects'</span>. </p>
<p style="margin-left: 4em;">Overlay method. Supported methods include: 'Intersects', 'Disjoint', 'Within', 'Equals', 'Touches'.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="set-feature-feature-fid-none" tabindex="-1"><a class="header-anchor" href="#set-feature-feature-fid-none"><span>set_feature<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(feature, fid = None)</span></span></a></h3>
<p>Rewrite an existing feature. To set a feature, but create it if it doesn't exist.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>feature</b>: <code style="text-indent: 0em;">Feature</code>. </p>
<p style="margin-left: 4em;">A vector feature.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>fid </b> = <code style="text-indent: 0em;">int||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The FID added to the layer. Defaults to the feature's FID.</p>
<h3 id="set-spatial-filter-geom-none" tabindex="-1"><a class="header-anchor" href="#set-spatial-filter-geom-none"><span>set_spatial_filter<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(geom = None)</span></span></a></h3>
<h3 id="shared-paths-other-kwargs" tabindex="-1"><a class="header-anchor" href="#shared-paths-other-kwargs"><span>shared_paths<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other, **kwargs)</span></span></a></h3>
<p>Calculate the shared paths between two layers.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<p style="margin-left: 4em;">Another GMA Layer!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="shift-distance-1-kwargs" tabindex="-1"><a class="header-anchor" href="#shift-distance-1-kwargs"><span>shift<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(distance = 1, **kwargs)</span></span></a></h3>
<p>Shilf a distance of the layer.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>distance </b> = <code style="text-indent: 0em;">float||list</code>. <span style="color:#48566B;"> Default 1</span>. </p>
<p style="margin-left: 4em;">X, Y shift distance. If a single value is provided, it is assumed that X = Y.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="shortest-line-other-kwargs" tabindex="-1"><a class="header-anchor" href="#shortest-line-other-kwargs"><span>shortest_line<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other, **kwargs)</span></span></a></h3>
<p>Calculate the shortest line between the geometries of tow layers.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<p style="margin-left: 4em;">Another GMA Layer!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="simplify-tolerance-0-preserve-topology-false-kwargs" tabindex="-1"><a class="header-anchor" href="#simplify-tolerance-0-preserve-topology-false-kwargs"><span>simplify<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(tolerance = 0, preserve_topology = False, **kwargs)</span></span></a></h3>
<p>Simplify geometries in the Layer.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>tolerance </b> = <code style="text-indent: 0em;">float</code>. <span style="color:#48566B;"> Default 0.0</span>. </p>
<p style="margin-left: 4em;">Tolerance allowed when simplifying geometric features.</p>
<p style="margin-left: 2em;"><b>preserve_topology </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Simplify the geometry while preserving topology.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="snap-other-none-tolerance-0-kwargs" tabindex="-1"><a class="header-anchor" href="#snap-other-none-tolerance-0-kwargs"><span>snap<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other = None, tolerance = 0, **kwargs)</span></span></a></h3>
<p>Snap vertices to the nearest vertices of another geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>other </b> = <code style="text-indent: 0em;">None||Layer</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Another GMA Layer! If None, snap to the grid.</p>
<p style="margin-left: 2em;"><b>tolerance </b> = <code style="text-indent: 0em;">float</code>. <span style="color:#48566B;"> Default 0.0</span>. </p>
<p style="margin-left: 4em;">Tolerance allowed when processing features. If snapped to the grid, this parameter represents the size of the grid. All points and vertices will be aligned to a grid defined by its origin and size.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="sym-difference-other-o-prefix-l1-kwargs" tabindex="-1"><a class="header-anchor" href="#sym-difference-other-o-prefix-l1-kwargs"><span>sym_difference<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other, o_prefix = &quot;L1_&quot;, **kwargs)</span></span></a></h3>
<p>Symmetrical difference of two layers.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<p style="margin-left: 4em;">Another GMA Layer!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>o_prefix </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'L1_'</span>. </p>
<p style="margin-left: 4em;">Set a prefix for the field names that will be created from the fields of the method layer.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to io.CreateLayer.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="to-bytearray-keep-geom-false-keep-fields-true" tabindex="-1"><a class="header-anchor" href="#to-bytearray-keep-geom-false-keep-fields-true"><span>to_bytearray<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(keep_geom = False, keep_fields = True)</span></span></a></h3>
<p>Read vector attribute table to a bytearray.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>keep_geom </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Whether to export the geometry in WKT format!</p>
<p style="margin-left: 2em;"><b>keep_fields </b> = <code style="text-indent: 0em;">bool||list</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Whether to retain attribute table fields. If list, it specifies the field names to be retained.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">bytearray</code>. </p>
<h3 id="to-crs-crs-wgs84-kwargs" tabindex="-1"><a class="header-anchor" href="#to-crs-crs-wgs84-kwargs"><span>to_crs<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(crs = &quot;WGS84&quot;, **kwargs)</span></span></a></h3>
<p>Reproject to another coordinate system.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>crs </b> = <code style="text-indent: 0em;">str||int||class</code>. <span style="color:#48566B;"> Default 'WGS84'</span>. </p>
<p style="margin-left: 4em;">The output coordinate system. Can be EPSG, WKT, Proj4, and other types of coordinate characters.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="to-dataset-resolution-1-field-none-bounds-none-nodata-none-kwargs" tabindex="-1"><a class="header-anchor" href="#to-dataset-resolution-1-field-none-bounds-none-nodata-none-kwargs"><span>to_dataset<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(resolution = 1, field = None, bounds = None, nodata = None, **kwargs)</span></span></a></h3>
<p>Translate Layer to DataSet!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>resolution </b> = <code style="text-indent: 0em;">float</code>. <span style="color:#48566B;"> Default 1</span>. </p>
<p style="margin-left: 4em;">Resolution of the DataSet.</p>
<p style="margin-left: 2em;"><b>field </b> = <code style="text-indent: 0em;">str||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The field to be translated. By default (None), the DataSet will be generated with 0 and 1.</p>
<p style="margin-left: 2em;"><b>bounds </b> = <code style="text-indent: 0em;">tuple</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The four boundaries of the interpolation result are the minimum longitude (left), the minimum latitude (bottom), the maximum longitude (right), and the maximum latitude (top). The default (None) is the bounds of the input Layer.</p>
<p style="margin-left: 2em;"><b>nodata </b> = <code style="text-indent: 0em;">float||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The output DataSet nodata value. By default (None), the nodata value is automatically calculated.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to algos.dataio.utils.CreateRasterEx.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">DataSet</code>. </p>
<h3 id="to-dim-dim-xy-z-none-m-none-kwargs" tabindex="-1"><a class="header-anchor" href="#to-dim-dim-xy-z-none-m-none-kwargs"><span>to_dim<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(dim = &quot;XY&quot;, z = None, m = None, **kwargs)</span></span></a></h3>
<p>Casting space dimension of Layer.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>dim </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'XY'</span>. </p>
<p style="margin-left: 4em;">Space dimensions. Can be 'XY', 'XYZ', 'XYM' or 'XYZM'.</p>
<p style="margin-left: 2em;"><b>z </b> = <code style="text-indent: 0em;">float||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Z value. Only valid when SDIM is in 'XYZ', 'ZYZM' and layer SDIM is 'XY'.</p>
<p style="margin-left: 2em;"><b>m </b> = <code style="text-indent: 0em;">float||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">M value. Only valid when SDIM is in 'XYM', 'ZYZM' and layer SDIM is 'XY'.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="to-file-out-dst-driver-esri-shapefile-layer-name-none-mode-none-kwargs" tabindex="-1"><a class="header-anchor" href="#to-file-out-dst-driver-esri-shapefile-layer-name-none-mode-none-kwargs"><span>to_file<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(out_dst, driver = &quot;ESRI Shapefile&quot;, layer_name = None, mode = None, **kwargs)</span></span></a></h3>
<p>in_src, out_dst = None, driver = None, optional Save Layer as a vector file.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>out_dst</b>: <code style="text-indent: 0em;">str</code>. </p>
<p style="margin-left: 4em;">The output vector file path.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>driver </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'ESRI Shapefile'</span>. </p>
<p style="margin-left: 4em;">Output file driver. For other drivers, see ._algos.geo.driver.DriveStatistics().vectors.</p>
<p style="margin-left: 2em;"><b>layer_name </b> = <code style="text-indent: 0em;">str||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Output layer name. Default(None) is the self name.</p>
<p style="margin-left: 2em;"><b>mode </b> = <code style="text-indent: 0em;">str||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Access mode. Default(None) is 'creation'. Other supported mode include:</p>
<p style="margin-left: 4em;">'update', 'append', 'upsert' and 'overwrite'.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<h3 id="to-gtype-gtype-multipolygon-kwargs" tabindex="-1"><a class="header-anchor" href="#to-gtype-gtype-multipolygon-kwargs"><span>to_gtype<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(gtype = &quot;MultiPolygon&quot;, **kwargs)</span></span></a></h3>
<p>Change the geometric type of Layer.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>gtype </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'MultiPolygon'</span>. </p>
<p style="margin-left: 4em;">Output geometry type. Supported geometry type include:</p>
<p style="margin-left: 6em;">'Point', 'MultiPoint', 'Line', 'MultiLine', 'Polygon', 'MultiPolygon'.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="to-pandas-keep-geom-false-keep-fields-true-kwargs" tabindex="-1"><a class="header-anchor" href="#to-pandas-keep-geom-false-keep-fields-true-kwargs"><span>to_pandas<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(keep_geom = False, keep_fields = True, **kwargs)</span></span></a></h3>
<p>Read vector attribute table to a pandas DataFrame.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>keep_geom </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Whether to export the geometry in WKT format!</p>
<p style="margin-left: 2em;"><b>keep_fields </b> = <code style="text-indent: 0em;">bool||list</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Whether to retain attribute table fields. If list, it specifies the field names to be retained.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to pd.read_csv.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">DataFrame</code>. </p>
<h3 id="union-other-o-prefix-l1-kwargs" tabindex="-1"><a class="header-anchor" href="#union-other-o-prefix-l1-kwargs"><span>union<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other, o_prefix = &quot;L1_&quot;, **kwargs)</span></span></a></h3>
<p>Union of two layers.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<p style="margin-left: 4em;">Another GMA Layer!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>o_prefix </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'L1_'</span>. </p>
<p style="margin-left: 4em;">Set a prefix for the field names that will be created from the fields of the method layer.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to io.CreateLayer.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="update-other-kwargs" tabindex="-1"><a class="header-anchor" href="#update-other-kwargs"><span>update<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other, **kwargs)</span></span></a></h3>
<p>Update this layer with features from the update layer.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<p style="margin-left: 4em;">Another GMA Layer!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to io.CreateLayer.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="vertices-to-points-kwargs" tabindex="-1"><a class="header-anchor" href="#vertices-to-points-kwargs"><span>vertices_to_points<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(**kwargs)</span></span></a></h3>
<p>Creates points generated from specified vertices or locations.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="voronoj-diagram-ext-frame-size-5-edges-only-false-kwargs" tabindex="-1"><a class="header-anchor" href="#voronoj-diagram-ext-frame-size-5-edges-only-false-kwargs"><span>voronoj_diagram<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(ext_frame_size = 5, edges_only = False, **kwargs)</span></span></a></h3>
<p>Return a geometric object representing the Voronoj Diagram corresponding to the input Geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>ext_frame_size </b> = <code style="text-indent: 0em;">float</code>. <span style="color:#48566B;"> Default 5(%)</span>. </p>
<p style="margin-left: 4em;">Allows to arbitrarily set the percent extension of the bounding frame.</p>
<p style="margin-left: 2em;"><b>edges_only </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Whether the output geometry should be filled polygons(False) or just boundary lines(True).</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h3 id="xy-table-to-point-x-field-y-field-crs-wgs84-kwargs" tabindex="-1"><a class="header-anchor" href="#xy-table-to-point-x-field-y-field-crs-wgs84-kwargs"><span>xy_table_to_point<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(x_field, y_field, crs = &quot;WGS84&quot;, **kwargs)</span></span></a></h3>
<p>Creates a point Layer based on X, Y-coordinates from a table.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>x_field</b>: <code style="text-indent: 0em;">str</code>. </p>
<p style="margin-left: 4em;">The field in the input table that contains the x-coordinates (or longitude).</p>
<p style="margin-left: 2em;"><b>y_field</b>: <code style="text-indent: 0em;">str</code>. </p>
<p style="margin-left: 4em;">The field in the input table that contains the y-coordinates (or latitude).</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>crs </b> = <code style="text-indent: 0em;">str||int||class||None</code>. <span style="color:#48566B;"> Default 'WGS84'</span>. </p>
<p style="margin-left: 4em;">The output coordinate system. Can be EPSG, WKT, Proj4, and other types of coordinate characters.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<h2 id="property" tabindex="-1"><a class="header-anchor" href="#property"><span>Property</span></a></h2>
<h3 id="bounds" tabindex="-1"><a class="header-anchor" href="#bounds"><span>bounds</span></a></h3>
<p style="margin-left: 2em;">Layer bounds(left, bottom, right, top). --> <code style="text-indent: 0em;">tuple</code></p>
<h3 id="crs" tabindex="-1"><a class="header-anchor" href="#crs"><span>crs</span></a></h3>
<p style="margin-left: 2em;">Layer coordinate reference system. --> <code style="text-indent: 0em;">CoordinateReferenceSystem</code></p>
<h3 id="driver" tabindex="-1"><a class="header-anchor" href="#driver"><span>driver</span></a></h3>
<p style="margin-left: 2em;">Layer driver. --> <code style="text-indent: 0em;">VectorDriver</code></p>
<h3 id="fid-col" tabindex="-1"><a class="header-anchor" href="#fid-col"><span>fid_col</span></a></h3>
<p style="margin-left: 2em;">FID field name. --> <code style="text-indent: 0em;">str</code></p>
<h3 id="ftypes" tabindex="-1"><a class="header-anchor" href="#ftypes"><span>ftypes</span></a></h3>
<p style="margin-left: 2em;">Field definitions. --> <code style="text-indent: 0em;">FieldTypes</code></p>
<h3 id="geom-col" tabindex="-1"><a class="header-anchor" href="#geom-col"><span>geom_col</span></a></h3>
<p style="margin-left: 2em;">Geometry field name. --> <code style="text-indent: 0em;">str</code></p>
<h3 id="gtype" tabindex="-1"><a class="header-anchor" href="#gtype"><span>gtype</span></a></h3>
<p style="margin-left: 2em;">Layer geometry type. --> <code style="text-indent: 0em;">GMADataType</code></p>
<h3 id="link" tabindex="-1"><a class="header-anchor" href="#link"><span>link</span></a></h3>
<p style="margin-left: 2em;">Layer path link. --> <code style="text-indent: 0em;">str</code></p>
<h3 id="name" tabindex="-1"><a class="header-anchor" href="#name"><span>name</span></a></h3>
<h3 id="spatial-filter" tabindex="-1"><a class="header-anchor" href="#spatial-filter"><span>spatial_filter</span></a></h3>
<h3 id="tb" tabindex="-1"><a class="header-anchor" href="#tb"><span>tb</span></a></h3>
</div></template>


