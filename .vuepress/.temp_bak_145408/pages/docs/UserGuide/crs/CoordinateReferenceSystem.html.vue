<template><div><p style="font-size: 120%;font-weight: bold;">gma.crs.CoordinateReferenceSystem</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">CoordinateReferenceSystem</span><span style="font-style: italic; color: black;font-size: 130%;">(crs = <span style="color:#48566B">"WGS84"</span>):</span></span>
<p>Coordinate system!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>crs</b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'WGS84'</span>. </p>
<p style="margin-left: 4em;">Coordinate system. Can be EPSG, WKT, Proj4 and other types of coordinate characters, or a CoordinateReferenceSystem object.</p>
<h2 id="method" tabindex="-1"><a class="header-anchor" href="#method"><span>Method</span></a></h2>
<h3 id="copy" tabindex="-1"><a class="header-anchor" href="#copy"><span>copy<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span></span></a></h3>
<p>Clone crs. --> <code style="text-indent: 0em;">CoordinateReferenceSystem</code></p>
<h3 id="get-proj-parms" tabindex="-1"><a class="header-anchor" href="#get-proj-parms"><span>get_proj_parms<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span></span></a></h3>
<p>Get projection parameters.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">dict</code>. </p>
<h3 id="plot-ax-none" tabindex="-1"><a class="header-anchor" href="#plot-ax-none"><span>plot<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(ax = None)</span></span></a></h3>
<p>Make area of use of the CoordinateReferenceSystem in world.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>ax</b> = <code style="text-indent: 0em;">None or matplotlib.~.AxesSubplot</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">A matplotlib subplot. If None, a default axes will be created.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other plotting parameters of CoordinateReferenceSystem's geometry. For more, see:</p>
<p style="margin-left: 4em;">~.carto.utils.PolyCollection.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">matplotlib.~.AxesSubplot</code>. </p>
<h3 id="to-str-ctype-wkt" tabindex="-1"><a class="header-anchor" href="#to-str-ctype-wkt"><span>to_str<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(ctype = &quot;Wkt&quot;)</span></span></a></h3>
<p>Export projection to string.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>ctype</b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'Wkt'</span>. </p>
<p style="margin-left: 4em;">Export format. Can be 'MICoordSys', 'PrettyWkt',</p>
<p style="margin-left: 4em;">'Proj4', 'Wkt', 'XML'.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">str</code>. </p>
<h3 id="to-list-ctype-pci" tabindex="-1"><a class="header-anchor" href="#to-list-ctype-pci"><span>to_list<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(ctype = &quot;PCI&quot;)</span></span></a></h3>
<p>Export projection to list.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>ctype</b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'PCI'</span>. </p>
<p style="margin-left: 4em;">Export format. Can be 'PCI', 'USGS'.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">list</code>. </p>
<h3 id="to-dict" tabindex="-1"><a class="header-anchor" href="#to-dict"><span>to_dict<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span></span></a></h3>
<p>Export projection to dict(json).</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">dict</code>. </p>
<h2 id="property" tabindex="-1"><a class="header-anchor" href="#property"><span>Property</span></a></h2>
<h3 id="angular-units" tabindex="-1"><a class="header-anchor" href="#angular-units"><span>angular_units</span></a></h3>
<p style="margin-left: 2em;">Angular units. --> <code style="text-indent: 0em;">tuple(float, str)</code></p>
<h3 id="area-of-use" tabindex="-1"><a class="header-anchor" href="#area-of-use"><span>area_of_use</span></a></h3>
<p style="margin-left: 2em;">Get the area where the coordinate system is used. --> <code style="text-indent: 0em;">tuple(West, South, East, North in degree).</code></p>
<h3 id="area-of-interest" tabindex="-1"><a class="header-anchor" href="#area-of-interest"><span>area_of_interest</span></a></h3>
<p style="margin-left: 2em;">The area of use's geometry of the crs in WGS84. --> <code style="text-indent: 0em;">Geometry.</code></p>
<h3 id="axes-count" tabindex="-1"><a class="header-anchor" href="#axes-count"><span>axes_count</span></a></h3>
<p style="margin-left: 2em;">Number of coordinate axes. --> <code style="text-indent: 0em;">int</code></p>
<h3 id="central-longitude" tabindex="-1"><a class="header-anchor" href="#central-longitude"><span>central_longitude</span></a></h3>
<p style="margin-left: 2em;">Get the longitude of the central meridian. --> <code style="text-indent: 0em;">float</code></p>
<h3 id="change-longitude" tabindex="-1"><a class="header-anchor" href="#change-longitude"><span>change_longitude</span></a></h3>
<p style="margin-left: 2em;">Date Line --> <code style="text-indent: 0em;">float</code></p>
<h3 id="datum-name" tabindex="-1"><a class="header-anchor" href="#datum-name"><span>datum_name</span></a></h3>
<p style="margin-left: 2em;">Datum name. --> <code style="text-indent: 0em;">str</code></p>
<h3 id="gcs" tabindex="-1"><a class="header-anchor" href="#gcs"><span>gcs</span></a></h3>
<p style="margin-left: 2em;">Get projection parameters. --> <code style="text-indent: 0em;">CoordinateReferenceSystem</code></p>
<h3 id="inv-flattening" tabindex="-1"><a class="header-anchor" href="#inv-flattening"><span>inv_flattening</span></a></h3>
<p style="margin-left: 2em;">Inverse flattening. --> <code style="text-indent: 0em;">float</code></p>
<h3 id="linear-units" tabindex="-1"><a class="header-anchor" href="#linear-units"><span>linear_units</span></a></h3>
<p style="margin-left: 2em;">Linear units and name. --> <code style="text-indent: 0em;">tuple(float, str).</code></p>
<h3 id="name" tabindex="-1"><a class="header-anchor" href="#name"><span>name</span></a></h3>
<p style="margin-left: 2em;">Name of the coordinate system. --> <code style="text-indent: 0em;">str</code></p>
<h3 id="planet" tabindex="-1"><a class="header-anchor" href="#planet"><span>planet</span></a></h3>
<p style="margin-left: 2em;">The planet of the coordinate system. --> <code style="text-indent: 0em;">str</code></p>
<h3 id="primem" tabindex="-1"><a class="header-anchor" href="#primem"><span>primem</span></a></h3>
<p style="margin-left: 2em;">The prime meridian and name. --> <code style="text-indent: 0em;">tuple(float, str)</code></p>
<h3 id="proj-method" tabindex="-1"><a class="header-anchor" href="#proj-method"><span>proj_method</span></a></h3>
<p style="margin-left: 2em;">The project method name. --> <code style="text-indent: 0em;">str</code></p>
<h3 id="radius" tabindex="-1"><a class="header-anchor" href="#radius"><span>radius</span></a></h3>
<p style="margin-left: 2em;">Ellipsoid radius. --> <code style="text-indent: 0em;">float</code></p>
<h3 id="semi-major" tabindex="-1"><a class="header-anchor" href="#semi-major"><span>semi_major</span></a></h3>
<p style="margin-left: 2em;">Semi-major axis. --> <code style="text-indent: 0em;">float</code></p>
<h3 id="semi-minor" tabindex="-1"><a class="header-anchor" href="#semi-minor"><span>semi_minor</span></a></h3>
<p style="margin-left: 2em;">Semi-minor axis. --> <code style="text-indent: 0em;">float</code></p>
<h3 id="spheroid-name" tabindex="-1"><a class="header-anchor" href="#spheroid-name"><span>spheroid_name</span></a></h3>
<p style="margin-left: 2em;">Spheroid name. --> <code style="text-indent: 0em;">str</code></p>
<h3 id="type" tabindex="-1"><a class="header-anchor" href="#type"><span>type</span></a></h3>
<p style="margin-left: 2em;">Space Reference Type. --> <code style="text-indent: 0em;">str</code></p>
<h3 id="wkid" tabindex="-1"><a class="header-anchor" href="#wkid"><span>WKID</span></a></h3>
<p style="margin-left: 2em;">Well-known ID Code and name. --> <code style="text-indent: 0em;">tuple(float, str)</code></p>
</div></template>


