---
title: SNHT
date: 2022-08-28
sidebar: false
---

## gma.climet.Diagnosis.**SNHT**(*Data, Axis = None*)<Badge text="1.1.1 +"/>

---

**功能：**【SNHT 突变点检验】。基于 SNHT 法对时间序列数据进行突变点检验。

**参数：**

&emsp;Data：`list||array` 。需要检验的数据。

**可选参数：**

&emsp;Axis = `int`  。计算轴。如果不设置（None），多维数据会将所有数据展开到一维计算。


**返回：** `namedtuple`。

&emsp;&emsp;MAXT：SNHT T 检验最大统计量。

&emsp;&emsp;LOC：突变位置。

---

**示例：**

```python
import gma
# 这里建立一个随机序列来模拟代码数据处理过程
import numpy as np
np.random.seed(0)
Data = np.random.uniform(size = 72)

SD = gma.climet.Diagnosis.SNHT(Data)

print(SD)
```
> \>>> SNHT(MAXT=6.46938054846884, LOC=43)

