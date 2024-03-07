---
title: ProjCS
date: 2024-01-10
sidebar: false
---

## gma.crs.**ProjCS**(*Name='GMA PCS', LinearUnit='Meter', ProjMethod = 'AlbersConicEqualArea', GCS='WGS84', AeraOfUse=None*)

---

**功能：** 创建一个自定义投影坐标系。

**可选参数：**

&emsp; Name = `str`。坐标系名称。

&emsp; LinearUnit = `str||float`。线性单位。若为 str，则必须是内置线性单位的名称。

&emsp; ProjMethod = `str||class`。投影方法。若为 str，则必须是内置投影方法中的类名称。若为 class，则必须为 crs.ProjMethod 下自定义的投影方法。

&emsp; GCS = `str||int||class`。地理坐标系。可为 EPSG，WKT，Proj4，空间参考类或其他任何可识别坐标系。

&emsp; AeraOfUse = `None||list`。坐标系的使用范围（左、下、右、上），经纬度单位。若为 None，则视为世界范围 [-180, -90, 180, 90]。

**返回：** `SpatRef`。

**示例：**

```python
from gma import crs

PCS = crs.ProjCS(Name = 'GMA PCS', LinearUnit = 'Meter', ProjMethod = 'AlbersConicEqualArea', 
                 GCS = 'WGS84', AeraOfUse = None)
print(GCS)
```

> \>>> PROJCS["GMA PCS",
>     GEOGCS["WGS 84",
>         DATUM["WGS_1984",
>             SPHEROID["WGS 84",6378137,298.257223563,
>                 AUTHORITY["EPSG","7030"]],
>             AUTHORITY["EPSG","6326"]],
>         PRIMEM["Greenwich",0,
>             AUTHORITY["EPSG","8901"]],
>         UNIT["degree",0.0174532925199433,
>             AUTHORITY["EPSG","9122"]],
>         AUTHORITY["EPSG","4326"]],
>     PROJECTION["Albers_Conic_Equal_Area"],
>     PARAMETER["longitude_of_center",0],
>     PARAMETER["latitude_of_center",0],
>     PARAMETER["false_easting",0],
>     PARAMETER["false_northing",0],
>     PARAMETER["standard_parallel_1",25],
>     PARAMETER["standard_parallel_2",47],
>     UNIT["Meter",1],
>     AXIS["Easting",EAST],
>     AXIS["Northing",NORTH]]
