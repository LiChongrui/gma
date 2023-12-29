---
title: CreateLayer
date: 2023-04-04
sidebar: false
---

## io.**CreateLayer**(*\*GMAFeature, Projection = 'WGS84', GeomType = 'Polygon'*)

---

**功能：** 【从 Feature 创建 Layer】。

**参数：**

&emsp;*GMAFeature：`Feature` 。一个或多个 Feature。

**可选参数：**

&emsp; Projection = `str||int`。生成 Layer 的坐标系。所有输入 Feature 都会被重投影到此坐标系。默认为 WGS84（EPSG:4326）。

&emsp; GeomType = `str`。生成 Layer 中几何体的类型。所有输入的 Feature 都会被变换到此类型。默认为 多边形（'Polygon'）。

**返回：**`Layer`。

---

```python
from gma import io
Points = [[112.5, 34.4], [30, 60], [2.3, 48.8], [47.5, -18.9], [112.5, 34.4]]
# 创建多边形 Feature
FPolygon = io.CreateFeature(Points, GeomType = 'Polygon')
Layer = io.CreateLayer(FPolygon)
```
> \>>> <gma.algos.dataio.veds.Layer at 0x......>