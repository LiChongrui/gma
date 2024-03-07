---
title: GeogCS
date: 2024-01-10
sidebar: false
---

## gma.crs.**GeogCS**(*Name='GMA GCS', AngularUnit='Degree', Primem='Greenwich', Ellipsoid='WGS84', Datum=None, AeraOfUse=None*)

---

**功能：** 创建一个自定义地理坐标系。

**可选参数：**

&emsp; Name = `str`。坐标系名称。

&emsp; AngularUnit = `str||float`。角度单位值。若为str，则必须是内置角度单位的名称。

&emsp; Primem = `str||float`。本初子午线值。若为str，则必须是内置子午线的名称。

&emsp; Ellipsoid = `str||class`。椭球体。若为 str，则必须是内置椭球体的名称；若为 class，则必须为 crs.Ellipsoid 初始化的椭球体类。

&emsp; Datum = `None||class`。基准面。若为 None，则根据椭球体自动配置基准面；若为 class，则必须为 crs.Datum 初始化的椭球体类，且 Ellipsoid 参数将被忽略。

&emsp; AeraOfUse = `None||list`。坐标系的使用范围（左、下、右、上），经纬度单位。若为None，则视为世界范围 [-180, -90, 180, 90]。

**返回：** `SpatRef`。

**示例：**

```python
from gma import crs

GCS = crs.GeogCS(Name = 'GMA GCS', AngularUnit = 'Degree', Primem = 'Greenwich', Ellipsoid = 'WGS84', 
                 Datum = None, AeraOfUse = None)
print(GCS)
```

> \>>> GEOGCS["GMA GCS",
>     DATUM["WGS84",
>         SPHEROID["WGS84",6378137,298.257223563]],
>     PRIMEM["Greenwich",0],
>     UNIT["Degree",0.0174532925199433],
>     AXIS["Longitude",EAST],
>     AXIS["Latitude",NORTH]]
