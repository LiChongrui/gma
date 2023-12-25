---
title: SPI
date: 2023-08-25
sidebar: false
---

## gma.climet.Index.**SPI**(*PRE, Axis = None, Scale = 1, Periodicity = 12, Distribution = 'Gamma', FitMethod = 'MLE', Calibration = None*) <Badge text="1.0.10 +"/>

---

**功能：**【标准化降水指数】。基于 Gamma 分布计算标准化降水指数。

**参数：**

&emsp;PRE: `array`。降水量（mm）。

**可选参数：**

&emsp; Axis = `int`。计算轴。如果不设置（None），多维数据会将所有数据展开到一维计算。

&emsp; Scale = `int`。时间尺度。默认为 1。例如：1月、3月或其他。

&emsp; Periodicity = `int`。周期。默认为 12。例如：月尺度可以以 12 为周期，日尺度可以以 365 为周期。

&emsp; Distribution = `str`<Badge text="1.1.1 +"/>。用于内部拟合/变换计算的分布类型。默认为 Gamma。

::: tip 支持的分布类型

'Gamma'：伽马分布；

'LogLogistic'：对数逻辑斯蒂分布；

'Pearson3'：泊松 III 分布。

:::

&emsp; FitMethod = `str` <Badge text="2.0.4 +"/>。用于内部拟合/变换计算的参数估计方法。默认为 MLE。

::: tip 支持的分布类型

'MLE'：最大似然估计；

'LMoment'(PWD)：L-矩估计（概率加权矩）；

'LMoment'：L-矩估计。

:::

&emsp; Calibration = `list||slice||None`<Badge text="2.0.4 +"/>。提取参与内部参数拟合运算的数据（基于周期）。默认（None）为全部数据。

**返回：**`array`。

**参考文献：**

&emsp;McKee T B, Doesken N J, Kleis J. The relationship of drought frequency and duration to time scales[R]. Eighth Conf. on Applied Climatology, Anaheim, CA: American Meteor Society, 1993.

---

**示例 ：**

```python
from gma import climet
```
*基于 Excel 表数据（下载 [示例数据](/climet/PRE_ET0.xlsx)）*
```python
import pandas as pd
# 读取数据。Excel 数据有一列，为 PRE 降水，共 480 个数据 
Data = pd.read_excel('PRE_ET0.xlsx')
# 提取 PRE 用于 SPI 运算
PRE = Data['PRE'].values
# 分别计算1个月、3个月、6个月、12个月、24个月、60个月尺度的 SPI 数据
SPI1 = climet.Index.SPI(PRE)
SPI3 = climet.Index.SPI(PRE, Scale = 3)
SPI6 = climet.Index.SPI(PRE, Scale = 6)
SPI12 = climet.Index.SPI(PRE, Scale = 12)
SPI24 = climet.Index.SPI(PRE, Scale = 24)
SPI60 = climet.Index.SPI(PRE, Scale = 60)
# 将结果保存到文件
OUT = pd.DataFrame([SPI1, SPI3, SPI6, SPI12, SPI24, SPI60],
                   index = ['SPI1','SPI3','SPI6','SPI12','SPI24','SPI60']).T
OUT.to_excel(r'.\SPI.xlsx', index = False)
```
> 对不同尺度 SPI 结果进行绘制

![](/climet/SPIPlot.svg)

> 绘图代码参考：[SPEI](/UserGuide/climet/SPEI.html)

*基于栅格数据（下载 [示例数据](/climet/PRE_ET0.7z)）*

```python
import numpy as np
from gma import io
# 读取数据集
PRESet = io.Open('PRE_Luoyang_1981-2020.tif')
PRE = PRESet.ToArray()
PRE[PRE == PRESet.NoData] = np.nan
# 读取的数据为三维数据（波段，行，列），第一维为时间序列（月数据）。因此按照轴 0 来计算
SPI1 = climet.Index.SPI(PRE, Axis = 0)
SPI3 = climet.Index.SPI(PRE, Axis = 0, Scale = 3)
SPI6 = climet.Index.SPI(PRE, Axis = 0, Scale = 6)
SPI12 = climet.Index.SPI(PRE, Axis = 0, Scale = 12)
SPI24 = climet.Index.SPI(PRE, Axis = 0, Scale = 24)
SPI60 = climet.Index.SPI(PRE, Axis = 0, Scale = 60)
# 存储计算结果
S = [1,3,6,12,24,60]
for i in S:
	# 保存所有结果中的非全 nan 波段。即：去除时间尺度累积时序列前无效的波段。
    io.SaveArrayAsRaster(eval(f'SPI{i}')[i-1:],
                         fr'.\1981-2020_SPI{i}.tif', 
                         Projection = PRESet.Projection,
                         Transform = PRESet.GeoTransform, 
                         DataType = 'Float32', 
                         NoData = np.nan)  
```
> 绘制最后一个月（2020年12月）计算结果（绘图代码请参考：[PenmanMonteith](/UserGuide/climet/ET0/PenmanMonteith.html)）

![](/climet/SPI.webp)