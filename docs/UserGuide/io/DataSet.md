---
title: 【DataSet】
sidebar: false
---

&emsp;　下载 [示例栅格](/Open/ELE_China_GEBCO_2020.tif)。

```python
from gma import io
RO = io.ReadRaster('ELE_China_GEBCO_2020.tif')
```

&emsp;　打开的 **栅格数据** 具有如下所列的 方法/属性：


| 序号  | 名称          | 描述                                                         | 返回值类型       | 实例       |
| :----- | :------------- | :------------------------------------------------------------ | :---------- |:---------- |
| M.1     | [GetGDALDataset](/UserGuide/io/DataSet.html#getgdaldataset)      | 从 GMA 数据集转到 GDAL 数据集                             |`<osgeo.gdal.Dataset>`| RO.GetGDALDataset()     |
| M.2     | [ToArray](/UserGuide/io/DataSet.html#toarray-leftrow-0-leftcolumn-0-rowsize-none-columnsize-none-bandlist-none)      | 读取栅格数据集到 NumPy 数组                            | `<numpy.array>`| RO.ToArray()   |
| P.1     | Bands         |波段数 |  `int`|RO.Bands       |
| P.2     | Boundary         | 四至边界 | `list`|RO.Boundary       |
| P.3     | Columns         |列数 |  `int`|RO.Columns       |
| P.4     | DataType         | 数据类型 | `int`|RO.DataType       |
| P.5     | Driver         | 栅格驱动 | `str`|RO.Driver    |
| P.6     | GeoTransform         | 仿射变换 | `tuple`|RO.GeoTransform     |
| P.7     | Info        |栅格信息 |  `dict`|RO.Info   |
| P.8     | Metadata         | 元数据 |`dict`| RO.Metadata      |
| P.9     | NoData         | 无效值 |`float`| RO.NoData       |
| P.10     | Projection         | WKT 格式的坐标系/投影 | `str`|RO.Projection      |
| P.11     | Rows         | 行数 | `int`|RO.Rows       |


## **GetGDALDataset**()

---

**功能：**【获取 GDALDataset】。读取栅格数据为 gdal.GDALDataset。

**返回：**`osgeo.gdal.Dataset`。

```python
RO.GetGDALDataset()
```
> \>>> <osgeo.gdal.Dataset; proxy of <Swig Object of type 'GDALDatasetShadow *' at 0x......> >

---


## **ToArray**(*LeftRow = 0, LeftColumn = 0, RowSize = None, ColumnSize = None, BandList = None*)

---

**功能：**【转为数组】。将栅格数据读取为 Numpy 数组。

**可选参数：**

 &emsp;LeftRow = `int`。需要读取数据的起始行。默认（0）为第一行。

 &emsp;LeftColumn = `int`。需要读取数据的起始列。默认（0）为第一列。

 &emsp;RowSize = `int`。从起始行开始读取的行数（数据窗口的行宽度）。默认（None）从起始行开始的全部行。

 &emsp;ColumnSize = `int`。从起始列开始读取的列数（数据窗口的列宽度）。默认（None）从起始列开始的全部列。

 &emsp;BandList = `int||list`。读取数据的波段编号或波段编号列表。默认（None）全部波段（编号从 1 开始）。

**返回：**`array`。

```python
Data = RO.ToArray()
Data.shape
```
> \>>> (47, 62)

---



