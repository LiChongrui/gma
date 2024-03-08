---
title: ToVector
date: 2021-10-30
sidebar: false
---

## gma.rasp.Extraction.**ToVector**(*InFile, OutVector, FieldName = 'Value', Band = 0, GeomType = 'Polygon', OutFormat = 'ESRI Shapefile'*)

---

**功能：**【栅格转矢量】。将栅格数据转换为矢量数据。

**参数：** 

&emsp;InFile：`str`。输入栅格路径。

&emsp;OutVector：`str`。输出矢量路径。

**可选参数：**

&emsp;FieldName  = `str`。输出矢量字段的名称。默认为 Value。

&emsp;Band  = `int`。要转换的波段。默认转换第一个波段（0）。

&emsp;GeomType = `str`。矢量几何类型。默认为多边形（'Polygon'）。

&emsp;OutFormat   = `str`。输出矢量文件格式，默认为 ESRI Shapefile。其他格式详见 vesp.ToOtherFormat 函数。

---

**示例：**

```python
from gma import rasp

InFile = 'ESA_LC2020_TT.tif'
OutFile = 'ToVector.shp'
rasp.Extraction.ToVector(InFile, OutFile, GeomType = 'Polygon')
```

> 原始数据与转为矢量后数据对比：

![](/rasp/ToVector.png)
