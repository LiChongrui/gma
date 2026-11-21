---
title: NDVI
date: 2026-08-15
---

<p style="font-size: 120%;font-weight: bold;">gma.rsvi.NDVI</p><span style="background-color:#F4F4F5;display: block;line-height:1.5;border-radius: 0.3rem;"><span style="color: gray;font-size:90%;">[function] </span><span style="color: #616AE5; font-weight: bold;font-size: 125%;">NDVI</span><span style="font-style: italic; color: black;font-size: 120%;">(red, nir):</span></span>

<p>Calculate the Normalized Differnce Vegetation Index.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Parameters:</p>
<p style="margin-left: 2em;"><b>red</b>: <code style="text-indent: 0em;">array</code>. </p>
<p style="margin-left: 4em;">Red-infrared band data.</p>
<p style="margin-left: 2em;"><b>nir</b>: <code style="text-indent: 0em;">array</code>. </p>
<p style="margin-left: 4em;">Near-infrared band data.</p>
<p style="font-size: 120%;color:#9298ED; font-weight: bold;">Returns:</p>
<p style="margin-left: 2em;"><b>Type</b>: <code style="text-indent: 0em;">array</code>. </p>

## Example

```python
import numpy as np
from gma import rsvi

# Simulated surface reflectance (0-1) of the red and nir bands
red = np.random.uniform(0.05, 0.5, (512, 512)).astype('float32')
nir = np.random.uniform(0.1, 0.6, (512, 512)).astype('float32')

# Calculate the Normalized Difference Vegetation Index
ndvi = rsvi.NDVI(red, nir)
```
