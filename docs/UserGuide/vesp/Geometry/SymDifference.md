---
title: SymDifference
date: 2021-10-30
sidebar: false
---

## gma.vesp.Geometry.**SymDifference**(*InFile, MethodFile, OutFile, OutFormat = 'ESRI Shapefile'*)

---

**功能：**【交集取反】。取两个矢量不相交的部分。

**参数：** 

&emsp;InFile：`str`。第一个矢量文件路径。

&emsp;MethodFile：`str`。第二个矢量文件路径。

&emsp;OutFile：`str`。输出矢量文件路径。

**可选参数：** 

&emsp;OutFormat = `str`。输出矢量文件格式，默认为 ESRI Shapefile。其他格式详见 ToOtherFormat 函数。

---

**示例：（下载 [示例矢量](/Open/China_Province_2022.7z)）**

```python
from gma import vesp

InFile = 'China_Province_2022.shp'
MethodFile = 'Method_Vector.shp'
OutFile = 'SymDifference.shp'

vesp.Geometry.SymDifference(InFile, MethodFile, OutFile)
```

> 结果对比：

![](/vesp/SymDifference.png)