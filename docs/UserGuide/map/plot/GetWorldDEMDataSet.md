---
title: GetWorldDEMDataSet
date: 2023-03-01
sidebar: false
---

## gma.map.plot.**GetWorldDEMDataSet**()<Badge text="1.1.4 +"/> 

---

**功能：** 【获取内置 DEM 数据集】。打开内置的低精度世界陆地和海洋地形数据集（GEBCO 2022，分辨率 0.2°）。

**返回：** `gma.algorithm.core.dataio.DataSet`。

---

**示例：**
```python
from gma.map import plot
WorldDS = plot.GetWorldDEMDataSet()
```
> \>>> <gma.algorithm.core.dataio.DataSet at 0x...>

