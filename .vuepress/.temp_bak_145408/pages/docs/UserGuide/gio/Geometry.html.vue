<template><div><p style="font-size: 120%;font-weight: bold;">gma.gio.Geometry</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">Geometry</span><span style="font-style: italic; color: black;font-size: 130%;">(data = <span style="color:#48566B">None</span>, gtype = <span style="color:#48566B">None</span>, crs = <span style="color:#48566B">None</span>):</span></span>
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
<h2 id="method" tabindex="-1"><a class="header-anchor" href="#method"><span>Method</span></a></h2>
<h3 id="add-geometry-other" tabindex="-1"><a class="header-anchor" href="#add-geometry-other"><span>add_geometry<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other)</span></span></a></h3>
<p>Add a geometry to this geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">The other geometry to add.</p>
<h3 id="add-point-point" tabindex="-1"><a class="header-anchor" href="#add-point-point"><span>add_point<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(point)</span></span></a></h3>
<p>Add a point to this geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>point</b>: <code style="text-indent: 0em;">list||tuple</code>. </p>
<p style="margin-left: 4em;">The point coordinates to add. Should be a list or tuple of length 2, 3 or 4 depending on the geometry dimension.</p>
<h3 id="buffer-distance-quadsecs-30" tabindex="-1"><a class="header-anchor" href="#buffer-distance-quadsecs-30"><span>buffer<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(distance, quadsecs = 30)</span></span></a></h3>
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
<h3 id="centroid" tabindex="-1"><a class="header-anchor" href="#centroid"><span>centroid<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span></span></a></h3>
<p>Compute the geometry centroid.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b></p>
<h3 id="close-rings" tabindex="-1"><a class="header-anchor" href="#close-rings"><span>close_rings<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span></span></a></h3>
<p>Force rings to be closed.</p>
<h3 id="concave-hull-ratio-0-0-allow-holes-true" tabindex="-1"><a class="header-anchor" href="#concave-hull-ratio-0-0-allow-holes-true"><span>concave_hull<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(ratio = 0.0, allow_holes = True)</span></span></a></h3>
<p style="margin-left: 2em;">concave_hull(double ratio, bool allowHoles) --> <code style="text-indent: 0em;">Geometry</code></p>
<h3 id="contains-other" tabindex="-1"><a class="header-anchor" href="#contains-other"><span>contains<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other)</span></span></a></h3>
<p>Test for containment.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">the other geometry to compare.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if this contains the other geometry, otherwise False.</p>
<h3 id="convex-hull" tabindex="-1"><a class="header-anchor" href="#convex-hull"><span>convex_hull<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span></span></a></h3>
<p>Compute convex hull.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">a handle to A newly allocated geometry now owned by the caller.</p>
<h3 id="copy" tabindex="-1"><a class="header-anchor" href="#copy"><span>copy<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span></span></a></h3>
<p>Make a copy of this object.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">The copy of the geometry with the same spatial reference system as the original.</p>
<h3 id="crosses-other" tabindex="-1"><a class="header-anchor" href="#crosses-other"><span>crosses<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other)</span></span></a></h3>
<p>Test for crossing.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">the other geometry to compare.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if they are crossing, otherwise False.</p>
<h3 id="delaunay-triangulation-tolerance-0-0-only-edges-true" tabindex="-1"><a class="header-anchor" href="#delaunay-triangulation-tolerance-0-0-only-edges-true"><span>delaunay_triangulation<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(tolerance = 0.0, only_edges = True)</span></span></a></h3>
<p>Return a Delaunay triangulation of the vertices of the geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>dfTolerance </b> = <code style="text-indent: 0em;">float||default 0</code>. </p>
<p style="margin-left: 4em;">optional snapping tolerance to use for improved robustness</p>
<p style="margin-left: 2em;"><b>bOnlyEdges </b> = <code style="text-indent: 0em;">bool||default True</code>. </p>
<p style="margin-left: 4em;">If True, will return a MULTILINESTRING, otherwise it will return a GEOMETRYCOLLECTION containing triangular POLYGONs.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">The geometry resulting from the Delaunay triangulation.</p>
<h3 id="difference-other" tabindex="-1"><a class="header-anchor" href="#difference-other"><span>difference<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other)</span></span></a></h3>
<p>Perform spatial difference between two Geometries.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">The other geometry to overlay.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">A new geometry.</p>
<h3 id="disjoint-other" tabindex="-1"><a class="header-anchor" href="#disjoint-other"><span>disjoint<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other)</span></span></a></h3>
<p>Test for disjointness.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">The other geometry to compare.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if they are disjoint, otherwise False.</p>
<h3 id="distance-other" tabindex="-1"><a class="header-anchor" href="#distance-other"><span>distance<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other)</span></span></a></h3>
<p>Compute distance between two geometries.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">The other geometry to compare against.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>float</b>: </p>
<p style="margin-left: 4em;">The distance between the geometries or -1 if an error occurs.</p>
<h3 id="empty" tabindex="-1"><a class="header-anchor" href="#empty"><span>empty<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span></span></a></h3>
<p>Clear geometry information.</p>
<h3 id="equals-other" tabindex="-1"><a class="header-anchor" href="#equals-other"><span>equals<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other)</span></span></a></h3>
<p>Returns True if two geometries are equivalent.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">The other geometry to test against.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if equivalent or False otherwise.</p>
<h3 id="extent" tabindex="-1"><a class="header-anchor" href="#extent"><span>extent<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span></span></a></h3>
<p>The extent of a geometry is the bounding rectangle.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<h3 id="flatten" tabindex="-1"><a class="header-anchor" href="#flatten"><span>flatten<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span></span></a></h3>
<p>Convert geometry to strictly 2D.</p>
<h3 id="get-area-geodesic-false" tabindex="-1"><a class="header-anchor" href="#get-area-geodesic-false"><span>get_area<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(geodesic = False)</span></span></a></h3>
<p>Compute geometry area.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>geodesic </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">whether considered as a surface on the underlying ellipsoid of the SRS attached to the geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>float</b>: </p>
<p style="margin-left: 4em;">the area in square meters, or a negative value for unsupported geometry types.</p>
<h3 id="get-length-geodesic-false" tabindex="-1"><a class="header-anchor" href="#get-length-geodesic-false"><span>get_length<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(geodesic = False)</span></span></a></h3>
<p>Compute geometry length.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>geodesic </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default False</span>. </p>
<p style="margin-left: 4em;">whether considered as a surface on the underlying ellipsoid of the SRS attached to the geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>float</b>: </p>
<p style="margin-left: 4em;">the area in meters, or a negative value for unsupported geometry types.</p>
<h3 id="intersection-other" tabindex="-1"><a class="header-anchor" href="#intersection-other"><span>intersection<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other)</span></span></a></h3>
<p>Perform spatial intersection between two Geometries.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">The other geometry to overlay.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">A new geometry.</p>
<h3 id="intersects-other" tabindex="-1"><a class="header-anchor" href="#intersects-other"><span>intersects<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other)</span></span></a></h3>
<p>Determines whether two geometries intersect.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">The other geometry to test against.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if the geometries intersect, otherwise False.</p>
<h3 id="is-empty" tabindex="-1"><a class="header-anchor" href="#is-empty"><span>is_empty<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span></span></a></h3>
<p>Test if the geometry is empty.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if the geometry has no points, otherwise False.</p>
<h3 id="is-measured" tabindex="-1"><a class="header-anchor" href="#is-measured"><span>is_measured<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span></span></a></h3>
<p>See whether this geometry is measured.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if the geometry has M coordinates.</p>
<h3 id="is-ring" tabindex="-1"><a class="header-anchor" href="#is-ring"><span>is_ring<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span></span></a></h3>
<p>Test if the geometry is a ring.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if the geometry has no points, otherwise False.</p>
<h3 id="is-simple" tabindex="-1"><a class="header-anchor" href="#is-simple"><span>is_simple<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span></span></a></h3>
<p>Returns True if the geometry is simple.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if object is simple, otherwise False.</p>
<h3 id="is-valid" tabindex="-1"><a class="header-anchor" href="#is-valid"><span>is_valid<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span></span></a></h3>
<p>Test if the geometry is valid.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if the geometry has no points, otherwise False.</p>
<h3 id="make-valid-options" tabindex="-1"><a class="header-anchor" href="#make-valid-options"><span>make_valid<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(options = [])</span></span></a></h3>
<p>Attempts to make an invalid geometry valid without losing vertices.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>options </b> = <code style="text-indent: 0em;">list[str]</code>. <span style="color:#48566B;"> Default []</span>. </p>
<p style="margin-left: 4em;">papszOptions to be passed in. For example: ["METHOD=STRUCTURE"].</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">A newly allocated geometry now owned by the caller.</p>
<h3 id="normalize" tabindex="-1"><a class="header-anchor" href="#normalize"><span>normalize<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span></span></a></h3>
<p>Attempts to bring geometry into normalized/canonical form.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">A newly allocated geometry now owned by the caller.</p>
<h3 id="overlaps-other" tabindex="-1"><a class="header-anchor" href="#overlaps-other"><span>overlaps<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other)</span></span></a></h3>
<p>Test for overlap.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">the other geometry to compare.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if they are overlapping, otherwise False.</p>
<h3 id="plot-ax-none-kwargs" tabindex="-1"><a class="header-anchor" href="#plot-ax-none-kwargs"><span>plot<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(ax = None, **kwargs)</span></span></a></h3>
<p>Make plots of Geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>ax </b> = <code style="text-indent: 0em;">None||matplotlib</code>. <span style="color:#48566B;">~.AxesSubplot. Default None</span>. </p>
<p style="margin-left: 4em;">A matplotlib subplot. If None, a default axes will be created.</p>
<p style="margin-left: 2em;"><b>**kwargs</b></p>
<p style="margin-left: 4em;">Other plotting parameters. For more, see:</p>
<p style="margin-left: 6em;">~.carto.utils.PolyCollection/LineCollection/PointCollection.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>matplotlib.~.AxesSubplot</b></p>
<h3 id="point-on-surface" tabindex="-1"><a class="header-anchor" href="#point-on-surface"><span>point_on_surface<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span></span></a></h3>
<p>Returns a point guaranteed to lie on the surface.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">A point guaranteed to lie on the surface.</p>
<h3 id="remove-geometry-i" tabindex="-1"><a class="header-anchor" href="#remove-geometry-i"><span>remove_geometry<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(i)</span></span></a></h3>
<p>remove_geometry(int iSubGeom)</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>i</b>: <code style="text-indent: 0em;">int</code>. </p>
<p style="margin-left: 4em;">Sub geom's id.</p>
<h3 id="remove-lower-dimension-sub-geoms" tabindex="-1"><a class="header-anchor" href="#remove-lower-dimension-sub-geoms"><span>remove_lower_dimension_sub_geoms<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span></span></a></h3>
<p>remove lower dimension sub geoms.</p>
<h3 id="segmentize-max-length" tabindex="-1"><a class="header-anchor" href="#segmentize-max-length"><span>segmentize<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(max_length)</span></span></a></h3>
<p>Modify the geometry such it has no segment longer then the given distance.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>max_length</b>: <code style="text-indent: 0em;">float</code>. </p>
<p style="margin-left: 4em;">the maximum distance between 2 points after segmentization</p>
<h3 id="set-crs-crs" tabindex="-1"><a class="header-anchor" href="#set-crs-crs"><span>set_crs<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(crs)</span></span></a></h3>
<p>Set the geometry's crs.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>crs</b>: <code style="text-indent: 0em;">str||int</code>. </p>
<p style="margin-left: 4em;">The output coordinate system. Can be EPSG, WKT, Proj4, and other types of coordinate characters. The default is no coordinate system!</p>
<h3 id="set-dim-dim-xy" tabindex="-1"><a class="header-anchor" href="#set-dim-dim-xy"><span>set_dim<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(dim = &quot;XY&quot;)</span></span></a></h3>
<p>Set space dimension of geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>dim </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'XY'</span>. </p>
<p style="margin-left: 4em;">Space dimensions. Can be 'XY', 'XYZ', 'XYM' or 'XYZM'.</p>
<h3 id="simplify-tolerance-preserve-topology-false" tabindex="-1"><a class="header-anchor" href="#simplify-tolerance-preserve-topology-false"><span>simplify<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(tolerance, preserve_topology = False)</span></span></a></h3>
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
<h3 id="swap" tabindex="-1"><a class="header-anchor" href="#swap"><span>swap<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span></span></a></h3>
<p>Swap x and y coordinates.</p>
<h3 id="sym-difference-other" tabindex="-1"><a class="header-anchor" href="#sym-difference-other"><span>sym_difference<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other)</span></span></a></h3>
<p>Perform spatial symmetric difference between two Geometries.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">The other geometry to overlay.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">A new geometry.</p>
<h3 id="to-bytearray-stype-wkb" tabindex="-1"><a class="header-anchor" href="#to-bytearray-stype-wkb"><span>to_bytearray<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(stype = &quot;wkb&quot;)</span></span></a></h3>
<p>Convert a geometry into bytearray.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>stype </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'wkb'</span>. </p>
<p style="margin-left: 4em;">Export string type: 'iso_wkb' or 'wkb'.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bytes or str</b></p>
<h3 id="to-crs-crs-copy-true" tabindex="-1"><a class="header-anchor" href="#to-crs-crs-copy-true"><span>to_crs<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(crs, copy = True)</span></span></a></h3>
<p>Reproject geometry to new spatial reference system.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>crs</b>: <code style="text-indent: 0em;">CoordinateReferenceSystem</code>. </p>
<p style="margin-left: 4em;">The spatial reference system to apply.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>copy </b> = <code style="text-indent: 0em;">bool</code>. <span style="color:#48566B;"> Default True</span>. </p>
<p style="margin-left: 4em;">Whether to return a copy of the reprojected geometry.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry(copy = True) or None(copy = False)</b>: </p>
<h3 id="to-geom-base" tabindex="-1"><a class="header-anchor" href="#to-geom-base"><span>to_geom_base<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span></span></a></h3>
<p>Split complex geometry into basic geometries.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>dict of list of Geometry</b>: </p>
<p style="margin-left: 4em;">A dictionary containing lists of basic geometries categorized by their types:</p>
<p style="margin-left: 4em;">'Polygon', 'LineString', and 'Point'.</p>
<h3 id="to-points-ndim-2-node-false" tabindex="-1"><a class="header-anchor" href="#to-points-ndim-2-node-false"><span>to_points<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(ndim = 2, node = False)</span></span></a></h3>
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
<h3 id="to-precision-precision" tabindex="-1"><a class="header-anchor" href="#to-precision-precision"><span>to_precision<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(precision)</span></span></a></h3>
<p>Set the geometry's precision.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>precision</b>: <code style="text-indent: 0em;">float</code>. </p>
<p style="margin-left: 4em;">Geometric coordinate precision. e.g: 0.001.</p>
<h3 id="to-str-stype-wkt" tabindex="-1"><a class="header-anchor" href="#to-str-stype-wkt"><span>to_str<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(stype = &quot;wkt&quot;)</span></span></a></h3>
<p>Convert a geometry into str / bytes.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>stype </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'wkt'</span>. </p>
<p style="margin-left: 4em;">Export string type: 'iso_wkt', 'json', 'kml' or 'wkt'.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>str</b></p>
<h3 id="touches-other" tabindex="-1"><a class="header-anchor" href="#touches-other"><span>touches<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other)</span></span></a></h3>
<p>Test for touching.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">the other geometry to compare.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if they are touching, otherwise False.</p>
<h3 id="unary-union" tabindex="-1"><a class="header-anchor" href="#unary-union"><span>unary_union<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span></span></a></h3>
<p>Union all sum Geometries.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b></p>
<h3 id="union-other" tabindex="-1"><a class="header-anchor" href="#union-other"><span>union<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other)</span></span></a></h3>
<p>Perform spatial union between two Geometries.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">The other geometry to overlay.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">A new geometry.</p>
<h3 id="within-other" tabindex="-1"><a class="header-anchor" href="#within-other"><span>within<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other)</span></span></a></h3>
<p>Test for containment.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">the other geometry to compare.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>bool</b>: </p>
<p style="margin-left: 4em;">True if this is within other, otherwise False.</p>
<h3 id="wkb-size" tabindex="-1"><a class="header-anchor" href="#wkb-size"><span>wkb_size<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span></span></a></h3>
<p>Returns size of related binary representation.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>int</b></p>
<h2 id="property" tabindex="-1"><a class="header-anchor" href="#property"><span>Property</span></a></h2>
<h3 id="boundary" tabindex="-1"><a class="header-anchor" href="#boundary"><span>boundary</span></a></h3>
<p>Compute boundary.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Geometry</b>: </p>
<p style="margin-left: 4em;">A new geometry.</p>
<h3 id="bounds" tabindex="-1"><a class="header-anchor" href="#bounds"><span>bounds</span></a></h3>
<p>Computes and returns the bounds for this geometry in the passed psEnvelope structure.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>list of float</b>: </p>
<p style="margin-left: 4em;">minx, maxx, miny, maxy</p>
<h3 id="crs" tabindex="-1"><a class="header-anchor" href="#crs"><span>crs</span></a></h3>
<p style="margin-left: 2em;">Geometry coordinate reference system. --> <code style="text-indent: 0em;">CoordinateReferenceSystem</code></p>
<h3 id="dim" tabindex="-1"><a class="header-anchor" href="#dim"><span>dim</span></a></h3>
<p style="margin-left: 2em;">The dimension of the geometry. --> <code style="text-indent: 0em;">str(XY(2), XYZ(3) and XYM(3), XYZM(4)).</code></p>
<h3 id="gtype" tabindex="-1"><a class="header-anchor" href="#gtype"><span>gtype</span></a></h3>
<p style="margin-left: 2em;">Fetch WKT name for geometry type. --> <code style="text-indent: 0em;">str</code></p>
</div></template>


