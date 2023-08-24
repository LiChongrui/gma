---
title: Pettitt
date: 2022-08-28
sidebar: false
---

## gma.climet.Diagnosis.**Pettitt**(*Data, Axis = None*)<Badge text="1.1.1 +"/>

---

**功能：**【Pettitt 突变点检验】。基于 Pettitt 法对时间序列数据进行突变点检验。

**参数：**

&emsp;Data：`list||array` 。需要检验的数据。

**可选参数：**

&emsp;Axis = `int`  。计算轴。如果不设置（None），多维数据会将所有数据展开到一维计算。


**返回：** `namedtuple`。

&emsp;&emsp;MAXU：最大统计量。

&emsp;&emsp;LOC：突变位置。

&emsp;&emsp;p：显著性检验 p 值（单尾）。

---

**示例：**

```python
from gma import climet
# 这里建立一个随机序列来模拟代码数据处理过程
import numpy as np
np.random.seed(0)
Data = np.random.uniform(size = 72)

PD = climet.Diagnosis.Pettitt(Data)

print(PD)
```
> \>>> Pettitt(MAXU=412.0, LOC=40, p=0.13558910074593938)

