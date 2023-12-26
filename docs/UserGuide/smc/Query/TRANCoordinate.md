---
title: TRANCoordinate
date: 2021-10-30
sidebar: false
---

## gma.smc.Query.**TRANCoordinate**(*Points, InProjection = 'WGS84', OutProjection = 'EPSG:4490'*)
---

**功能：** 【坐标转换】。将输入单点或多点的坐标转换为目标坐标系下的坐标。

**参数：**

&emsp;Points：`list||tuple||array` 。需要转换坐标点（或多点）的  X（经度），Y（纬度）坐标。如果有，也可包含 Z（高程）。

::: tip 示例

Points = [(130.1, 45.2), (131.5, 40.2)]

:::

**可选参数：**

&emsp;InProjection = `str`。输入坐标点的坐标系。默认为 WGS84（EPSG:4326）。

&emsp;OutProjection = `str`。输出坐标点的坐标系。默认为 China Geodetic Coordinate System 2000（EPSG:4490）。

**返回：**`array`。

---


**示例：**
```python
from gma import smc
Points =  [(130.1, 45.2), (131.5, 40.2)]
# 将输入点坐标（WGS 84 坐标系）转到 EPSG:32650（WGS 84 / UTM zone 50N）下的坐标
smc.Query.TRANCoordinate(Points, InProjection = 'WGS84', OutProjection = 'EPSG:32650')
```
> \>>> array([[1528762.07788357, 5089353.92316552], [1736214.64875059, 4552113.0446395 ]])
