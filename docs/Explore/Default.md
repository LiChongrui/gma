---
title: 默认设置
date: 2021-10-29
---

## 默认参数

&emsp;&emsp; 默认参数已经内置在 gma.relation.key 模块中，**下表列出 gma 定义了的参数**。

| 变量 / 函数 | 类型 | 说明 | 详细介绍 |
| :----| :---- | :---- | :----- |
| RasterDataType | 字典 | 数据类型 | Unknown: 0, Byte: 1, UInt16: 2, Int16: 3, UInt32: 4, Int32: 5, Float32: 6, Float64: 7, CInt16: 8, CInt32: 9, CFloat32: 10, CFloat64: 11 |
| ResampleMethod | 字典 | 重采样方法 | Nearest Neighbour: 0, Bilinear: 1, Cubic: 2, CubicSpline: 3, Lanczos: 4, Average: 5, RMS: 6, Mode: 7 |
| FeatureType | 字典 | 矢量要素类型 | Unknown: 0, Point: 1, Line: 2, Polygon: 3, Multipoint: 4, Multiline: 5, Multipolygon: 6, LinearRing: 101 |
| FieldDataType | 字典 | 属性表字段数据类型 | Integer: 0, IntegerList:1, Real:2, RealList:3, String:4, StringList: 5, WideString: 6, WideStringList: 7, Binary: 8,  Date: 9, Time: 10, DateTime: 11, Integer64: 12, Integer64List: 13 |

::: warning 注意
仅可根据 变量 / 函数 查看内置设置，不能对内置设置进行修改。
:::

## 数据类型

|英文 | 中文 | 标识 / 来源 | 示例 | 扩展 |
| :--- | :---- | :---- | :---- | :---- |
|list   |列表 |[ ] |[1, 'a', 2] |可与其他类型数据进行嵌套 |
| tuple | 元组 | ( ) | (1, 2, 3) | 可与其他类型数据有限制的嵌套 |
| dict | 字典 | { } | {'a': 1, 'b': 2} | 可与其他类型数据进行嵌套 |
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
