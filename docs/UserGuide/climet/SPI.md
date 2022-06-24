---
title: SPI
date: 2022-06-25
sidebar: false
---

## gma.climet.**SPI**(*PRE, Axis = None, Scale = 1, Periodicity = 12*) <Badge text="1.0.10 +"/>

---

**功能：**【标准化降水指数】。基于 Gamma 分布计算标准化降水指数。

**参数：**

&emsp;PRE: `array`。降水量（mm）。

**可选参数：**

&emsp; Axis = `int`。计算轴。如果不设置（None），多维数据会将所有数据展开到一维计算。

&emsp; Scale = `int`。时间尺度。默认为 1。例如：1月、3月或其他。

&emsp; Periodicity = `int`。周期。默认为 12。例如：月尺度可以以 12 为周期，日尺度可以以 365 为周期。

::: warning 注意

Scale、Periodicity 基于计算轴！

:::

**返回：**`array`。

**参考文献：**

&emsp;Thornthwaite, C.W. (1948) An approach toward a rational classification of climate. Geographical Review, Vol. 38, 55-94.

---

