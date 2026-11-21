<template><div><p style="font-size: 120%;font-weight: bold;">gma.crs.AngleUnits</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[const] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">AngleUnits</span></span>
<p>Angle units object. Conversion factors relative to the radian.</p>
<p>Attribute names are derived from the PROJ database and accessed directly as instance attributes:</p>
<div class="language-python line-numbers-mode" data-highlighter="prismjs" data-ext="py" data-title="py"><pre v-pre><code><span class="line"><span class="token keyword">from</span> gma <span class="token keyword">import</span> crs</span>
<span class="line">crs<span class="token punctuation">.</span>AngleUnits<span class="token punctuation">.</span>DEGREE</span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div></div></div><p>crs.AngleUnits.DEGREE --> <code style="text-indent: 0em;">0.017453292519943278</code></p>
<h2 id="constants" tabindex="-1"><a class="header-anchor" href="#constants"><span>Constants</span></a></h2>
<table>
<thead>
<tr>
<th>Constant</th>
<th>Value (to radian)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code v-pre>ARC_MINUTE</code></td>
<td>0.0002908882086657213</td>
</tr>
<tr>
<td><code v-pre>ARC_SECOND</code></td>
<td>4.848136811095355e-06</td>
</tr>
<tr>
<td><code v-pre>CENTESIMAL_MINUTE</code></td>
<td>0.0001570796326794895</td>
</tr>
<tr>
<td><code v-pre>CENTESIMAL_SECOND</code></td>
<td>1.570796326794895e-06</td>
</tr>
<tr>
<td><code v-pre>DEGREE</code></td>
<td>0.017453292519943278</td>
</tr>
<tr>
<td><code v-pre>GON</code></td>
<td>0.01570796326794895</td>
</tr>
<tr>
<td><code v-pre>GRAD</code></td>
<td>0.01570796326794895</td>
</tr>
<tr>
<td><code v-pre>MICRORADIAN</code></td>
<td>1e-06</td>
</tr>
<tr>
<td><code v-pre>MILLIARC_SECOND</code></td>
<td>4.848136811095355e-09</td>
</tr>
<tr>
<td><code v-pre>MIL_6400</code></td>
<td>0.0009817477042468094</td>
</tr>
<tr>
<td><code v-pre>RADIAN</code></td>
<td>1.0</td>
</tr>
</tbody>
</table>
</div></template>


