---
title: Gamma
date: 2023-01-30
sidebar: false
---

## gma.math.Correction.**Gamma**(*Data, Constant = 1, IgnoreValue = None, GammaV = 1*)<Badge text="1.1.3 +"/>

---

**功能：** 【Gamma 变换】。对输入数组进行 gamma 函数变换。

::: tip 参考公式
Out = Constant * ((Data - Min) / RangeV) ** GammaV) * RangeV
:::


**参数：** 

&emsp;Data: `array`。需要矫正的数据。

**可选参数：**

&emsp;Constant = `float`。变换常量。默认为 1。

&emsp;IgnoreValue = `float`。不参与计算的忽略值。默认无（None）。

&emsp;GammaV = `float`。伽马值。默认为 1。

::: warning 注意
如果输入数据类型为 uint8，则将数据将在 0 ~ 255 之间进行变换。否则，将在输入数组的最大值、最小值之间变换。
:::

**返回：**`array`。

---

