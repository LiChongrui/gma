---
title: 默认设置
date: 2021-10-29
---

## 默认参数

&emsp;&emsp; 默认参数已经内置在 key 文件中，**下表列出 gma 定义了的参数。**

| 变量 / 函数 | 类型 | 说明 | 详细介绍 |
| :----| :---- | :---- | :----- |
| RasterFormat | 集合 | 支持的栅格数据驱动 | AAIGrid，BT，CALS，COG，DTED，EHdr，ENVI，ERS，EXR，FIT，GIF，GPKG，GRIB，GS7BG，GSAG，GSBG，GTiff，HDF4Image,HF2，HFA，ISCE，ISIS2，ISIS3，JP2OpenJPEG，JPEG，LAN，MBTiles，XPM，XYZ，netCDF，MFF2，MRF，NITF，PAux，PCIDSK，PCRaster，PNG，RST，Rasterlite，SIGDEM，USGSDEM，VICAR，VRT，BMP |
| VectorFormat | 集合 | 支持的矢量数据驱动 | ESRI Shapefile，PCIDSK，PDS4，PDF，MBTiles，MapInfo File，Memory，CSV，GML，LIBKML，KML，GeoJSON，OGR_GMT，GPKG，SQLite，WAsP，FlatGeobuf，Geoconcept，GeoRSS，ODS，XLSX，JML，VDV，MVT，MapML |
| DataType | 字典 | 数据类型 | Unknown:0，Byte:1，UInt16:2，Int16:3，UInt32:4，Int32:5，Float32:6，Float64:7，CInt16:8，CInt32:9，CFloat32:10，CFloat64:11 |
| ResampleMethod | 字典 | 重采样方法 | Nearest Neighbour:0，Bilinear:1，Cubic:2，CubicSpline:3，Lanczos:4，Average:5，RMS:6，Mode:7 |
| FeatureType | 字典 | 矢量要素类型 | Unknown:0，Point:1，Line:2，Polygon:3，Multipoint:4，Multiline:5，Multipolygon:6，LinearRing:101 |
| GetGTiffOptions | 函数 | GTiff 的创建参数 | 1. 不生成 ESRI 世界文件（ .tfw ）。<br> 2. 不生成（ .RPB ）文件来描述 RPC（有理多项式系数）。<br> 3.  不设置数据位深（NBITS）。<br> 4. 默认 LZW 压缩。<br> 5.  默认通过估算生成文件大小来确定是否生成 BIGTIFF 文件。 |
| GenRCOptions | 函数 | 根据栅格驱动生成创建选项 | 支持的栅格驱动见 RasterFormat  |
| GetRasterEXTFromDriver | 函数 | 根据栅格驱动格式返回扩展名|  支持的栅格驱动见 RasterFormat   |
| GetSHPOptions | 函数 | ESRI Shapefile 的创建参数  | 1. 默认创建矢量文件的字段编码为 UTF-8 。<br> 2. 自动调整字段大小。 <br> 3. 不强制解除 .SHP、.DBF 文件 2GB 大小的限制。 <br> 4. 不生成空间索引文件（ .qix ）。 |
| GenVCOptions | 函数 | 根据矢量驱动生成创建选项 | 支持的矢量驱动见 VectorFormat   |
| GetVectorEXTFromDriver | 函数 | 根据矢量驱动格式返回扩展名 | 支持的矢量驱动见 VectorFormat |

::: warning 注意
仅可根据 变量 / 函数 查看内置设置，不能对内置设置进行修改。
:::

## 数据类型

|英文 | 中文 | 标识 / 来源 | 示例 | 扩展 |
| :--- | :---- | :---- | :---- | :---- |
|list   |列表 |[ ] |[1, 'a', 2] |可与其他类型数据进行嵌套 |
| tuple | 元组 | ( ) | (1, 2, 3) | 可与其他类型数据进行嵌套 |
| dict | 字典 | { } | {'a': 1, 'b': 2} | 可与其他类型数据进行嵌套 |
| array | 数组 | numpy.array      | [1 2]            | 可进行数组运算或向量运算 |
| mat | 矩阵     | numpy.mat        | [1 2]            | 实现数学中的矩阵运算  |
| str | 字符串 | ' ' 或 " " | 'str' |  |
| int | 整型数 |                  | 5、-1            | 包括 uint （无符号整型）和 int（有符号整型） |
| float | 浮点数 |                  | -1、1.0、6       | 主要有 float16（半精度）、float32 和 float64（双精度） |
| DataFrame | 数据帧 | pandas.DataFrame | 参考 dict        | pandas 中高效处理二维数据的组织形式 |
| Series | 数据系列 | pandas.Series | 参考 dict | pandas 中高效处理一维数据的组织形式 |
| bool | 布尔型 |  | True、False |  |
| set | 集合 | { } | {1, 2, 3} | 交、并、差、补等集合运算的常用形式 |
| def | 函数 | | 参考 Python 函数定义 |  |
