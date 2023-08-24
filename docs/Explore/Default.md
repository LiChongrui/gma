---
title: 默认设置
date: 2023-08-20
---

## 默认参数

| 变量 / 函数 | 类型 | 说明 | 详细介绍 |
| :----| :---- | :---- | :----- |
| RasterDataType | 字典 | 数据类型 | Byte, UInt16, Int16, UInt32, Int32, Float32, Float64, CInt16, CInt32, CFloat32, CFloat64|
| ResampleMethod | 字典 | 重采样方法 | Nearest Neighbour, Bilinear, Cubic, CubicSpline, Lanczos, Average, RMS, Mode |
| FeatureType | 字典 | 矢量要素类型 | Point, Line, Polygon, Multipoint, Multiline, Multipolygon |

## 数据类型

|英文 | 中文 | 标识 / 来源 | 示例 | 扩展 |
| :--- | :---- | :---- | :---- | :---- |
|list   |列表 |[ ] |[1, 'a', 2] |可与其他类型数据进行嵌套 |
| tuple | 元组 | ( ) | (1, 2, 3) | 可与其他类型数据有限制的嵌套 |
| dict | 字典 | { } | {'a': 1, 'b': 2} | 可与其他类型数据进行嵌套 |
| namedtuple | 具名元组 | collections.namedtuple |M(X=1, Y=2.1) |  与字典功能类似 |
| array | 数组 | numpy.array      | [1 2]            | 可进行数组运算或向量运算 |
| mat | 矩阵     | numpy.mat        | [1 2]            | 实现数学中的矩阵运算  |
| str | 字符串 | ' ' 或 " " | 'str' |  |
| int | 整型数 |                  | 5、-1            | 包括 uint （无符号整型）和 int（有符号整型） |
| float | 浮点数 |                  | -1、1.0、6       | 主要有 float16（半精度）、float32 和 float64（双精度） |
| DataFrame | 数据帧 | pandas.DataFrame | 参考 dict        | pandas 中高效处理二维数据的组织形式 |
| Series | 数据系列 | pandas.Series | 参考 dict | pandas 中高效处理一维数据的组织形式 |
| DatetimeIndex | 日期时间索引 | pandas.DatetimeIndex | 参考 list | pandas 中高效处理一维日期时间序列的组织形式 |
| bool | 布尔型 |  | True、False |  |
| set | 集合 | { } | {1, 2, 3} | 交、并、差、补等集合运算的常用形式 |
| def | 函数 | | 参考 Python 函数定义 |  |
