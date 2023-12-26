---
title: 初始化
date: 2023-01-10
sidebar: false
---

## gma.map.rcs.**SpatRef**(*Proj*)

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
from gma.map import rcs
SR = rcs.SpatRef('WGS84')
```

> \>>> <gma.map.rcs.SpatRef at 0x......>

**已包含的类方法/属性：**

| 类型  | 名称          | 描述                                                         | 返回值类型       |
| :----- | :------------- | :------------------------------------------ | :---------- |
| 属性     | AeraOfUse      | 坐标系使用的经纬度范围。无法识别范围的坐标系则根据中央经线自动生成最大范围         |   `list`      |
| 属性     | AngularUnits   | 角度单位值                                                  |    `float`        |
| 属性     | AngularUnitsName  |  角度单位名称                           |   `str`         |
| 属性     | EPSG    | 坐标系 EPSG 编码。没有 EPSG 编码的坐标系则值为 0          | `int`      |
| 方法     | [Export](/UserGuide/map/rcs/SpatRef/Export.html)    | 导出坐标系。支持 MICoordSys，PCI，PROJJSON，PrettyWkt，Proj4，USGS，Wkt，XML 格式      | `str` |
| 方法     | GetProjParms    | 获取坐标系的投影参数          |  `dict`       |
| 方法     | GetUseFeature    | 获取坐标系的使用区域 Feature          |  `gma.algorithm.core.dataio.Feature`       |
| 方法     | GetUseFeatureInWGS84   | 获取坐标系的使用区域 Feature（WGS84）         |    `gma.algorithm.core.dataio.Feature`         |
| 属性     | InvFlattening    | 椭球体反扁率          |    `float`         |
| 属性     | LinearUnits    | 线形单位值          |    `float`         |
| 属性     | LinearUnitsName   | 线形单位名称         |    `str`         |
| 属性     | Name    | 坐标系名称          |   `str`          |
| 属性     | PRIMEM    | 坐标系的本初子午线          |      `dict`       |
| 属性     | Proj    | WKT 格式的坐标系          |   `str`          |
| 属性     | SemiMajor   | 椭球体长半轴          |  `float`           |
| 属性     | SemiMinor   | 椭球体短半轴          |    `float`      |
| 属性     | Type   | 坐标系类型          |  `str`      |


