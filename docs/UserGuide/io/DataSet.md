---
title: Open:DataSet
date: 2022-03-09
sidebar: false
---

&emsp;　下载 [示例栅格](/Open/ELE_China_GEBCO_2020.tif)。

```python
import gma
RO = gma.Open('ELE_China_GEBCO_2020.tif')
```

&emsp;　打开的 **栅格数据** 具有如下所列的 方法/属性：

## **Bands** 

---

**功能：**【波段数】。类属性，获取栅格波段数。

**返回：**`str`。

```python
RO.Bands
```
> \>>> 1

## **Boundary** 

---

**功能：**【四至边界】。类属性，获取栅格的四至边界范围。

**返回：**`list`。

```python
RO.Boundary
```
> \>>> [73.5000000000002, 6.562499999999972, 135.5000000000002, 53.56249999999997]

---

## **Columns** 

---

**功能：**【列数】。类属性，获取栅格列数（X）。

**返回：**`int`。

```python
RO.Columns
```
> \>>> 62

---

## **DataType**

---

**功能：**【数据类型】。类属性，获取栅格数据的数据类型。如果为多波段数据，则取所有波段数据类型的众数。

**返回：**`int`。

```python
RO.DataType
```
> \>>> 3

---

## **Driver**

---

**功能：**【栅格驱动】。获取栅格数据驱动。

**返回：**`str`。

```python
RO.Driver
```
> \>>> 'GTiff'

---

## **GeoTransform**

---

**功能：**【仿射变换】。类属性，获取栅格仿射变换。

**返回：**`tuple`。

```python
RO.GeoTransform
```
> \>>> (73.5000000000002, 1.0, 0.0, 53.56249999999997, 0.0, -1.0)

---

## **GetGDALDataset**()

---

**功能：**【获取 GDALDataset】。读取栅格数据为 gdal.GDALDataset。

**返回：**`osgeo.gdal.Dataset`。

```python
RO.GetGDALDataset()
```
> \>>> <osgeo.gdal.Dataset; proxy of <Swig Object of type 'GDALDatasetShadow *' at 0x......> >

---

## **Info**

---

**功能：**【栅格信息】。类属性，获取栅格信息。

**返回：**`dict`。

```python
RO.Info
```
> \>>> {'description': 'ELE_China_GEBCO_2020.tif',
 'driverShortName': 'GTiff',
 'driverLongName': 'GeoTIFF',
 ......}

---

## **Metadata**

---

**功能：**【元数据】。类属性，获取栅格元数据。

**返回：**`dict`。

```python
RO.Metadata
```
> \>>> {'AREA_OR_POINT': 'Area', 'DataType': 'Thematic'}

---

## **NoData**

---

**功能：**【无效值】。类属性，获取栅格无效值。

**返回：**`float||None`。

```python
RO.NoData
```
> \>>> 32767.0

---

## **Projection**

---

**功能：**【坐标系】。类属性，获取栅格坐标系。

**返回：**`str`。

```python
RO.Projection
```
> \>>> 'GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563, AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0],UNIT["degree", 0.0174532925199433,AUTHORITY["EPSG","9122"]],AXIS["Latitude",NORTH],AXIS["Longitude",EAST], AUTHORITY["EPSG","4326"]]'

---

## **Rows**

**功能：**【行数】。类属性，获取栅格行数（Y）。

**返回：**`int`。

```python
RO.Rows
```
> \>>> 11338

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



