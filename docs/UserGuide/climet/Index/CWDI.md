---
title: CWDI
date: 2024-07-01
sidebar: false
---

## gma.climet.Index.**CWDI**(*PRE, ETc, Axis=None, Weights=[0.3, 0.25, 0.2, 0.15, 0.1], DurationPerWeight=10*) <Badge text="2.0.11 +"/>

---

**功能：**【作物水分亏缺指数】。计算作物水分亏缺指数（Crop Water Deficit Index）。

**参数：**

&emsp;PRE: `array`。降水量（mm）。

&emsp;ETc: `array`。作物需水量（mm）。

**可选参数：**

&emsp; Axis = `int||None`。计算轴。如果不设置（None），多维数据会将所有数据展开到一维计算。

&emsp; Weights = `list`。分组权重。默认为 [0.3, 0.25, 0.2, 0.15, 0.1]。

&emsp; DurationPerWeight = `int`。与权重对应，每个权重系数对应的时长。默认为 10。

::: tip 每日 CWDI

用以计算每日 CWDI 的数据为当日及之前 len(Weights) × DurationPerWeight 日数据。默认情况下为 50 天（组）。

:::

**返回：**`array`。单位为 %。

**参考文献：**

&emsp;Li Chongrui, You Songcai, Wu Yongfeng, Wang Yihao. Improved crop water deficit index for monitoring drought disaster change process of spring maize in the Northeast China[J]. Transactions of the Chinese Society of Agricultural Engineering (Transactions of the CSAE),  2019, 35(21): 175-185. DOI: 10.11975/j.issn.1002-6819.2019.21.021

---

**示例 ：*基于 Excel 表数据（下载 [示例数据](/climet/PRE_ET0.xlsx)）***

```python
from gma import climet, io

ELSXLayer = io.ReadVector('PRE_ET0.xlsx')
Data = ELSXLayer.ToDataFrame()

PRE = Data['PRE'].values
ETc = Data['ET0'].values    ##这里仅做演示，实际使用时请使用真实的ETc。

# 计算 CWDI 指数
CWDI = climet.Index.CWDI(PRE, ETc)
```
> CWDI 计算结果

![](/climet/CWDI.svg)
