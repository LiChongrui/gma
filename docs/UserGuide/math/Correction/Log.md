---
title: Log
date: 2023-01-30
sidebar: false
---

## gma.math.Correction.**Log**(*Data, Constant = 1, IgnoreValue = None, Inverse = False*)<Badge text="1.1.3 +"/>

---

**功能：** 【对数变换】。对输入数组进行对数函数变换。

::: tip 参考公式
Out = log2(1 + (Data - Min) / RangeV) * RangeV * Constant
:::

**参数：** 

&emsp;Data: `array`。需要矫正的数据。

**可选参数：**

&emsp;Constant = `float`。变换常量。默认为 1。

&emsp;IgnoreValue = `float`。不参与计算的忽略值。默认无（None）。

&emsp;Inverse = `bool`。是否进行逆变化。默认不进行逆变化（False）。

**返回：**`array`。

---

