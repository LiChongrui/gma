---
title: translate
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.etools.translate</p><span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[function] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">translate</span><span style="font-style: italic; color: black;font-size: 120%;">(in_src, out_dst = <span style="color:#48566B">None</span>, tr_type = <span style="color:#48566B">"warp"</span>, **kwargs):</span></span>

<p>Geographic data translate!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>in_src</b>: <code style="text-indent: 0em;">str||list</code>. </p>
<p style="margin-left: 4em;">The input raster path or path collection.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>out_dst </b> = <code style="text-indent: 0em;">str||None</code>. <span style="color:#48566B;"> Default None</span>. </p>
<p style="margin-left: 4em;">The output raster file path. If not set (None), a memory file is created.</p>
<p style="margin-left: 2em;"><b>tr_type </b> = <code style="text-indent: 0em;">str</code>. <span style="color:#48566B;"> Default 'warp'</span>. </p>
<p style="margin-left: 4em;">The type of geographic data translation. Supported types include:</p>
<p style="margin-left: 4em;">'warp',  'translate', 'vrt', 'dem' - Raster data translate.</p>
<p style="margin-left: 4em;">'vector' - Vector data translate.</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to ._algos.geo.dataset.raster_translate or ._algos.geo.layer.vector_translate.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">DataSet('warp'||'translate'||'vrt'||'dem') / Layer('vector')</code>. </p>
