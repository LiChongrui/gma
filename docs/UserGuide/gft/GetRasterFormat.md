---
title: GetRasterFormat
date: 2022-04-17
sidebar: false
---

## gma.config.**GetRasterFormat**(*Format*)

---

**功能：**【类】。【获取栅格格式】，实现针对某一栅格驱动详细信息的获取。

**初始化：** 

&emsp;Format：`str`。栅格驱动格式名称。

**示例：**
```python
import gma

# 获取 GTiff 格式
RAFormat = gma.config.GetRasterFormat('GTiff')
```
---

## 类内属性/方法

### **ColorTableDataType**

---

**功能：**【色彩映射表数据类型】。类属性，色彩映射表支持的数据类型。

**返回：**`dict`。

```python
RAFormat.ColorTableDataType
```
> \>>> {'Byte': 1, 'UInt16': 2}

---

###  **CompressMode**

---

**功能：**【压缩方式】。类属性，支持的压缩方式。

**返回：**`list`。

```python
RAFormat.CompressMode
```
> \>>> ['NONE', 'LZW', 'PACKBITS', 'JPEG', 'CCITTRLE', 'CCITTFAX3', 'CCITTFAX4', 'DEFLATE', 'LZMA', 'ZSTD', 'WEBP', 'LERC', 'LERC_DEFLATE', 'LERC_ZSTD']

---

### CreationDataType

---

**功能：**【创建数据类型】。类属性，支持创建的数据类型。

**返回：**`dict`。

```python
RAFormat.CreationDataType
```
> \>>> {'Byte': 1, 'UInt16': 2, 'Int16': 3, 'UInt32': 4, 'Int32': 5, 'Float32': 6, 'Float64': 7, 'CInt16': 8, 'CInt32': 9, 'CFloat32': 10, 'CFloat64': 11}

---

### Details

---

**功能：**【详细信息】。类属性，全部支持内容的详细信息。

**返回：**`dict`。

```python
RAFormat.Details
```
> \>>> {'Creation': 'Yes', 
 'Copy': 'Yes',
 'Geo Referencing': 'Yes',
 'Open': 'Yes',
 'Raster': 'Yes',
 'Virtualio': 'Yes',
 'Creation Data Types': 'Byte UInt16 Int16 UInt32 Int32 Float32 Float64 CInt16 CInt32 CFloat32 CFloat64',
 'Extension': '.tif .tiff',
 'Long Name': 'GeoTIFF',
 'Subdatasets': 'Yes',
 'Coordinate Epoch': 'Yes',
 'Mime Type': 'image/tiff',
 'Color Table Data Type': 'Byte UInt16',
 'Update': 'Yes',
 'Multiband': 'Yes',
 'Compress': 'NONE LZW PACKBITS JPEG CCITTRLE CCITTFAX3 CCITTFAX4 DEFLATE LZMA ZSTD WEBP LERC LERC_DEFLATE LERC_ZSTD',
 'Short Name': 'GTiff'}

---

### Extension

---

**功能：**【扩展名】。类属性，驱动格式的扩展名。

**返回：**`str`。

```python
RAFormat.Extension
```
> \>>> '.tif'

---

### GeoReferencing

---

**功能：**【地理参考支持】。类属性，是否支持地理参考。

**返回：**`str`。

```python
RAFormat.GeoReferencing
```
> \>>> 'Yes'

---

### LongName

---

**功能：**【长名称】。类属性，驱动格式的长名称。

**返回：**`str`。

```python
RAFormat.LongName
```
> \>>> 'GeoTIFF'

---

### Multiband

---

**功能：**【多波段支持】。类属性，是否支持多波段或支持的波段数。

**返回：**`str||list`。

```python
RAFormat.Multiband
```
> \>>> 'Yes'

---

### Update

---

**功能：**【更新支持】。类属性，是否支持更新（修改）。

**返回：**`str||list`。

```python
RAFormat.Update
```
> \>>> 'Yes'

---

