<template><div><p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[const] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">ProjMethods</span></span>
<p>The projection methods container. All supported projection methods are mounted as attributes - each attribute is a projection method class, and instantiating it creates a projection method object which holds the parameters and renders the <code style="text-indent: 0em;">PROJECTION</code> fragment of WKT (attributes: <b>name</b>, <b>pars</b>).</p>
<div class="language-python line-numbers-mode" data-highlighter="prismjs" data-ext="py" data-title="py"><pre v-pre><code><span class="line"><span class="token keyword">from</span> gma <span class="token keyword">import</span> crs</span>
<span class="line"></span>
<span class="line">method <span class="token operator">=</span> crs<span class="token punctuation">.</span>ProjMethods<span class="token punctuation">.</span>Mercator<span class="token punctuation">(</span>central_meridian <span class="token operator">=</span> <span class="token number">110</span><span class="token punctuation">)</span></span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>crs.ProjMethods.Mercator() --> <code style="text-indent: 0em;">&lt;ProjMethod:Mercator&gt;</code></p>
<h2 id="projection-methods" tabindex="-1"><a class="header-anchor" href="#projection-methods"><span>Projection methods</span></a></h2>
<table>
<thead>
<tr>
<th>Method</th>
<th>Description</th>
<th>Parameters</th>
</tr>
</thead>
<tbody>
<tr>
<td><RouteLink to="/docs/UserGuide/crs/ProjMethods/Aitoff.html"><code v-pre>Aitoff</code></RouteLink></td>
<td>Aitoff projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><RouteLink to="/docs/UserGuide/crs/ProjMethods/AlbersConicEqualArea.html"><code v-pre>AlbersConicEqualArea</code></RouteLink></td>
<td>Albers Conic Equal Area projection method.</td>
<td><code style="text-indent: 0em;">longitude_of_center, latitude_of_center, false_easting, false_northing</code></td>
</tr>
<tr>
<td><RouteLink to="/docs/UserGuide/crs/ProjMethods/AzimuthalEquidistant.html"><code v-pre>AzimuthalEquidistant</code></RouteLink></td>
<td>Azimuthal equidistant projection method.</td>
<td><code style="text-indent: 0em;">longitude_of_center, latitude_of_center, false_easting, false_northing</code></td>
</tr>
<tr>
<td><RouteLink to="/docs/UserGuide/crs/ProjMethods/Bonne.html"><code v-pre>Bonne</code></RouteLink></td>
<td>Bonne projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><RouteLink to="/docs/UserGuide/crs/ProjMethods/CassiniSoldner.html"><code v-pre>CassiniSoldner</code></RouteLink></td>
<td>Cassini soldner projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, latitude_of_origin, false_easting, false_northing</code></td>
</tr>
<tr>
<td><RouteLink to="/docs/UserGuide/crs/ProjMethods/CompactMiller.html"><code v-pre>CompactMiller</code></RouteLink></td>
<td>Compact Miller projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><RouteLink to="/docs/UserGuide/crs/ProjMethods/CylindricalEqualArea.html"><code v-pre>CylindricalEqualArea</code></RouteLink></td>
<td>Cylindrical equal area projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><RouteLink to="/docs/UserGuide/crs/ProjMethods/EckertI.html"><code v-pre>EckertI</code></RouteLink></td>
<td>Eckert I projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><RouteLink to="/docs/UserGuide/crs/ProjMethods/EckertII.html"><code v-pre>EckertII</code></RouteLink></td>
<td>Eckert II projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><RouteLink to="/docs/UserGuide/crs/ProjMethods/EckertIII.html"><code v-pre>EckertIII</code></RouteLink></td>
<td>Eckert III projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><RouteLink to="/docs/UserGuide/crs/ProjMethods/EckertIV.html"><code v-pre>EckertIV</code></RouteLink></td>
<td>Eckert IV projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><RouteLink to="/docs/UserGuide/crs/ProjMethods/EckertV.html"><code v-pre>EckertV</code></RouteLink></td>
<td>Eckert V projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><RouteLink to="/docs/UserGuide/crs/ProjMethods/EckertVI.html"><code v-pre>EckertVI</code></RouteLink></td>
<td>Eckert VI projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><RouteLink to="/docs/UserGuide/crs/ProjMethods/EquidistantConic.html"><code v-pre>EquidistantConic</code></RouteLink></td>
<td>Equidistant Conic projection method.</td>
<td><code style="text-indent: 0em;">longitude_of_center, latitude_of_center, false_easting, false_northing</code></td>
</tr>
<tr>
<td><RouteLink to="/docs/UserGuide/crs/ProjMethods/Equirectangular.html"><code v-pre>Equirectangular</code></RouteLink></td>
<td>Equirectangular projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><RouteLink to="/docs/UserGuide/crs/ProjMethods/GallStereographic.html"><code v-pre>GallStereographic</code></RouteLink></td>
<td>Gall Stereographic projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><RouteLink to="/docs/UserGuide/crs/ProjMethods/GoodeHomolosine.html"><code v-pre>GoodeHomolosine</code></RouteLink></td>
<td>Goode Homolosine projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><RouteLink to="/docs/UserGuide/crs/ProjMethods/LambertAzimuthalEqualArea.html"><code v-pre>LambertAzimuthalEqualArea</code></RouteLink></td>
<td>Lambert Azimuthal Equal Area projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, latitude_of_center, false_easting, false_northing</code></td>
</tr>
<tr>
<td><RouteLink to="/docs/UserGuide/crs/ProjMethods/LambertConformalConic2SP.html"><code v-pre>LambertConformalConic2SP</code></RouteLink></td>
<td>Lambert Conformal Conic 2SP projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, latitude_of_origin, false_easting, false_northing</code></td>
</tr>
<tr>
<td><RouteLink to="/docs/UserGuide/crs/ProjMethods/Loximuthal.html"><code v-pre>Loximuthal</code></RouteLink></td>
<td>Loximuthal projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, latitude_of_origin, false_easting, false_northing</code></td>
</tr>
<tr>
<td><RouteLink to="/docs/UserGuide/crs/ProjMethods/Mercator.html"><code v-pre>Mercator</code></RouteLink></td>
<td>Mercator 1sp projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing, scale_factor</code></td>
</tr>
<tr>
<td><RouteLink to="/docs/UserGuide/crs/ProjMethods/Mercator2SP.html"><code v-pre>Mercator2SP</code></RouteLink></td>
<td>Mercator 2SP projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><RouteLink to="/docs/UserGuide/crs/ProjMethods/Mollweide.html"><code v-pre>Mollweide</code></RouteLink></td>
<td>Mollweide projection method.</td>
<td><code style="text-indent: 0em;">longitude_of_center, false_easting, false_northing</code></td>
</tr>
<tr>
<td><RouteLink to="/docs/UserGuide/crs/ProjMethods/NaturalEarth.html"><code v-pre>NaturalEarth</code></RouteLink></td>
<td>Natural earth projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><RouteLink to="/docs/UserGuide/crs/ProjMethods/NaturalEarthII.html"><code v-pre>NaturalEarthII</code></RouteLink></td>
<td>Natural earth II projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><RouteLink to="/docs/UserGuide/crs/ProjMethods/Polyconic.html"><code v-pre>Polyconic</code></RouteLink></td>
<td>Polyconic projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, latitude_of_origin, false_easting, false_northing</code></td>
</tr>
<tr>
<td><RouteLink to="/docs/UserGuide/crs/ProjMethods/Robinson.html"><code v-pre>Robinson</code></RouteLink></td>
<td>Robinson projection method.</td>
<td><code style="text-indent: 0em;">longitude_of_center, false_easting, false_northing</code></td>
</tr>
<tr>
<td><RouteLink to="/docs/UserGuide/crs/ProjMethods/Sinusoidal.html"><code v-pre>Sinusoidal</code></RouteLink></td>
<td>Sinusoidal projection method.</td>
<td><code style="text-indent: 0em;">longitude_of_center, false_easting, false_northing</code></td>
</tr>
<tr>
<td><RouteLink to="/docs/UserGuide/crs/ProjMethods/Times.html"><code v-pre>Times</code></RouteLink></td>
<td>Times projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><RouteLink to="/docs/UserGuide/crs/ProjMethods/TransverseMercator.html"><code v-pre>TransverseMercator</code></RouteLink></td>
<td>Transverse Mercator projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, latitude_of_origin, false_easting, false_northing, scale_factor</code></td>
</tr>
<tr>
<td><RouteLink to="/docs/UserGuide/crs/ProjMethods/VanDerGrinten.html"><code v-pre>VanDerGrinten</code></RouteLink></td>
<td>Van der Grinten projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><RouteLink to="/docs/UserGuide/crs/ProjMethods/WinkelI.html"><code v-pre>WinkelI</code></RouteLink></td>
<td>Winkel I projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><RouteLink to="/docs/UserGuide/crs/ProjMethods/WinkelII.html"><code v-pre>WinkelII</code></RouteLink></td>
<td>Winkel II projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><RouteLink to="/docs/UserGuide/crs/ProjMethods/WinkelTripel.html"><code v-pre>WinkelTripel</code></RouteLink></td>
<td>Winkel Tripel projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
</tbody>
</table>
</div></template>


