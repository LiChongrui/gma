---
title: HourAngle
date: 2022-09-20
sidebar: false
---

## gma.climet.Astronomy.**HourAngle**(*Day, LAT*) <Badge text="1.0.13 +"/>

---

**功能：**【时角】。基于 FAO-56 推荐的方法计算时角（t）。

**参数：**

&emsp;Day: `int||array` 。日期，以日序（儒略日）表示。1-365（平年）或 366（闰年）。

&emsp;LAT: `float||array` 。纬度（°）。

**返回：**`array` 。

---

**示例 ：**

```python
from gma import climet
climet.Astronomy.HourAngle([1,2,3], 34)
```
> \>>> array([[1.28076788], [1.2819664 ], [1.28326103]])