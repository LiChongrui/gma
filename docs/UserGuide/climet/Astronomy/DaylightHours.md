---
title: DaylightHours
date: 2022-09-15
sidebar: false
---

## gma.climet.Other.**DaylightHours**(*Day, LAT*) <Badge text="1.0.13 +"/>

---

**功能：**【白昼时数】。基于 FAO-56 推荐的方法计算白昼时数（h）。

**参数：**

&emsp;Day: `int||array` 。日期，以日序（儒略日）表示。1-365（平年）或 366（闰年）。

&emsp;LAT: `float||array` 。纬度（°）。

**返回：**`array` 。

---

**示例 ：**

```python
from gma import climet
climet.Astronomy.DaylightHours([1,2,3],35)
```
> \>>> array([[9.69732946], [9.70686719], [9.71716952]])