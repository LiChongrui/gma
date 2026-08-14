---
title: translate
date: 2026-08-14
sidebar: true
---
# gma.etools.translate


<span style="background-color:#EFF0FC;display: block;line-height:1.5"><span style="color: gray;font-size:90%;">function</span> <span style="color: #616AE5; font-weight: bold;font-size: 150%;">translate</span><span style="font-style: italic; color: black;font-size: 130%;">(in_src, out_dst = <span style="color:#48566B">None</span>, tr_type = <span style="color:#48566B">"warp"</span>, **kwargs):</span></span>

Geographic data translate!

<p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Parameters:</p><p style="text-indent: 1em;"><b>in_src: </b> <code>str||list</code>.</p><p style="padding-left: 1em;text-indent: 1em;">    The input raster path or path collection.</p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Optional:</p><p style="text-indent: 1em;"><b>out_dst  = </b> <code>str||None</code>. <span style="color:#48566B;">Default None.</span></p><p style="padding-left: 1em;text-indent: 1em;">    The output raster file path. If not set (None), a memory file is created.</p><p style="text-indent: 1em;"><b>tr_type  = </b> <code>str</code>. <span style="color:#48566B;">Default 'warp'.</span></p><p style="padding-left: 1em;text-indent: 1em;">The type of geographic data translation. Supported types include: 'warp',  'translate', 'vrt', 'dem' - Raster data translate.</p><p style="padding-left: 1em;text-indent: 1em;">'vector' - Vector data translate.</p><p style="text-indent: 1em;"><b>**kwargs:</b></p><p style="padding-left: 1em;text-indent: 1em;">    Other parameters passed to ._algos.geo.dataset.raster_translate or ._algos.geo.layer.vector_translate.   </p><p style="background-color:none;font-size: 120%;display: block;color:#9298ED; font-weight: bold;">Returns:</p><p style="text-indent: 1em;"><b>Type: </b> <code>DataSet('warp'||'translate'||'vrt'||'dem')/Layer('vector')</code>.</p>

---