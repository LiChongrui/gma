<template><div><p style="font-size: 120%;font-weight: bold;">gma.crs.GeographicCoordinateSystem</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">GeographicCoordinateSystem</span><span style="font-style: italic; color: black;font-size: 130%;">(name = <span style="color:#48566B">"GMA GCS"</span>, angular_unit = <span style="color:#48566B">"degree"</span>, primem = <span style="color:#48566B">"Greenwich"</span>, ellipsoid = <span style="color:#48566B">"WGS_84"</span>, datum = <span style="color:#48566B">None</span>):</span></span>
<p>Create a geographic coordinate system!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>name</b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'GMA GCS'</span>. </p>
<p style="margin-left: 4em;">Name of the new geographical coordinate system.</p>
<p style="margin-left: 2em;"><b>angular_unit</b> = <code style="text-indent: 0em;">float or str</code>. <span style="color:#48566B;"> Default 'Degree'</span>. </p>
<p style="margin-left: 4em;">Angular unit value. See more default angular units: AngularUnits class!</p>
<p style="margin-left: 4em;">If you need to customize the angle unit, you can enter a real number.</p>
<p style="margin-left: 2em;"><b>primem</b> = <code style="text-indent: 0em;">float or str</code>. <span style="color:#48566B;"> Default 'Greenwich'</span>. </p>
<p style="margin-left: 4em;">Prime meridian. See more default prime meridians: PRIMEMs class!</p>
<p style="margin-left: 4em;">If you need to customize the prime meridian, you can enter a real number.</p>
<p style="margin-left: 2em;"><b>ellipsoid</b> = <code style="text-indent: 0em;">str or a class of Ellipsoid</code>. <span style="color:#48566B;"> Default 'WGS84'</span>. </p>
<p style="margin-left: 4em;">Ellipsoid. See more default prime ellipsoids: Ellips class!</p>
<p style="margin-left: 4em;">If you need to customize the ellipsoid, please use the Ellipsoid class to initialize.</p>
<p style="margin-left: 2em;"><b>datum</b> = <code style="text-indent: 0em;">None or a class of Datum</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">Datum. If None, the ellipsoid is automatically configured based on the datum.</p>
<p style="margin-left: 4em;">If it is a class of Datum, the parameter of Ellipsoid will be ignored.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">CoordinateReferenceSystem</code>. </p>
<div class="inherit-card">
<div class="inherit-card__label">Inheritance</div>
<div class="inherit-card__body">
<p style="margin: 0 0 0.35rem;">All properties and methods of <b>GeographicCoordinateSystem</b> are inherited from <b>CoordinateReferenceSystem</b> - they are not repeated on this page. See the parent class documentation for details.</p>
<a class="inherit-card__btn" href="/docs/UserGuide/crs/CoordinateReferenceSystem.html">gma.crs.CoordinateReferenceSystem &rarr;</a>
</div>
</div>
</div></template>


