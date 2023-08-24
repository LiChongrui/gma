---
title: MKMutationTest
date: 2022-08-28
sidebar: false
---

## gma.climet.Diagnosis.**MKMutationTest**(*Data, Axis = None*)<Badge text="1.0.12 +"/>

---

**功能：**【Mann-Kendall 突变检验】。基于 Mann-Kendall 方法对时间序列数据进行突变检验。

**参数：**

&emsp;Data：`list||array` 。需要检验的数据。

**可选参数：**

&emsp;Axis = `int`  。计算轴。如果不设置（None），多维数据会将所有数据展开到一维计算。

**返回：** `namedtuple`。包含正向（UFk）和反向（UBk）结果。

---

**示例：**

```python
from gma import climet
# 这里建立一个随机序列来模拟代码数据处理过程
import numpy as np
np.random.seed(0)
Data = np.random.uniform(size = 72)

MKD = climet.Diagnosis.MKMutationTest(Data)

# 输出具名元组字段名
print(MKD._fields)
```
> \>>> ('UFk', 'UBk')

>绘制结果

![](/climet/MKMT.svg)
