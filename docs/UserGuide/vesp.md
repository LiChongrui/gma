---
title: 矢量处理
date: 2021-10-30
---

**&emsp;&emsp;矢量处理** 为 **gma.vesp** 内所有矢量处理操作相关函数的详细功能、参数设置和引用方法说明，如果您想了解 gma 所有函数的整体情况，请移步 [函数列表](/Functions/Function.html) 。

## Split

::: theorem

**引用：** gma.vesp.Split(InFile, OutPath, OutNameField = None, Separator = None, OutFormat = 'ESRI Shapefile')

**功能：**【矢量文件分解】。将矢量文件中的每个要素拆分为单个矢量文件。

**参数：** 

&emsp;InFile：`str`。输入矢量文件路径。

&emsp;OutPath：`str`。输出文件夹路径。

**可选参数：**

&emsp;OutNameField = `str||list`。标记输出文件名的字段名称或字段名称列表。默认（None）按照 <0.shp, 1.shp, ... >的方式输出。

&emsp;Separator = `str`。多字段连接方式。默认（None）不以任何进行字段连接。

<Boxx type='tips' title='说明' content='OutNameField = ["City", "Country"],  Separator = "_" <br>&emsp;> > > City_County.shp'/>

&emsp;OutFormat = `str`。输出矢量文件格式，默认为 ESRI Shapefile。其他格式详见 ToOtherFormat 函数。

:::

## Check

::: theorem

**引用：** gma.vesp.Check(InFile)

**功能：**【检查】。检查每个矢量要素的有效性。

**参数：** 

&emsp;InFile：`str`。输入矢量文件路径。

**返回：** 如果输入矢量通过检查，则返回 Pass。否则返回无效信息（dict）。无效信息组成：{ Invalid float: 无效要素的数量。Invalid layer&FID: 无效图层和图层内无效要素的FID}。

:::

## ToRaster

::: theorem

**引用：** gma.vesp.ToRaster(InFile, OutFile, Resolution, Attribute = None, OutNoData = None, OutFormat = 'GTiff')

**功能：**【矢量转栅格】。将矢量图层转换为栅格文件。

**参数：** 

&emsp;InFile：`str`。输入矢量文件路径。

&emsp;OutFile：`str`。输出栅格文件路径。

&emsp;Resolution：`int`。输出栅格的分辨率。

**可选参数：** 

&emsp;Attribute = `str`。进行转换的矢量数据的字段。如果未设置，则生成由 0 和 1 组成的栅格，0 是 nodata 值。

&emsp;OutNoData = `float`。输出栅格的值无效。默认不设置（None）无效值。

<Boxx type='warning' title='注意' content='如果 Attribute 不为 None 且 OutNoData 未设置，则 OutNoData 修改为无穷大（inf）。'/>

&emsp;OutFormat = `str`。输出栅格文件格式，默认为 GTiff。其他格式详见 rasp.ToOtherFormat 函数。

:::

## Clip

::: theorem

**引用：** gma.vesp.Clip(InFile, MethodFile, OutFile, OutFormat = 'ESRI Shapefile')

**功能：**【裁剪】。矢量裁剪矢量。

**参数：** 

&emsp;InFile：`str`。输入矢量文件路径。

&emsp;MethodFile：`str`。裁剪矢量范围文件路径。

&emsp;OutFile：`str`。输出矢量文件路径。

**可选参数：** 

&emsp;OutFormat = `str`。输出矢量文件格式，默认为 ESRI Shapefile。其他格式详见 ToOtherFormat 函数。

:::

## Erase

::: theorem

**引用：** gma.vesp.Erase(InFile, MethodFile, OutFile, OutFormat = 'ESRI Shapefile')

**功能：**【擦除】。从第一个矢量中去除与第二个矢量交叉的部分。

**参数：** 

&emsp;InFile：`str`。输入矢量文件路径。

&emsp;MethodFile：`str`。擦除矢量范围文件路径。

&emsp;OutFile：`str`。输出矢量文件路径。

**可选参数：** 

&emsp;OutFormat = `str`。输出矢量文件格式，默认为 ESRI Shapefile。其他格式详见 ToOtherFormat 函数。

:::

## Intersection

::: theorem

**引用：** gma.vesp.Intersection(InFile, MethodFile, OutFile, OutFormat = 'ESRI Shapefile')

**功能：**【交集】。取两个矢量的交集。

**参数：** 

&emsp;InFile：`str`。第一个矢量文件路径。

&emsp;MethodFile：`str`。第二个矢量文件路径。

&emsp;OutFile：`str`。输出矢量文件路径。

**可选参数：** 

&emsp;OutFormat = `str`。输出矢量文件格式，默认为 ESRI Shapefile。其他格式详见 ToOtherFormat 函数。

:::

## Union

::: theorem

**引用：** gma.vesp.Union(InFile, MethodFile, OutFile, OutFormat = 'ESRI Shapefile')

**功能：**【联合】。取两个矢量的并集。

**参数：** 

&emsp;InFile：`str`。输入矢量文件路径。

&emsp;MethodFile：`str`。联合矢量文件路径。

&emsp;OutFile：`str`。输出矢量文件路径。

**可选参数：** 

&emsp;OutFormat = `str`。输出矢量文件格式，默认为 ESRI Shapefile。其他格式详见 ToOtherFormat 函数。

:::

## Update

::: theorem

**引用：** gma.vesp.Update(InFile, MethodFile, OutFile, OutFormat = 'ESRI Shapefile')

**功能：**【更新】。用一个矢量更新另一个矢量。

**参数：** 

&emsp;InFile：`str`。输入矢量文件路径。

&emsp;MethodFile：`str`。更新矢量文件路径。

&emsp;OutFile：`str`。输出矢量文件路径。

**可选参数：** 

&emsp;OutFormat = `str`。输出矢量文件格式，默认为 ESRI Shapefile。其他格式详见 ToOtherFormat 函数。

:::

## ToOtherFormat

::: theorem

**引用：** gma.vesp.ToOtherFormat(InFile, OutFile, OutFormat = 'ESRI Shapefile')

**功能：**【格式转换】。一种矢量格式转换为另一种矢量格式。

**参数：** 

&emsp;InFile：`str`。输入矢量文件路径。

&emsp;OutFile：`str`。输出矢量文件路径。

**可选参数：** 

&emsp;OutFormat = `str`。输出矢量文件格式，默认为 ESRI Shapefile。

<Boxx type='tip' title='其他支持格式' content='&emsp;ESRI Shapefile，PCIDSK，PDS4，PDF，MBTiles，MapInfo File，Memory，CSV，GML，LIBKML，KML，GeoJSON，OGR_GMT，GPKG，SQLite，WAsP，FlatGeobuf，Geoconcept，GeoRSS，ODS， XLSX，JML，VDV，MVT，MapML。' />

:::

## Reproject

::: theorem

**引用：** gma.vesp.Reproject(InFile, OutFile, Projection, OutFormat = 'ESRI Shapefile')

**功能：**【重投影】。将矢量数据从一种坐标系投影到另一种坐标系。

**参数：** 

&emsp;InFile：`str`。输入矢量文件路径。

&emsp;OutFile：`str`。输出矢量文件路径。

**可选参数：** 

&emsp;Projection = `str`。输出矢量坐标系（EPSG 或 wkb 格式）。

&emsp;OutFormat = `str`。输出矢量文件格式，默认为 ESRI Shapefile。其他格式详见 ToOtherFormat 函数。

:::

## SymDifference<Badge text="1.0.4 +"/>

::: theorem

**引用：** gma.vesp.SymDifference(InFile, MethodFile, OutFile, OutFormat = 'ESRI Shapefile')

**功能：**【交集取反】。取两个矢量不相交的部分。

**参数：** 

&emsp;InFile：`str`。第一个矢量文件路径。

&emsp;MethodFile：`str`。第二个矢量文件路径。

&emsp;OutFile：`str`。输出矢量文件路径。

**可选参数：** 

&emsp;OutFormat = `str`。输出矢量文件格式，默认为 ESRI Shapefile。其他格式详见 ToOtherFormat 函数。

:::