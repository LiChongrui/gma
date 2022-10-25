---
title: Trend
date: 2022-10-25
sidebar: false
---

## gma.smc.Interpolate.**Trend**(*Points, Values, Boundary = None, Resolution = None, Order = 1*)<Badge text="1.1.0 +"/>
---

**功能：** 【趋势面法插值】。使用趋势面法（Trend）（全局多项式插值法）将点插值成二维数组。

**参数：**

&emsp;Points：`list||tuple||array` 。插值点 X（经度），Y（纬度）坐标。至少有 4 个坐标点。

::: tip 示例

Points = [(122.52,  52.97), (124.72,  52.35), (124.4 ,  51.67), (126.63,  51.73)]

:::


&emsp;Values：`array`。坐标点对应的数据值，与 Points 数量相同。

**可选参数：**

&emsp;Boundary = `tuple`。插值结果的四至边界，分别为最小经度（左）、最小纬度（下）、最大经度（右）、最大纬度（上）。默认（None）从输入坐标点提取范围。

&emsp;Resolution = `float`。插值结果的分辨率。默认（None）为 Boundary 经度、纬度差最小值的十分之一。

&emsp;Order = `int`。多项式阶数。默认为 1。

**返回：** 类型：`namedtuple`。包含数据（Data）、仿射变换（Transform）以及多项式系数的估计协方差（PCOV）。

---

**示例：**

```python
import gma
import pandas as pd

Data = pd.read_excel("Interpolate.xlsx")
Points = Data.loc[:, ['经度','纬度']].values
Values = Data.loc[:, ['值']].values

# 插值（2阶多项式）
TrendD  = gma.smc.Interpolate.Trend(Points, Values, Resolution = 0.05, Order = 2)

gma.rasp.WriteRaster(r'.\gma_Trend_2.tif',
                     TrendD.Data,
                     Projection = 'WGS84',
                     Transform = TrendD.Transform, 
                     DataType = 'Float32')
```

*与 ArcGIS Trend 插值结果（重分类后）对比：*

![fdg](/smc/Trend.webp)

