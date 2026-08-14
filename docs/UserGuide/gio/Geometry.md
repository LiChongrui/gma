---
title: Geometry
date: 2026-08-14
sidebar: true
---
# gma.gio.Geometry


<span style="background-color:#EFF0FC;display: block;line-height:1.5"><span style="color: gray;font-size:90%;">class</span> <span style="color: #616AE5; font-weight: bold;font-size: 150%;">Geometry</span><span style="font-style: italic; color: black;font-size: 130%;">(data = <span style="color:#48566B">None</span>, gtype = <span style="color:#48566B">None</span>, crs = <span style="color:#48566B">None</span>):</span></span>

Geometry object for vector data. Create a Geometry object.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>data: </b> <code>varioustypes</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">The data to create the geometry from. It can be: - None: create an empty geometry of type gtype.</p><p style="padding-left: 1em;text-indent: 1em;">- str: a string representation of the geometry in WKT, GeoJSON, GML, etc.</p><p style="padding-left: 1em;text-indent: 1em;">- list, tuple or np.ndarray: a collection of points to create the geometry from.</p><p style="text-indent: 1em;"><b>gtype: </b> <code>str</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">The geometry type to create. It can be 'Point', 'LineString', 'Polygon', etc.</p><p style="padding-left: 1em;text-indent: 1em;">This parameter is required if data is a list, tuple or np.ndarray.</p><p style="text-indent: 1em;"><b>crs: </b> <code>str</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The projection of the geometry. If None, no projection is set.</p>

---

## Methods 



### add_geometry




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">add_geometry</span><span style="font-style: italic; color: black;font-size: 120%;">(other):</span></span>


Add a geometry to this geometry.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>other: </b> <code>Geometry</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    The other geometry to add.</p>

---

### add_point




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">add_point</span><span style="font-style: italic; color: black;font-size: 120%;">(point):</span></span>


Add a point to this geometry.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>point: </b> <code>list||tuple</code>.</p><p style="padding-left: 1em;text-indent: 1em;">The point coordinates to add. Should be a list or tuple of length 2, 3 or 4 depending on the geometry dimension.</p>

---

### buffer




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">buffer</span><span style="font-style: italic; color: black;font-size: 120%;">(distance, quadsecs = <span style="color:#48566B">30</span>):</span></span>


Compute buffer of geometry.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>distance: </b> <code>float</code>.</p><p style="padding-left: 1em;text-indent: 1em;">The buffer distance to be applied. Should be expressed into the same unit as the coordinates of the geometry.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>quadsecs  = </b> <code>int</code>. <span style="color:#48566B;">Default 30.</span></p><p style="padding-left: 1em;text-indent: 1em;">The number of segments used to approximate a 90 degree (quadrant) of curvature.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Geometry:</b></p><p style="padding-left: 1em;text-indent: 1em;">    The newly created geometry.</p>

---

### centroid




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">centroid</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>


Compute the geometry centroid.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Geometry</b>.</p>

---

### close_rings




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">close_rings</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>


Force rings to be closed.



---

### concave_hull




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">concave_hull</span><span style="font-style: italic; color: black;font-size: 120%;">(ratio = <span style="color:#48566B">0.0</span>, allow_holes = <span style="color:#48566B">True</span>):</span></span>


concave_hull(double ratio, bool allowHoles) -> Geometry



---

### contains




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">contains</span><span style="font-style: italic; color: black;font-size: 120%;">(other):</span></span>


Test for containment.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>other: </b> <code>Geometry</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    the other geometry to compare.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>bool:</b></p><p style="padding-left: 1em;text-indent: 1em;">    True if this contains the other geometry, otherwise False.</p>

---

### convex_hull




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">convex_hull</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>


Compute convex hull.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Geometry:</b></p><p style="padding-left: 1em;text-indent: 1em;">    a handle to A newly allocated geometry now owned by the caller.</p>

---

### copy




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">copy</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>


Make a copy of this object.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Geometry:</b></p><p style="padding-left: 1em;text-indent: 1em;">The copy of the geometry with the same spatial reference system as the original.</p>

---

### crosses




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">crosses</span><span style="font-style: italic; color: black;font-size: 120%;">(other):</span></span>


Test for crossing.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>other: </b> <code>Geometry</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    the other geometry to compare.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>bool:</b></p><p style="padding-left: 1em;text-indent: 1em;">    True if they are crossing, otherwise False.</p>

---

### delaunay_triangulation




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">delaunay_triangulation</span><span style="font-style: italic; color: black;font-size: 120%;">(tolerance = <span style="color:#48566B">0.0</span>, only_edges = <span style="color:#48566B">True</span>):</span></span>


Return a Delaunay triangulation of the vertices of the geometry.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>dfTolerance  = </b> <code>float||default0</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    optional snapping tolerance to use for improved robustness</p><p style="text-indent: 1em;"><b>bOnlyEdges  = </b> <code>bool||defaultTrue</code>.</p><p style="padding-left: 1em;text-indent: 1em;">If True, will return a MULTILINESTRING, otherwise it will return a GEOMETRYCOLLECTION containing triangular POLYGONs.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Geometry:</b></p><p style="padding-left: 1em;text-indent: 1em;">    The geometry resulting from the Delaunay triangulation.</p>

---

### difference




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">difference</span><span style="font-style: italic; color: black;font-size: 120%;">(other):</span></span>


Perform spatial difference between two Geometries.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>other: </b> <code>Geometry</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    The other geometry to overlay.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Geometry:</b></p><p style="padding-left: 1em;text-indent: 1em;">    A new geometry.</p>

---

### disjoint




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">disjoint</span><span style="font-style: italic; color: black;font-size: 120%;">(other):</span></span>


Test for disjointness.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>other: </b> <code>Geometry</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    The other geometry to compare.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>bool:</b></p><p style="padding-left: 1em;text-indent: 1em;">    True if they are disjoint, otherwise False.</p>

---

### distance




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">distance</span><span style="font-style: italic; color: black;font-size: 120%;">(other):</span></span>


Compute distance between two geometries.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>other: </b> <code>Geometry</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    The other geometry to compare against.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>float:</b></p><p style="padding-left: 1em;text-indent: 1em;">    The distance between the geometries or -1 if an error occurs.</p>

---

### empty




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">empty</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>


Clear geometry information.



---

### equals




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">equals</span><span style="font-style: italic; color: black;font-size: 120%;">(other):</span></span>




<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>other: </b> <code>Geometry</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    The other geometry to test against.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>bool:</b></p><p style="padding-left: 1em;text-indent: 1em;">    True if equivalent or False otherwise.</p>

---

### extent




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">extent</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>


The extent of a geometry is the bounding rectangle.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code>Geometry</code>.</p>

---

### flatten




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">flatten</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>


Convert geometry to strictly 2D.



---

### get_area




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">get_area</span><span style="font-style: italic; color: black;font-size: 120%;">(geodesic = <span style="color:#48566B">False</span>):</span></span>


Compute geometry area.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>geodesic  = </b> <code>bool</code>. <span style="color:#48566B;">Default False.</span></p><p style="padding-left: 1em;text-indent: 1em;">    whether considered as a surface on the underlying ellipsoid of the SRS attached to the geometry.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>float:</b></p><p style="padding-left: 1em;text-indent: 1em;">    the area in square meters, or a negative value for unsupported geometry types. </p>

---

### get_length




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">get_length</span><span style="font-style: italic; color: black;font-size: 120%;">(geodesic = <span style="color:#48566B">False</span>):</span></span>


Compute geometry length.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>geodesic  = </b> <code>bool</code>. <span style="color:#48566B;">Default False.</span></p><p style="padding-left: 1em;text-indent: 1em;">    whether considered as a surface on the underlying ellipsoid of the SRS attached to the geometry.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>float:</b></p><p style="padding-left: 1em;text-indent: 1em;">    the area in meters, or a negative value for unsupported geometry types.</p>

---

### intersection




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">intersection</span><span style="font-style: italic; color: black;font-size: 120%;">(other):</span></span>


Perform spatial intersection between two Geometries.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>other: </b> <code>Geometry</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    The other geometry to overlay.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Geometry:</b></p><p style="padding-left: 1em;text-indent: 1em;">    A new geometry.</p>

---

### intersects




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">intersects</span><span style="font-style: italic; color: black;font-size: 120%;">(other):</span></span>


Determines whether two geometries intersect.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>other: </b> <code>Geometry</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    The other geometry to test against.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>bool:</b></p><p style="padding-left: 1em;text-indent: 1em;">    True if the geometries intersect, otherwise False.</p>

---

### is_empty




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">is_empty</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>


Test if the geometry is empty.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>bool:</b></p><p style="padding-left: 1em;text-indent: 1em;">    True if the geometry has no points, otherwise False.</p>

---

### is_measured




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">is_measured</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>


See whether this geometry is measured.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>bool:</b></p><p style="padding-left: 1em;text-indent: 1em;">    True if the geometry has M coordinates.</p>

---

### is_ring




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">is_ring</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>


Test if the geometry is a ring.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>bool:</b></p><p style="padding-left: 1em;text-indent: 1em;">    True if the geometry has no points, otherwise False.</p>

---

### is_simple




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">is_simple</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>




<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>bool:</b></p><p style="padding-left: 1em;text-indent: 1em;">    True if object is simple, otherwise False.</p>

---

### is_valid




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">is_valid</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>


Test if the geometry is valid.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>bool:</b></p><p style="padding-left: 1em;text-indent: 1em;">    True if the geometry has no points, otherwise False.</p>

---

### make_valid




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">make_valid</span><span style="font-style: italic; color: black;font-size: 120%;">(options = <span style="color:#48566B">[]</span>):</span></span>


Attempts to make an invalid geometry valid without losing vertices.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>options  = </b> <code>list[str]</code>. <span style="color:#48566B;">Default [].</span></p><p style="padding-left: 1em;text-indent: 1em;">    papszOptions to be passed in. For example: ["METHOD=STRUCTURE"].</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Geometry:</b></p><p style="padding-left: 1em;text-indent: 1em;">    A newly allocated geometry now owned by the caller.</p>

---

### normalize




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">normalize</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>


Attempts to bring geometry into normalized/canonical form.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Geometry:</b></p><p style="padding-left: 1em;text-indent: 1em;">    A newly allocated geometry now owned by the caller.</p>

---

### overlaps




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">overlaps</span><span style="font-style: italic; color: black;font-size: 120%;">(other):</span></span>


Test for overlap.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>other: </b> <code>Geometry</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    the other geometry to compare.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>bool:</b></p><p style="padding-left: 1em;text-indent: 1em;">    True if they are overlapping, otherwise False.</p>

---

### plot




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">plot</span><span style="font-style: italic; color: black;font-size: 120%;">(ax = <span style="color:#48566B">None</span>, **kwargs):</span></span>


Make plots of Geometry.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>ax  = </b> <code>None||matplotlib.~.AxesSubplot</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    A matplotlib subplot. If None, a default axes will be created. </p><p style="text-indent: 1em;"><b>**kwargs</b>.</p><p style="padding-left: 1em;text-indent: 1em;">Other plotting parameters. For more, see: ~.carto.utils.PolyCollection/LineCollection/PointCollection.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>matplotlib.~.AxesSubplot</b>.</p>

---

### point_on_surface




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">point_on_surface</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>




<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Geometry:</b></p><p style="padding-left: 1em;text-indent: 1em;">    A point guaranteed to lie on the surface.</p>

---

### remove_geometry




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">remove_geometry</span><span style="font-style: italic; color: black;font-size: 120%;">(i):</span></span>


remove_geometry(int iSubGeom)

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>i: </b> <code>int</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Sub geom's id.</p>

---

### remove_lower_dimension_sub_geoms




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">remove_lower_dimension_sub_geoms</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>


remove lower dimension sub geoms.



---

### segmentize




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">segmentize</span><span style="font-style: italic; color: black;font-size: 120%;">(max_length):</span></span>


Modify the geometry such it has no segment longer then the given distance.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>max_length: </b> <code>float</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    the maximum distance between 2 points after segmentization</p>

---

### set_crs




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">set_crs</span><span style="font-style: italic; color: black;font-size: 120%;">(crs):</span></span>


Set the geometry's crs.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>crs: </b> <code>str||int</code>.</p><p style="padding-left: 1em;text-indent: 1em;">The output coordinate system. Can be EPSG, WKT, Proj4, and other types of coordinate characters. The default is no coordinate system!</p>

---

### set_dim




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">set_dim</span><span style="font-style: italic; color: black;font-size: 120%;">(dim = <span style="color:#48566B">"XY"</span>):</span></span>


Set space dimension of geometry.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>dim  = </b> <code>str</code>. <span style="color:#48566B;">Default 'XY'.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Space dimensions. Can be 'XY', 'XYZ', 'XYM' or 'XYZM'.</p>

---

### simplify




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">simplify</span><span style="font-style: italic; color: black;font-size: 120%;">(tolerance, preserve_topology = <span style="color:#48566B">False</span>):</span></span>


Compute a simplified geometry.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>tolerance: </b> <code>float</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    The distance tolerance for the simplification.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>preserve_topology  = </b> <code>bool</code>. <span style="color:#48566B;">Default False.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Simplify the geometry while preserving topology.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Geometry:</b></p><p style="padding-left: 1em;text-indent: 1em;">    The simplified geometry or None if an error occurs.</p>

---

### swap




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">swap</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>


Swap x and y coordinates.



---

### sym_difference




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">sym_difference</span><span style="font-style: italic; color: black;font-size: 120%;">(other):</span></span>


Perform spatial symmetric difference between two Geometries.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>other: </b> <code>Geometry</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    The other geometry to overlay.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Geometry:</b></p><p style="padding-left: 1em;text-indent: 1em;">    A new geometry.</p>

---

### to_bytearray




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">to_bytearray</span><span style="font-style: italic; color: black;font-size: 120%;">(stype = <span style="color:#48566B">"wkb"</span>):</span></span>


Convert a geometry into bytearray.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>stype  = </b> <code>str</code>. <span style="color:#48566B;">Default 'wkb'.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Export string type: 'iso_wkb' or 'wkb'.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>bytes or str</b>.</p>

---

### to_crs




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">to_crs</span><span style="font-style: italic; color: black;font-size: 120%;">(crs, copy = <span style="color:#48566B">True</span>):</span></span>


Reproject geometry to new spatial reference system.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>crs: </b> <code>CoordinateReferenceSystem</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    The spatial reference system to apply.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>copy  = </b> <code>bool</code>. <span style="color:#48566B;">Default True.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Whether to return a copy of the reprojected geometry.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Geometry(copy = True) or None(copy = False):</b></p>

---

### to_geom_base




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">to_geom_base</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>


Split complex geometry into basic geometries.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>dict of list of Geometry:</b></p><p style="padding-left: 1em;text-indent: 1em;">A dictionary containing lists of basic geometries categorized by their types: 'Polygon', 'LineString', and 'Point'.</p>

---

### to_points




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">to_points</span><span style="font-style: italic; color: black;font-size: 120%;">(ndim = <span style="color:#48566B">2</span>, node = <span style="color:#48566B">False</span>):</span></span>


Get all points from the geometry.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>ndim: </b> <code>int</code>. <span style="color:#48566B;">Default 0.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The number of dimensions for each point: 2, 3 or 4. If 0, it will use the geometry's own dimension.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>node  = </b> <code>bool||defaultFalse</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Whether to add node markers for points.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>list of x, y points, vert's codes(codes = True):</b></p><p style="padding-left: 1em;text-indent: 1em;">    A list containing all points in the geometry.</p>

---

### to_precision




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">to_precision</span><span style="font-style: italic; color: black;font-size: 120%;">(precision):</span></span>


Set the geometry's precision.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>precision: </b> <code>float</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    Geometric coordinate precision. e.g: 0.001.</p>

---

### to_str




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">to_str</span><span style="font-style: italic; color: black;font-size: 120%;">(stype = <span style="color:#48566B">"wkt"</span>):</span></span>


Convert a geometry into str / bytes.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>stype  = </b> <code>str</code>. <span style="color:#48566B;">Default 'wkt'.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Export string type: 'iso_wkt', 'json', 'kml' or 'wkt'.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>str</b>.</p>

---

### touches




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">touches</span><span style="font-style: italic; color: black;font-size: 120%;">(other):</span></span>


Test for touching.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>other: </b> <code>Geometry</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    the other geometry to compare.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>bool:</b></p><p style="padding-left: 1em;text-indent: 1em;">    True if they are touching, otherwise False.</p>

---

### unary_union




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">unary_union</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>


Union all sum Geometries.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Geometry</b>.</p>

---

### union




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">union</span><span style="font-style: italic; color: black;font-size: 120%;">(other):</span></span>


Perform spatial union between two Geometries.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>other: </b> <code>Geometry</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    The other geometry to overlay.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Geometry:</b></p><p style="padding-left: 1em;text-indent: 1em;">    A new geometry.</p>

---

### within




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">within</span><span style="font-style: italic; color: black;font-size: 120%;">(other):</span></span>


Test for containment.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>other: </b> <code>Geometry</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    the other geometry to compare.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>bool:</b></p><p style="padding-left: 1em;text-indent: 1em;">    True if this is within other, otherwise False.</p>

---

### wkb_size




<span style="background-color:#F4F4F5;display: block;line-height:1.5"><span style="color: lightgray;font-size:90%;">[method]</span> .<span style="color: #616AE5; font-weight: bold;font-size: 125%;">wkb_size</span><span style="font-style: italic; color: black;font-size: 120%;">():</span></span>




<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>int</b>.</p>

---

## Property 



### boundary


Compute boundary.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Geometry:</b></p><p style="padding-left: 1em;text-indent: 1em;">    A new geometry.</p>

---

### bounds


Computes and returns the bounds for this geometry in the passed psEnvelope structure.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>list of float:</b></p><p style="padding-left: 1em;text-indent: 1em;">    minx, maxx, miny, maxy</p>

---

### crs


Geometry coordinate reference system. -> CoordinateReferenceSystem



---

### dim


The dimension of the geometry. -> str(XY(2), XYZ(3) and XYM(3), XYZM(4)).



---

### gtype


Fetch WKT name for geometry type. -> str



---