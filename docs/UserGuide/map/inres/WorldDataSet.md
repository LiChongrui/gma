---
title: WorldDataSet
date: 2023-01-10
sidebar: false
---

## gma.map.inres.**WorldDataSet**<Badge text="1.1.5 +"/> 

---

**功能：** 【获取世界数据集】。内置的低精度世界数据集。

**包括：** 

| 属性         | 说明                            |
| ------------ | ------------------------------- |
| DEM          | GEBCO 2022 世界陆地和海洋 DEM。 |
| NaturalEarth | Natural Earth 自然地球影像。    |

---

**示例：**

```python
from gma.map import inres
DEM = inres.WorldDataSet.DEM
```
> \>>> <gma.algorithm.core.dataio.DataSet at 0x...>

### DEM

![](/map/DEM.jpg)

### 自然地球影像

![](/map/NEImage.jpg)
