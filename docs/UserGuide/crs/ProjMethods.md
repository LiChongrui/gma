---
title: ProjMethods
date: 2026-11-20
---

<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[const] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">ProjMethods</span></span>

<p>The projection methods container. All supported projection methods are mounted as attributes - each attribute is a projection method class, and instantiating it creates a projection method object which holds the parameters and renders the <code style="text-indent: 0em;">PROJECTION</code> fragment of WKT (attributes: <b>name</b>, <b>pars</b>).</p>

```python
from gma import crs

method = crs.ProjMethods.Mercator(central_meridian = 110)
```

<p>crs.ProjMethods.Mercator() --> <code style="text-indent: 0em;">&lt;ProjMethod:Mercator&gt;</code></p>

## Parameters

<p>Parameters shared by projection methods. The default value of each parameter depends on the method and is shown in each method signature below. Values outside the range raise an error.</p>

| Parameter | Range | Description |
| --- | --- | --- |
| <code style="text-indent: 0em;">central_meridian</code> | [-180°, 180°] | The central meridian. |
| <code style="text-indent: 0em;">false_easting</code> | — | X offset from planar origin. |
| <code style="text-indent: 0em;">false_northing</code> | — | Y offset from planar origin. |
| <code style="text-indent: 0em;">latitude_of_center</code> | [-90°, 90°] | The central latitude. |
| <code style="text-indent: 0em;">latitude_of_origin</code> | [-90°, 90°] | The origin latitude. |
| <code style="text-indent: 0em;">longitude_of_center</code> | [-180°, 180°] | The central longitude. |
| <code style="text-indent: 0em;">scale_factor</code> | — | The scale factor. |
| <code style="text-indent: 0em;">standard_parallel_1</code> | [-90°, 90°] | The first standard parallels latitude of correct scale. |
| <code style="text-indent: 0em;">standard_parallel_2</code> | [-90°, 90°] | The second standard parallels latitude of correct scale. |

### Aitoff

<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.Aitoff</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">Aitoff</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>

<p>Aitoff projection method.</p>

### AlbersConicEqualArea

<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.AlbersConicEqualArea</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">AlbersConicEqualArea</span><span style="font-style: italic; color: black;font-size: 130%;">(longitude_of_center = <span style="color:#48566B">0</span>, latitude_of_center = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>, standard_parallel_1 = <span style="color:#48566B">25</span>, standard_parallel_2 = <span style="color:#48566B">47</span>):</span></span>

<p>Albers Conic Equal Area projection method.</p>

### AzimuthalEquidistant

<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.AzimuthalEquidistant</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">AzimuthalEquidistant</span><span style="font-style: italic; color: black;font-size: 130%;">(longitude_of_center = <span style="color:#48566B">0</span>, latitude_of_center = <span style="color:#48566B">90</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>

<p>Azimuthal equidistant projection method.</p>

### Bonne

<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.Bonne</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">Bonne</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, standard_parallel_1 = <span style="color:#48566B">60</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>

<p>Bonne projection method.</p>

### CassiniSoldner

<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.CassiniSoldner</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">CassiniSoldner</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, latitude_of_origin = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>

<p>Cassini soldner projection method.</p>

### CompactMiller

<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.CompactMiller</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">CompactMiller</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>

<p>Compact Miller projection method.</p>

### CylindricalEqualArea

<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.CylindricalEqualArea</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">CylindricalEqualArea</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, standard_parallel_1 = <span style="color:#48566B">30</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>

<p>Cylindrical equal area projection method.</p>

### EckertI

<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.EckertI</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">EckertI</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>

<p>Eckert I projection method.</p>

### EckertII

<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.EckertII</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">EckertII</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>

<p>Eckert II projection method.</p>

### EckertIII

<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.EckertIII</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">EckertIII</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>

<p>Eckert III projection method.</p>

### EckertIV

<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.EckertIV</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">EckertIV</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>

<p>Eckert IV projection method.</p>

### EckertV

<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.EckertV</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">EckertV</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>

<p>Eckert V projection method.</p>

### EckertVI

<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.EckertVI</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">EckertVI</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>

<p>Eckert VI projection method.</p>

### EquidistantConic

<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.EquidistantConic</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">EquidistantConic</span><span style="font-style: italic; color: black;font-size: 130%;">(longitude_of_center = <span style="color:#48566B">0</span>, latitude_of_center = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>, standard_parallel_1 = <span style="color:#48566B">60</span>, standard_parallel_2 = <span style="color:#48566B">60</span>):</span></span>

<p>Equidistant Conic projection method.</p>

### Equirectangular

<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.Equirectangular</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">Equirectangular</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, standard_parallel_1 = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>

<p>Equirectangular projection method.</p>

### GallStereographic

<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.GallStereographic</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">GallStereographic</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>

<p>Gall Stereographic projection method.</p>

### GoodeHomolosine

<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.GoodeHomolosine</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">GoodeHomolosine</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>

<p>Goode Homolosine projection method.</p>

### LambertAzimuthalEqualArea

<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.LambertAzimuthalEqualArea</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">LambertAzimuthalEqualArea</span><span style="font-style: italic; color: black;font-size: 130%;">(longitude_of_center = <span style="color:#48566B">0</span>, latitude_of_center = <span style="color:#48566B">90</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>

<p>Lambert Azimuthal Equal Area projection method.</p>

### LambertConformalConic2SP

<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.LambertConformalConic2SP</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">LambertConformalConic2SP</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, latitude_of_origin = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>, standard_parallel_1 = <span style="color:#48566B">60</span>, standard_parallel_2 = <span style="color:#48566B">60</span>):</span></span>

<p>Lambert Conformal Conic 2SP projection method.</p>

### Loximuthal

<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.Loximuthal</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">Loximuthal</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, latitude_of_origin = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>

<p>Loximuthal projection method.</p>

### Mercator

<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.Mercator</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">Mercator</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>, scale_factor = <span style="color:#48566B">1</span>):</span></span>

<p>Mercator 1sp projection method.</p>

### Mercator2SP

<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.Mercator2SP</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">Mercator2SP</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, standard_parallel_1 = <span style="color:#48566B">60</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>

<p>Mercator 2SP projection method.</p>

### Mollweide

<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.Mollweide</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">Mollweide</span><span style="font-style: italic; color: black;font-size: 130%;">(longitude_of_center = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>

<p>Mollweide projection method.</p>

### NaturalEarth

<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.NaturalEarth</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">NaturalEarth</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>

<p>Natural earth projection method.</p>

### NaturalEarthII

<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.NaturalEarthII</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">NaturalEarthII</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>

<p>Natural earth II projection method.</p>

### Polyconic

<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.Polyconic</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">Polyconic</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, latitude_of_origin = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>

<p>Polyconic projection method.</p>

### Robinson

<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.Robinson</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">Robinson</span><span style="font-style: italic; color: black;font-size: 130%;">(longitude_of_center = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>

<p>Robinson projection method.</p>

### Sinusoidal

<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.Sinusoidal</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">Sinusoidal</span><span style="font-style: italic; color: black;font-size: 130%;">(longitude_of_center = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>

<p>Sinusoidal projection method.</p>

### Times

<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.Times</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">Times</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>

<p>Times projection method.</p>

### TransverseMercator

<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.TransverseMercator</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">TransverseMercator</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, latitude_of_origin = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>, scale_factor = <span style="color:#48566B">1</span>):</span></span>

<p>Transverse Mercator projection method.</p>

### VanDerGrinten

<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.VanDerGrinten</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">VanDerGrinten</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>

<p>Van der Grinten projection method.</p>

### WinkelI

<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.WinkelI</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">WinkelI</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, standard_parallel_1 = <span style="color:#48566B">60</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>

<p>Winkel I projection method.</p>

### WinkelII

<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.WinkelII</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">WinkelII</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, standard_parallel_1 = <span style="color:#48566B">60</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>

<p>Winkel II projection method.</p>

### WinkelTripel

<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.WinkelTripel</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">WinkelTripel</span><span style="font-style: italic; color: black;font-size: 130%;">(central_meridian = <span style="color:#48566B">0</span>, standard_parallel_1 = <span style="color:#48566B">60</span>, false_easting = <span style="color:#48566B">0</span>, false_northing = <span style="color:#48566B">0</span>):</span></span>

<p>Winkel Tripel projection method.</p>
