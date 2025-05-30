---
title: SolarRadiationFluxOA
date: 2022-09-26
sidebar: false
---

## gma.climet.Astronomy.**SolarRadiationFluxOA**(*Day, LAT*) <Badge text="1.0.13 +"/>

---

**功能：**【大气层外太阳辐射通量】。基于 FAO-56 推荐的方法计算大气层外太阳辐射通量（MJ/m2）。

**参数：**

&emsp;Day: `int||array` 。日期，以日序（儒略日）表示。1-365（平年）或 366（闰年）。

&emsp;LAT: `float||array` 。纬度（°）。

**返回：**`array` 。

---

**示例 ：**

```python
from gma import climet
climet.Astronomy.SolarRadiationFluxOA([1,2,3],34)
```
> \>>> array([[17.5426866 ], [17.59680637], [17.65521884]])