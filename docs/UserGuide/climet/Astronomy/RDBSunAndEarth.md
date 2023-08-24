---
title: RDBSunAndEarth
date: 2022-09-20
sidebar: false
---

## gma.climet.Other.**RDBSunAndEarth**(*Day*) <Badge text="1.0.13 +"/>

---

**功能：**【日地相对距离】。基于 FAO-56 推荐的方法计算日地相对距离（AU）。

**参数：**

&emsp;Day: `int||array` 。日期，以日序（儒略日）表示。1-365（平年）或 366（闰年）。

**返回：**`array` 。

---

**示例 ：**

```python
from gma import climet
climet.Astronomy.RDBSunAndEarth([1,2,3])
```
> \>>> array([0.96805879, 0.96807254, 0.96809544])