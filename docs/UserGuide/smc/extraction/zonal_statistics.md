---
title: zonal_statistics
date: 2026-08-14
sidebar: true
---
# gma.smc.extraction.zonal_statistics


<span style="background-color:#EFF0FC;display: block;line-height:1.5"><span style="color: gray;font-size:90%;">function</span> <span style="color: #616AE5; font-weight: bold;font-size: 150%;">zonal_statistics</span><span style="font-style: italic; color: black;font-size: 130%;">(in_ly, in_ds, agg_fun = <span style="color:#48566B">np.sum</span>):</span></span>

Statistics by region according to Features.

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>in_ly: </b> <code>Layer</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    A gma vector layer.</p><p style="text-indent: 1em;"><b>in_ds: </b> <code>Dataset</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    A gma raster dataset.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>agg_fun: </b> <code>def</code>. <span style="color:#48566B;">Default np.sum.</span></p><p style="padding-left: 1em;text-indent: 1em;">Calculate functions. For Example: def calFun(in_ar): return in_ar.mean() agg_fun = calFun in_ar: Input NumPy arrays with region shape and a masked use in_ds nodata.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code>DataFrame</code>.</p>

---