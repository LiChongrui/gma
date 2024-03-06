---
title: CreateFeature
date: 2023-04-04
sidebar: false
---

## io.**CreateFeature**(*GeomStrOrPoints, Type = 'Polygon', Projection = 'WGS84'*)

---

**功能：** 【从点或者几何字符创建 Feature】。

**参数：**

&emsp;GeomStrOrPoints：`list||str`。几何多边形字符串或几何顶点的 X（经度），Y（纬度）坐标。


**可选参数：**

&emsp; GeomType = `str`。生成 Feature 中几何体的类型。默认为 多边形（'Polygon'）。

::: tip 其他类型
'Point'：点； 'MultiPoint'：多点；'Line'：线；'MultiLine'：多线； 'Polygon'：多边形；'MultiPolygon'：多多边形。
:::

&emsp; Projection = `str||int`。输入坐标点的坐标系。默认为 WGS84（EPSG:4326）。

**返回：**`Feature`。

***&emsp;类内属性/方法详见：[Feature](Feature.html)。***

---

**示例**

```python
from gma import io
Points = [[112.5, 34.4], [30, 60], [2.3, 48.8], [47.5, -18.9], [112.5, 34.4]]
# 创建多边形 Feature
FPolygon = io.CreateFeature(Points, GeomType = 'Polygon')
```
> \>>> <gma.algos.dataio.veds.Feature at 0x......>