---
title: Datum
date: 2026-11-20
---


<p style="font-size: 120%;font-weight: bold;">gma.crs.Datum</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">Datum</span><span style="font-style: italic; color: black;font-size: 130%;">(name = <span style="color:#48566B">"GMA Datum"</span>, ellipsoid = <span style="color:#48566B">"GMA Ellipsoid"</span>, semi_major = <span style="color:#48566B">6378137.0</span>, inv_flattening = <span style="color:#48566B">298.2572236</span>):</span></span>

<p>Define a datum</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>name</b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'GMA Datum'</span>. </p>
<p style="margin-left: 4em;">Name of the new datum.</p>
<p style="margin-left: 2em;"><b>ellipsoid</b> = <code style="text-indent: 0em;">str or Ellipsoid</code>. <span style="color:#48566B;"> Default 'GMA Ellipsoid'</span>. </p>
<p style="margin-left: 4em;">Name of the new datum. if ellipsoid is a Ellipsoid object,</p>
<p style="margin-left: 4em;">then semi_major, inv_flattening will be ignore.</p>
<p style="margin-left: 2em;"><b>semi_major</b> = <code style="text-indent: 0em;">float or None</code>. <span style="color:#48566B;"> Default 6378137.0</span>. </p>
<p style="margin-left: 4em;">The semi-major axis of the ellipsoid.</p>
<p style="margin-left: 2em;"><b>inv_flattening</b> = <code style="text-indent: 0em;">float</code>. <span style="color:#48566B;"> Default 298.2572236</span>. </p>
<p style="margin-left: 4em;">The inverse flattening of the ellipsoid.</p>

<p>Inherits all properties from <a href="/docs/UserGuide/crs/Ellipsoid.html">Ellipsoid</a>.</p>