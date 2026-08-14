---
title: orthorectification
date: 2026-08-14
sidebar: true
---
# gma.etools.orthorectification


<span style="background-color:#EFF0FC;display: block;line-height:1.5"><span style="color: gray;font-size:90%;">function</span> <span style="color: #616AE5; font-weight: bold;font-size: 150%;">orthorectification</span><span style="font-style: italic; color: black;font-size: 130%;">(in_src, out_dst, dem = <span style="color:#48566B">None</span>, **kwargs):</span></span>

Orthorectify the image based on rational polynomial coefficients (RPC).

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>in_src: </b> <code>str</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    The input raster file path.</p><p style="text-indent: 1em;"><b>out_dst: </b> <code>str</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    The output raster file path.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>dem  = </b> <code>float||str||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">The name of the fixed height or DEM file used for RPC calculations. Default is not set (None).</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code>DataSet</code>.</p>

---