---
title: ChangeGeometryType
date: 2022-11-12
sidebar: false
---

## gma.vesp.**ChangeGeometryType**(*InFile, OutFile, GType = 'MultiPolygon', OutFormat = 'ESRI Shapefile'*)

---

**功能：**【几何类型转换】。转换输入矢量的几何类型。

**参数：** 

&emsp;InFile：`str`。输入矢量文件路径。

&emsp;OutFile：`str`。输出矢量文件路径。

**可选参数：** 

&emsp;GType = `str`。输出几何体类型。默认为 MultiPolygon。

::: tip 支持的几何类型：

Point（点），MultiPoint（多点），Line（线），MultiLine（多线），Polygon（多边形），MultiPolygon（多多边形）。

:::

&emsp;OutFormat = `str`。输出矢量文件格式，默认为 ESRI Shapefile。其他格式详见 ToOtherFormat 函数。

---

**示例：（下载 [示例矢量](/Open/China_Province_2022.7z)）**
```python
import gma

# 多边形转线
gma.vesp.ChangeGeometryType('China_Province_2022.shp',
                            'China_Province_2022_Line.shp',
                            GType = 'Line')
```



