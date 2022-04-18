---
title: 栅格分析
date: 2022-03-20
---

**&emsp;&emsp;栅格分析** 为 **gma.raa** 内所有栅格处理操作相关函数的详细功能、参数设置和引用方法说明。如果您想了解 gma 所有函数的整体情况，请移步 [函数列表](/Functions/Function.html) 。

## DEM 类<Badge text="1.0.7 +"/>

::: theorem

**功能：** 【DEM 分析】。利用 DEM 数据实现地形分析。

:::

### Roughness
::: theorem

**引用：** gma.raa.DEM.Roughness(InFile, OutFile, OutFormat = 'GTiff', ComputeEdges = True, Band = 1)

**功能：**【粗糙度】。从任何支持的 DEM 栅格文件计算粗糙度！

**参数：** 

&emsp;InFile：`str`。输入栅格路径。

&emsp;OutFile：`str`。输出栅格路径。

**可选参数：**

&emsp;OutFormat  = `str`。输出栅格文件格式。默认为 GTiff，其他格式详见 rasp.ToOtherFormat 函数。

&emsp;ComputeEdges = `bool`。是否计算栅格边缘数据和无数据值附近的数据。默认（True）是，其他设置值均视为否（False）。

&emsp;Band = `int`。需要计算的波段，编号从 1 开始。默认（1）为第一个波段。

::: 

### HillShade

::: theorem

**引用：** gma.raa.DEM.HillShade(InFile, OutFile, OutFormat = 'GTiff', ComputeEdges = True, Band = 1, ZFactor = 1.0, Scale = 1.0, Azimuth = 315.0, Altitude = 45.0, Combined = False, ZevenbergenThorne = False)

**功能：**【山体阴影】。从任何支持的 DEM 栅格文件计算山体阴影！

**参数：** 

&emsp;InFile：`str`。输入栅格路径。

&emsp;OutFile：`str`。输出栅格路径。

**可选参数：**

&emsp;OutFormat  = `str`。输出栅格文件格式。默认为 GTiff，其他格式详见 rasp.ToOtherFormat 函数。

&emsp;ComputeEdges = `bool`。是否计算栅格边缘数据和无数据值附近的数据。默认（True）是，其他设置值均视为否（False）。

&emsp;Band = `int`。需要计算的波段，编号从 1 开始。默认（1）为第一个波段。

&emsp;ZFactor = `float`。垂直放大比例。默认为 1 。

&emsp;Scale = `float`。垂直单位与水平单位的比值。默认为 1 。若垂直单位为 m 而水平单位为 °（即栅格坐标系为地理坐标系），可设置 Scale = 111120。

&emsp;Azimuth = `float`。光线方位角（°）。默认为 315 。

&emsp;Altitude = `float`。光线高度角（°）。默认为 45 。

&emsp;Combined = `bool`。是否计算混合阴影。默认不计算（False）。不为 True 的设置值均视为否（False）。

&emsp;ZevenbergenThorne = `False`。是否改用 ZevenbergenThorne 法计算。默认（False）不使用（即采用 Horn 法计算）。不为 True 的设置均视为 Fasle。

::: 

### Slope

::: theorem

**引用：** gma.raa.DEM.Slope(InFile, OutFile, OutFormat = 'GTiff', ComputeEdges = True, Band = 1, Scale = 1.0, UseDegree = True, ZevenbergenThorne = False)

**功能：**【坡度】。从任何支持的 DEM 栅格文件计算坡度！

**参数：** 

&emsp;InFile：`str`。输入栅格路径。

&emsp;OutFile：`str`。输出栅格路径。

**可选参数：**

&emsp;OutFormat  = `str`。输出栅格文件格式。默认为 GTiff，其他格式详见 rasp.ToOtherFormat 函数。

&emsp;ComputeEdges = `bool`。是否计算栅格边缘数据和无数据值附近的数据。默认（True）是，其他设置值均视为否（False）。

&emsp;Band = `int`。需要计算的波段，编号从 1 开始。默认（1）为第一个波段。

&emsp;Scale = `float`。垂直单位与水平单位的比值。默认为 1 。若垂直单位为 m 而水平单位为 °（即栅格坐标系为地理坐标系），可设置 Scale = 111120。

&emsp;UseDegree = `bool`。是否使用度（°）来表示坡度。默认（True）使用。若为否（False），则采用百分比（%）表示坡度。

&emsp;ZevenbergenThorne = `False`。是否改用 ZevenbergenThorne 法计算。默认（False）不使用（即采用 Horn 法计算）。不为 True 的设置均视为 Fasle。

::: 

### Aspect

::: theorem

**引用：** gma.raa.DEM.Aspect(InFile, OutFile, OutFormat = 'GTiff', ComputeEdges = True, Band = 1,  ZevenbergenThorne = False, Trigonometric = False, ZeroForFlat = False)

**功能：**【坡向】。从任何支持的 DEM 栅格文件计算坡向！

**参数：** 

&emsp;InFile：`str`。输入栅格路径。

&emsp;OutFile：`str`。输出栅格路径。

**可选参数：**

&emsp;OutFormat  = `str`。输出栅格文件格式。默认为 GTiff，其他格式详见 rasp.ToOtherFormat 函数。

&emsp;ComputeEdges = `bool`。是否计算栅格边缘数据和无数据值附近的数据。默认（True）是，其他设置值均视为否（False）。

&emsp;Band = `int`。需要计算的波段，编号从 1 开始。默认（1）为第一个波段。

&emsp;ZevenbergenThorne = `False`。是否改用 ZevenbergenThorne 法计算。默认（False）不使用（即采用 Horn 法计算）。不为 True 的设置均视为 Fasle。

&emsp;Trigonometric = `bool`。是否使用（三角）角度。默认（False）不使用（即使用方位角）。不为 True 的设置均视为 Fasle。

<Boxx type='tip' title='提示' content='方位角角度：以正北方向为 0°，依顺时针方向到目标方向线之间的水平夹角。</br>（三角）角度：以正东方向为 0°。依逆时针针方向到目标方向线之间的水平夹角。'/>

&emsp;ZeroForFlat = `bool`。是否将坡向为 0°的的区域赋值为 0。默认不赋值为 0 （即赋值为 NoData(-9999)）。不为 True 的设置均视为 Fasle。

::: 

### TRI

::: theorem

**引用：** gma.raa.DEM.TRI(InFile, OutFile, OutFormat = 'GTiff', ComputeEdges = True, Band = 1)

**功能：**【地形耐用度指数】。从任何支持的 DEM 栅格文件计算地形耐用度指数！

**参数：** 

&emsp;InFile：`str`。输入栅格路径。

&emsp;OutFile：`str`。输出栅格路径。

**可选参数：**

&emsp;OutFormat  = `str`。输出栅格文件格式。默认为 GTiff，其他格式详见 rasp.ToOtherFormat 函数。

&emsp;ComputeEdges = `bool`。是否计算栅格边缘数据和无数据值附近的数据。默认（True）是，其他设置值均视为否（False）。

&emsp;Band = `int`。需要计算的波段，编号从 1 开始。默认（1）为第一个波段。

:::

### TPI

::: theorem

**引用：** gma.raa.DEM.TPI(InFile, OutFile, OutFormat = 'GTiff', ComputeEdges = True, Band = 1)

**功能：**【地形位置指数】。从任何支持的 DEM 栅格文件计算地形位置指数！

**参数：** 

&emsp;InFile：`str`。输入栅格路径。

&emsp;OutFile：`str`。输出栅格路径。

**可选参数：**

&emsp;OutFormat  = `str`。输出栅格文件格式。默认为 GTiff，其他格式详见 rasp.ToOtherFormat 函数。

&emsp;ComputeEdges = `bool`。是否计算栅格边缘数据和无数据值附近的数据。默认（True）是，其他设置值均视为否（False）。

&emsp;Band = `int`。需要计算的波段，编号从 1 开始。默认（1）为第一个波段。

:::
