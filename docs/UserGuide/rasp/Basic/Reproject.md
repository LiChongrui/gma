---
title: Reproject
date: 2021-10-30
sidebar: false
---

## gma.rasp.**Reproject**(*InFile, OutFile, OutProjection, InNoData = None, OutNoData = None, OutFormat = 'GTiff'*)

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

