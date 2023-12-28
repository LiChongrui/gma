---
title: Reproject
date: 2021-10-30
sidebar: false
---

## gma.vesp.Basic.**Reproject**(*InFile, OutFile, Projection, OutFormat = 'ESRI Shapefile'*)

---

**功能：**【重投影】。将矢量数据从一种坐标系投影到另一种坐标系。

**参数：** 

&emsp;InFile：`str`。输入矢量文件路径。

&emsp;OutFile：`str`。输出矢量文件路径。

&emsp;Projection: `str||EPSG||WKT||Proj4||SpatRef||...` 。输出矢量坐标系。

**可选参数：** 

&emsp;OutFormat = `str`。输出矢量文件格式，默认为 ESRI Shapefile。其他格式详见 ToOtherFormat 函数。

---


**示例：（下载 [示例矢量](/Open/China_Province_2022.7z)）**

```python
from gma import vesp

InFile = 'China_Province_2022.shp'
OutFile = 'China_Province_2022_Reproject.shp'

# 重投影到 WGS 84 / NSIDC EASE-Grid 2.0 North（EPSF: 6931）
vesp.Basic.Reproject(InFile, OutFile, 6931)
```

> 结果对比：

![](/vesp/Reproject.png)
