---
title: Percentage
date: 2023-01-30
sidebar: false
---

## gma.math.Stretch.**Percentage**(*Data, MinLabel = None, MaxLabel = None, IgnoreValue = None, MinPER = 5, MaxPER = 95*)<Badge text="1.1.3 +"/>

---

**功能：** 【百分比截断】。以百分比处数据作为直方图的端点，应用线性拉伸。

**参数：** 

&emsp;Data: `array`。需要拉伸的数据。

**可选参数：**

&emsp;MinLabel = `float`。拉伸后最小值。默认为输入数组的最小值（None）。

&emsp;MaxLabel = `float`。拉伸后最大值。默认为输入数组的最大值（None）。

&emsp;IgnoreValue = `float`。不参与计算的忽略值。默认无（None）。

&emsp;MinPER = `float`。截断最小值百分比（0~100）。默认 5。

&emsp;MaxPER = `float`。截断最大值百分比（0~100）。默认 95。

**返回：**`array`。

---

