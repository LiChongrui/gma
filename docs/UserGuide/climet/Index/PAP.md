---
title: PAP
date: 2022-06-26
sidebar: false
---

## gma.climet.Index.**PAP**(*PRE, Axis = None, Scale = 1, Periodicity = 12*) <Badge text="1.0.10 +"/>

---

**功能：**【降水距平百分率】。计算降水值到多年平均值的波动情况。

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

# 分别计算1个月、3个月、6个月、12个月、24个月、60个月尺度的 SPI 数据
PAP1 = climet.Index.PAP(PRE)
PAP3 = climet.Index.PAP(PRE, Scale = 3)
PAP6 = climet.Index.PAP(PRE, Scale = 6)
PAP12 = climet.Index.PAP(PRE, Scale = 12)
PAP24 = climet.Index.PAP(PRE, Scale = 24)
PAP60 = climet.Index.PAP(PRE, Scale = 60)

# 将结果保存到文件
OUT = pd.DataFrame([PAP1, PAP3, PAP6, PAP12, PAP24, PAP60],
                   index = ['PAP1','PAP3','PAP6','PAP12','PAP24','PAP60']).T
OUT.to_excel(r'.\PAP.xlsx', index = False)
```
> 对不同尺度 PAP 结果进行绘制

![](/climet/PAPPlot.svg)

> 绘图代码参考：[SPEI](/UserGuide/climet/SPEI.html)

*基于栅格数据（下载 [示例数据](/climet/PRE_ET0.7z)）*

```python
import numpy as np
from gma import io
# 读取数据集
PRESet = gma.Open('PRE_Luoyang_1981-2020.tif')
PRE = PRESet.ToArray()
PRE[PRE == PRESet.NoData] = np.nan
# 读取的数据为三维数据（波段，行，列），第一维为时间序列（月数据）。因此按照轴 0 来计算
PAP1 = climet.Index.PAP(PRE, Axis = 0)
PAP3 = climet.Index.PAP(PRE, Axis = 0, Scale = 3)
PAP6 = climet.Index.PAP(PRE, Axis = 0, Scale = 6)
PAP12 = climet.Index.PAP(PRE, Axis = 0, Scale = 12)
PAP24 = climet.Index.PAP(PRE, Axis = 0, Scale = 24)
PAP60 = climet.Index.PAP(PRE, Axis = 0, Scale = 60)
# 存储计算结果
S = [1,3,6,12,24,60]
for i in S:
	# 保存所有结果中的非全 nan 波段。即：去除时间尺度累积时序列前无效的波段。
    io.SaveArrayAsRaster(eval(f'PAP{i}')[i-1:],
                         fr'.\1981-2020_PAP{i}.tif', 
                         Projection = PRESet.Projection,
                         Transform = PRESet.GeoTransform, 
                         DataType = 'Float32', 
                         NoData = np.nan)  
```

