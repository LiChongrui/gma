---
title: orthorectification
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.etools.orthorectification</p><span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[function] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">orthorectification</span><span style="font-style: italic; color: black;font-size: 120%;">(in_src, out_dst, dem = <span style="color:#48566B">None</span>, **kwargs):</span></span>

<p>Orthorectify the image based on rational polynomial coefficients (RPC).</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>in_src</b>: <code style="text-indent: 0em;">str</code>. </p>
<p style="margin-left: 4em;">The input raster file path.</p>
<p style="margin-left: 2em;"><b>out_dst</b>: <code style="text-indent: 0em;">str</code>. </p>
<p style="margin-left: 4em;">The output raster file path.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>dem </b> = <code style="text-indent: 0em;">float||str||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The name of the fixed height or DEM file used for RPC calculations. Default is not set (None).</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">DataSet</code>. </p>
