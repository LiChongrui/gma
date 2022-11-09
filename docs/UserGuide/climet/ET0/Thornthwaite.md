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

**可选参数：**

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

**示例：**

```python
import gma

TEM = [0.95, 2.15, 5.75, 13, 19.95, 23.7, 24.8, 23.9, 20.15, 15.2, 10.6, 3.4,
       0.0, 3.8, 9.85, 14.95, 20.7, 25.05, 26.55, 24.5, 19.55, 12.65, 5.9, 2.4]

THD = gma.climet.ET0.Thornthwaite(TEM, LAT = 34.17, StartYear = 1980)
```

> 绘制计算结果

![](/climet/Thornthwaite.svg)

> 绘图代码示例

```python
import matplotlib.pyplot as plt
PAR = {'font.sans-serif': 'Times New Roman',
       'axes.unicode_minus': False,
      }
plt.rcParams.update(PAR)

X = gma.osf.DateSeries('198101','198301',DateDelta='M', Format='%Y%m').strftime('%Y-%m')

plt.figure(figsize = (10, 5), dpi = 300)

### 绘制数据
plt.plot(X, THD, linewidth = 0.8, c = 'gray')
plt.xticks(X[::2])

### 绘制其他网格
plt.grid(True, linestyle = (0,(6,6)), linewidth = 0.3)

plt.xlabel('Date')
plt.ylabel('Thornthwaite PET(mm)')
plt.show()

```
