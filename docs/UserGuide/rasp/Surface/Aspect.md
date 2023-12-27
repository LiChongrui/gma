---
title: Aspect
date: 2022-03-20
sidebar: false
---

## gma.rasp.Surface.**Aspect**(*InFile, OutFile, OutFormat = 'GTiff', ComputeEdges = True, Band = 1,  ZevenbergenThorne = False, Trigonometric = False, ZeroForFlat = False*)

---

**功能：**【坡向】。从任何支持的 DEM 栅格文件计算坡向！

**参数：** 

&emsp;InFile：`str`。输入栅格路径。

&emsp;OutFile：`str`。输出栅格路径。

**可选参数：**

&emsp;OutFormat  = `str`。输出栅格文件格式。默认为 GTiff，其他格式详见 rasp.ToOtherFormat 函数。

&emsp;ComputeEdges = `bool`。是否计算栅格边缘数据和无数据值附近的数据。默认（True）是，其他设置值均视为否（False）。

&emsp;Band = `int`。需要计算的波段，编号从 1 开始。默认（1）为第一个波段。

&emsp;ZevenbergenThorne = `bool`。是否改用 ZevenbergenThorne 法计算。默认（False）不使用（即采用 Horn 法计算）。不为 True 的设置均视为 Fasle。

&emsp;Trigonometric = `bool`。是否使用（三角）角度。默认（False）不使用（即使用方位角）。不为 True 的设置均视为 Fasle。

::: tip 提示

方位角角度：以正北方向为 0°，依顺时针方向到目标方向线之间的水平夹角。</br>（三角）角度：以正东方向为 0°。依逆时针针方向到目标方向线之间的水平夹角。

:::

&emsp;ZeroForFlat = `bool`。是否将坡向为 0°的的区域赋值为 0。默认不赋值为 0 （即赋值为 NoData(-9999)）。不为 True 的设置均视为 Fasle。

---

**示例：**

```python
from gma import rasp

InFile = 'DEM.tif'
OutFile = 'Aspect.tif'

rasp.Surface.Aspect(InFile, OutFile, OutFormat = 'GTiff')
```

> 原始DEM与坡向结果：

![](/rasp/Aspect.png)