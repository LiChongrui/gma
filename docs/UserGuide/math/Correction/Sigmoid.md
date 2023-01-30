---
title: Sigmoid
date: 2023-01-30
sidebar: false
---

## gma.math.Correction.**Sigmoid**(*Data, Constant = 1, IgnoreValue = None, Inverse = False, Cutoff = 0.5*)<Badge text="1.1.3 +"/>

---

**功能：** 【S型曲线函数变换】。对输入数组进行的S型曲线函数变换。

::: tip 参考公式
Out = 1 / (1 + exp(Constant * (Cutoff - (Data - Min) / RangeV))) * RangeV
:::

**参数：** 

&emsp;Data: `array`。需要矫正的数据。

**可选参数：**

&emsp;Constant = `float`。变换常量。默认为 1。

&emsp;IgnoreValue = `float`。不参与计算的忽略值。默认无（None）。

&emsp;Inverse = `bool`。是否进行逆变化。默认不进行逆变化（False）。

&emsp;Cutoff = `float`。S型曲线的截点。默认为中点（0.5）。

**返回：**`array`。

---

