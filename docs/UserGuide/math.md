---
title: 数学运算
date: 2021-10-30
---

**&emsp;&emsp;数学运算** 为 **gma.math** 内所有数学方法相关函数的详细功能、参数设置和引用方法说明，如果您想了解 gma 所有函数的整体情况，请移步 [函数功能列表](/Functions/Function.html) 。

## _DFToNumeric

::: theorem
**引用：** gma.index._DFToNumeric(DataFrame)

**功能：**【强制转换为数字】。强制转换 DataFrame 中非数字字符串为 NAN。

**参数：**

&emsp;DataFrame：`DataFrame` 。需要转换的 DataFrame。

**返回：**`DataFrame`。
::: 


## FillNoData

::: theorem
**引用：** gma.index.FillNoData(Data, FillValue = None, Method = 'linear', **kwargs)

**功能：**【填充缺失值】。对缺失值或异常值值进行插值替换。

**参数：**

&emsp;Data：`list||tuple||Series||DataFrame||array` 。需要插补的数据。

**可选参数：**

&emsp;FillValue = `float||list`。 需要进行插补的缺失值。默认不设置（None）。

<Boxx type='warning' title='注意' content='1.当 FillValue 为列表时，列表内所有值都将被插补。<br> 2.数据内原有的NAN、INF以及不能被转化为数字的字符串等异常值也将被插补。' />

&emsp;Method = `str`。 插补方法。默认线性插值（linear）。

<Boxx type='tip' title='其他插补方法' content='time（时间）, index（索引）, values（序列值），pad（前向填充），nearest（最邻近），zero（零值），slinear（滑动线性），quadratic（2次方），cubic（3次方），spline（样条函数），barycentric（重心），polynomial（分段多项式），from_derivatives（衍生），krogh（克罗格），piecewise_polynomial（分段多项式），pchip（分段三次 Hermite 多项式插值），akima（akima 光滑插值），cubicspline（3次样条）等。'/>

&emsp;**kwargs。传递给插值函数的其他参数。例如：Method 为 polynomial 或 spline 需要设置 order（阶数），默认阶数为 3。

**返回：** Series，DataFrame 返回 `输入类型`；list，tuple，array 返回 `array`。

::: 

## Smooth 类

::: theorem

**引用：** gma.index.Smooth(Data, WindowSize, Times = 1)

**功能：** 数据平滑（滤波）。

**初始化：**

&emsp;Data：1D `array`。需要平滑的 1 维数据。

&emsp;WindowSize：`int`。平滑窗口大小。必须为正奇数。

&emsp;Times = `int`。平滑次数。默认平滑 1 次。

::: 

::: warning 注意
类内函数引用前请先初始化 `Smooth` 类！
::: 

### SavitzkyGolay

::: theorem

**引用：** gma.math.Smooth().SavitzkyGolay(Polyorder = 2, Delta = 1, Mode = 'interp')

&emsp;注意：*引用前请先初始化 `Smooth` 类。*

**功能：**【Savitzky-Golay】。利用 SavitzkyGolay 方法对数据进行平滑。

**可选参数：**

&emsp;Polyorder = `int`。平滑多项式阶数。默认为 2 。

&emsp;Delta = `float`。将应用过滤器的样本间距。默认为 1。

&emsp;Mode = `str`。边缘数据处理方法。默认为 插补（interp）。

<Boxx type='tip' title='其他方法' content='其他处理方法还包括：mirror，nearest，wrap。' />

**返回：**`array`。

:::
	
### MovingAverage
::: theorem

**引用：** gma.math.Smooth().MovingAverage(Mode = 'nearest')

&emsp;  注意：*引用前请先初始化 `Smooth` 类。*

**功能：**【滑动平均】。利用滑动平均法对数据进行平滑

**可选参数：**

&emsp;Mode = `str`。边缘数据处理方法。默认为 采用最近数据填充（nearest）。

<Boxx type='tip' title='其他方法' content='其他处理方法还包括：mirror，interp，wrap。' />

**返回：**`array`。
:::

## Evaluation 类

::: theorem

**引用：** gma.index.Evaluation(Measure, Simulation)

**功能**：数据评估。

**初始化：**

&emsp;Measure：`list||array`。实测数据。

&emsp;Simulation：`list||array`。模拟数据。

::: 

::: warning 注意
类内函数引用前请先初始化 `Evaluation` 类！
::: 

### RMSE
::: theorem

**引用：** gma.index.Evaluation().RMSE()

&emsp;  注意：*引用前请先初始化 `Evaluation` 类。*

**功能：**【RMSE】。均方根误差。

**返回：**`float`。

::: 

### NRMSE

::: theorem

**引用：** gma.index.Evaluation().NRMSE()

&emsp;  注意：*引用前请先初始化 `Evaluation` 类。*

**功能：**【NRMSE】。归一化均方根误差。

**返回：**`float`。

::: 

### D

::: theorem

**引用：** gma.index.Evaluation().D()

&emsp;  注意：*引用前请先初始化 `Evaluation` 类。*

**功能：**【D】。D指标。

**返回：**`float`。

::: 

### CORR
::: theorem

**引用：** gma.index.Evaluation().CORR(Method = 'pearson')

&emsp;  注意：*引用前请先初始化 `Evaluation` 类。*

**功能：**【r，P】。相关系数和显著性水平。

**可选参数：** 

&emsp;Method = `str`。默认计算皮尔逊相关（pearson）。
        
<Boxx type='tip' title='其他支持的方法' content='kendall（肯德尔秩相关），spearman（斯皮尔曼相关）。' />

**返回：**`tuple`。

::: 

### R2

::: theorem

**引用：** gma.index.Evaluation().R2()

&emsp;  注意：*引用前请先初始化 `Evaluation` 类。*

**功能：**【R2】。决定系数。

**返回：**`float`。

::: 

### MaxAE

::: theorem

**引用：** gma.index.Evaluation().MaxAE()

&emsp;  注意：*引用前请先初始化 `Evaluation` 类。*

**功能：**【MaxAE】。最大绝对误差。

**返回：**`float`。

::: 

### Select

::: theorem

**引用：** gma.index.Evaluation().Select(Method = 'ALL')

&emsp;  注意：*引用前请先初始化 `Evaluation` 类。*

**功能：**【选择方法】。按选择的方法返回结果。

**可选参数：** 

&emsp;Method = `str||list||tuple||set`。默认为输出所有方法的结果（ALL）。

<Boxx type='tip' title='其他参数设置' content='1. list、tuple 或 set: 列表、元组或集合内所有方法（ Evaluation 已经定义过算法）的结果。<br>2. str: 单个评价方法（Evaluation 已经定义过算法，例如 RMSE ）的结果。' />

<Boxx type='warning' title='注意' content='选择的方法只支持默认的可选参数。例如 CORR，其计算相关系数的方法只能为 pearson，不能传入其他方法。'/>

**返回：**`dict`。

::: 

### Methods

::: theorem

**引用：** gma.index.Evaluation().Methods()

&emsp;  注意：*引用前请先初始化 `Evaluation` 类。*

**功能：**【记录方法】。记录 Evaluation 类中所有的评估方法。

**返回：**`list`。
::: 
