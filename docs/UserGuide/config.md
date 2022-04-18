---
title: 高级配置
date: 2022-04-17
---

&emsp;&emsp;自 <Badge text="1.0.7" vertical='middle'/> 版本开始，gma 引入 config 高级配置模块，提供库配置和支持内容查询和设置等相关功能。如果您想了解 gma 所有函数的整体情况，请移步 [函数列表](/Functions/Function.html) 。



## GetRACreationOption

::: theorem

**引用：** gma.config.GetRACreationOption(Format)

**功能：**【栅格创建选项】。获取栅格驱动格式支持的高级创建选项！

**参数：** 

&emsp;Format：`str`。栅格驱动格式名称。

**返回：**`DataFrame`。

::: 

## GetVELayerCreationOption

::: theorem

**引用：** gma.config.GetVELayerCreationOption(Format)

**功能：**【矢量图层创建选项】。获取矢量驱动格式支持的图层高级创建选项！

**参数：** 

&emsp;Format：`str`。栅格驱动格式名称。

**返回：**`DataFrame`。

::: 

## GetRasterFormat 类

::: theorem

**引用：** gma.config.GetRasterFormat(Format)

**功能：**【获取栅格格式】。实现针对某一栅格驱动详细信息的获取。

**初始化：** 

&emsp;Format：`str`。栅格驱动格式名称。

::: 

::: warning 注意
类内 属性/方法 引用前请先初始化 `GetRasterFormat` 类！
::: 

### ColorTableDataType

::: theorem

**引用：** gma.config.GetRasterFormat().ColorTableDataType

**功能：**【色彩映射表数据类型】。类属性，色彩映射表支持的数据类型。

**返回：**`dict`。

::: 

### CompressMode

::: theorem

**引用：** gma.config.GetRasterFormat().CompressMode

**功能：**【压缩方式】。类属性，支持的压缩方式。

**返回：**`list`。

::: 

### CreationDataType

::: theorem

**引用：** gma.config.GetRasterFormat().CreationDataType

**功能：**【创建数据类型】。类属性，支持创建的数据类型。

**返回：**`dict`。

::: 

### Details

::: theorem

**引用：** gma.config.GetRasterFormat().Details

**功能：**【详细信息】。类属性，全部支持内容的详细信息。

**返回：**`dict`。

::: 

### Extension

::: theorem

**引用：** gma.config.GetRasterFormat().Extension

**功能：**【扩展名】。类属性，驱动格式的扩展名。

**返回：**`str`。

::: 

### GeoReferencing

::: theorem

**引用：** gma.config.GetRasterFormat().GeoReferencing

**功能：**【地理参考支持】。类属性，是否支持地理参考。

**返回：**`str`。

::: 

### LongName

::: theorem

**引用：** gma.config.GetRasterFormat().LongName

**功能：**【长名称】。类属性，驱动格式的长名称。

**返回：**`str`。

::: 

### Multiband

::: theorem

**引用：** gma.config.GetRasterFormat().Multiband

**功能：**【多波段支持】。类属性，是否支持多波段或支持的波段数。

**返回：**`str||list`。

::: 

### Update

::: theorem

**引用：** gma.config.GetRasterFormat().Update

**功能：**【更新支持】。类属性，是否支持更新（修改）。

**返回：**`str||list`。

::: 

## GetVectorFormat 类

::: theorem

**引用：** gma.config.GetVectorFormat(Format)

**功能：**【获取矢量格式】。实现针对某一矢量驱动详细信息的获取。

**初始化：** 

&emsp;Format：`str`。矢量驱动格式名称。

::: 

::: warning 注意
类内 属性/方法 引用前请先初始化 `GetVectorFormat` 类！
::: 

### CreationFieldDataType

::: theorem

**引用：** gma.config.GetVectorFormat().CreationFieldDataType

**功能：**【属性表字段类型】。类属性，支持创建属性表字段的数据类型。

**返回：**`dict`。

::: 

### Details

::: theorem

**引用：** gma.config.GetVectorFormat().Details

**功能：**【详细信息】。类属性，全部支持内容的详细信息。

**返回：**`dict`。

::: 

### Extension

::: theorem

**引用：**  gma.config.GetVectorFormat().Extension

**功能：**【扩展名】。类属性，驱动格式的扩展名。

**返回：**`str`。

::: 

### GeoReferencing

::: theorem

**引用：** gma.config.GetVectorFormat().GeoReferencing

**功能：**【地理参考支持】。类属性，是否支持地理参考。

**返回：**`str`。

::: 

### LongName

::: theorem

**引用：** gma.config.GetVectorFormat().LongName

**功能：**【长名称】。类属性，驱动格式的长名称。

**返回：**`str`。

::: 

### MultiLayer

::: theorem

**引用：** gma.config.GetVectorFormat().MultiLayer

**功能：**【多图层支持】。类属性，是否支持多图层。

**返回：**`str`。

::: 

### Update

::: theorem

**引用：** gma.config.GetVectorFormat().Update

**功能：**【更新支持】。类属性，是否支持更新（修改）。

**返回：**`str||list`。

::: 

## RasterFormatInfo 类

::: theorem

**引用：** gma.config.RasterFormatInfo()

**功能：**【栅格驱动格式信息】。获取所有栅格驱动格式分类的详细信息。

::: 

### AddableColorTableFormats

::: theorem

**引用：** gma.config.GetVectorFormat().AddableColorTableFormats

**功能：**【色彩映射表支持】。类属性，支持色彩映射表的驱动格式。

**返回：**`set`。

::: 

### CompressibleFormats

::: theorem

**引用：** gma.config.GetVectorFormat().CompressibleFormats

**功能：**【压缩支持】。类属性，支持压缩的驱动格式。

**返回：**`set`。

::: 

### CopyableFormats

::: theorem

**引用：** gma.config.GetVectorFormat().CopyableFormats

**功能：**【复制支持】。类属性，支持复制的驱动格式。

**返回：**`set`。

::: 

### CreatableFormats

::: theorem

**引用：** gma.config.GetVectorFormat().CreatableFormats

**功能：**【创建支持】。类属性，支持创建的驱动格式。

**返回：**`set`。

::: 

### MultibandFormats

::: theorem

**引用：** gma.config.GetVectorFormat().MultibandFormats

**功能：**【多波段支持】。类属性，支持多波段的驱动格式。

**返回：**`set`。

::: 

### ReadableFormats

::: theorem

**引用：** gma.config.GetVectorFormat().ReadableFormats

**功能：**【读取支持】。类属性，支持读取的驱动格式。

**返回：**`set`。

::: 

### TransformableFormats

::: theorem

**引用：** gma.config.GetVectorFormat().TransformableFormats

**功能：**【转换支持】。类属性，支持转换的驱动格式。

**返回：**`set`。

::: 

### UpdatableFormats

::: theorem

**引用：** gma.config.GetVectorFormat().UpdatableFormats

**功能：**【更新支持】。类属性，支持更新的驱动格式。

**返回：**`set`。

::: 

## VectorFormatInfo 类

::: theorem

**引用：** gma.config.VectorFormatInfo()

**功能：**【矢量驱动格式信息】。获取所有矢量驱动格式分类的详细信息。

::: 

### CopyableFormats

::: theorem

**引用：** gma.config.VectorFormatInfo().CopyableFormats

**功能：**【复制支持】。类属性，支持复制的驱动格式。

**返回：**`set`。

::: 

### CreatableFormats

::: theorem

**引用：** gma.config.VectorFormatInfo().CreatableFormats

**功能：**【创建支持】。类属性，支持创建的驱动格式。

**返回：**`set`。

::: 

### MultiLayerFormats

::: theorem

**引用：** gma.config.VectorFormatInfo().CreatableFormats

**功能：**【多图层支持】。类属性，支持多图层的驱动格式。

**返回：**`set`。

::: 

### ReadableFormats

::: theorem

**引用：** gma.config.VectorFormatInfo().ReadableFormats

**功能：**【读取支持】。类属性，支持读取的驱动格式。

**返回：**`set`。

::: 

### TransformableFormats

::: theorem

**引用：** gma.config.VectorFormatInfo().TransformableFormats

**功能：**【转换支持】。类属性，支持转换的驱动格式。

**返回：**`set`。

::: 

### UpdatableFormats

::: theorem

**引用：** gma.config.VectorFormatInfo().UpdatableFormats

**功能：**【更新支持】。类属性，支持更新的驱动格式。

**返回：**`set`。

::: 
