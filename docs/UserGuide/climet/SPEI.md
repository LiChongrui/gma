---
title: SPEI
date: 2022-06-24
sidebar: false
---

## gma.climet.**SPEI**(*PRE, PET, Axis = None, Scale = 1, Periodicity = 12*) <Badge text="1.0.10 +"/>

---

**功能：**【标准化降水蒸散指数】。基于 Log-Logistic 分布计算标准化降水蒸散指数。

**参数：**

&emsp;PRE: `array`。降水量（mm）。

&emsp;PET: `array`。潜在蒸散量（mm）。

**可选参数：**

&emsp; Axis = `int`。计算轴。如果不设置（None），多维数据会将所有数据展开到一维计算。

&emsp; Scale = `int`。时间尺度。默认为 1。例如：1月、3月或其他。

&emsp; Periodicity = `int`。周期。默认为 12。例如：月数据可以以 12 为周期。

::: warning 注意

Scale、Periodicity 基于计算轴！

:::

**返回：**`array`。

**参考文献：**

&emsp;Vicente-Serrano S M , S Beguería, JI López-Moreno. A Multiscalar Drought Index Sensitive to Global Warming: The Standardized Precipitation Evapotranspiration Index[J]. Journal of Climate, 2010, 23(7):1696-1718.  

---

