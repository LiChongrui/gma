---
title: WorldLayer
date: 2023-03-10
sidebar: false
---

## gma.map.inres.WorldLayer<Badge text="1.1.5 +"/> 

---

**功能：** 【获取内置 矢量 数据集】。内置的低精度世界矢量。

**包括：** 

| 属性    | 说明                               |
| ------- | ---------------------------------- |
| Country | Natural Earth 世界国家或政区边界。 |
| Lake    | Natural Earth 世界大型湖泊。       |
| Land    | Natural Earth 世界陆地。           |
| Ocean   | Natural Earth 世界海洋。           |
| River   | Natural Earth 世界大型河流。       |

---

**示例：**

```python
from gma.map import inres
Country = inres.WorldLayer.Country
```
> \>>> <gma.algorithm.core.dataio.Layer at 0x...>

### Country

![](/map/NECountry.jpg)

### Lake

![](/map/NELake.jpg)

### Land

![](/map/NELand.jpg)

### Ocean

![](/map/NEOcean.jpg)

### Ocean

![](/map/NERiver.jpg)
