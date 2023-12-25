---
title: Aggregate
date: 2022-08-10
sidebar: false
---

## gma.math.Kernel.**Aggregate**(*Data, KernelSize = 3, NoData = None, Axis = None, Method = 'Max'*)<Badge text="1.0.11 +"/>

---

**功能：** 【数组聚合】。生成缩小后数组。

**参数：** 

&emsp;Data: `list||array`。需要计算的数据。

**可选参数：**

&emsp;KernelSize = `int`。缩放系数。输出数组会缩放 KernelSize 倍。默认为 3 。

&emsp;NoData = `float`。输入数组中的无效值。此值不会参与聚合计算，默认自动设置（None）。

&emsp;Axis = `int||list`。计算轴。默认自动扩展到所有轴（None）。

&emsp;Method = `str`。聚合方法。指出确定每个输出像元值的方式。默认取最大值（Max）。

::: tip 其他聚合方法

Mean（均值）， Min（最小值），Sum（求和），Median（中值）。

:::

**返回：**`array`。

---

**示例：**
```python
from gma import math
import numpy as np

np.random.seed(1992)
Data = np.random.uniform(0, 100, (9, 9)).round(2)

Agg3Max = math.Kernel.Aggregate(Data, KernelSize = 3, Method = 'Max')
Agg2Min = math.Kernel.Aggregate(Data, KernelSize = 2, Method = 'Min')
```

![](/math/Aggregate.svg)
