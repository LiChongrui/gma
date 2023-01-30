---
title: HistEqualize
date: 2023-01-30
sidebar: false
---

## gma.math.Stretch.**HistEqualize**(*Data, MinLabel = None, MaxLabel = None, IgnoreValue = None, Bins = 256*)<Badge text="1.1.3 +"/>

---

**功能：** 【直方图均衡化】。通过改变图像的直方图来改变图像中各像素的灰度。

**参数：** 

&emsp;Data: `array`。需要拉伸的数据。

**可选参数：**

&emsp;MinLabel = `float`。拉伸后最小值。默认为输入数组的最小值（None）。

&emsp;MaxLabel = `float`。拉伸后最大值。默认为输入数组的最大值（None）。

&emsp;IgnoreValue = `float`。不参与计算的忽略值。默认无（None）。

&emsp;Bins = `int`。直方图数量。默认 256 个。

**返回：**`array`。

---

