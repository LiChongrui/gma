---
title: Split
date: 2021-10-30
sidebar: false
---

## gma.vesp.Extraction.**Split**(*InFile, OutPath, FieldName = None, Connector = None, OutFormat = 'ESRI Shapefile'*)

---

**功能：**【矢量文件分解】。将矢量文件中的每个要素拆分为单个矢量文件。

**参数：** 

&emsp;InFile：`str`。输入矢量文件路径。

&emsp;OutPath：`str`。输出文件夹路径。

**可选参数：**

&emsp;FieldName = `str||list`。标记输出文件名的字段名称或字段名称列表。默认（None）按照 <0.shp, 1.shp, ... >的方式输出。

&emsp;Connector = `str`。多字段连接方式。默认（None）不以任何进行字段连接。

::: tip 说明

OutNameField = ["City", "Country"],  Separator = "_" 

&emsp;> > > City_County.shp

:::

&emsp;OutFormat = `str`。输出矢量文件格式，默认为 ESRI Shapefile。其他格式详见 ToOtherFormat 函数。

---


**示例：（下载 [示例矢量](/Open/China_Province_2022.7z)）**

```python
from gma import vesp

InFile = 'China_Province_2022.shp'
OutPath = 'Split'

vesp.Basic.Reproject(InFile, OutPath, OutNameField = '', Separator = '_')
```
> \>>> 安徽省_340000.shp