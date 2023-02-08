---
title: AlbersEqualArea
date: 2023-01-10
sidebar: false
---

## gma.map.rcs.**AlbersEqualArea**(*CentralLongitude = 112, CentralLatitude = 34, FalseEasting = 0.0, FalseNorthing = 0.0, StandardParallels = (25, 47)*)<Badge text="1.1.2 +"/> 

---

**功能：** 【创建阿尔伯斯等面积投影】。

**可选参数：**

&emsp; CentralLongitude = `float`。中央经线。默认 112°E。

&emsp; CentralLatitude = `float`。中央纬线。默认 34°N。

&emsp; FalseEasting = `float`。假东距。默认 0.0。

&emsp; FalseNorthing = `float`。假北距。默认 0.0。

&emsp; StandardParallels = `tuple`。两条标准纬线。默认 25°N 和 47°N。

**返回：**[`gma.map.rcs.SpatRef`](/UserGuide/map/rcs/SpatRef/)。

---

**示例：**
```python
from gma.map import rcs

AEA = rcs.AlbersEqualArea()
```

> \>>> <gma.map.rcs.SpatRef at 0x......>
