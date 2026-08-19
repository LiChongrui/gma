---
title: Geometry
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.gio.Geometry</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">Geometry</span><span style="font-style: italic; color: black;font-size: 130%;">(data = <span style="color:#48566B">None</span>, gtype = <span style="color:#48566B">None</span>, crs = <span style="color:#48566B">None</span>):</span></span>

<p>Create a Geometry object.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>data </b> = <code style="text-indent: 0em;">str||list||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The data to create the geometry from. It can be:</p>
<p style="margin-left: 4em;">- None: create an empty geometry of type gtype.</p>
<p style="margin-left: 4em;">- str: a string representation of the geometry in WKT, GeoJSON, GML, etc.</p>
<p style="margin-left: 4em;">- list, tuple or np.ndarray: a collection of points to create the geometry from.</p>
<p style="margin-left: 2em;"><b>gtype </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The geometry type to create. It can be 'Point', 'LineString', 'Polygon', etc.</p>
<p style="margin-left: 4em;">This parameter is required if data is a list, tuple or np.ndarray.</p>
<p style="margin-left: 2em;"><b>crs </b> = <code style="text-indent: 0em;">str||int||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The projection of the geometry. If None, no projection is set.</p>

## Method

### add_geometry
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.add_geometry</span><span style="font-style: italic; color: black;font-size: 120%;">(other):</span></span>

<p>Add a geometry to this geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">The other geometry to add.</p>

### add_point
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.add_point</span><span style="font-style: italic; color: black;font-size: 120%;">(point):</span></span>

<p>Add a point to this geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>point</b>: <code style="text-indent: 0em;">list||tuple</code>. </p>
<p style="margin-left: 4em;">The point coordinates to add. Should be a list or tuple of length 2, 3 or 4 depending on the geometry dimension.</p>

### buffer
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.buffer</span><span style="font-style: italic; color: black;font-size: 120%;">(distance, quadsecs = <span style="color:#48566B">30</span>):</span></span>

<p>Compute buffer of geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>distance</b>: <code style="text-indent: 0em;">float</code>. </p>
<p style="margin-left: 4em;">The buffer distance to be applied. Should be expressed into the same unit as the coordinates of the geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>quadsecs </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 30</span>. </p>
<p style="margin-left: 4em;">The number of segments used to approximate a 90 degree (quadrant) of curvature.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">The newly created geometry.</p>

### centroid
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.centroid</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>

<p>Compute the geometry centroid.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b></p>

### close_rings
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.close_rings</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>

<p>Force rings to be closed.</p>

### concave_hull
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.concave_hull</span><span style="font-style: italic; color: black;font-size: 120%;">(ratio = <span style="color:#48566B">0.0</span>, allow_holes = <span style="color:#48566B">True</span>):</span></span>

<p style="margin-left: 2em;">concave_hull(double ratio, bool allowHoles) --> <code style="text-indent: 0em;">Geometry</code></p>

### contains
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.contains</span><span style="font-style: italic; color: black;font-size: 120%;">(other):</span></span>

<p>Test for containment.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">the other geometry to compare.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if this contains the other geometry, otherwise False.</p>

### convex_hull
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.convex_hull</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>

<p>Compute convex hull.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">a handle to A newly allocated geometry now owned by the caller.</p>

### copy
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.copy</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>

<p>Make a copy of this object.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">The copy of the geometry with the same spatial reference system as the original.</p>

### crosses
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.crosses</span><span style="font-style: italic; color: black;font-size: 120%;">(other):</span></span>

<p>Test for crossing.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">the other geometry to compare.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if they are crossing, otherwise False.</p>

### delaunay_triangulation
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.delaunay_triangulation</span><span style="font-style: italic; color: black;font-size: 120%;">(tolerance = <span style="color:#48566B">0.0</span>, only_edges = <span style="color:#48566B">True</span>):</span></span>

<p>Return a Delaunay triangulation of the vertices of the geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>dfTolerance </b> = <code style="text-indent: 0em;">float||default 0</code>. </p>
<p style="margin-left: 4em;">optional snapping tolerance to use for improved robustness</p>
<p style="margin-left: 2em;"><b>bOnlyEdges </b> = <code style="text-indent: 0em;">bool||default True</code>. </p>
<p style="margin-left: 4em;">If True, will return a MULTILINESTRING, otherwise it will return a GEOMETRYCOLLECTION containing triangular POLYGONs.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">The geometry resulting from the Delaunay triangulation.</p>

### difference
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.difference</span><span style="font-style: italic; color: black;font-size: 120%;">(other):</span></span>

<p>Perform spatial difference between two Geometries.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">The other geometry to overlay.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">A new geometry.</p>

### disjoint
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.disjoint</span><span style="font-style: italic; color: black;font-size: 120%;">(other):</span></span>

<p>Test for disjointness.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">The other geometry to compare.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if they are disjoint, otherwise False.</p>

### distance
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.distance</span><span style="font-style: italic; color: black;font-size: 120%;">(other):</span></span>

<p>Compute distance between two geometries.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">The other geometry to compare against.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>float</b>: </p>
<p style="margin-left: 4em;">The distance between the geometries or -1 if an error occurs.</p>

### empty
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.empty</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>

<p>Clear geometry information.</p>

### equals
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.equals</span><span style="font-style: italic; color: black;font-size: 120%;">(other):</span></span>

<p>Returns True if two geometries are equivalent.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">The other geometry to test against.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if equivalent or False otherwise.</p>

### extent
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.extent</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>

<p>The extent of a geometry is the bounding rectangle.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Geometry</code>. </p>

### flatten
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.flatten</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>

<p>Convert geometry to strictly 2D.</p>

### get_area
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.get_area</span><span style="font-style: italic; color: black;font-size: 120%;">(geodesic = <span style="color:#48566B">False</span>):</span></span>

<p>Compute geometry area.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>geodesic </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">whether considered as a surface on the underlying ellipsoid of the SRS attached to the geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>float</b>: </p>
<p style="margin-left: 4em;">the area in square meters, or a negative value for unsupported geometry types.</p>

### get_length
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.get_length</span><span style="font-style: italic; color: black;font-size: 120%;">(geodesic = <span style="color:#48566B">False</span>):</span></span>

<p>Compute geometry length.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>geodesic </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">whether considered as a surface on the underlying ellipsoid of the SRS attached to the geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>float</b>: </p>
<p style="margin-left: 4em;">the area in meters, or a negative value for unsupported geometry types.</p>

### intersection
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.intersection</span><span style="font-style: italic; color: black;font-size: 120%;">(other):</span></span>

<p>Perform spatial intersection between two Geometries.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">The other geometry to overlay.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">A new geometry.</p>

### intersects
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.intersects</span><span style="font-style: italic; color: black;font-size: 120%;">(other):</span></span>

<p>Determines whether two geometries intersect.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">The other geometry to test against.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if the geometries intersect, otherwise False.</p>

### is_empty
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.is_empty</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>

<p>Test if the geometry is empty.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if the geometry has no points, otherwise False.</p>

### is_measured
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.is_measured</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>

<p>See whether this geometry is measured.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if the geometry has M coordinates.</p>

### is_ring
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.is_ring</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>

<p>Test if the geometry is a ring.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if the geometry has no points, otherwise False.</p>

### is_simple
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.is_simple</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>

<p>Returns True if the geometry is simple.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if object is simple, otherwise False.</p>

### is_valid
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.is_valid</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>

<p>Test if the geometry is valid.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if the geometry has no points, otherwise False.</p>

### make_valid
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.make_valid</span><span style="font-style: italic; color: black;font-size: 120%;">(options = <span style="color:#48566B">[]</span>):</span></span>

<p>Attempts to make an invalid geometry valid without losing vertices.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>options </b> = <code style="text-indent: 0em;">list[str]</code>. <span style="color:#48566B;"> Default []</span>. </p>
<p style="margin-left: 4em;">papszOptions to be passed in. For example: ["METHOD=STRUCTURE"].</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">A newly allocated geometry now owned by the caller.</p>

### normalize
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.normalize</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>

<p>Attempts to bring geometry into normalized/canonical form.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">A newly allocated geometry now owned by the caller.</p>

### overlaps
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.overlaps</span><span style="font-style: italic; color: black;font-size: 120%;">(other):</span></span>

<p>Test for overlap.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">the other geometry to compare.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if they are overlapping, otherwise False.</p>

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

### point_on_surface
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.point_on_surface</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>

<p>Returns a point guaranteed to lie on the surface.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">A point guaranteed to lie on the surface.</p>

### remove_geometry
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.remove_geometry</span><span style="font-style: italic; color: black;font-size: 120%;">(i):</span></span>

<p>remove_geometry(int iSubGeom)</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>i</b>: <code style="text-indent: 0em;">int</code>. </p>
<p style="margin-left: 4em;">Sub geom's id.</p>

### remove_lower_dimension_sub_geoms
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.remove_lower_dimension_sub_geoms</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>

<p>remove lower dimension sub geoms.</p>

### segmentize
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.segmentize</span><span style="font-style: italic; color: black;font-size: 120%;">(max_length):</span></span>

<p>Modify the geometry such it has no segment longer then the given distance.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>max_length</b>: <code style="text-indent: 0em;">float</code>. </p>
<p style="margin-left: 4em;">the maximum distance between 2 points after segmentization</p>

### set_crs
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.set_crs</span><span style="font-style: italic; color: black;font-size: 120%;">(crs):</span></span>

<p>Set the geometry's crs.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>crs</b>: <code style="text-indent: 0em;">str||int</code>. </p>
<p style="margin-left: 4em;">The output coordinate system. Can be EPSG, WKT, Proj4, and other types of coordinate characters. The default is no coordinate system!</p>

### set_dim
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.set_dim</span><span style="font-style: italic; color: black;font-size: 120%;">(dim = <span style="color:#48566B">"XY"</span>):</span></span>

<p>Set space dimension of geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>dim </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'XY'</span>. </p>
<p style="margin-left: 4em;">Space dimensions. Can be 'XY', 'XYZ', 'XYM' or 'XYZM'.</p>

### simplify
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.simplify</span><span style="font-style: italic; color: black;font-size: 120%;">(tolerance, preserve_topology = <span style="color:#48566B">False</span>):</span></span>

<p>Compute a simplified geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>tolerance</b>: <code style="text-indent: 0em;">float</code>. </p>
<p style="margin-left: 4em;">The distance tolerance for the simplification.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>preserve_topology </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Simplify the geometry while preserving topology.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">The simplified geometry or None if an error occurs.</p>

### swap
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.swap</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>

<p>Swap x and y coordinates.</p>

### sym_difference
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.sym_difference</span><span style="font-style: italic; color: black;font-size: 120%;">(other):</span></span>

<p>Perform spatial symmetric difference between two Geometries.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">The other geometry to overlay.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">A new geometry.</p>

### to_bytearray
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.to_bytearray</span><span style="font-style: italic; color: black;font-size: 120%;">(stype = <span style="color:#48566B">"wkb"</span>):</span></span>

<p>Convert a geometry into bytearray.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>stype </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'wkb'</span>. </p>
<p style="margin-left: 4em;">Export string type: 'iso_wkb' or 'wkb'.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bytes or str</b></p>

### to_crs
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.to_crs</span><span style="font-style: italic; color: black;font-size: 120%;">(crs, copy = <span style="color:#48566B">True</span>):</span></span>

<p>Reproject geometry to new spatial reference system.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>crs</b>: <code style="text-indent: 0em;">CoordinateReferenceSystem</code>. </p>
<p style="margin-left: 4em;">The spatial reference system to apply.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>copy </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default True</span>. </p>
<p style="margin-left: 4em;">Whether to return a copy of the reprojected geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry(copy = True) or None(copy = False)</b>: </p>

### to_geom_base
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.to_geom_base</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>

<p>Split complex geometry into basic geometries.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>dict of list of Geometry</b>: </p>
<p style="margin-left: 4em;">A dictionary containing lists of basic geometries categorized by their types:</p>
<p style="margin-left: 4em;">'Polygon', 'LineString', and 'Point'.</p>

### to_points
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.to_points</span><span style="font-style: italic; color: black;font-size: 120%;">(ndim = <span style="color:#48566B">2</span>, node = <span style="color:#48566B">False</span>):</span></span>

<p>Get all points from the geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>ndim</b>: <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 0</span>. </p>
<p style="margin-left: 4em;">The number of dimensions for each point: 2, 3 or 4. If 0, it will use the geometry's own dimension.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>node </b> = <code style="text-indent: 0em;">bool||default False</code>. </p>
<p style="margin-left: 4em;">Whether to add node markers for points.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>list of x, y points, vert's codes(codes = True)</b>: </p>
<p style="margin-left: 4em;">A list containing all points in the geometry.</p>

### to_precision
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.to_precision</span><span style="font-style: italic; color: black;font-size: 120%;">(precision):</span></span>

<p>Set the geometry's precision.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>precision</b>: <code style="text-indent: 0em;">float</code>. </p>
<p style="margin-left: 4em;">Geometric coordinate precision. e.g: 0.001.</p>

### to_str
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.to_str</span><span style="font-style: italic; color: black;font-size: 120%;">(stype = <span style="color:#48566B">"wkt"</span>):</span></span>

<p>Convert a geometry into str / bytes.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>stype </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'wkt'</span>. </p>
<p style="margin-left: 4em;">Export string type: 'iso_wkt', 'json', 'kml' or 'wkt'.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>str</b></p>

### touches
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.touches</span><span style="font-style: italic; color: black;font-size: 120%;">(other):</span></span>

<p>Test for touching.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">the other geometry to compare.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if they are touching, otherwise False.</p>

### unary_union
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.unary_union</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>

<p>Union all sum Geometries.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b></p>

### union
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.union</span><span style="font-style: italic; color: black;font-size: 120%;">(other):</span></span>

<p>Perform spatial union between two Geometries.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">The other geometry to overlay.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">A new geometry.</p>

### within
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.within</span><span style="font-style: italic; color: black;font-size: 120%;">(other):</span></span>

<p>Test for containment.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">the other geometry to compare.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if this is within other, otherwise False.</p>

### wkb_size
<span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[method] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.wkb_size</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>

<p>Returns size of related binary representation.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>int</b></p>

## Property

### boundary
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.boundary</span><span style=""></span></span>

<p>Compute boundary.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">A new geometry.</p>

### bounds
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.bounds</span><span style=""></span></span>

<p>Computes and returns the bounds for this geometry in the passed psEnvelope structure.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>list of float</b>: </p>
<p style="margin-left: 4em;">minx, maxx, miny, maxy</p>

### crs
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.crs</span><span style=""></span></span>

<p style="margin-left: 2em;">Geometry coordinate reference system. --> <code style="text-indent: 0em;">CoordinateReferenceSystem</code></p>

### dim
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.dim</span><span style=""></span></span>

<p style="margin-left: 2em;">The dimension of the geometry. --> <code style="text-indent: 0em;">str(XY(2), XYZ(3) and XYM(3), XYZM(4)).</code></p>

### gtype
<span style=""><span style="color: gray;font-size:90%;">[property] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">.gtype</span><span style=""></span></span>

<p style="margin-left: 2em;">Fetch WKT name for geometry type. --> <code style="text-indent: 0em;">str</code></p>
