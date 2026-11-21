---
title: ProjectedCoordinateSystem
date: 2026-11-20
---


<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjectedCoordinateSystem</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">ProjectedCoordinateSystem</span><span style="font-style: italic; color: black;font-size: 130%;">(name = <span style="color:#48566B">"GMA PCS"</span>, linear_unit = <span style="color:#48566B">"metre"</span>, proj_method = <span style="color:#48566B">"AlbersConicEqualArea"</span>, gcs = <span style="color:#48566B">"WGS84"</span>):</span></span>

<p>Create a projected coordinate system!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>name</b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'GMA PCS'</span>. </p>
<p style="margin-left: 4em;">name of the new projected coordinate system.</p>
<p style="margin-left: 2em;"><b>linear_unit</b> = <code style="text-indent: 0em;">float or str</code>. <span style="color:#48566B;"> Default 'metre'</span>. </p>
<p style="margin-left: 4em;">Linear unit value. See more default linear units: LinearUnits class!</p>
<p style="margin-left: 4em;">If you need to customize the linear unit, you can enter a real number.</p>
<p style="margin-left: 2em;"><b>proj_method</b> = <code style="text-indent: 0em;">a class of a default projection method or str(class name)</code>. <span style="color:#48566B;"> Default 'AlbersConicEqualArea'</span>. </p>
<p style="margin-left: 4em;">Projection method. If it is the name of a projection method class, it will refer</p>
<p style="margin-left: 4em;">to the default projection parameters of the projection method. See more projection</p>
<p style="margin-left: 4em;">method class: projection module!</p>
<p style="margin-left: 2em;"><b>gcs</b> = <code style="text-indent: 0em;">str, int or CoordinateReferenceSystem</code>. <span style="color:#48566B;"> Default 'WGS84'</span>. </p>
<p style="margin-left: 4em;">Geographic coordinate system in the projected coordinate system. Can be EPSG, WKT, Proj4,</p>
<p style="margin-left: 4em;">and other types of coordinate characters or a CoordinateReferenceSystem class.</p>

<div class="inherit-card">
<div class="inherit-card__label">Inheritance</div>
<div class="inherit-card__body">
<p style="margin: 0 0 0.35rem;">All properties and methods of <b>ProjectedCoordinateSystem</b> are inherited from <b>CoordinateReferenceSystem</b> - they are not repeated on this page. See the parent class documentation for details.</p>
<a class="inherit-card__btn" href="/docs/UserGuide/crs/CoordinateReferenceSystem.html">gma.crs.CoordinateReferenceSystem &rarr;</a>
</div>
</div>
