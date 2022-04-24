---
title: TRANCoordinate
date: 2021-10-30
sidebar: false
---

## gma.smc.**TRANCoordinate**(*Points, InProjection = 'WGS84', OutProjection = 'EPSG:4490'*)<Badge text="1.0.5 +"/>
---

**功能：** 【坐标转换】。将输入点的坐标转换为目标坐标系的坐标。

**参数：**

&emsp;Points：`list||tuple||array` 。需要计算距离的两点（或多点）的 X（纬度），Y（经度）坐标。如果有，也可包含 Z（高程）。可为嵌套列表或元组。

::: tip 示例

Points = [(45.2, 130.1), (40.2, 131.5)]

:::

**可选参数：**

&emsp;InProjection = `str`。输入坐标点的坐标系。默认为 WGS84（EPSG:4326）。

&emsp;OutProjection = `str`。输出坐标点的坐标系。默认为 China Geodetic Coordinate System 2000（EPSG:4490）。

**返回：**`list`。

---