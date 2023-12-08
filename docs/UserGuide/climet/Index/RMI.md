---
title: RMI
date: 2023-12-08
sidebar: false
---

## gma.climet.Index.**RMI**(*PRE, PET, Axis = None, Scale = 1*) <Badge text="2.0.4 +"/>

---

**功能：**【相对湿润度指数】。计算相对湿润度指数。

**参数：**

&emsp;PRE: `array`。降水量（mm）。

&emsp;PET: `array`。潜在蒸散量（mm）。

**可选参数：**

&emsp; Axis = `int||None`。计算轴。如果不设置（None），多维数据会将所有数据展开到一维计算。

&emsp; Scale = `int`。时间尺度。默认为 1。例如：1月、3月或其他。

::: warning 注意

Scale 基于计算轴！

:::

**返回：**`array`。

---

**示例 ：**

```python
from gma import climet
```
*基于 Excel 表数据（下载 [示例数据](/climet/PRE_ET0.xlsx)）*
```python
import pandas as pd
Data = pd.read_excel('PRE_ET0.xlsx')
PRE = Data['PRE'].values
ET0 = Data['ET0'].values

# 分别计算1个月、3个月、6个月、12个月、24个月、60个月尺度的 RMI 数据
RMI1 = climet.Index.RMI(PRE, ET0)
RMI3 = climet.Index.RMI(PRE, ET0, Scale = 3)
RMI6 = climet.Index.RMI(PRE, ET0, Scale = 6)
RMI12 = climet.Index.RMI(PRE, ET0, Scale = 12)
RMI24 = climet.Index.RMI(PRE, ET0, Scale = 24)
RMI60 = climet.Index.RMI(PRE, ET0, Scale = 60)

# 将结果保存到文件
OUT = pd.DataFrame([RMI1, RMI3, RMI6, RMI12, RMI24, RMI60],
                   index = ['RMI1','RMI3','RMI6','RMI12','RMI24','RMI60']).T
OUT.to_excel(r'.\RMI.xlsx', index = False)
```
> 对不同尺度 PAP 结果进行绘制

![](/climet/RMIPlot.svg)

