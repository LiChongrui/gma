---
title: MaxMin
date: 2023-01-30
sidebar: false
---

## gma.math.Stretch.**MaxMin**(*Data, MinLabel = None, MaxLabel = None, IgnoreValue = None, MinV = None, MaxV = None*)<Badge text="1.1.3 +"/>

---

**功能：** 【最大值最小值拉伸】。以最小输出和最大输出像素值作为直方图的端点，应用线性拉伸。

**参数：** 

&emsp;Data: `array`。需要拉伸的数据。

**可选参数：**

&emsp;MinLabel = `float`。拉伸后最小值。默认为输入数组的最小值（None）。

&emsp;MaxLabel = `float`。拉伸后最大值。默认为输入数组的最大值（None）。

&emsp;IgnoreValue = `float`。不参与计算的忽略值。默认无（None）。

&emsp;MinV = `float`。拉伸最小值。默认为输入数组的最小值（None）。

&emsp;MaxV = `float`。拉伸最大值。默认为输入数组的最大值（None）。

**返回：**`array`。

---

