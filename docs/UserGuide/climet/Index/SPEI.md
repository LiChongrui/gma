---
title: SPEI
date: 2023-08-25
sidebar: false
---

## gma.climet.Index.**SPEI**(*PRE, PET, Axis = None, Scale = 1, Periodicity = 12, Distribution = 'LogLogistic', FitMethod = 'LMoment', Calibration = None*)<Badge text="1.0.10 +"/>

---

**功能：**【标准化降水蒸散指数】。基于 Log-Logistic 分布计算标准化降水蒸散指数。

**参数：**

&emsp;PRE: `array`。降水量（mm）。

&emsp;PET: `array`。潜在蒸散量（mm）。

**可选参数：**

&emsp; Axis = `int`。计算轴。如果不设置（None），多维数据会将所有数据展开到一维计算。

&emsp; Scale = `int`。时间尺度。默认为 1。例如：1月、3月或其他。

&emsp; Periodicity = `int`。周期。默认为 12。例如：月数据可以以 12 为周期。

&emsp; Distribution = `str` <Badge text="1.1.1 +"/>。用于内部拟合/变换计算的分布类型。默认为 LogLogistic。

::: tip 支持的分布类型

'Gamma'：伽马分布；

'LogLogistic'：对数逻辑斯蒂分布；

'Pearson3'：泊松 III 分布。

:::

&emsp; FitMethod = `str` <Badge text="2.0.4 +"/>。用于内部拟合/变换计算的参数估计方法。默认为 LMoment。

::: tip 支持的分布类型

'MLE'：最大似然估计；

'LMoment'(PWD)：L-矩估计（概率加权矩）；

'LMoment'：L-矩估计。

:::

&emsp; Calibration = `list||slice||None`<Badge text="2.0.4 +"/>。提取参与内部参数拟合运算的数据（基于周期）。默认（None）为全部数据。

**返回：**`array`。

**参考文献：**

&emsp;Vicente-Serrano S M , S Beguería, JI López-Moreno. A Multiscalar Drought Index Sensitive to Global Warming: The Standardized Precipitation Evapotranspiration Index[J]. Journal of Climate, 2010, 23(7):1696-1718.  

---

**示例：**

```python
from gma import climet
```
*基于 Excel 表数据（下载 [示例数据](/climet/PRE_ET0.xlsx)）*
```python
import pandas as pd
Data = pd.read_excel('PRE_ET0.xlsx')
PRE = Data['PRE'].values
ET0 = Data['ET0'].values

# 分别计算1个月、3个月、6个月、12个月、24个月、60个月尺度的 SPEI 数据
SPEI1 = climet.Index.SPEI(PRE, ET0)
SPEI3 = climet.Index.SPEI(PRE, ET0, Scale = 3)
SPEI6 = climet.Index.SPEI(PRE, ET0, Scale = 6)
SPEI12 = climet.Index.SPEI(PRE, ET0, Scale = 12)
SPEI24 = climet.Index.SPEI(PRE, ET0, Scale = 24)
SPEI60 = climet.Index.SPEI(PRE, ET0, Scale = 60)
# 将结果保存到文件
OUT = pd.DataFrame([SPEI1, SPEI3, SPEI6, SPEI12, SPEI24, SPEI60],
                   index = ['SPEI1','SPEI3','SPEI6','SPEI12','SPEI24','SPEI60']).T
OUT.to_excel(r'.\SPEI.xlsx', index = False)
```
> 对不同尺度 SPEI 结果进行绘制

![](/climet/SPEIPlot.svg)

> 绘图代码示例：
```python
from gma import osf
import matplotlib.pyplot as plt
PAR = {'font.sans-serif': 'Times New Roman',
       'axes.unicode_minus': False,
      }
plt.rcParams.update(PAR)

## 标记一下不同时间尺度结果变量的不同
S = [1,3,6,12,24,60]
## 准备横坐标（年份）的标签
X = range(len(PRE))
Date = osf.DateSeries('198101','202101',DateDelta='M', Format='%Y%m').strftime('%Y-%m')

## 循环绘制 6 个尺度的 SPEI 结果
plt.figure(figsize = (18, 14), dpi = 300)
for i in range(6):
    ax = plt.subplot(4, 2, i + 1) 
    ### 绘制数据
    ax.plot(X, eval(f'SPEI{S[i]}'), linewidth = 0.8, c = 'gray')
    ### 添加图例
    ax.legend([f'SPEI{S[i]}'],frameon = False)
    ### 添加横坐标标签
    ax.set_xticks(X[::72], Date[::72], rotation = 0)
    ### 定义横纵坐标显示范围
    ax.set_xlim(-12)
    ax.set_ylim(-3.8, 3.8)
    ### 绘制干（-1）湿（1）分界线
    plt.axhline(y = -1, ls = (0,(6,6)), c = "r", linewidth = 0.4)
    plt.axhline(y = 1, ls = (0,(6,6)), c = "b", linewidth = 0.4)
    ### 绘制其他网格
    ax.grid(True, linestyle = (0,(6,6)), linewidth = 0.3)
## 修改子图边距
plt.subplots_adjust(wspace = 0.04, hspace = 0.18)
plt.show()
```

*基于栅格数据（下载 [示例数据](/climet/PRE_ET0.7z)）*

```python
import numpy as np
from gma import io
# 读取数据集
PRESet = io.ReadRaster('PRE_Luoyang_1981-2020.tif')
ET0Set = io.ReadRaster('ET0_Luoyang_1981-2020.tif')
PRE = PRESet.ToArray()
ET0 = ET0Set.ToArray()
# 读取的数据为三维数据（波段，行，列），第一维为时间序列（月数据）。因此按照轴 0 来计算
SPEI1 = climet.Index.SPEI(PRE, ET0, Axis = 0)
SPEI3 = climet.Index.SPEI(PRE, ET0, Axis = 0, Scale = 3)
SPEI6 = climet.Index.SPEI(PRE, ET0, Axis = 0, Scale = 6)
SPEI12 = climet.Index.SPEI(PRE, ET0, Axis = 0, Scale = 12)
SPEI24 = climet.Index.SPEI(PRE, ET0, Axis = 0, Scale = 24)
SPEI60 = climet.Index.SPEI(PRE, ET0, Axis = 0, Scale = 60)
# 存储计算结果
S = [1,3,6,12,24,60]
for i in S:
	# 保存所有结果中的非全 nan 波段。即：去除时间尺度累积时序列前无效的波段。
    io.SaveArrayAsRaster(eval(f'SPEI{i}')[i-1:],
                         fr'.\1981-2020_SPEI{i}.tif', 
                         Projection = PRESet.Projection,
                         Transform = PRESet.GeoTransform, 
                         DataType = 'Float32', 
                         NoData = np.nan)  
```
>绘制最后一个月（2020年12月）计算结果（绘图代码请参考：[PenmanMonteith](/UserGuide/climet/ET0/PenmanMonteith.html)）

![](/climet/SPEI.webp)