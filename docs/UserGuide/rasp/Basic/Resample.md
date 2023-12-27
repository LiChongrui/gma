---
title: Resample
date: 2021-10-30
sidebar: false
---

## gma.rasp.Basic.**Resample**(*InFile, OutFile, Resolution, Method = 2, InNoData = None, OutNoData = None, OutFormat = 'GTiff'*)

---

**功能：**【重采样】。更改栅格数据的空间分辨率。

**参数：** 

&emsp;InFile：`str`。输入栅格路径。

&emsp;OutFile：`str`。输出栅格路径。

&emsp;Resolution：`float`。重采样分辨率。

**可选参数：**

&emsp;Method = `int||str`。重采样方法。默认为 Cubic 法（2）。

::: tip 支持的重采样方法

0: Nearest Neighbour，1: Bilinear，2: Cubic，3: CubicSpline，4: Lanczos，5: Average，6: RMS，7: Mode

:::

&emsp;InNoData  = `float`。输入栅格的无效值。默认自动搜索输入栅格的无效值（None）。

&emsp;OutNoData  = `float`。输出栅格的无效值。默认与 InNoData 的无效值相同（None）。

&emsp;OutFormat  = `str`。输出栅格文件格式。默认为 GTiff，其他格式详见 ToOtherFormat 函数。

---

**示例：**

```python
from gma import rasp

InFile = 'ESA_LC2020_Luoyang.tif'
OutFile = 'Resample.tif'

# 重采样到 0.01°
rasp.Basic.Resample(InFile, OutFile, Resolution = 0.01)
```

> 原始数据与重采样结果：

![](/rasp/Resample.png)