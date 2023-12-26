---
title: ExtractValues
date: 2022-10-20
sidebar: false
---

## gma.smc.Extraction.**ExtractValues**(*Points, GMADataSet*)
---

**功能：** 【计算面积】。计算输入多点组成多边形的面积。

**参数：**

&emsp;Points：`list||tuple||array` 。需要提取数据点的 X（经度），Y（纬度）坐标。

::: tip 示例

Points = [(130.1, 45.2), (131.5, 40.2), (131.5, 45.2)]

:::

&emsp;GMADataSet：`DataSet` 。用于提取数据的 gma 栅格数据集 DataSet。

::: warning 注意

请保证坐标点和栅格数据集的坐标系相同。

:::

**返回：**`DataFrame`。

---

**示例：**
```python
from gma.map import inres
from gma import smc

DEMDS = inres.WorldDataSet.DEM
Points = [[112, 30], [120, 45]]

EVData = smc.Extraction.ExtractValues(Points, DEMDS)
```

> \>>> 

|    |   X |   Y |   Band1 |
|---:|----:|----:|--------:|
|  0 | 112 |  30 |      44 |
|  1 | 120 |  45 |     742 |
