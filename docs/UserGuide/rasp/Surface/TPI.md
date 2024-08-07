---
title: TPI
date: 2022-03-20
sidebar: false
---

##  gma.rasp.Surface.**TPI**(*InFile, OutFile, OutFormat = 'GTiff', ComputeEdges = True, Band = 0*)

---

**功能：**【地形位置指数】。从任何支持的 DEM 栅格文件计算地形位置指数！

**参数：** 

&emsp;InFile：`str`。输入栅格路径。

&emsp;OutFile：`str`。输出栅格路径。

**可选参数：**

&emsp;OutFormat  = `str`。输出栅格文件格式。默认为 GTiff，其他格式详见 rasp.ToOtherFormat 函数。

&emsp;ComputeEdges = `bool`。是否计算栅格边缘数据和无数据值附近的数据。默认（True）是，其他设置值均视为否（False）。

&emsp;Band = `int`。需要计算的波段，编号从 0 开始。默认（0）为第一个波段。

---

**示例：**

```python
from gma import rasp

InFile = 'DEM.tif'
OutFile = 'TPI.tif'

rasp.Surface.TPI(InFile, OutFile, OutFormat = 'GTiff')
```

> 原始DEM与地形位置指数结果：

![](/rasp/TPI.png)