<template><div><p style="font-size: 120%;font-weight: bold;">gma.rsvi.NDVI</p><span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[function] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">NDVI</span><span style="font-style: italic; color: black;font-size: 120%;">(red, nir):</span></span>
<p>Calculate the Normalized Differnce Vegetation Index.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>red</b>: <code style="text-indent: 0em;">array</code>. </p>
<p style="margin-left: 4em;">Red-infrared band data.</p>
<p style="margin-left: 2em;"><b>nir</b>: <code style="text-indent: 0em;">array</code>. </p>
<p style="margin-left: 4em;">Near-infrared band data.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">array</code>. </p>
<h2 id="example" tabindex="-1"><a class="header-anchor" href="#example"><span>Example</span></a></h2>
<div class="language-python line-numbers-mode" data-highlighter="prismjs" data-ext="py" data-title="py"><pre v-pre><code><span class="line"><span class="token keyword">import</span> numpy <span class="token keyword">as</span> np</span>
<span class="line"><span class="token keyword">from</span> gma <span class="token keyword">import</span> rsvi</span>
<span class="line"></span>
<span class="line"><span class="token comment"># Simulated surface reflectance (0-1) of the red and nir bands</span></span>
<span class="line">red <span class="token operator">=</span> np<span class="token punctuation">.</span>random<span class="token punctuation">.</span>uniform<span class="token punctuation">(</span><span class="token number">0.05</span><span class="token punctuation">,</span> <span class="token number">0.5</span><span class="token punctuation">,</span> <span class="token punctuation">(</span><span class="token number">512</span><span class="token punctuation">,</span> <span class="token number">512</span><span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">.</span>astype<span class="token punctuation">(</span><span class="token string">'float32'</span><span class="token punctuation">)</span></span>
<span class="line">nir <span class="token operator">=</span> np<span class="token punctuation">.</span>random<span class="token punctuation">.</span>uniform<span class="token punctuation">(</span><span class="token number">0.1</span><span class="token punctuation">,</span> <span class="token number">0.6</span><span class="token punctuation">,</span> <span class="token punctuation">(</span><span class="token number">512</span><span class="token punctuation">,</span> <span class="token number">512</span><span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">.</span>astype<span class="token punctuation">(</span><span class="token string">'float32'</span><span class="token punctuation">)</span></span>
<span class="line"></span>
<span class="line"><span class="token comment"># Calculate the Normalized Difference Vegetation Index</span></span>
<span class="line">ndvi <span class="token operator">=</span> rsvi<span class="token punctuation">.</span>NDVI<span class="token punctuation">(</span>red<span class="token punctuation">,</span> nir<span class="token punctuation">)</span></span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div></div></template>


