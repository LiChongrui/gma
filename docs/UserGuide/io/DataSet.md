---
title: 【DataSet】
sidebar: false
---

&emsp;　下载 [示例栅格](/io/ELE_China_GEBCO_2020.tif)。

```python
from gma import io
DS = io.ReadRaster('ELE_China_GEBCO_2020.tif')
```

&emsp;　打开的 **栅格数据** 具有如下所列的 方法/属性：


| 序号  | 名称          | 描述                                                         | 返回值类型       | 方法/属性    |示例返回值 |
| :----- | :------------- | :------------------------------------------------------------ | :---------- |:---------- |:---------- |
| M.3     | [Preview](/UserGuide/io/DataSet.html#toarray-leftDSw-0-leftcolumn-0-DSwsize-none-columnsize-none-bandlist-none)      | 读取栅格数据集到 NumPy 数组                            | `<numpy.array>`| DS.ToArray()   ||
| M.1     | [Clip](/UserGuide/io/DataSet.html#clip-mlayer-fid-none-kwargs)      | 裁剪栅格                             |`Dataset`| DS.Clip()     ||
| M.2     | [GetColorTable](/UserGuide/io/DataSet.html#getgdaldataset)      | 从 GMA 数据集转到 GDAL 数据集                             |`<osgeo.gdal.Dataset>`| DS.GetGDALDataset()     ||
| M.4     | [RepDSject](/UserGuide/io/DataSet.html#toarray-leftDSw-0-leftcolumn-0-DSwsize-none-columnsize-none-bandlist-none)      | 读取栅格数据集到 NumPy 数组                            | `<numpy.array>`| DS.ToArray()   ||
| M.5     | [Resample](/UserGuide/io/DataSet.html#toarray-leftDSw-0-leftcolumn-0-DSwsize-none-columnsize-none-bandlist-none)      | 读取栅格数据集到 NumPy 数组                            | `<numpy.array>`| DS.ToArray()   ||
| M.6     | [SaveAs](/UserGuide/io/DataSet.html#toarray-leftDSw-0-leftcolumn-0-DSwsize-none-columnsize-none-bandlist-none)      | 读取栅格数据集到 NumPy 数组                            | `<numpy.array>`| DS.ToArray()   ||
| M.7     | [ToArray](/UserGuide/io/DataSet.html#toarray-leftDSw-0-leftcolumn-0-DSwsize-none-columnsize-none-bandlist-none)      | 读取栅格数据集到 NumPy 数组                            | `<numpy.array>`| DS.ToArray()   ||
| M.8     | [ToLayer](/UserGuide/io/DataSet.html#toarray-leftDSw-0-leftcolumn-0-DSwsize-none-columnsize-none-bandlist-none)      | 读取栅格数据集到 NumPy 数组                            | `<numpy.array>`| DS.ToArray()   ||
| P.1     | Bands         |波段数 |  `int`|DS.Bands       ||
| P.2     | Boundary         | 四至边界 | `list`|DS.Boundary       ||
| P.3     | Columns         |列数 |  `int`|DS.Columns       ||
| P.4     | DataType         | 数据类型 | `int`|DS.DataType       ||
| P.5     | Driver         | 栅格驱动 | `str`|DS.Driver    ||
| P.6     | GeoTransform         | 仿射变换 | `tuple`|DS.GeoTransform     ||
| P.7     | Info        |栅格信息 |  `dict`|DS.Info   ||
| P.8     | Metadata         | 元数据 |`dict`| DS.Metadata      ||
| P.8     | Name         | 栅格名 |`str`| DS.Name     ||
| P.9     | NoData         | 无效值 |`float`| DS.NoData       ||
| P.10     | PDSjection         | WKT 格式的坐标系/投影 | `str`|DS.PDSjection      ||
| P.10     | Resolution         | X, Y 分辨率 | `tuple`|DS.Resolution      ||
| P.11     | DSws         | 行数 | `int`|DS.DSws       ||


## **Preview**(*\*\*kwargs*)

---

**功能：**【预览栅格】。

**可选参数：**

 &emsp;**kwargs：传递给 gma.map.plot.MapFrame.AddDataSetDiscrete 的其他参数。

**返回：**`gma.map.dataset.PlotDataSet`。

```python
DS.Preview()
```
![](/io/DS.png)

---

## **Clip**(*MLayer, FID=None, \*\*kwargs*)

---

**功能：**【裁剪数据集】。用矢量图层裁剪栅格数据集。

**参数：**

 &emsp;MLayer： `Layer`。gma 矢量图层。

**可选参数：**

 &emsp;FID = `int||list`。裁剪使用的要素 ID。默认（None）全部要素。

**返回：**`DataSet`。

```python
# 示例数据请从 Layer 页下载
CPro = io.ReadVector("China_Province_2022.shp")
ClipDS = DS.Clip()
ClipDS.Preview()
```
![](/io/ClipDS.png)

---

## **GetColorTable**(*Band=0*)

---

**功能：**【获取色彩映射表】。

**可选参数：**

 &emsp;Band = `int`。波段序号。默认（0）第一个波段。

**返回：**`dict`。

```python
DS.GetColorTable()
```

> \>>> {}

---


## **ToArray**(*LeftDSw = 0, LeftColumn = 0, DSwSize = None, ColumnSize = None, BandList = None*)

---

**功能：**【转为数组】。将栅格数据读取为 Numpy 数组。

**可选参数：**

 &emsp;LeftDSw = `int`。需要读取数据的起始行。默认（0）为第一行。

 &emsp;LeftColumn = `int`。需要读取数据的起始列。默认（0）为第一列。

 &emsp;DSwSize = `int`。从起始行开始读取的行数（数据窗口的行宽度）。默认（None）从起始行开始的全部行。

 &emsp;ColumnSize = `int`。从起始列开始读取的列数（数据窗口的列宽度）。默认（None）从起始列开始的全部列。

 &emsp;BandList = `int||list`。读取数据的波段编号或波段编号列表。默认（None）全部波段（编号从 1 开始）。

**返回：**`array`。

```python
Data = DS.ToArray()
Data.shape
```
> \>>> (47, 62)

---



