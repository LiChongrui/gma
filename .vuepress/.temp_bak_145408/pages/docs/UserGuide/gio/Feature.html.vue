<template><div><p style="font-size: 120%;font-weight: bold;">gma.gio.Feature</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">Feature</span><span style="font-style: italic; color: black;font-size: 130%;">(geom = <span style="color:#48566B">None</span>, values = <span style="color:#48566B">[]</span>, gtype = <span style="color:#48566B">None</span>, ftypes = <span style="color:#48566B">None</span>, crs = <span style="color:#48566B">None</span>):</span></span>
<p>Create a Feature object.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
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
<h2 id="method" tabindex="-1"><a class="header-anchor" href="#method"><span>Method</span></a></h2>
<h3 id="copy" tabindex="-1"><a class="header-anchor" href="#copy"><span>copy<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">()</span></span></a></h3>
<p style="margin-left: 2em;">copy self. --> <code style="text-indent: 0em;">Feature</code></p>
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
<h3 id="set-fid-fid" tabindex="-1"><a class="header-anchor" href="#set-fid-fid"><span>set_fid<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(fid)</span></span></a></h3>
<p>Set the feature identifier.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>fid</b>: <code style="text-indent: 0em;">int</code>. </p>
<p style="margin-left: 4em;">the new feature identifier value to assign.</p>
<h3 id="set-geom-geom" tabindex="-1"><a class="header-anchor" href="#set-geom-geom"><span>set_geom<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(geom)</span></span></a></h3>
<p>Set feature geometry. This function updates the features geometry, except that this function does not assume ownership of the passed geometry, but instead makes a copy of it.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>geom</b>: <code style="text-indent: 0em;">Geometry</code>. </p>
<p style="margin-left: 4em;">new geometry to apply to feature.</p>
<h3 id="update-other" tabindex="-1"><a class="header-anchor" href="#update-other"><span>update<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">(other)</span></span></a></h3>
<p>Set one feature from another. Overwrite the contents of this feature from the geometry and attributes of another.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>other</b>: <code style="text-indent: 0em;">Feature</code>. </p>
<p style="margin-left: 4em;">feature from which geometry and field values will be copied.</p>
<h2 id="property" tabindex="-1"><a class="header-anchor" href="#property"><span>Property</span></a></h2>
<h3 id="crs" tabindex="-1"><a class="header-anchor" href="#crs"><span>crs</span></a></h3>
<p style="margin-left: 2em;">Get coordinate reference system. --> <code style="text-indent: 0em;">CoordinateReferenceSystem</code></p>
<h3 id="fid" tabindex="-1"><a class="header-anchor" href="#fid"><span>fid</span></a></h3>
<p style="margin-left: 2em;">Get feature identifier. --> <code style="text-indent: 0em;">int</code></p>
<h3 id="fields" tabindex="-1"><a class="header-anchor" href="#fields"><span>fields</span></a></h3>
<p style="margin-left: 2em;">Get fields for feature. --> <code style="text-indent: 0em;">dict</code></p>
<h3 id="ftypes" tabindex="-1"><a class="header-anchor" href="#ftypes"><span>ftypes</span></a></h3>
<p style="margin-left: 2em;">Get field types for feature. --> <code style="text-indent: 0em;">FieldTypes</code></p>
<h3 id="geom" tabindex="-1"><a class="header-anchor" href="#geom"><span>geom</span></a></h3>
<p style="margin-left: 2em;">Get geometry for feature. --> <code style="text-indent: 0em;">Geometry</code></p>
</div></template>


