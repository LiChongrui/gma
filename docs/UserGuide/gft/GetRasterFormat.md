---
title: GetRasterFormat
date: 2022-04-17
sidebar: true
---

## gma.gft.**GetRasterFormat**(*Format = 'GTiff'*)

---

**功能：**【类】。【获取栅格格式】，实现针对某一栅格驱动详细信息的获取。

**初始化：** 

&emsp;Format = `str`。栅格驱动格式名称。默认为 GTiff 格式。

**示例：**
```python
from gma import gft

# 获取 GTiff 格式
RAFormat = gft.GetRasterFormat('GTiff')
```
---

## 类内属性/方法

### **ColorTableDataTypes**

---

**功能：**【色彩映射表支持的数据类型】。类属性，色彩映射表支持的数据类型。

**返回：**`list`。

```python
RAFormat.ColorTableDataTypes
```
> \>>> ['Byte', 'UInt16']

---

###  **CompressModes**

---

**功能：**【压缩方式】。类属性，支持的压缩方式。

**返回：**`list`。

```python
RAFormat.CompressModes
```
> \>>> ['NONE', 'LZW', 'PACKBITS', 'JPEG', 'CCITTRLE', 'CCITTFAX3', 'CCITTFAX4', 'DEFLATE', 'LZMA', 'ZSTD', 'WEBP', 'LERC', 'LERC_DEFLATE', 'LERC_ZSTD']

---

### Copyable

---

**功能：**【可复制性】。类属性。是否可以通过复制的方式创建文件。

**返回：**`str`。

```python
RAFormat.Copyable
```
> \>>> 'Yes'
---

### Creatable

---

**功能：**【可创建性】。类属性。部分格式仅支持读取，不支持创建。

**返回：**`str`。

```python
RAFormat.Creatable
```
> \>>> 'Yes'
---

### CreationDataTypes

---

**功能：**【支持创建数据类型】。类属性。

**返回：**`list`。

```python
RAFormat.CreationDataTypes
```
> \>>> ['Byte', 'UInt16', 'Int16', 'UInt32', 'Int32', 'Float32', 'Float64', 'CInt16', 'CInt32', 'CFloat32', 'CFloat64']

---

### CreationOptionInfo

---

**功能：**【创建配置信息】。类属性。可查看此驱动支持的配置参数以及说明。

**返回：**`DataFrame`。

```python
RAFormat.CreationOptionInfo
```
|    | name                           | type          | description                                                                                                              | default     | Value                                                                                                  |
|---:|:-------------------------------|:--------------|:-------------------------------------------------------------------------------------------------------------------------|:------------|:-------------------------------------------------------------------------------------------------------|
|  0 | COMPRESS                       | string-select | nan                                                                                                                      | DEFLATE     | NONE LZW PACKBITS JPEG CCITTRLE CCITTFAX3 CCITTFAX4 DEFLATE LZMA ZSTD WEBP LERC LERC_DEFLATE LERC_ZSTD |
|  1 | PREDICTOR                      | int           | Predictor Type (1=default, 2=horizontal differencing, 3=floating point prediction)                                       | 2           | nan                                                                                                    |
|  2 | DISCARD_LSB                    | string        | Number of least-significant bits to set to clear as a single value or comma-separated list of values for per-band values | nan         | nan                                                                                                    |
|  ... | ...                   | ...        | ...                                                                                                    | ...          | ...      |
---

### CreationOptions

---

**功能：**【创建选项】。栅格文件创建过程中使用的参数。

**返回：**`dict`。

```python
RAFormat.CreationOptions
```
> \>>>{'COMPRESS': 'DEFLATE', 'PREDICTOR': '2', 'JPEG_QUALITY': '75', 'JPEGTABLESMODE': '1', 'ZLEVEL': '12', 'LZMA_PRESET': '6', 'ZSTD_LEVEL': '9', 'NUM_THREADS': 'ALL_CPUS', 'INTERLEAVE': 'PIXEL', 'TILED': 'Yes', 'SPARSE_OK': 'FALSE', 'PROFILE': 'GDALGeoTIFF', 'BIGTIFF': 'IF_SAFER', 'ENDIANNESS': 'NATIVE', 'STREAMABLE_OUTPUT': 'NO', 'GEOTIFF_KEYS_FLAVOR': 'STANDARD'}

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

### SetCreationOptions(*\*\*kwargs*)

---

**功能：**【设置创建选项】。类方法，为此驱动格式修改创建选项。

**可选参数：**

&emsp; \**kwargs：需要配置的参数设置。参数名详见 CreationOptionInfo 中的 name 列。

```python
## 设置 GTiff 压缩方式为 LZW
RAFormat.SetCreationOptions(COMPRESS = 'LZW')
```

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

