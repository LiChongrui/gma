---
title: Kriging
date: 2022-10-29
sidebar: false
---

## gma.smc.Interpolate.**Kriging**(*Points, Values, Boundary = None, Resolution = None, SearchRadius = 12, InProjection = 'WGS84', VariogramModel = 'Linear',  VariogramParameters = None, KMethod = 'Ordinary', \*\*kwargs*)<Badge text="1.1.0 +"/>
---

**功能：** 【克里金法插值】。使用普通克里金法（Ordinary Kriging）或泛克里金法（Universal Kriging）将点插值成二维数组。

**参数：**

&emsp;Points：`list||tuple||array` 。插值点 X（经度），Y（纬度）坐标。至少有 4 个坐标点。

::: tip 示例

Points = [(122.52,  52.97), (124.72,  52.35), (124.4 ,  51.67), (126.63,  51.73)]

:::


&emsp;Values：`array`。坐标点对应的数据值，与 Points 数量相同。

**可选参数：**

&emsp;Boundary = `tuple`。插值结果的四至边界，分别为最小经度（左）、最小纬度（下）、最大经度（右）、最大纬度（上）。默认（None）从输入坐标点提取范围。

&emsp;Resolution = `float`。插值结果的分辨率。默认（None）为 Boundary 经度、纬度差最小值的十分之一。

&emsp;SearchRadius = `int`。搜索范围。指定要用于执行插值的最邻近输入采样点数量，默认为 12 个点。

&emsp;InProjection = `str`。输入坐标点的坐标系。默认为 WGS84（EPSG:4326）。

&emsp;VariogramModel = `str`。克里金插值所使用的半变异函数模型，默认为 线性模型（Linear）。

&emsp;VariogramParameters = `dict`。半变异模型对应的参数。默认利用最小二乘法自动计算变异函数模型参数（None）。

::: tip 支持的模型及可配置的参数

+ 线性模型：Linear，可配置参数：Slope，Nugget
+ 乘方模型：Power，可配置参数：Scale, Exponent, Nugget
+ 高斯模型：Gaussian，可配置参数：PSill, Range, Nugget     
+ 球面模型：Spherical，可配置参数：PSill, Range, Nugget    
+ 指数模型：Exponential，可配置参数：PSill, Range, Nugget      
+ 空穴效应模型：HoleEffect，可配置参数：PSill, Range, Nugget
:::

&emsp;KMethod = `str`。克里金方法。包括 Ordinary（普通克里金）或 Universal（泛克里金），默认为 Ordinary。

**其他参数（kwargs）：**（当 VariogramParameters = None 时生效）

&emsp;NLags = `int`。半变异函数的平均箱数。默认值为 6。

&emsp;Weight = `bool`。指定是否应将较小滞后的半方差加权。默认否（False）。

**返回：** 类型：`namedtuple`。包含数据（Data）、误差（SigmaSQ）和仿射变换（Transform）。

**参考文献：**

&emsp;[1] P.K. Kitanidis, Introduction to Geostatistcs: Applications in Hydrogeology, Cambridge University Press, 1997(p272).

&emsp;[2] N. Cressie, Statistics for spatial data, Wiley Series in Probability and Statistics, 1993(p137).

---

**示例 *（下载 [示例数据](/smc/Interpolate.xlsx)）*：**

```python
from gma import smc, io

ELSXLayer = io.ReadVector("Interpolate.xlsx")
Data = ELSXLayer.ToDataFrame()

Points = Data.loc[:, ['经度','纬度']].values
Values = Data.loc[:, ['值']].values

# 普通克里金（球面函数模型）插值
KD = smc.Interpolate.Kriging(Points, Values, Resolution = 0.05, 
                             VariogramModel = 'Spherical', 
                             VariogramParameters = None,
                             KMethod = 'Ordinary',
                             InProjection = 'EPSG:4326')
```

*与 ArcGIS Ordinary Kriging 插值结果（重分类后）对比：*

![fdg](/smc/OKriging.webp)

*与 pykrige 包 Universal Kriging 插值结果（重分类后）对比：*

![fdg](/smc/UKriging.webp)

