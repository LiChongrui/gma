---
title: TRI
date: 2022-03-20
sidebar: false
---

## gma.raa.DEM.**TRI**(*InFile, OutFile, OutFormat = 'GTiff', ComputeEdges = True, Band = 1*)<Badge text="1.0.7 +"/>

---

**功能：**【地形耐用度指数】。从任何支持的 DEM 栅格文件计算地形耐用度指数！

**参数：** 

&emsp;InFile：`str`。输入栅格路径。

&emsp;OutFile：`str`。输出栅格路径。

**可选参数：**

&emsp;OutFormat  = `str`。输出栅格文件格式。默认为 GTiff，其他格式详见 rasp.ToOtherFormat 函数。

&emsp;ComputeEdges = `bool`。是否计算栅格边缘数据和无数据值附近的数据。默认（True）是，其他设置值均视为否（False）。

&emsp;Band = `int`。需要计算的波段，编号从 1 开始。默认（1）为第一个波段。

---

