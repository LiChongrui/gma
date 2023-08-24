---
title: Hargreaves
date: 2022-06-22
sidebar: false
---

## gma.climet.ET0.**Hargreaves**(*TMAX, TMIN, LAT = 34.6, TMean = None, Axis = None, StartYear = 1992, StartDayOfYear = 1*) <Badge text="1.0.10 +"/>

---

**功能：**【Hargreaves】。基于 哈格里夫斯（Hargreaves 1998）法计算日潜在蒸散量。

**参数：**

&emsp;TMAX: `float||array`。日最高气温（℃）。

&emsp;TMIN: `float||array`。日最低气温（℃）。

**可选参数：**

&emsp;LAT = `float||array`。数据纬度值（°）。默认北纬 34.6°。

::: tip 提示

若 LAT 为数组，其在非计算轴上应与输入数据具有相同的形状！

:::

&emsp;TMean = `float||array`。日最高气温（℃）。默认（None）为最高最低气温的平均值（TMAX + TMIN） * 0.5。

&emsp;Axis = `int`。计算轴。如果不设置（None），多维数据会将所有数据展开到一维计算。

&emsp;StartYear = `int`。数据起始年份。默认 1992 年。

&emsp;StartDayOfYear = `int`。数据起始日序。默认为 1。

::: warning 注意

StartYear、StartDayOfYear 基于计算轴！

:::

**返回：**`array`。

**参考文献：**

&emsp;Allen, Richard et al (1998) Crop evapotranspiration - Guidelines for computing crop  water requirements - FAO Irrigation and drainage paper 56 ISBN 92-5-104219-5

---

```python
from gma import climet
import numpy as np
np.random.seed(0)

TMAX = np.random.uniform(20, 30, size = 48)
TMIN = np.random.uniform(10, 20, size = 48)

THD = climet.ET0.Hargreaves(TMAX, TMIN)
```
> \>>> array([2.20254352, 2.09796738, 2.26378286, 1.60532567, 1.84185121,
       2.1940866 , 2.04971425, 2.27649286, 2.57712085, 1.7926611 ,
       2.60771494, 1.96530488, 2.03299078, 2.50441209, 0.73454371,
       1.27599509, 1.55238039, 2.56200767, 2.32908408, 2.8287616 ,
       2.65669559, 2.42848895, 2.31957885, 2.7729996 ])