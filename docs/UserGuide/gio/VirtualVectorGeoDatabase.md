---
title: VirtualVectorGeoDatabase
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.gio.VirtualVectorGeoDatabase</p><span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[class] </span><span style="color: #616AE5; font-weight: bold;font-size: 150%;">VirtualVectorGeoDatabase</span><span style="font-style: italic; color: black;font-size: 130%;">(gma_lys, **kwargs):</span></span>

<p>Create a VRT GeoDatabase object!</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>gma_lys</b>: <code style="text-indent: 0em;">str||GeoDatabase||Layer||list[str/GeoDatabase/Layer]</code>. </p>
<p style="margin-left: 4em;">Layers, GeoDatabases or paths.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Optional:</p>
<p style="margin-left: 2em;"><b>**kwargs</b>: </p>
<p style="margin-left: 4em;">Other parameters passed to _algos.geo.vrt.VRTGeoDatabase.add_layer.</p>

<div class="inherit-card">
<div class="inherit-card__label">Inheritance</div>
<div class="inherit-card__body">
<p style="margin: 0 0 0.35rem;">All properties and methods of <b>VirtualVectorGeoDatabase</b> are inherited from <b>GeoDatabase</b> - they are not repeated on this page. See the parent class documentation for details.</p>
<a class="inherit-card__btn" href="/docs/UserGuide/gio/GeoDatabase.html">gma.gio.GeoDatabase &rarr;</a>
</div>
</div>

## Example

```python
from gma import gio

ly = gio.open_vector('Australia.shp')
vvgd = gio.VirtualVectorGeoDatabase([ly])    # combine Layers into a virtual GeoDatabase

print(type(vvgd).__name__, vvgd.layer_names)
print('features:', len(vvgd.get_layer(0)))
```

```text
VirtualVectorGeoDatabase ['Australia']
features: 11
```
