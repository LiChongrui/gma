---
title: Geometry
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.gio.Geometry</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">Geometry</span><span style="font-style: italic; color: black;font-size: 130%;">(data = <span style="color:#48566B">None</span>, gtype = <span style="color:#48566B">None</span>, crs = <span style="color:#48566B">None</span>):</span></span>

<p>Create a Geometry object.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
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

### add_geometry<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other)</span>

<p>Add a geometry to this geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">The other geometry to add.</p>

### add_point<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(point)</span>

<p>Add a point to this geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>point</b>: <code style="text-indent: 0em;">list||tuple</code>. </p>
<p style="margin-left: 4em;">The point coordinates to add. Should be a list or tuple of length 2, 3 or 4 depending on the geometry dimension.</p>

### buffer<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(distance, quadsecs = 30)</span>

<p>Compute buffer of geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>distance</b>: <code style="text-indent: 0em;">float</code>. </p>
<p style="margin-left: 4em;">The buffer distance to be applied. Should be expressed into the same unit as the coordinates of the geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>quadsecs </b> = <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 30</span>. </p>
<p style="margin-left: 4em;">The number of segments used to approximate a 90 degree (quadrant) of curvature.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">The newly created geometry.</p>

### centroid<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span>

<p>Compute the geometry centroid.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b></p>

### close_rings<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span>

<p>Force rings to be closed.</p>

### concave_hull<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(ratio = 0.0, allow_holes = True)</span>

<p style="margin-left: 2em;">concave_hull(double ratio, bool allowHoles) --> <code style="text-indent: 0em;">Geometry</code></p>

### contains<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other)</span>

<p>Test for containment.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">the other geometry to compare.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if this contains the other geometry, otherwise False.</p>

### convex_hull<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span>

<p>Compute convex hull.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">a handle to A newly allocated geometry now owned by the caller.</p>

### copy<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span>

<p>Make a copy of this object.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">The copy of the geometry with the same spatial reference system as the original.</p>

### crosses<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other)</span>

<p>Test for crossing.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">the other geometry to compare.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if they are crossing, otherwise False.</p>

### delaunay_triangulation<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(tolerance = 0.0, only_edges = True)</span>

<p>Return a Delaunay triangulation of the vertices of the geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>dfTolerance </b> = <code style="text-indent: 0em;">float||default 0</code>. </p>
<p style="margin-left: 4em;">optional snapping tolerance to use for improved robustness</p>
<p style="margin-left: 2em;"><b>bOnlyEdges </b> = <code style="text-indent: 0em;">bool||default True</code>. </p>
<p style="margin-left: 4em;">If True, will return a MULTILINESTRING, otherwise it will return a GEOMETRYCOLLECTION containing triangular POLYGONs.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">The geometry resulting from the Delaunay triangulation.</p>

### difference<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other)</span>

<p>Perform spatial difference between two Geometries.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">The other geometry to overlay.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">A new geometry.</p>

### disjoint<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other)</span>

<p>Test for disjointness.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">The other geometry to compare.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if they are disjoint, otherwise False.</p>

### distance<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other)</span>

<p>Compute distance between two geometries.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">The other geometry to compare against.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>float</b>: </p>
<p style="margin-left: 4em;">The distance between the geometries or -1 if an error occurs.</p>

### empty<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span>

<p>Clear geometry information.</p>

### equals<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other)</span>

<p>Returns True if two geometries are equivalent.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">The other geometry to test against.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if equivalent or False otherwise.</p>

### extent<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span>

<p>The extent of a geometry is the bounding rectangle.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Geometry</code>. </p>

### flatten<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span>

<p>Convert geometry to strictly 2D.</p>

### get_area<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(geodesic = False)</span>

<p>Compute geometry area.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>geodesic </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">whether considered as a surface on the underlying ellipsoid of the SRS attached to the geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>float</b>: </p>
<p style="margin-left: 4em;">the area in square meters, or a negative value for unsupported geometry types.</p>

### get_length<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(geodesic = False)</span>

<p>Compute geometry length.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>geodesic </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">whether considered as a surface on the underlying ellipsoid of the SRS attached to the geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>float</b>: </p>
<p style="margin-left: 4em;">the area in meters, or a negative value for unsupported geometry types.</p>

### intersection<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other)</span>

<p>Perform spatial intersection between two Geometries.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">The other geometry to overlay.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">A new geometry.</p>

### intersects<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other)</span>

<p>Determines whether two geometries intersect.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">The other geometry to test against.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if the geometries intersect, otherwise False.</p>

### is_empty<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span>

<p>Test if the geometry is empty.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if the geometry has no points, otherwise False.</p>

### is_measured<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span>

<p>See whether this geometry is measured.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if the geometry has M coordinates.</p>

### is_ring<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span>

<p>Test if the geometry is a ring.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if the geometry has no points, otherwise False.</p>

### is_simple<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span>

<p>Returns True if the geometry is simple.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if object is simple, otherwise False.</p>

### is_valid<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span>

<p>Test if the geometry is valid.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if the geometry has no points, otherwise False.</p>

### make_valid<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(options = [])</span>

<p>Attempts to make an invalid geometry valid without losing vertices.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>options </b> = <code style="text-indent: 0em;">list[str]</code>. <span style="color:#48566B;"> Default []</span>. </p>
<p style="margin-left: 4em;">papszOptions to be passed in. For example: ["METHOD=STRUCTURE"].</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">A newly allocated geometry now owned by the caller.</p>

### normalize<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span>

<p>Attempts to bring geometry into normalized/canonical form.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">A newly allocated geometry now owned by the caller.</p>

### overlaps<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other)</span>

<p>Test for overlap.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">the other geometry to compare.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if they are overlapping, otherwise False.</p>

### plot<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(ax = None, **kwargs)</span>

<p>Make plots of Geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>ax </b> = <code style="text-indent: 0em;">None||matplotlib</code>. <span style="color:#48566B;">~.AxesSubplot. Default None</span>. </p>
<p style="margin-left: 4em;">A matplotlib subplot. If None, a default axes will be created.</p>
<p style="margin-left: 2em;"><b>**kwargs</b></p>
<p style="margin-left: 4em;">Other plotting parameters. For more, see:</p>
<p style="margin-left: 6em;">~.carto.utils.PolyCollection/LineCollection/PointCollection.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>matplotlib.~.AxesSubplot</b></p>

### point_on_surface<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span>

<p>Returns a point guaranteed to lie on the surface.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">A point guaranteed to lie on the surface.</p>

### remove_geometry<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(i)</span>

<p>remove_geometry(int iSubGeom)</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>i</b>: <code style="text-indent: 0em;">int</code>. </p>
<p style="margin-left: 4em;">Sub geom's id.</p>

### remove_lower_dimension_sub_geoms<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span>

<p>remove lower dimension sub geoms.</p>

### segmentize<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(max_length)</span>

<p>Modify the geometry such it has no segment longer then the given distance.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>max_length</b>: <code style="text-indent: 0em;">float</code>. </p>
<p style="margin-left: 4em;">the maximum distance between 2 points after segmentization</p>

### set_crs<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(crs)</span>

<p>Set the geometry's crs.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>crs</b>: <code style="text-indent: 0em;">str||int</code>. </p>
<p style="margin-left: 4em;">The output coordinate system. Can be EPSG, WKT, Proj4, and other types of coordinate characters. The default is no coordinate system!</p>

### set_dim<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(dim = "XY")</span>

<p>Set space dimension of geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>dim </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'XY'</span>. </p>
<p style="margin-left: 4em;">Space dimensions. Can be 'XY', 'XYZ', 'XYM' or 'XYZM'.</p>

### simplify<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(tolerance, preserve_topology = False)</span>

<p>Compute a simplified geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>tolerance</b>: <code style="text-indent: 0em;">float</code>. </p>
<p style="margin-left: 4em;">The distance tolerance for the simplification.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>preserve_topology </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">Simplify the geometry while preserving topology.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">The simplified geometry or None if an error occurs.</p>

### swap<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span>

<p>Swap x and y coordinates.</p>

### sym_difference<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other)</span>

<p>Perform spatial symmetric difference between two Geometries.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">The other geometry to overlay.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">A new geometry.</p>

### to_bytearray<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(stype = "wkb")</span>

<p>Convert a geometry into bytearray.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>stype </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'wkb'</span>. </p>
<p style="margin-left: 4em;">Export string type: 'iso_wkb' or 'wkb'.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bytes or str</b></p>

### to_crs<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(crs, copy = True)</span>

<p>Reproject geometry to new spatial reference system.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>crs</b>: <code style="text-indent: 0em;">CoordinateReferenceSystem</code>. </p>
<p style="margin-left: 4em;">The spatial reference system to apply.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>copy </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default True</span>. </p>
<p style="margin-left: 4em;">Whether to return a copy of the reprojected geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry(copy = True) or None(copy = False)</b>: </p>

### to_geom_base<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span>

<p>Split complex geometry into basic geometries.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>dict of list of Geometry</b>: </p>
<p style="margin-left: 4em;">A dictionary containing lists of basic geometries categorized by their types:</p>
<p style="margin-left: 4em;">'Polygon', 'LineString', and 'Point'.</p>

### to_points<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(ndim = 2, node = False)</span>

<p>Get all points from the geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>ndim</b>: <code style="text-indent: 0em;">int</code>. <span style="color:#48566B;"> Default 0</span>. </p>
<p style="margin-left: 4em;">The number of dimensions for each point: 2, 3 or 4. If 0, it will use the geometry's own dimension.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>node </b> = <code style="text-indent: 0em;">bool||default False</code>. </p>
<p style="margin-left: 4em;">Whether to add node markers for points.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>list of x, y points, vert's codes(codes = True)</b>: </p>
<p style="margin-left: 4em;">A list containing all points in the geometry.</p>

### to_precision<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(precision)</span>

<p>Set the geometry's precision.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>precision</b>: <code style="text-indent: 0em;">float</code>. </p>
<p style="margin-left: 4em;">Geometric coordinate precision. e.g: 0.001.</p>

### to_str<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(stype = "wkt")</span>

<p>Convert a geometry into str / bytes.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>stype </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'wkt'</span>. </p>
<p style="margin-left: 4em;">Export string type: 'iso_wkt', 'json', 'kml' or 'wkt'.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>str</b></p>

### touches<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other)</span>

<p>Test for touching.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">the other geometry to compare.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if they are touching, otherwise False.</p>

### unary_union<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span>

<p>Union all sum Geometries.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b></p>

### union<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other)</span>

<p>Perform spatial union between two Geometries.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">The other geometry to overlay.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">A new geometry.</p>

### within<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other)</span>

<p>Test for containment.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">the other geometry to compare.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if this is within other, otherwise False.</p>

### wkb_size<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span>

<p>Returns size of related binary representation.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>int</b></p>

## Property

### boundary

<p>Compute boundary.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">A new geometry.</p>

### bounds

<p>Computes and returns the bounds for this geometry in the passed psEnvelope structure.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>list of float</b>: </p>
<p style="margin-left: 4em;">minx, maxx, miny, maxy</p>

### crs

<p style="margin-left: 2em;">Geometry coordinate reference system. --> <code style="text-indent: 0em;">CoordinateReferenceSystem</code></p>

### dim

<p style="margin-left: 2em;">The dimension of the geometry. --> <code style="text-indent: 0em;">str(XY(2), XYZ(3) and XYM(3), XYZM(4)).</code></p>

### gtype

<p style="margin-left: 2em;">Fetch WKT name for geometry type. --> <code style="text-indent: 0em;">str</code></p>

## Example

```python
from gma import gio

# Create geometries from WKT strings
pt = gio.Geometry('POINT (114 30)')
pg = gio.Geometry('POLYGON ((110 28, 118 28, 118 32, 110 32, 110 28))')

# Spatial operations
buf = pg.buffer(1)
print(pg.contains(pt))

# Create a LineString from a coordinate list
ln = gio.Geometry([[114, 30], [115, 31]], gtype='LineString')
```
