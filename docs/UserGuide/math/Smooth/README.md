---
title: \_\_init\_\_
date: 2021-10-30
sidebar: false
---

## gma.index.**Smooth**(*Data, WindowSize, Times = 1, Axis = None*)

---

**功能：** 【类】。数据平滑（滤波）。

**初始化：**

&emsp;Data：1D `array`。需要平滑的 1 维数据。

&emsp;WindowSize：`int`。平滑窗口大小。必须为正奇数。

&emsp;Times = `int`。平滑次数。默认平滑 1 次。

&emsp;Axis = `int` <Badge text="1.0.8 +"/> 。数据平滑使用的轴。默认（None）数据小于 3 维以第 1 个维度为轴，高于 3 维以倒数第 3 个维度为轴。

::: warning 注意

类内 属性/方法 引用前请先初始化 `Smooth` 类！

::: 

---

**示例：**
```python
import gma
Data = [0.16359164, 0.16359164, 0.17469311, 0.20163227, 0.22857143, 0.32706435, 0.21466192, 0.10225949]
SM = gma.math.Smooth(Data, 5, Times = 1)
## 查看类型所有的 方法/属性
print([M for M in dir(SM) if '_' not in M])
```
> \>>> ['MovingAverage', 'SavitzkyGolay']

