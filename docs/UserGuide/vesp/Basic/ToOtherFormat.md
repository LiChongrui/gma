---
title: ToOtherFormat
date: 2021-10-30
sidebar: false
---

## gma.vesp.Basic.**ToOtherFormat**(*InFile, OutFile, OutFormat = 'ESRI Shapefile'*)

---

**功能：**【格式转换】。一种矢量格式转换为另一种矢量格式。

**参数：** 

&emsp;InFile：`str`。输入矢量文件路径。

&emsp;OutFile：`str`。输出矢量文件路径。

**可选参数：** 

&emsp;OutFormat = `str`。输出矢量文件格式，默认为 ESRI Shapefile。

::: tip 其他支持格式

ESRI Shapefile，PCIDSK，PDS4，PDF，MBTiles，MapInfo File，Memory，CSV，GML，LIBKML，KML，GeoJSON，OGR_GMT，GPKG，SQLite，WAsP，FlatGeobuf，Geoconcept，GeoRSS，ODS， XLSX，JML，VDV，MVT，MapML。

:::

---

**示例：（下载 [示例矢量](/Open/China_Province_2022.7z)）**

```python
from gma import vesp

# 多边形转线
InFile = 'China_Province_2022.shp'
OutFile = 'China_Province_2022_ToOtherFormat.gpkg'

# 转换为 GPKG 文件
vesp.Basic.ToOtherFormat(InFile, OutFile, OutFormat = 'GPKG')
```