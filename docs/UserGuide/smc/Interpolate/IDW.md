---
title: IDW
date: 2022-10-06
sidebar: false
---

## gma.smc.interpolate.**IDW**(*Points, Values, Boundary = None, Resolution = None, Power = 2, SearchRadius = 12*, InProjection = 'WGS84')<Badge text="1.1.0 +"/>
---

**功能：** 【反距离权重插值】。使用反距离加权法（IDW）将点插值成二维数组。

**参数：**

&emsp;Points：`list||tuple||array` 。插值点 X（经度），Y（纬度）坐标，且必须为经纬度坐标。可为嵌套列表或元组，至少有 2 个坐标点。

&emsp;Values：`array`。坐标点对应的数据值，与 Points 数量相同。

**可选参数：**

&emsp;Boundary = `tuple`。插值结果的四至边界，分别为最小经度（左）、最小纬度（下）、最大经度（右）、最大纬度（上）。默认（None）从输入坐标点提取范围。

&emsp;Resolution = `float`。插值结果的分辨率。默认（None）为 Boundary 经度、纬度差最小值的十分之一。

&emsp;Power = `float`。距离指数（幂）。用来控制插值周围点的显著性，默认为 2。

&emsp;SearchRadius = `int`。搜索范围。指定要用于执行插值的最邻近输入采样点数量，默认为 12 个点。

&emsp;InProjection = `str`。输入坐标点的坐标系。默认为 WGS84（EPSG:4326）。

**返回：** 类型：`namedtuple`。包含数据（Data）和仿射变换（Transform）。

---

