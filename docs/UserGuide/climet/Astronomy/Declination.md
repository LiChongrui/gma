---
title: Declination
date: 2022-09-18
sidebar: false
---

## gma.climet.Other.**Declination**(*Day*) <Badge text="1.0.13 +"/>

---

**功能：**【赤纬】。基于 FAO-56 推荐的方法计算赤纬（red）。

**参数：**

&emsp;Day: `int||array` 。日期，以日序（儒略日）表示。1-365（平年）或 366（闰年）。

**返回：**`array` 。

---

**示例 ：**

```python
from gma import climet
climet.Astronomy.Declination([1,2,3])
```
> \>>> array([-0.40100809, -0.39956372, -0.39800096])