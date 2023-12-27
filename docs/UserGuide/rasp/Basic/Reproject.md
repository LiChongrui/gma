---
title: Reproject
date: 2021-10-30
sidebar: false
---

## gma.rasp.Basic.**Reproject**(*InFile, OutFile, OutProjection, InNoData = None, OutNoData = None, OutFormat = 'GTiff'*)

---

**功能：**【重投影】。将空间数据从一种坐标系投影到另一种坐标系。

**参数：** 

&emsp;InFile：`str`。输入栅格路径。

&emsp;OutFile：`str`。输出栅格路径。

&emsp;OutProjection：`str`。输出栅格坐标系（EPSG 或 wkb 格式）。

**可选参数：**

&emsp;InNoData  = `float`。输入栅格的无效值。默认自动搜索输入栅格的无效值（None）。

&emsp;OutNoData  = `float`。输出栅格的无效值。默认与 InNoData 的无效值相同（None）。

&emsp;OutFormat  = `str`。输出栅格文件格式。默认为 GTiff，其他格式详见 ToOtherFormat 函数。

---

**示例：**

```python
from gma import rasp

InFile = 'ESA_LC2020_Luoyang.tif'
OutFile = 'Reproject_6931.tif'

# 重投影到 WGS 84 / NSIDC EASE-Grid 2.0 North（EPSG:6931）
rasp.Basic.Reproject(InFile, OutFile, 6931)
```
::: tip 提示
InNoData：如果输入栅格已经定义或不含 NoData 值，则不需要配置 InNoData 值。<br>
OutNoData：如果配置了此值，输入栅格 NoData 的区域将被修改为此值。
:::

> 原始数据与重投影结果：

![](/rasp/Reproject.png)