---
title: PCI
date: 2024-04-10
sidebar: false
---

## gma.climet.Index.**PCI**(*PRE, Axis = None, Scale = 1, Periodicity = 12*) <Badge text="2.0.8 +"/>

---

**功能：**【降水集中度指数】。计算降水集中度指数（Precipitation Concentration Index）。

**参数：**

&emsp;PRE: `array`。降水量（mm）。

**可选参数：**

&emsp; Axis = `int`。计算轴。如果不设置（None），多维数据会将所有数据展开到一维计算。

&emsp; Scale = `int`。时间尺度。默认为 1。例如：1月、3月或其他。

&emsp; Periodicity = `int`。周期。默认为 12。

::: warning 注意

Scale、Periodicity 基于计算轴！

:::

**返回：**`array`。

::: warning 注意

PCI 指数会缩减 Axis 上数据数量。在 Axis 上，每个周期仅有一组结果！

:::

---

**示例 ：**

```python
from gma import climet
```
*基于 Excel 表数据（下载 [示例数据](/climet/PRE_ET0.xlsx)）*
```python
from gma import io

ELSXLayer = io.ReadVector('PRE_ET0.xlsx')
Data = ELSXLayer.ToDataFrame()

PRE = Data['PRE'].values

# 分别计算1个月、3个月、6个月、12个月、24个月、60个月尺度的 PCI 指数
PCI1 = climet.Index.PCI(PRE)
PCI3 = climet.Index.PCI(PRE, Scale = 3)
```
> 不同尺度 PCI 结果

![](/climet/PCIPlot.svg)

