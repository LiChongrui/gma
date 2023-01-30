---
title: STD
date: 2023-01-30
sidebar: false
---

## gma.math.Stretch.**STD**(*Data, MinLabel = None, MaxLabel = None, IgnoreValue = None, NUMofSTD = 2*)<Badge text="1.1.3 +"/>

---

**功能：** 【标准差拉伸】。以标准差作为直方图的端点，应用线性拉伸。

**参数：** 

&emsp;Data: `array`。需要拉伸的数据。

**可选参数：**

&emsp;MinLabel = `float`。拉伸后最小值。默认为输入数组的最小值（None）。

&emsp;MaxLabel = `float`。拉伸后最大值。默认为输入数组的最大值（None）。

&emsp;IgnoreValue = `float`。不参与计算的忽略值。默认无（None）。

&emsp;NUMofSTD = `float`。标准差数量。

::: tip 提示
在 均值 ± 标准差 * 标准差数量 之内的数据将被拉伸，之外的数据将被赋值为 均值 ± 标准差 * 标准差数量。
:::

**返回：**`array`。

---

