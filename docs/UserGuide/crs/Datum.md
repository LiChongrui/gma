---
title: Datum
date: 2026-08-15
sidebar: true
---
<span style="font-size: 120%;font-weight: bold;">gma.crs.Datum</span>


<span style="background-color:#EFF0FC;display: block;line-height:1.5"><span style="color: gray;font-size:90%;">class</span> <span style="color: #616AE5; font-weight: bold;font-size: 150%;">Datum</span><span style="font-style: italic; color: black;font-size: 130%;">(name = <span style="color:#48566B">"GMA Datum"</span>, ellipsoid = <span style="color:#48566B">"GMA Ellipsoid"</span>, semi_major = <span style="color:#48566B">6378137.0</span>, inv_flattening = <span style="color:#48566B">298.2572236</span>):</span></span>

Datum object. Define a datum.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>name  = </b> <code style="text-indent: 0">str</code>. <span style="color:#48566B;">Default 'GMA Datum'.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Name of the new datum.</p><p style="text-indent: 1em;"><b>ellipsoid  = </b> <code style="text-indent: 0">str||Ellipsoid</code>. <span style="color:#48566B;">Default 'GMA Ellipsoid'.</span></p><p style="padding-left: 1em;text-indent: 1em;">Name of the new datum. if ellipsoid is a Ellipsoid object, then semi_major, inv_flattening will be ignore.</p><p style="text-indent: 1em;"><b>semi_major  = </b> <code style="text-indent: 0">float||None</code>. <span style="color:#48566B;">Default 6378137.0.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The semi-major axis of the ellipsoid.</p><p style="text-indent: 1em;"><b>inv_flattening  = </b> <code style="text-indent: 0">float</code>. <span style="color:#48566B;">Default 298.2572236.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The inverse flattening of the ellipsoid.</p>

---

## Property 



### ellipsoid_name




---

### inv_flattening




---

### semi_major




---