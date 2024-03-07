---
title: ProjMethod
date: 2024-01-10
sidebar: false
---

&emsp; crs.ProjMethod 内置了大量投影方，以 Python 类的形式存储。可以通过修改参数，配置自定义投影坐标系。

## 通用投影参数

&emsp;不同的投影方法可配置的参数略有不同，但主要包括一下参数：

| 投影参数           | 说明       | 参数数据类型 | 参数范围    |
| ------------------ | ---------- | ------------ | ----------- |
| CentralLongitude   | 中央经线   | float        | [-180, 180] |
| CentralLatitude   | 中央纬线   | float        | [-90, 90]   |
| FalseEasting      | 东偏移量   | float        | ≥0          |
| FalseNorthing     | 北偏移量   | float        | ≥0          |
| StandardParallels1 | 标准纬线1  | float        | [-90, 90]   |
| StandardParallels2 | 标准纬线2  | float        | [-90, 90]   |
| ScaleFactor        | 比例因子   | float        | ≥0          |
| OriginLatitude    | 起始纬度   | float        | [-90, 90]   |
| CentralMeridian   | 中央子午线 | float        | [-180, 180] |

## 主要投影方法

| 投影方法                  | 中文名                        | 可配置参数                                                   | 投影图示                                   |
| ------------------------- | ----------------------------- | ------------------------------------------------------------ | ------------------------------------------ |
| Aitof                     | 埃托夫投影                    | CentralMeridian <br />FalseEasting <br /> FalseNorthing <br /> | ![](/crs/PM/Aitoff.jpg)                    |
| AlbersConicEqualArea      | 阿尔伯斯等积圆锥投影          | CentralLongitude <br />  CentralLatitude <br />FalseEasting <br /> FalseNorthing <br /> StandardParallels1 <br /> StandardParallels2 | ![](/crs/PM/AlbersConicEqualArea.jpg)      |
| AzimuthalEquidistant      | 等距方位投影                  | CentralLongitude <br />  CentralLatitude <br /> FalseEasting <br /> FalseNorthing <br /> | ![](/crs/PM/AzimuthalEquidistant.jpg)      |
| Bonne                     | 彭纳投影                      | CentralMeridian <br /> StandardParallels1 <br /> FalseEasting <br /> FalseNorthing <br /> | ![](/crs/PM/Bonne.jpg)                     |
| CassiniSoldner            | 卡西尼-斯罗德投影             | CentralMeridian <br /> OriginLatitude <br /> FalseEasting <br /> FalseNorthing <br /> | ![](/crs/PM/CassiniSoldner.jpg)            |
| CompactMiller             | 紧凑型米勒投影                | CentralMeridian <br /> FalseEasting <br /> FalseNorthing <br /> | ![](/crs/PM/CompactMiller.jpg)             |
| CylindricalEqualArea      | 圆柱等积投影                  | CentralMeridian <br /> StandardParallels1 <br /> FalseEasting <br /> FalseNorthing <br /> | ![](/crs/PM/CylindricalEqualArea.jpg)      |
| EckertI                   | 埃克特I投影                   | CentralMeridian <br /> FalseEasting <br /> FalseNorthing <br /> | ![](/crs/PM/EckertI.jpg)                   |
| EckertII                  | 埃克特II投影                  | CentralMeridian <br /> FalseEasting <br /> FalseNorthing <br /> | ![](/crs/PM/EckertII.jpg)                  |
| EckertIII                 | 埃克特III投影                 | CentralMeridian <br /> FalseEasting <br /> FalseNorthing <br /> | ![](/crs/PM/EckertIII.jpg)                 |
| EckertIV                  | 埃克特IV投影                  | CentralMeridian <br /> FalseEasting <br /> FalseNorthing <br /> | ![](/crs/PM/EckertIV.jpg)                  |
| EckertV                   | 埃克特V投影                   | CentralMeridian <br /> FalseEasting <br /> FalseNorthing <br /> | ![](/crs/PM/EckertV.jpg)                   |
| EckertVI                  | 埃克特VI投影                  | CentralMeridian <br /> FalseEasting <br /> FalseNorthing <br /> | ![](/crs/PM/EckertVI.jpg)                  |
| EquidistantConic          | 等距圆锥投影                  | CentralLongitude <br />  CentralLatitude <br /> FalseEasting <br /> FalseNorthing <br /> StandardParallels1 <br /> StandardParallels2 | ![](/crs/PM/EquidistantConic.jpg)          |
| Equirectangular           | 等距圆柱投影                  | CentralMeridian <br /> StandardParallels1 <br /> FalseEasting <br /> FalseNorthing <br /> | ![](/crs/PM/Equirectangular.jpg)           |
| GallStereographic         | 高尔立体投影                  | CentralMeridian <br /> FalseEasting <br /> FalseNorthing <br /> | ![](/crs/PM/GallStereographic.jpg)         |
| GoodeHomolosine           | 古蒂等面积投影                | CentralMeridian <br /> FalseEasting <br /> FalseNorthing <br /> | ![](/crs/PM/GoodeHomolosine.jpg)           |
| LambertAzimuthalEqualArea | 兰勃特方位等积投影            | CentralLongitude <br />  CentralLatitude <br /> FalseEasting <br /> FalseNorthing <br /> | ![](/crs/PM/LambertAzimuthalEqualArea.jpg) |
| LambertConformalConic2SP  | 兰勃特等角圆锥投影  2标准纬线 | CentralMeridian <br /> OriginLatitude <br /> FalseEasting <br /> FalseNorthing <br /> StandardParallels1 <br /> StandardParallels2 | ![](/crs/PM/LambertConformalConic2SP.jpg)  |
| Loximuthal                | 洛西马塔尔投影                | CentralMeridian <br /> OriginLatitude <br /> FalseEastin  FalseNorthing <br /> | ![](/crs/PM/Loximuthal.jpg)                |
| Mercator                  | 墨卡托投影                    | CentralMeridian <br /> FalseEasting <br /> FalseNorthing <br /> ScaleFactor | ![](/crs/PM/Mercator.jpg)                  |
| Mercator2SP               | 墨卡托投影  2标准纬线         | CentralMeridian <br /> StandardParallels1 <br /> FalseEasting <br /> FalseNorthing <br /> | ![](/crs/PM/Mercator2SP.jpg)               |
| Mollweide                 | 摩尔维特投影                  | CentralLongitude <br />  FalseEasting <br /> FalseNorthing <br /> | ![](/crs/PM/Mollweide.jpg)                 |
| NaturalEarth              | 自然地球投影                  | CentralMeridian <br /> FalseEasting <br /> FalseNorthing <br /> | ![](/crs/PM/NaturalEarth.jpg)              |
| NaturalEarthII            | 自然地球投影II                | CentralMeridian <br /> FalseEasting <br /> FalseNorthing <br /> | ![](/crs/PM/NaturalEarthII.jpg)            |
| Polyconic                 | 多圆锥投影                    | CentralMeridian <br /> OriginLatitude <br /> FalseEasting <br /> FalseNorthing <br /> | ![](/crs/PM/Polyconic.jpg)                 |
| Robinson                  | 罗宾森投影                    | CentralLongitude <br />  FalseEasting <br /> FalseNorthing <br /> | ![](/crs/PM/Robinson.jpg)                  |
| Sinusoidal                | 正弦曲线投影                  | CentralLongitude <br />  FalseEasting <br /> FalseNorthing <br /> | ![](/crs/PM/Sinusoidal.jpg)                |
| Times                     | 泰晤士投影                    | CentralMeridian <br /> FalseEasting <br /> FalseNorthing <br /> | ![](/crs/PM/Times.jpg)                     |
| TransverseMercator        | 横轴墨卡托投影                | CentralMeridian <br /> OriginLatitude <br /> FalseEasting <br /> FalseNorthing <br /> ScaleFactor | ![](/crs/PM/TransverseMercator.jpg)        |
| VanDerGrinten             | 范德格林氏投影                | CentralMeridian <br /> FalseEasting <br /> FalseNorthing <br /> | ![](/crs/PM/VanDerGrinten.jpg)             |
| WinkelI                   | 温克尔I投影                   | CentralMeridian <br /> StandardParallels1 <br /> FalseEasting <br /> FalseNorthing <br /> | ![](/crs/PM/WinkelI.jpg)                   |
| WinkelII                  | 温克尔II投影                  | CentralMeridian <br /> StandardParallels1 <br /> FalseEasting <br /> FalseNorthing <br /> | ![](/crs/PM/WinkelII.jpg)                  |
| WinkelTripel              | 温克尔三重投影                | CentralMeridian <br /> StandardParallels1 <br /> FalseEasting <br /> FalseNorthing <br /> | ![](/crs/PM/WinkelTripel.jpg)              |

**示例：**

```python
from gma import crs

AitoffC0 = crs.ProjMethod.Aitoff(CentralMeridian = 0)
print(AitoffC0)

```

> \>>> <gma.algos.spat.projection.Aitoff at 0x0...>
