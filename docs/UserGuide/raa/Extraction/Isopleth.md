---
title: Isopleth
date: 2022-09-26
sidebar: false
---

## gma.raa.Extraction.**Isopleth**(*InFile, OutFile, Band = 1, Interval = 50, Base = 0, OutFormat = 'ESRI Shapefile'*)<Badge text="1.0.13 +"/>

---

**功能：** 【等值线】。生成数量指标值相等的各点连成的平滑曲线。

**参数：** 

&emsp;InFile：`str`。输入栅格路径。

&emsp;OutFile：`str`。输出栅格路径。

**可选参数：**

&emsp;Band = `int`。需要计算的波段，编号从 1 开始。默认（1）为第一个波段。

&emsp;Interval = `float`。等值线间隔。默认为 50。

&emsp;Base = `float`。相对于间隔起始零点的偏移量。默认为 0。

&emsp;OutFormat = `str`。输出文件格式，默认为 ESRI Shapefile。其他格式详见 vesp.ToOtherFormat 函数。

---

