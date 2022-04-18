---
title: 其他函数
date: 2022-03-09
---

&emsp;&emsp;自 <Badge text="1.0.6" vertical='middle'/> 版本开始，增加 **其他函数** 板块，为 **gma** 下包含的辅助函数的详细功能、参数设置和引用方法说明。如果您想了解 gma 所有函数的整体情况，请移步 [函数列表](/Functions/Function.html) 。

## Open

::: theorem

**引用：** gma.Open(InFile, Mode = 0)

**功能：**【打开文件】。打开栅格或矢量数据文件。

**参数：**

&emsp;InFile：`str`。输入文件路径。

**可选参数：**

&emsp;Mode = `int`。打开方式，默认为只读（0），也可为 1（可写模式）。参数设置错误则返回只读模式。

**返回：** 多维数据：返回子数据集列表；其他栅格：返回 [RasterOpen](other.html#open-rasteropen)。矢量数据：返回 [VectorOpen](other.html#open-vectoropen)。

:::

::: tip 提示

多维数据如果需要打开子数据集，需要重新 Open 子数据集路径（一般为每个子数据集信息的第一个元素）！

:::


## Open:RasterOpen

&emsp;&emsp;打开的**栅格数据**具有如下所列的 方法/属性：

### Bands

::: theorem

**引用：** gma.Open().Bands 

**功能：**【波段数】。类属性，获取栅格波段数。

**返回：**`str`。

:::

### Columns

::: theorem

**引用：** gma.Open().Columns 

**功能：**【列数】。类属性，获取栅格列数（X）。

**返回：**`int`。

:::

### Rows

::: theorem

**引用：** gma.Open().Rows

**功能：**【行数】。类属性，获取栅格行数（Y）。

**返回：**`int`。

:::

### ToArray

::: theorem

**引用：** gma.Open().ToArray(LeftRow = 0, LeftColumn = 0, RowSize = None, ColumnSize = None, BandList = None)

**功能：**【转为数组】。将栅格数据读取为 Numpy 数组。

**可选参数：**

 &emsp;LeftRow = `int`。需要读取数据的起始行。默认（0）为第一行。

 &emsp;LeftColumn = `int`。需要读取数据的起始列。默认（0）为第一列。

 &emsp;RowSize = `int`。从起始行开始读取的行数（数据窗口的行宽度）。默认（None）从起始行开始的全部行。

 &emsp;ColumnSize = `int`。从起始列开始读取的列数（数据窗口的列宽度）。默认（None）从起始列开始的全部列。

 &emsp;BandList = `int||list`。读取数据的波段编号或波段编号列表。默认（None）全部波段（编号从 1 开始）。

**返回：**`array`。

:::

### DataType

::: theorem

**引用：** gma.Open().DataType

**功能：**【数据类型】。类属性，获取栅格数据的数据类型。如果为多波段数据，则取所有波段数据类型的众数。

**返回：**`int`。

:::

### Driver

::: theorem

**引用：** gma.Open().Driver

**功能：**【栅格驱动】。获取栅格数据驱动。

**返回：**`str`。

:::

### GeoTransform

::: theorem

**引用：** gma.Open().GeoTransform

**功能：**【仿射变换】。类属性，获取栅格仿射变换。

**返回：**`tuple`。

:::

### GetBand

::: theorem

**引用：** gma.Open().GetBand(Band)

**功能：**【获取 Band】。读取某一波段为 gdal.Band。

**参数：** 

&emsp;Band：`int`。栅格文件的波段数。从 1 开始。

**返回：**`gdal.Band`。

:::

### GetBandToArray

::: theorem

**引用：** gma.Open().GetBandToArray(Band) 

**参数：** 

&emsp;Band：`int`。栅格文件的波段数。从 1 开始。

**功能：**【转换波段为数组】。将某一波段读取为 Numpy 数组。

**返回：**`array`。

:::

### GetGDALDataset

::: theorem

**引用：** gma.Open().GetGDALDataset()

**功能：**【获取 GDALDataset】。读取栅格数据为 gdal.GDALDataset。

**返回：**`gdal.GDALDataset`。

:::

### NoData

::: theorem

**引用：** gma.Open().NoData

**功能：**【无效值】。类属性，获取栅格无效值。

**返回：**`float||None`。

:::

### Projection

::: theorem

**引用：** gma.Open().Projection

**功能：**【坐标系】。类属性，获取栅格坐标系。

**返回：**`str`。

:::

### Info

::: theorem

**引用：** gma.Open().Info

**功能：**【栅格信息】。类属性，获取栅格信息。

**返回：**`dict`。

:::

### Metadata

::: theorem

**引用：** gma.Open().Metadata

**功能：**【元数据】。类属性，获取栅格元数据。

**返回：**`dict`。

:::

### GetBandMetadata

::: theorem

**引用：** gma.Open().GetBandMetadata(Band)

**功能：**【波段元数据】。获取某一波段的元数据。

**参数：** 

&emsp;Band：`int`。栅格文件的波段数。从 1 开始。

**返回：**`dict`。

:::

## Open:VectorOpen

&emsp;&emsp;打开的**矢量数据**具有如下所列的 方法/属性：

### Driver

::: theorem

**引用：** gma.Open().Driver

**功能：**【矢量驱动】。类属性，获取矢量数据驱动。

**返回：**`str`。

:::

### LayerCount

::: theorem

**引用：** gma.Open().LayerCount

**功能：**【图层数】。类属性，获取矢量数据的图层数量。

**返回：**`int`。

:::

### LayerNames

::: theorem

**引用：** gma.Open().LayerNames

**功能：**【图层名】。类属性，获取矢量数据每个图层的名称。

**返回：**`list`。

:::

### GetOGRDataSource

::: theorem

**引用：** gma.Open().GetOGRDataSource()

**功能：**【获取 DataSource】。读取矢量数据为 ogr.DataSource。

**返回：**`ogr.DataSource`。

:::

### GetLayer

::: theorem

**引用：** gma.Open().GetLayer(ID)

**功能：**【打开图层】。打开某一图层。

**参数：** 

&emsp;ID：`int`。矢量图层的编号。从 0 开始。

**返回：**[Layer](other.html#getlayer-layer)。

:::

## GetLayer:Layer

&emsp;&emsp;打开的**矢量数据的图层**具有如下所列的 方法/属性：

### FeatureCount

::: theorem

**引用：** gma.Open().GetLayer().FeatureCount

**功能：**【要素数】。类属性，获取图层要素的数量。

**返回：**`int`。

:::

### Projection

::: theorem

**引用：** gma.Open().GetLayer().Projection

**功能：**【坐标系/投影】。获取图层坐标系/投影。

**返回：**`str`。

:::

### Boundary

::: theorem

**引用：** gma.Open().GetLayer().Boundary

**功能：**【四至边界】。类属性，获取图层的左、右、下、上边界。

**返回：**`tuple`。

:::

### GetAttributeTable

::: theorem

**引用：** gma.Open().GetLayer().GetAttributeTable()

**功能：**【获取属性表】。获取图层属性表。

**返回：**`DataFrame`。

:::

### FieldNames

::: theorem

**引用：** gma.Open().GetLayer().FieldNames

**功能：**【字段名】。类属性，获取属性表字段名列表。

**返回：**`list`。

:::

### FieldDataTypes

::: theorem

**引用：** gma.Open().GetLayer().FieldDataTypes

**功能：**【字段数据类型】。类属性，获取属性表字段名数据类型。

**返回：**`dict`。

:::