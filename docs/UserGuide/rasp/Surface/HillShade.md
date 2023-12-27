---
title: HillShade
date: 2022-03-20
sidebar: false
---

## gma.rasp.Surface.**HillShade**(*InFile, OutFile, OutFormat = 'GTiff', ComputeEdges = True, Band = 1, ZFactor = 1.0, Scale = 1.0, Azimuth = 315.0, Altitude = 45.0, Combined = False, ZevenbergenThorne = False*)

---

**功能：**【山体阴影】。从任何支持的 DEM 栅格文件计算山体阴影！

**参数：** 

&emsp;InFile：`str`。输入栅格路径。

&emsp;OutFile：`str`。输出栅格路径。

**可选参数：**

&emsp;OutFormat  = `str`。输出栅格文件格式。默认为 GTiff，其他格式详见 rasp.ToOtherFormat 函数。

&emsp;ComputeEdges = `bool`。是否计算栅格边缘数据和无数据值附近的数据。默认（True）是，其他设置值均视为否（False）。

&emsp;Band = `int`。需要计算的波段，编号从 1 开始。默认（1）为第一个波段。

&emsp;ZFactor = `float`。垂直放大比例。默认为 1 。

&emsp;Scale = `float`。垂直单位与水平单位的比值。默认为 1 。若垂直单位为 m 而水平单位为 °（即栅格坐标系为地理坐标系），可设置 Scale = 111120。

&emsp;Azimuth = `float`。光线方位角（°）。默认为 315 。

&emsp;Altitude = `float`。光线高度角（°）。默认为 45 。

&emsp;Combined = `bool`。是否计算混合阴影。默认不计算（False）。不为 True 的设置值均视为否（False）。

&emsp;ZevenbergenThorne = `bool`。是否改用 ZevenbergenThorne 法计算。默认（False）不使用（即采用 Horn 法计算）。不为 True 的设置均视为 Fasle。

---

**示例：**

```python
from gma import rasp

InFile = 'DEM.tif'
OutFile = 'HillShade.tif'

rasp.Surface.HillShade(InFile, OutFile, OutFormat = 'GTiff')
```

> 原始DEM与山体阴影结果：

![](/rasp/HillShade.png)