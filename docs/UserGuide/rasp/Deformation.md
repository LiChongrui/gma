---
title: Deformation
date: 2021-10-30
sidebar: false
---

## gma.rasp.**Deformation**(*InFiles, OutFile, CutLineFile = None, ResampleMethod = 0, Resolution = None, OutProjection = 'WGS84',  InNoData = None, OutNoData = None, OutFormat = 'GTiff'*)

---

**功能：**【流程化处理】。完成镶嵌-裁剪-重采样-重投影-格式转换等其中一个或多个功能。

**参数：** 

&emsp;InFiles：`str||list`。输入栅格路径。如果为列表，则列表内所有的栅格将被 镶嵌。

&emsp;OutFile：`str`。输出栅格路径。

**可选参数：**

&emsp;CutLineFile  = `str`。裁剪矢量文件路径。如果有，将用此 矢量文件 裁剪输出栅格。

&emsp;Resolution  = `float`。重采样分辨率。设置重采样分辨率。

&emsp;ResampleMethod  = `int||str`。重采样方法。默认为 Nearest Neighbour 法（0）。其他重采样方法详见 Resample 函数。

&emsp;OutProjection = `str`。输出栅格坐标系名称。输出栅格坐标系（EPSG 、 wkb 或 坐标名称）。

&emsp;InNoData  = `float`。输出无效值。输出栅格的无效值。

&emsp;OutNoData  = `float`。输出无效值。默认与 InNoData 的无效值相同（None）。

&emsp;OutFormat   = `str`。输出栅格文件格式。默认为 GTiff，其他格式详见 ToOtherFormat 函数。

---

