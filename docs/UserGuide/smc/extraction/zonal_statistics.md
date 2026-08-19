---
title: zonal_statistics
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.smc.extraction.zonal_statistics</p><span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[function] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">zonal_statistics</span><span style="font-style: italic; color: black;font-size: 120%;">(in_ly, in_ds, agg_fun = <span style="color:#48566B">np.sum</span>):</span></span>

<p>Statistics by region according to Features.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>in_ly</b>: <code style="text-indent: 0em;">Layer</code>. </p>
<p style="margin-left: 4em;">A gma vector layer.</p>
<p style="margin-left: 2em;"><b>in_ds</b>: <code style="text-indent: 0em;">Dataset</code>. </p>
<p style="margin-left: 4em;">A gma raster dataset.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">**Optional:</p>
<p style="margin-left: 2em;"><b>agg_fun </b> = <code style="text-indent: 0em;">def</code>. <span style="color:#48566B;"> Default np.sum</span>. </p>
<p style="margin-left: 4em;">Calculate functions. For Example:</p>

```python
def func(in_ar):
    return in_ar.mean()
agg_fun = func
```

<p style="margin-left: 4em;">in_ar: Input NumPy arrays with region shape and a masked use in_ds nodata.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">DataFrame</code>. </p>
