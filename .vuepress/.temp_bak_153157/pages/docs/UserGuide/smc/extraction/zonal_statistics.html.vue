<template><div><p style="font-size: 120%;font-weight: bold;">gma.smc.extraction.zonal_statistics</p><span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[function] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">zonal_statistics</span><span style="font-style: italic; color: black;font-size: 120%;">(in_ly, in_ds, agg_fun = <span style="color:#48566B">np.sum</span>):</span></span>
<p>Statistics by region according to Features.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>in_ly</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<p style="margin-left: 4em;">A gma vector layer.</p>
<p style="margin-left: 2em;"><b>in_ds</b>: <code style="text-indent: 0em;">Dataset</code>. </p>
<p style="margin-left: 4em;">A gma raster dataset.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>agg_fun </b> = <code style="text-indent: 0em;">def</code>. <span style="color:#48566B;"> Default np.sum</span>. </p>
<p style="margin-left: 4em;">Calculate functions. For Example:</p>
<div class="language-python line-numbers-mode" data-highlighter="prismjs" data-ext="py" data-title="py"><pre v-pre><code><span class="line"><span class="token keyword">def</span> <span class="token function">func</span><span class="token punctuation">(</span>in_ar<span class="token punctuation">)</span><span class="token punctuation">:</span></span>
<span class="line">    <span class="token keyword">return</span> in_ar<span class="token punctuation">.</span>mean<span class="token punctuation">(</span><span class="token punctuation">)</span></span>
<span class="line">agg_fun <span class="token operator">=</span> func</span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p style="margin-left: 4em;">in_ar: Input NumPy arrays with region shape and a masked use in_ds nodata.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">DataFrame</code>. </p>
</div></template>


