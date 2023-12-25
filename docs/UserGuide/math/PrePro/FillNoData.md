---
title: FillNoData
date: 2021-10-30
sidebar: false
---

## gma.math.PrePro.**FillNoData**(*Data, FillValue = None, Method = 'linear', Axis = None, \*\*kwargs*)

---

**功能：**【填充缺失值】。对缺失值或异常值值进行插值替换。

**参数：**

&emsp;Data：`list||tuple||Series||DataFrame||array` 。需要插补的数据。

**可选参数：**

&emsp;FillValue = `float||list`。 需要进行插补的缺失值。默认不设置（None）。

::: warning 注意

1. 当 FillValue 为列表时，列表内所有值都将被插补。

2. 数据内原有的NAN、INF以及不能被转化为数字的字符串等异常值也将被插补。

:::

&emsp;Method = `str`。 插补方法。默认线性插值（linear）。

::: tip 其他插补方法

 index（索引）, values（序列值），pad（前向填充），nearest（最邻近），zero（零值），slinear（滑动线性），quadratic（2次方），cubic（3次方），spline（样条函数），barycentric（重心），polynomial（分段多项式），from_derivatives（衍生），krogh（克罗格），piecewise_polynomial（分段多项式），pchip（分段三次 Hermite 多项式插值），akima（akima 光滑插值），cubicspline（3次样条）等。

:::

&emsp;Axis = `int` <Badge text="1.0.8"/> 。数据插补使用的轴。默认（None）数据小于 3 维以第 1 个维度为轴，高于 3 维以倒数第 3 个维度为轴。

&emsp;**kwargs。传递给插值函数的其他参数。例如：Method 为 polynomial 或 spline 需要设置 order（阶数），默认阶数为 3。

**返回：** Series，DataFrame 返回 `输入类型`；list，tuple，array 返回 `array`。

---

**示例：**
```python
from gma import math
```

*序列（1 维）*

```python
Data = [None, 0.16359164, 0.17469311, 'NULL', 0.22857143, 0.32706435, 10, 0.10225949]
# 未定义需要被填充的值则仅插值序列中的非数据值以及无穷值
math.PrePro.FillNoData(Data)
```
> \>>> array([0.16359164, 0.16359164, 0.17469311, 0.20163227, 0.22857143, 0.32706435, 10.0, 0.10225949])

::: tip 提示

不能处理边缘缺失值的插补方法（例如 linear 等）函数默认采用邻近值填充边缘缺失值！如有特定需求，请在插补前自行处理！

:::

```python
# 定义了需要被填充的值后此值也会被填充。不存在的值则自动忽略
math.PrePro.FillNoData(Data, FillValue = 10)
```

> \>>> array([0.16359164, 0.16359164, 0.17469311, 0.20163227, 0.22857143, 0.32706435, 0.21466192, 0.10225949])
