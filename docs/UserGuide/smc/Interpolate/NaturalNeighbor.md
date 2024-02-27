---
title: NaturalNeighbor
date: 2022-10-23
sidebar: false
---

## gma.smc.Interpolate.**NaturalNeighbor**(*Points, Values, Resolution = None*)<Badge text="1.1.0 +"/>
---

**功能：** 【自然邻域法插值】。使用自然邻域法（NaturalNeighbor）将点插值成二维数组。

**参数：**

&emsp;Points：`list||tuple||array` 。插值点 X（经度），Y（纬度）坐标。至少有 4 个坐标点。

::: tip 示例

Points = [(122.52,  52.97), (124.72,  52.35), (124.4 ,  51.67), (126.63,  51.73)]

:::

&emsp;Values：`array`。坐标点对应的数据值，与 Points 数量相同。

**可选参数：**

&emsp;Resolution = `float`。插值结果的分辨率。默认（None）为 Boundary 经度、纬度差最小值的十分之一。

**返回：** 类型：`namedtuple`。包含数据（Data）和仿射变换（Transform）。

::: warning 注意

1. NaturalNeighbor 插值不会包含输入点范围外的任何数据！

2. NaturalNeighbor 方法不会进行内部坐标转换！

:::

**参考文献：**

&emsp;[1] Sibson, R. (1981). “A brief description of natural neighbor interpolation (Chapter 2)”. In V. Barnett (ed.). Interpolating Multivariate Data. Chichester: John Wiley. pp. 21–36.

&emsp;[2] V.V. Belikov; V.D. Ivanov; V.K. Kontorovich; S.A. Korytnik; A.Y. Semenov (1997). “The non-Sibsonian interpolation: A new method of interpolation of the values of a function on an arbitrary set of points”. Computational mathematics and mathematical physics. 37 (1): 9–15.            

&emsp;[3] N.H. Christ; R. Friedberg, R.; T.D. Lee (1982). “Weights of links and plaquettes in a random lattice”. Nuclear Physics B. 210 (3): 337–346. 

---

**示例 *（下载 [示例数据](/smc/Interpolate.xlsx)）*：**

```python
from gma import smc, io

ELSXLayer = io.ReadVector("Interpolate.xlsx")
Data = ELSXLayer.ToDataFrame()

Points = Data.loc[:, ['经度','纬度']].values
Values = Data.loc[:, ['值']].values

# 插值
NND = smc.Interpolate.NaturalNeighbor(Points, Values, Resolution = 0.05)
```

*与 ArcGIS NaturalNeighbor 插值结果（重分类后）对比：*

![fdg](/smc/NaturalNeighbor.webp)

