---
title: Thornthwaite
date: 2022-06-21
sidebar: false
---

## gma.climet.ET0.**Thornthwaite**(*TEM, LAT = 34.6, Axis = None, StartYear = 1992, StartMonth = 1*) <Badge text="1.0.10 +"/>

---

**功能：**【Thornthwaite】。基于 桑斯维特（Thornthwaite 1948）法计算月潜在蒸散量。

**参数：**

&emsp;TEM: `array` 。月平均气温（℃）。

**可选参数（常量）：**

&emsp; LAT = `float||array`。数据纬度值（°）。默认为 34.6° N。

::: tip 提示

若 LAT 为数组，其在非计算轴上应与输入数据具有相同的形状！

:::

&emsp; Axis = `int`。计算轴。如果不设置（None），多维数据会将所有数据展开到一维计算。

&emsp; StartYear = `int`。数据起始年份。默认为 1992 年。

&emsp; StartMonth = `int`。数据起始月份。默认为 1。

::: warning 注意

StartYear、StartMonth 基于计算轴！

:::

**返回：**`array`。

**参考文献：**

&emsp;Thornthwaite, C.W. (1948) An approach toward a rational classification of climate. Geographical Review, Vol. 38, 55-94.

---

