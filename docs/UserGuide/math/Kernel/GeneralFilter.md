---
title: GeneralFilter
date: 2022-07-10
sidebar: false
---

## gma.math.Kernel.**GeneralFilter**(*Data, KernelSize = 3, NoData = None, Axis = None, EdgeEXPMode = 'Edge', Method = 'Mean'*)<Badge text="1.0.11 +"/>

---

**功能：** 【普通滤波】。对数组进行普通滤波处理。

**参数：** 

&emsp;Data: 所有数据类型。需要计算的数据。

**可选参数：**

&emsp;KernelSize = `int`。滤波核大小。默认为 3 。

&emsp;NoData = `float`。输入数组中的无效值。此值不会参与滤波计算，默认自动设置（None）。

&emsp;Axis = `int||list`。计算轴。默认自动扩展到所有轴（None）。

&emsp;EdgeEXPMode = `str||float`。边缘数据扩展方法。默认使用边缘值扩展（'Edge'）。

::: tip 其他边缘值处理方法

str: Edge，Linear_Ramp，Maximum，Mean，Median，Minimum，Reflect，Symmetric，Wrap，Empty。
            
float: 若配置为常数，则用此常数扩展。

:::       

&emsp;Method = `str`。滤波方法。默认中值滤波（Median）。

::: tip 其他滤波方法

Mean（均值滤波），Min（最小值滤波），Sum（求和滤波），Max（最大值滤波）。

:::

**返回：**`array`。

---

**示例：**
```python
from gma import math
import numpy as np

np.random.seed(1992)
Data = np.random.uniform(0, 100, (200, 200))

GeF3 = math.Kernel.GeneralFilter(Data, KernelSize = 3)
GeF9 = math.Kernel.GeneralFilter(Data, KernelSize = 9)
```

![](/math/GeneralFilter.svg)