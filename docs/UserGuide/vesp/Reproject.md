---
title: Reproject
date: 2021-10-30
sidebar: false
---

## gma.vesp.**Reproject**(*InFile, OutFile, Projection, OutFormat = 'ESRI Shapefile'*)

---

**功能：**【重投影】。将矢量数据从一种坐标系投影到另一种坐标系。

**参数：** 

&emsp;InFile：`str`。输入矢量文件路径。

&emsp;OutFile：`str`。输出矢量文件路径。

&emsp;Projection: `str`。输出矢量坐标系（EPSG 或 wkb 格式）。

**可选参数：** 

&emsp;OutFormat = `str`。输出矢量文件格式，默认为 ESRI Shapefile。其他格式详见 ToOtherFormat 函数。

---

