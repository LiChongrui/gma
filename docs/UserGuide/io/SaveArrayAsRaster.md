---
title: SaveArrayAsRaster
date: 2021-10-30
sidebar: false
---

## io.**SaveArrayAsRaster**(*Array, OutFile, Projection = None, Transform = None, DataType = None, NoData = None, Format = 'GTiff'*)

---

**功能：**【写出栅格】。将数组保存为栅格文件。

**参数：** 

&emsp;Array：`array`。输入数组。

&emsp;OutFile：`str`。输出栅格路径。

**可选参数：**

&emsp;Projection  = `str||EPSG||WKT||Proj4||SpatRef||...`。输出栅格坐标系。默认不指定坐标系（None）。

&emsp;Transform  = `tuple`。输出栅格的仿射变换。默认不指定仿射变换（None）。

&emsp;DataType  = `int||str`。输出栅格数据类型的代码或字符串标记。默认根据写出数组的数据类型确定（None），其他类型详见 rasp.Basic.ChangeDataType 函数。

&emsp;NoData = `float`。输出栅格的无效值。默认不设置无效值（None）。

&emsp;Format   = `str`。输出栅格文件格式。默认为 GTiff。其他格式详见 rasp.Basic.ToOtherFormat 函数。

---

