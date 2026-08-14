---
title: tri
date: 2026-08-14
sidebar: true
---
# gma.etools.tri


<span style="background-color:#EFF0FC;display: block;line-height:1.5"><span style="color: gray;font-size:90%;">function</span> <span style="color: #616AE5; font-weight: bold;font-size: 150%;">tri</span><span style="font-style: italic; color: black;font-size: 130%;">(in_src, out_dst, compute_edges = <span style="color:#48566B">None</span>, band = <span style="color:#48566B">1</span>, **kwargs):</span></span>

Calculate Terrain Ruggedness Index from any supported DEM raster file!

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>in_src: </b> <code>str</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    The input raster file path.</p><p style="text-indent: 1em;"><b>out_dst: </b> <code>str</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    The output raster file path.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>compute_edges  = </b> <code>bool</code>. <span style="color:#48566B;">Default True.</span></p><p style="padding-left: 1em;text-indent: 1em;">Whether to compute raster edge data and data near no data values.</p><p style="padding-left: 1em;text-indent: 1em;">Setting values that are not True are treated as False.</p><p style="text-indent: 1em;"><b>band  = </b> <code>int</code>. <span style="color:#48566B;">Default 1.</span></p><p style="padding-left: 1em;text-indent: 1em;">    Number of the element calculation band. Start with 1.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to translate.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code>DataSet</code>.</p>

---