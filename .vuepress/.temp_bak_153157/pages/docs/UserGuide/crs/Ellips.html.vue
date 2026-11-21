<template><div><p style="font-size: 120%;font-weight: bold;">gma.crs.Ellips</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[const] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">Ellips</span></span>
<p>Default ellipsoids. Built from the PROJ database when created.</p>
<p>Attribute names are derived from the PROJ database and accessed directly as instance attributes:</p>
<div class="language-python line-numbers-mode" data-highlighter="prismjs" data-ext="py" data-title="py"><pre v-pre><code><span class="line"><span class="token keyword">from</span> gma <span class="token keyword">import</span> crs</span>
<span class="line">crs<span class="token punctuation">.</span>Ellips<span class="token punctuation">.</span>WGS_84</span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div></div></div><p>crs.Ellips.WGS_84 --> <code style="text-indent: 0em;">{'semi_major': 6378137.0, 'inv_flattening': 298.257223563}</code></p>
<h2 id="constants" tabindex="-1"><a class="header-anchor" href="#constants"><span>Constants</span></a></h2>
<table>
<thead>
<tr>
<th>Constant</th>
<th>Semi-major axis (m)</th>
<th>Inverse flattening</th>
</tr>
</thead>
<tbody>
<tr>
<td><code v-pre>AIRY_1830</code></td>
<td>6377563.396</td>
<td>299.3249646</td>
</tr>
<tr>
<td><code v-pre>BESSEL_1841</code></td>
<td>6377397.155</td>
<td>299.1528128</td>
</tr>
<tr>
<td><code v-pre>BESSEL_MODIFIED</code></td>
<td>6377492.018</td>
<td>299.1528128</td>
</tr>
<tr>
<td><code v-pre>BESSEL_NAMIBIA</code></td>
<td>6377483.865</td>
<td>299.1528128</td>
</tr>
<tr>
<td><code v-pre>CGCS2000</code></td>
<td>6378137.0</td>
<td>298.257222101</td>
</tr>
<tr>
<td><code v-pre>DANISH_1876</code></td>
<td>6377019.27</td>
<td>300.0</td>
</tr>
<tr>
<td><code v-pre>FISCHER_1960</code></td>
<td>6378166.0</td>
<td>298.3</td>
</tr>
<tr>
<td><code v-pre>FISCHER_1968</code></td>
<td>6378150.0</td>
<td>298.3</td>
</tr>
<tr>
<td><code v-pre>FISCHER_MODIFIED</code></td>
<td>6378155.0</td>
<td>298.3</td>
</tr>
<tr>
<td><code v-pre>GEM_10C</code></td>
<td>6378137.0</td>
<td>298.257223563</td>
</tr>
<tr>
<td><code v-pre>GRS_1967</code></td>
<td>6378160.0</td>
<td>298.247167427</td>
</tr>
<tr>
<td><code v-pre>GRS_1980</code></td>
<td>6378137.0</td>
<td>298.257222101</td>
</tr>
<tr>
<td><code v-pre>GSK2011</code></td>
<td>6378136.5</td>
<td>298.2564151</td>
</tr>
<tr>
<td><code v-pre>HELMERT_1906</code></td>
<td>6378200.0</td>
<td>298.3</td>
</tr>
<tr>
<td><code v-pre>HOUGH_1960</code></td>
<td>6378270.0</td>
<td>297.0</td>
</tr>
<tr>
<td><code v-pre>IAG_1975</code></td>
<td>6378140.0</td>
<td>298.257</td>
</tr>
<tr>
<td><code v-pre>INTERNATIONAL_1924</code></td>
<td>6378388.0</td>
<td>297.0</td>
</tr>
<tr>
<td><code v-pre>INTERNATIONAL_1967</code></td>
<td>6378160.0</td>
<td>298.25</td>
</tr>
<tr>
<td><code v-pre>KAULA_1961</code></td>
<td>6378163.0</td>
<td>298.24</td>
</tr>
<tr>
<td><code v-pre>KRASSOWSKY_1940</code></td>
<td>6378245.0</td>
<td>298.3</td>
</tr>
<tr>
<td><code v-pre>LERCH_1979</code></td>
<td>6378139.0</td>
<td>298.257</td>
</tr>
<tr>
<td><code v-pre>MAUPERTIUS_1738</code></td>
<td>6397300.0</td>
<td>191.0</td>
</tr>
<tr>
<td><code v-pre>MERIT_1983</code></td>
<td>6378137.0</td>
<td>298.257</td>
</tr>
<tr>
<td><code v-pre>NWL_10D</code></td>
<td>6378135.0</td>
<td>298.26</td>
</tr>
<tr>
<td><code v-pre>NWL_9D</code></td>
<td>6378145.0</td>
<td>298.25</td>
</tr>
<tr>
<td><code v-pre>OSU86F</code></td>
<td>6378136.2</td>
<td>298.257223563</td>
</tr>
<tr>
<td><code v-pre>OSU91A</code></td>
<td>6378136.3</td>
<td>298.257223563</td>
</tr>
<tr>
<td><code v-pre>PLESSIS_1817</code></td>
<td>6376523.0</td>
<td>308.64</td>
</tr>
<tr>
<td><code v-pre>PZ90</code></td>
<td>6378136.0</td>
<td>298.257839303</td>
</tr>
<tr>
<td><code v-pre>STRUVE_1860</code></td>
<td>6378298.3</td>
<td>294.73</td>
</tr>
<tr>
<td><code v-pre>WALBECK</code></td>
<td>6376896.0</td>
<td>302.78</td>
</tr>
<tr>
<td><code v-pre>WAR_OFFICE</code></td>
<td>6378300.0</td>
<td>296.0</td>
</tr>
<tr>
<td><code v-pre>WGS_1966</code></td>
<td>6378145.0</td>
<td>298.25</td>
</tr>
<tr>
<td><code v-pre>WGS_60</code></td>
<td>6378165.0</td>
<td>298.3</td>
</tr>
<tr>
<td><code v-pre>WGS_72</code></td>
<td>6378135.0</td>
<td>298.26</td>
</tr>
<tr>
<td><code v-pre>WGS_84</code></td>
<td>6378137.0</td>
<td>298.257223563</td>
</tr>
<tr>
<td><code v-pre>ZACH_1812</code></td>
<td>6376045.0</td>
<td>310.0</td>
</tr>
</tbody>
</table>
</div></template>


