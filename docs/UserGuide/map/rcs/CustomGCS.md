---
title: CustomGCS
date: 2023-01-10
sidebar: false
---

## gma.map.rcs.**CustomGCS**(*CentralLongitude = 112*)<Badge text="1.1.2 +"/> 

---

**功能：** 【创建一个类 WGS84 坐标系（修改中央子午线）】。

**可选参数：**

&emsp; CentralLongitude = `float`。中央经线。默认 112°E。

**返回：**[`gma.map.rcs.SpatRef`](/UserGuide/map/rcs/SpatRef/)。

---

**示例：**
```python
from gma.map import rcs

CGCS = rcs.CustomGCS()
```

> \>>> <gma.map.rcs.SpatRef at 0x......>
