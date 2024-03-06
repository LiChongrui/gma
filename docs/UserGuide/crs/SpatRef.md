---
title: SpatRef
date: 2023-01-10
sidebar: false
---

## gma.crs.**SpatRef**(*Proj*)

---

**功能：** 【类】。初始化一个空间参考。

**初始化：**

&emsp; Proj：`str||int`。坐标系字符或编码。

::: tip 坐标系格式支持
EPSG，MICoordSys，PCI，PROJJSON，PrettyWkt，Proj4，USGS，Wkt，XML 或部分主要坐标系名称（例如 WGS84）。
::: 

---

**示例：**
```python
from gma import crs
SR = crs.SpatRef(4526)
```

> \>>> <gma.map.exspat.SpatRef at 0x......>

**已包含的类方法/属性：**

| 序号  | 名称          | 描述                                                         | 返回值类型       | 示例返回值  |
| :----- | :------------- | :------------------------------------------ | :---------- | ------ |
| P.1   | AeraOfUse      | 坐标系使用的经纬度范围         |   `list`      | [112.5, 21.52, 115.5, 45.45] |
| P.2   | AngularUnits   | 角度单位值，角度单位名称                                               |    `list`        | [0.017453292519943295, 'degree'] |
| P.3   | AxesCount      | 坐标系轴的数量         |   `list`      |   2     |
| P.4  | ChangeLon      | 基于此坐标系中央经线计算的变更线         |   `float`      |   1-66   |
| P.5 | DatumName      | 基准面名称         |   `str`      | 'China_2000' |
| P.6 | Info   | 坐标系参数信息         |  `DataFrame`      |        |
| P.7 | InvFlattening    | 椭球体反扁率          |    `float`         | 298.257222101 |
| P.8 | LinearUnits    | 线形单位值，线形单位名称           |    `list`         | [1.0, 'metre'] |
| P.9 | Name    | 坐标系名称          |   `str`          | 'CGCS2000 / 3-degree Gauss-Kruger zone 38' |
| P.10 | PlotAeraOfUse      | 使用此坐标系的绘图区域         |   `list`      | (112.5, 21.52, 115.5, 45.45) |
| P.11 | Primem    | 本初子午线值，本初子午线名称         |      `list`       | [0.0, 'Greenwich'] |
| P.12 | ProjMethod    | 投影方法         |      `str`       | 'Transverse_Mercator' |
| P.13 | SemiMajor   | 椭球体长半轴          |  `float`           |  6378137.0  |
| P.14 | SemiMinor   | 椭球体短半轴          |    `float`      | 6356752.314140356 |
| P.15 | SpheroidName | 椭球体名称 | `str` | 'CGCS2000' |
| P.16 | Type   | 坐标系类型          |  `str`      | 'Projected' |
| P.17 | WKID    | 坐标系编码，编码制定组织。          | `list`      | [4526, 'EPSG'] |
| M.1 | [Export](/UserGuide/map/rcs/SpatRef/Export.html)    | 导出坐标系。     | `str` |  |
| M.2 | GetProjParms    | 获取坐标系的投影参数          |  `dict`       |         |
| M.3 | GetUseFeature    | 获取坐标系的使用区域 Feature          |  `Feature`       |         |
| M.4 | GetUseFeatureInWGS84   | 获取坐标系的使用区域 Feature（WGS84）         |    `Feature`         |             |





