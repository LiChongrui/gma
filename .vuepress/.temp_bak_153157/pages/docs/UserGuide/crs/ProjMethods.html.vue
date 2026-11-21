<template><div><p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[const] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">ProjMethods</span></span>
<p>The projection methods container. All supported projection methods are mounted as attributes - each attribute is a projection method class, and instantiating it creates a projection method object which holds the parameters and renders the <code style="text-indent: 0em;">PROJECTION</code> fragment of WKT (attributes: <b>name</b>, <b>pars</b>).</p>
<div class="language-python line-numbers-mode" data-highlighter="prismjs" data-ext="py" data-title="py"><pre v-pre><code><span class="line"><span class="token keyword">from</span> gma <span class="token keyword">import</span> crs</span>
<span class="line"></span>
<span class="line">method <span class="token operator">=</span> crs<span class="token punctuation">.</span>ProjMethods<span class="token punctuation">.</span>Mercator<span class="token punctuation">(</span>central_meridian <span class="token operator">=</span> <span class="token number">110</span><span class="token punctuation">)</span></span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>crs.ProjMethods.Mercator() --> <code style="text-indent: 0em;">&lt;ProjMethod:Mercator&gt;</code></p>
<h2 id="parameters" tabindex="-1"><a class="header-anchor" href="#parameters"><span>Parameters</span></a></h2>
<p>Parameters shared by projection methods. The default value of each parameter depends on the method and is shown in each method signature below.</p>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code style="text-indent: 0em;">central_meridian</code></td>
<td>The central meridian.</td>
</tr>
<tr>
<td><code style="text-indent: 0em;">false_easting</code></td>
<td>X offset from planar origin.</td>
</tr>
<tr>
<td><code style="text-indent: 0em;">false_northing</code></td>
<td>Y offset from planar origin.</td>
</tr>
<tr>
<td><code style="text-indent: 0em;">latitude_of_center</code></td>
<td>The central latitude.</td>
</tr>
<tr>
<td><code style="text-indent: 0em;">latitude_of_origin</code></td>
<td>The origin latitude.</td>
</tr>
<tr>
<td><code style="text-indent: 0em;">longitude_of_center</code></td>
<td>The central longitude.</td>
</tr>
<tr>
<td><code style="text-indent: 0em;">scale_factor</code></td>
<td>The scale factor.</td>
</tr>
<tr>
<td><code style="text-indent: 0em;">standard_parallel_1</code></td>
<td>The first standard parallels latitude of correct scale.</td>
</tr>
<tr>
<td><code style="text-indent: 0em;">standard_parallel_2</code></td>
<td>The second standard parallels latitude of correct scale.</td>
</tr>
</tbody>
</table>
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
<td><a href="#aitoff"><code v-pre>Aitoff</code></a></td>
<td>Aitoff projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><a href="#albersconicequalarea"><code v-pre>AlbersConicEqualArea</code></a></td>
<td>Albers Conic Equal Area projection method.</td>
<td><code style="text-indent: 0em;">longitude_of_center, latitude_of_center, false_easting, false_northing</code></td>
</tr>
<tr>
<td><a href="#azimuthalequidistant"><code v-pre>AzimuthalEquidistant</code></a></td>
<td>Azimuthal equidistant projection method.</td>
<td><code style="text-indent: 0em;">longitude_of_center, latitude_of_center, false_easting, false_northing</code></td>
</tr>
<tr>
<td><a href="#bonne"><code v-pre>Bonne</code></a></td>
<td>Bonne projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><a href="#cassinisoldner"><code v-pre>CassiniSoldner</code></a></td>
<td>Cassini soldner projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, latitude_of_origin, false_easting, false_northing</code></td>
</tr>
<tr>
<td><a href="#compactmiller"><code v-pre>CompactMiller</code></a></td>
<td>Compact Miller projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><a href="#cylindricalequalarea"><code v-pre>CylindricalEqualArea</code></a></td>
<td>Cylindrical equal area projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><a href="#eckerti"><code v-pre>EckertI</code></a></td>
<td>Eckert I projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><a href="#eckertii"><code v-pre>EckertII</code></a></td>
<td>Eckert II projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><a href="#eckertiii"><code v-pre>EckertIII</code></a></td>
<td>Eckert III projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><a href="#eckertiv"><code v-pre>EckertIV</code></a></td>
<td>Eckert IV projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><a href="#eckertv"><code v-pre>EckertV</code></a></td>
<td>Eckert V projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><a href="#eckertvi"><code v-pre>EckertVI</code></a></td>
<td>Eckert VI projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><a href="#equidistantconic"><code v-pre>EquidistantConic</code></a></td>
<td>Equidistant Conic projection method.</td>
<td><code style="text-indent: 0em;">longitude_of_center, latitude_of_center, false_easting, false_northing</code></td>
</tr>
<tr>
<td><a href="#equirectangular"><code v-pre>Equirectangular</code></a></td>
<td>Equirectangular projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><a href="#gallstereographic"><code v-pre>GallStereographic</code></a></td>
<td>Gall Stereographic projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><a href="#goodehomolosine"><code v-pre>GoodeHomolosine</code></a></td>
<td>Goode Homolosine projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><a href="#lambertazimuthalequalarea"><code v-pre>LambertAzimuthalEqualArea</code></a></td>
<td>Lambert Azimuthal Equal Area projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, latitude_of_center, false_easting, false_northing</code></td>
</tr>
<tr>
<td><a href="#lambertconformalconic2sp"><code v-pre>LambertConformalConic2SP</code></a></td>
<td>Lambert Conformal Conic 2SP projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, latitude_of_origin, false_easting, false_northing</code></td>
</tr>
<tr>
<td><a href="#loximuthal"><code v-pre>Loximuthal</code></a></td>
<td>Loximuthal projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, latitude_of_origin, false_easting, false_northing</code></td>
</tr>
<tr>
<td><a href="#mercator"><code v-pre>Mercator</code></a></td>
<td>Mercator 1sp projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing, scale_factor</code></td>
</tr>
<tr>
<td><a href="#mercator2sp"><code v-pre>Mercator2SP</code></a></td>
<td>Mercator 2SP projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><a href="#mollweide"><code v-pre>Mollweide</code></a></td>
<td>Mollweide projection method.</td>
<td><code style="text-indent: 0em;">longitude_of_center, false_easting, false_northing</code></td>
</tr>
<tr>
<td><a href="#naturalearth"><code v-pre>NaturalEarth</code></a></td>
<td>Natural earth projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><a href="#naturalearthii"><code v-pre>NaturalEarthII</code></a></td>
<td>Natural earth II projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><a href="#polyconic"><code v-pre>Polyconic</code></a></td>
<td>Polyconic projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, latitude_of_origin, false_easting, false_northing</code></td>
</tr>
<tr>
<td><a href="#robinson"><code v-pre>Robinson</code></a></td>
<td>Robinson projection method.</td>
<td><code style="text-indent: 0em;">longitude_of_center, false_easting, false_northing</code></td>
</tr>
<tr>
<td><a href="#sinusoidal"><code v-pre>Sinusoidal</code></a></td>
<td>Sinusoidal projection method.</td>
<td><code style="text-indent: 0em;">longitude_of_center, false_easting, false_northing</code></td>
</tr>
<tr>
<td><a href="#times"><code v-pre>Times</code></a></td>
<td>Times projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><a href="#transversemercator"><code v-pre>TransverseMercator</code></a></td>
<td>Transverse Mercator projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, latitude_of_origin, false_easting, false_northing, scale_factor</code></td>
</tr>
<tr>
<td><a href="#vandergrinten"><code v-pre>VanDerGrinten</code></a></td>
<td>Van der Grinten projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><a href="#winkeli"><code v-pre>WinkelI</code></a></td>
<td>Winkel I projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><a href="#winkelii"><code v-pre>WinkelII</code></a></td>
<td>Winkel II projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
<tr>
<td><a href="#winkeltripel"><code v-pre>WinkelTripel</code></a></td>
<td>Winkel Tripel projection method.</td>
<td><code style="text-indent: 0em;">central_meridian, false_easting, false_northing</code></td>
</tr>
</tbody>
</table>
<h3 id="aitoff" tabindex="-1"><a class="header-anchor" href="#aitoff"><span>Aitoff</span></a></h3>
<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.Aitoff</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">Aitoff</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>
<p>Aitoff projection method.</p>
<h3 id="albersconicequalarea" tabindex="-1"><a class="header-anchor" href="#albersconicequalarea"><span>AlbersConicEqualArea</span></a></h3>
<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.AlbersConicEqualArea</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">AlbersConicEqualArea</span><span style="font-style: italic; color: black;font-size: 130%;">(longitude_of_center = <span style="color:#48566B">0</span>, latitude_of_center = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>, standard_parallel_1 = <span style="color:#48566B">25</span>, standard_parallel_2 = <span style="color:#48566B">47</span>):</span></span>
<p>Albers Conic Equal Area projection method.</p>
<h3 id="azimuthalequidistant" tabindex="-1"><a class="header-anchor" href="#azimuthalequidistant"><span>AzimuthalEquidistant</span></a></h3>
<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.AzimuthalEquidistant</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">AzimuthalEquidistant</span><span style="font-style: italic; color: black;font-size: 130%;">(longitude_of_center = <span style="color:#48566B">0</span>, latitude_of_center = <span style="color:#48566B">90</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>
<p>Azimuthal equidistant projection method.</p>
<h3 id="bonne" tabindex="-1"><a class="header-anchor" href="#bonne"><span>Bonne</span></a></h3>
<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.Bonne</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">Bonne</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, standard_parallel_1 = <span style="color:#48566B">60</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>
<p>Bonne projection method.</p>
<h3 id="cassinisoldner" tabindex="-1"><a class="header-anchor" href="#cassinisoldner"><span>CassiniSoldner</span></a></h3>
<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.CassiniSoldner</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">CassiniSoldner</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, latitude_of_origin = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>
<p>Cassini soldner projection method.</p>
<h3 id="compactmiller" tabindex="-1"><a class="header-anchor" href="#compactmiller"><span>CompactMiller</span></a></h3>
<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.CompactMiller</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">CompactMiller</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>
<p>Compact Miller projection method.</p>
<h3 id="cylindricalequalarea" tabindex="-1"><a class="header-anchor" href="#cylindricalequalarea"><span>CylindricalEqualArea</span></a></h3>
<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.CylindricalEqualArea</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">CylindricalEqualArea</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, standard_parallel_1 = <span style="color:#48566B">30</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>
<p>Cylindrical equal area projection method.</p>
<h3 id="eckerti" tabindex="-1"><a class="header-anchor" href="#eckerti"><span>EckertI</span></a></h3>
<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.EckertI</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">EckertI</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>
<p>Eckert I projection method.</p>
<h3 id="eckertii" tabindex="-1"><a class="header-anchor" href="#eckertii"><span>EckertII</span></a></h3>
<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.EckertII</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">EckertII</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>
<p>Eckert II projection method.</p>
<h3 id="eckertiii" tabindex="-1"><a class="header-anchor" href="#eckertiii"><span>EckertIII</span></a></h3>
<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.EckertIII</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">EckertIII</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>
<p>Eckert III projection method.</p>
<h3 id="eckertiv" tabindex="-1"><a class="header-anchor" href="#eckertiv"><span>EckertIV</span></a></h3>
<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.EckertIV</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">EckertIV</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>
<p>Eckert IV projection method.</p>
<h3 id="eckertv" tabindex="-1"><a class="header-anchor" href="#eckertv"><span>EckertV</span></a></h3>
<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.EckertV</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">EckertV</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>
<p>Eckert V projection method.</p>
<h3 id="eckertvi" tabindex="-1"><a class="header-anchor" href="#eckertvi"><span>EckertVI</span></a></h3>
<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.EckertVI</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">EckertVI</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>
<p>Eckert VI projection method.</p>
<h3 id="equidistantconic" tabindex="-1"><a class="header-anchor" href="#equidistantconic"><span>EquidistantConic</span></a></h3>
<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.EquidistantConic</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">EquidistantConic</span><span style="font-style: italic; color: black;font-size: 130%;">(longitude_of_center = <span style="color:#48566B">0</span>, latitude_of_center = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>, standard_parallel_1 = <span style="color:#48566B">60</span>, standard_parallel_2 = <span style="color:#48566B">60</span>):</span></span>
<p>Equidistant Conic projection method.</p>
<h3 id="equirectangular" tabindex="-1"><a class="header-anchor" href="#equirectangular"><span>Equirectangular</span></a></h3>
<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.Equirectangular</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">Equirectangular</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, standard_parallel_1 = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>
<p>Equirectangular projection method.</p>
<h3 id="gallstereographic" tabindex="-1"><a class="header-anchor" href="#gallstereographic"><span>GallStereographic</span></a></h3>
<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.GallStereographic</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">GallStereographic</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>
<p>Gall Stereographic projection method.</p>
<h3 id="goodehomolosine" tabindex="-1"><a class="header-anchor" href="#goodehomolosine"><span>GoodeHomolosine</span></a></h3>
<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.GoodeHomolosine</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">GoodeHomolosine</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>
<p>Goode Homolosine projection method.</p>
<h3 id="lambertazimuthalequalarea" tabindex="-1"><a class="header-anchor" href="#lambertazimuthalequalarea"><span>LambertAzimuthalEqualArea</span></a></h3>
<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.LambertAzimuthalEqualArea</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">LambertAzimuthalEqualArea</span><span style="font-style: italic; color: black;font-size: 130%;">(longitude_of_center = <span style="color:#48566B">0</span>, latitude_of_center = <span style="color:#48566B">90</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>
<p>Lambert Azimuthal Equal Area projection method.</p>
<h3 id="lambertconformalconic2sp" tabindex="-1"><a class="header-anchor" href="#lambertconformalconic2sp"><span>LambertConformalConic2SP</span></a></h3>
<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.LambertConformalConic2SP</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">LambertConformalConic2SP</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, latitude_of_origin = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>, standard_parallel_1 = <span style="color:#48566B">60</span>, standard_parallel_2 = <span style="color:#48566B">60</span>):</span></span>
<p>Lambert Conformal Conic 2SP projection method.</p>
<h3 id="loximuthal" tabindex="-1"><a class="header-anchor" href="#loximuthal"><span>Loximuthal</span></a></h3>
<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.Loximuthal</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">Loximuthal</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, latitude_of_origin = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>
<p>Loximuthal projection method.</p>
<h3 id="mercator" tabindex="-1"><a class="header-anchor" href="#mercator"><span>Mercator</span></a></h3>
<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.Mercator</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">Mercator</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>, scale_factor = <span style="color:#48566B">1</span>):</span></span>
<p>Mercator 1sp projection method.</p>
<h3 id="mercator2sp" tabindex="-1"><a class="header-anchor" href="#mercator2sp"><span>Mercator2SP</span></a></h3>
<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.Mercator2SP</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">Mercator2SP</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, standard_parallel_1 = <span style="color:#48566B">60</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>
<p>Mercator 2SP projection method.</p>
<h3 id="mollweide" tabindex="-1"><a class="header-anchor" href="#mollweide"><span>Mollweide</span></a></h3>
<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.Mollweide</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">Mollweide</span><span style="font-style: italic; color: black;font-size: 130%;">(longitude_of_center = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>
<p>Mollweide projection method.</p>
<h3 id="naturalearth" tabindex="-1"><a class="header-anchor" href="#naturalearth"><span>NaturalEarth</span></a></h3>
<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.NaturalEarth</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">NaturalEarth</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>
<p>Natural earth projection method.</p>
<h3 id="naturalearthii" tabindex="-1"><a class="header-anchor" href="#naturalearthii"><span>NaturalEarthII</span></a></h3>
<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.NaturalEarthII</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">NaturalEarthII</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>
<p>Natural earth II projection method.</p>
<h3 id="polyconic" tabindex="-1"><a class="header-anchor" href="#polyconic"><span>Polyconic</span></a></h3>
<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.Polyconic</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">Polyconic</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, latitude_of_origin = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>
<p>Polyconic projection method.</p>
<h3 id="robinson" tabindex="-1"><a class="header-anchor" href="#robinson"><span>Robinson</span></a></h3>
<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.Robinson</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">Robinson</span><span style="font-style: italic; color: black;font-size: 130%;">(longitude_of_center = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>
<p>Robinson projection method.</p>
<h3 id="sinusoidal" tabindex="-1"><a class="header-anchor" href="#sinusoidal"><span>Sinusoidal</span></a></h3>
<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.Sinusoidal</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">Sinusoidal</span><span style="font-style: italic; color: black;font-size: 130%;">(longitude_of_center = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>
<p>Sinusoidal projection method.</p>
<h3 id="times" tabindex="-1"><a class="header-anchor" href="#times"><span>Times</span></a></h3>
<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.Times</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">Times</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>
<p>Times projection method.</p>
<h3 id="transversemercator" tabindex="-1"><a class="header-anchor" href="#transversemercator"><span>TransverseMercator</span></a></h3>
<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.TransverseMercator</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">TransverseMercator</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, latitude_of_origin = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>, scale_factor = <span style="color:#48566B">1</span>):</span></span>
<p>Transverse Mercator projection method.</p>
<h3 id="vandergrinten" tabindex="-1"><a class="header-anchor" href="#vandergrinten"><span>VanDerGrinten</span></a></h3>
<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.VanDerGrinten</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">VanDerGrinten</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>
<p>Van der Grinten projection method.</p>
<h3 id="winkeli" tabindex="-1"><a class="header-anchor" href="#winkeli"><span>WinkelI</span></a></h3>
<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.WinkelI</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">WinkelI</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, standard_parallel_1 = <span style="color:#48566B">60</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>
<p>Winkel I projection method.</p>
<h3 id="winkelii" tabindex="-1"><a class="header-anchor" href="#winkelii"><span>WinkelII</span></a></h3>
<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.WinkelII</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">WinkelII</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, standard_parallel_1 = <span style="color:#48566B">60</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>
<p>Winkel II projection method.</p>
<h3 id="winkeltripel" tabindex="-1"><a class="header-anchor" href="#winkeltripel"><span>WinkelTripel</span></a></h3>
<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.WinkelTripel</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">WinkelTripel</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, standard_parallel_1 = <span style="color:#48566B">60</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>
<p>Winkel Tripel projection method.</p>
</div></template>


