---
title: Buishand
date: 2022-08-28
sidebar: false
---

## gma.climet.Diagnosis.**Buishand**(*Data, Axis = None, Method = 'Q'*)<Badge text="1.1.1 +"/>

---

**功能：**【Buishand 突变点检验】。基于 Buishand 法对时间序列数据进行突变点检验。

**参数：**

&emsp;Data：`list||array` 。需要检验的数据。

**可选参数：**

&emsp;Axis = `int`  。计算轴。如果不设置（None），多维数据会将所有数据展开到一维计算。

&emsp;Method = `Q`  。Buishand 方法。默认为 'Q'。

::: tip 其他方法
'Range'，'LL Ration'，'U'。
:::


**返回：** `namedtuple`。

&emsp;&emsp;最大统计量：R（Range）或 Q（Q）或 V（LL Ration）或 U（U）。

&emsp;&emsp;LOC：突变位置。

---

**示例：**

```python
from gma import climet
# 这里建立一个随机序列来模拟代码数据处理过程
import numpy as np
np.random.seed(0)
Data = np.random.uniform(size = 72)

BD = climet.Diagnosis.Buishand(Data, Method='Q')

print(BD)
```
> \>>> BuishandQ(Q=1.2571112721486875, LOC=40)

