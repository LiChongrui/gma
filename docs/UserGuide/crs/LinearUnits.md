---
title: LinearUnits
date: 2023-01-10
sidebar: false
---

&emsp;　gma 内置的线性单位位于 **crs.LinearUnits** 模块下。内置线性单位如下：

| 内置线性单位     | 中文名       | 值（米） |
| ---------------- | ------------ | -------- |
| Meter            | 米           | 1        |
| ClarkesLink      | 克拉克令     | 0.201166 |
| GoldCoastFoot    | 黄金海岸英尺 | 0.3048   |
| USSurveyFoot     | 美国测量英尺 | 0.304801 |
| Foot             | 英尺         | 0.3048   |
| ClarkesFoot      | 克拉克英尺   | 0.304797 |
| Link             | 令           | 0.201168 |
| BritishChain     | 英国测链     | 20.11676 |
| ClarkesYard      | 克拉克码     | 0.914392 |
| Kilometer        | 千米         | 1000     |
| IndianYard       | 印度码       | 0.914399 |
| BritishChain     | 英国测链     | 20.11678 |
| BritishYard      | 英国码       | 0.914398 |
| GermanLegalMeter | 德国法定米   | 1.000014 |
| BritishChain     | 英国测链     | 20.11677 |
| BritishFoot      | 英国英尺     | 0.304799 |

**示例：**

```python
from gma import crs

LinearUnit = crs.LinearUnits.Kilometer
print(LinearUnit)
```

> \>>> 1000
