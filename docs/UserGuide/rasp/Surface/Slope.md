---
title: Slope
date: 2022-03-20
sidebar: false
---

## gma.raa.DEM.**Slope**(*InFile, OutFile, OutFormat = 'GTiff', ComputeEdges = True, Band = 1, Scale = 1.0, UseDegree = True, ZevenbergenThorne = False*)<Badge text="1.0.7 +"/>

---

**功能：**【坡度】。从任何支持的 DEM 栅格文件计算坡度！

**参数：** 

&emsp;InFile：`str`。输入栅格路径。

&emsp;OutFile：`str`。输出栅格路径。

**可选参数：**

&emsp;OutFormat  = `str`。输出栅格文件格式。默认为 GTiff，其他格式详见 rasp.ToOtherFormat 函数。

&emsp;ComputeEdges = `bool`。是否计算栅格边缘数据和无数据值附近的数据。默认（True）是，其他设置值均视为否（False）。

&emsp;Band = `int`。需要计算的波段，编号从 1 开始。默认（1）为第一个波段。

&emsp;Scale = `float`。垂直单位与水平单位的比值。默认为 1 。若垂直单位为 m 而水平单位为 °（即栅格坐标系为地理坐标系），可设置 Scale = 111120。

&emsp;UseDegree = `bool`。是否使用度（°）来表示坡度。默认（True）使用。若为否（False），则采用百分比（%）表示坡度。

&emsp;ZevenbergenThorne = `bool`。是否改用 ZevenbergenThorne 法计算。默认（False）不使用（即采用 Horn 法计算）。不为 True 的设置均视为 Fasle。

---

