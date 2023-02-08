---
title: Robinson
date: 2023-01-10
sidebar: false
---

## gma.map.rcs.**Robinson**(*CentralLongitude = 112*)<Badge text="1.1.2 +"/> 

---

**功能：** 【创建伪圆柱投影】。

**可选参数：**

&emsp; CentralLongitude = `float`。中央经线。默认 112°E。

**返回：**[`gma.map.rcs.SpatRef`](/UserGuide/map/rcs/SpatRef/)。

---

**示例：**
```python
from gma.map import rcs

RB = rcs.创建伪圆柱投影()
```

> \>>> <gma.map.rcs.SpatRef at 0x......>
