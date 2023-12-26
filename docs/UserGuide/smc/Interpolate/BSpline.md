---
title: BSpline
date: 2022-10-29
sidebar: false
---

## gma.smc.Interpolate.**BSpline**(*Points, Values, Boundary = None, Resolution = None, Weights = 0.1*)<Badge text="1.1.0 +"/>
---

**功能：** 【B-样条函数法插值】。使用 B-样条函数法（BSpline）将点插值成二维数组。

**参数：**

&emsp;Points：`list||tuple||array` 。插值点 X（经度），Y（纬度）坐标。至少有 4 个坐标点。

::: tip 示例

Points = [(122.52,  52.97), (124.72,  52.35), (124.4 ,  51.67), (126.63,  51.73)]

:::

&emsp;Values：`array`。坐标点对应的数据值，与 Points 数量相同。

**可选参数：**

&emsp;Boundary = `tuple`。插值结果的四至边界，分别为最小经度（左）、最小纬度（下）、最大经度（右）、最大纬度（上）。默认（None）从输入坐标点提取范围。

&emsp;Resolution = `float`。插值结果的分辨率。默认（None）为 Boundary 经度、纬度差最小值的十分之一。

&emsp;Weights = `float||list`。权重。默认为 0.1 。

**返回：** 类型：`namedtuple`。包含数据（Data）、仿射变换（Transform）。

**参考文献：**

&emsp;[1] Dierckx P. An algorithm for surface fitting with spline functions Ima J. Numer. Anal. 1 (1981) 267-283.

&emsp;[2] Dierckx P. An algorithm for surface fitting with spline functions report tw50, Dept. Computer Science,K.U.Leuven, 1980.

&emsp;[3] Dierckx P. Curve and surface fitting with splines, Monographs on Numerical Analysis, Oxford University Press, 1993.

---

**示例 *（下载 [示例数据](/smc/Interpolate.xlsx)）*：**


```python
from gma import smc
import pandas as pd

Data = pd.read_excel("Interpolate.xlsx")
Points = Data.loc[:, ['经度','纬度']].values
Values = Data.loc[:, ['值']].values

# 插值
BSD  = smc.Interpolate.BSpline(Points, Values, Resolution = 0.05, Weights = 0.1)
```

*不同 Weights 插值结果（重分类后）对比：*

![fdg](/smc/BSpline.webp)

