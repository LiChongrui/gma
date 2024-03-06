---
title: CreateGeoDataBase
date: 2023-04-04
sidebar: false
---

## io.**CreateGeoDataBase**(*DBPath, Format='GPKG'*)

---

**功能：** 【创建地理数据库 GeoDataBase】。

**参数：**

&emsp;DBPath：`str`。创建地理数据库路径。

**可选参数：**

&emsp;Format   = `str`。数据库格式。默认为 GPKG。

::: tip 其他地理数据库格式

'NGW', 'S57', 'GPKG', 'KML', 'GML', 'DGN', 'ODS', 'Memory', 'LIBKML', 'PostgreSQL', 'PDF', 'SQLite', 'DXF', 'GPX', 'MSSQLSpatial', 'XLSX'

:::

**返回：**`GeoDataBase`。

***&emsp;类内属性/方法详见：[GeoDataBase](GeoDataBase.html)。***

---

**示例：** *下载 [示例矢量](/io/STLY.7z)*

```python
from gma import io, osf

GDB = io.CreateGeoDataBase('GeoDataBase.gpkg', Format = 'GPKG')

# 读取每一个 .shp 矢量数据，并将其添加到数据库中
SHPs = osf.FindPath('STLY', EXT = '.shp')
for shp in SHPs:
    Layer = io.ReadVector(shp)
    GDB.AddLayer(Layer)
```
> \>>> <gma.algos.dataio.database.GeoDataBase at 0x......>

