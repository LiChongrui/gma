---
title: CreateFeatureFromPoints
date: 2023-04-04
sidebar: false
---

## io.**CreateFeatureFromPoints**(*Points, Type = 'Polygon', Projection = 'WGS84', FieldsDefn = {}*)<Badge text="1.1.5 +"/> 

---

**功能：** 【从点创建 Feature】。

**参数：**

&emsp;Points：`list` 。几何顶点的 X（经度），Y（纬度）坐标。

::: warning 注意
此处必须为 列表（list）!
:::

**可选参数：**

&emsp; Type = `str`。生成 Feature 中几何体的类型。默认为 多边形（'Polygon'）。

::: tip 其他类型
'Point'：点； 'MultiPoint'：多点；'Line'：线；'MultiLine'：多线； 'Polygon'：多边形；'MultiPolygon'：多多边形。
:::

&emsp; Projection = `str||int`。输入坐标点的坐标系。默认为 WGS84（EPSG:4326）。

&emsp; FieldsDefn = `dict`。定义属性字段的名称及其对应的数据类型。默认为空（{}）。

::: tip 示例
FieldsDefn =             {
                Field Name:
                {
                    'Data Type Code': int,
                    'Precision': int, 
                    'Width': int
                    }
                }
:::
**返回：**`Feature`。

---

**示例**

```python
from gma import io
Points = [[112.5, 34.4], [30, 60], [2.3, 48.8], [47.5, -18.9], [112.5, 34.4]]
# 创建多边形 Feature
FPolygon = io.CreateFeatureFromPoints(Points, Type = 'Polygon')
```
> \>>> <gma.algorithm.core.dataio.Feature at 0x......>