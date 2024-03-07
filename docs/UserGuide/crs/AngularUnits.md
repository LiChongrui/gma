---
title: AngularUnits
date: 2023-01-10
sidebar: false
---

&emsp;　gma 内置的角度单位位于 **crs.AngularUnits** 模块下。内置角度单位如下：

| 角度单位名称     | 对应中文单位 | 值 / 每单位弧度(°）       |
| :--------------- | :----------- | :------------------------ |
| Arcminute        | 弧分         | 0.000290888208665721      |
| Arcsecond        | 弧秒         | 0.00000484813681109535    |
| Degree           | 度           | 0.0174532925199432        |
| Gon              | 百分制度     | 0.0157079632679489        |
| Grad             | 百分制度     | 0.0157079632679489        |
| Microradian      | 微弧度       | 0.000000999999999999999   |
| Mil6400          | 密尔6400     | 0.00098174770424681       |
| Milliarcsecond   | 毫微秒       | 0.00000000484813681109536 |
| MinuteCentesimal | 百分制分     | 0.000157079632679489      |
| Radian           | 弧度         | 1                         |
| SecondCentesimal | 百分制秒     | 0.00000157079632679489    |

**示例：**

```python
from gma import crs

Degree = crs.AngularUnits.Degree
print(Degree)
```

> \>>> 0.0174532925199433
