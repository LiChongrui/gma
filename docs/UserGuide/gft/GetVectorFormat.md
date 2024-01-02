---
title: GetVectorFormat
date: 2022-04-17
sidebar: true
---

## gma.gft.**GetVectorFormat**(*Format = 'ESRI Shapefile'*)

---

**功能：**【获取矢量格式】。实现针对某一矢量驱动详细信息的获取。

**参数：** 

&emsp;Format = `str`。矢量驱动格式名称。默认为 'ESRI Shapefile'。

**返回：** `VectorFormat`类。

**示例：**
```python
from gma import gft

# 获取 ESRI Shapefile 格式
VEFormat = gft.GetVectorFormat('ESRI Shapefile')
```

---

## 类内属性/方法

### Copyable

---

**功能：**【可复制性】。类属性。是否可以通过复制的方式创建文件。

**返回：**`str`。

```python
VEFormat.Copyable
```
> \>>> 'Yes'
---

### Creatable

---

**功能：**【可创建性】。类属性。部分格式仅支持读取，不支持创建。

**返回：**`str`。

```python
VEFormat.Creatable
```
> \>>> 'Yes'

---

### CreationFieldDataTypes

---

**功能：**【属性表字段类型】。类属性，支持创建属性表字段的数据类型。

**返回：**`list`。

```python
VEFormat.CreationFieldDataTypes
```
> \>>> ['Integer', 'Integer64', 'Real', 'String', 'Date']

---

### CreationOptionInfo

---

**功能：**【创建配置信息】。类属性。可查看此驱动支持的配置参数以及说明。

**返回：**`DataFrame`。

```python
VEFormat.CreationOptionInfo
```

|    | name                 | type          | description                                                        | default   | Value                                                                                                                                                    |
|---:|:---------------------|:--------------|:-------------------------------------------------------------------|:----------|:---------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | SHPT                 | string-select | type of shape                                                      | nan       | POINT ARC POLYGON MULTIPOINT POINTZ ARCZ POLYGONZ MULTIPOINTZ POINTM ARCM POLYGONM MULTIPOINTM POINTZM ARCZM POLYGONZM MULTIPOINTZM MULTIPATCH NONE NULL |
|  1 | 2GB_LIMIT            | boolean       | Restrict .shp and .dbf to 2GB                                      | NO        | nan                                                                                                                                                      |
|  2 | ENCODING             | string        | DBF encoding                                                       | UTF-8     | nan                                                                                                                                                      |
|  3 | RESIZE               | boolean       | To resize fields to their optimal size.                            | NO        | nan                                                                                                                                                      |
|  4 | SPATIAL_INDEX        | boolean       | To create a spatial index.                                         | NO        | nan                                                                                                                                                      |
|  5 | DBF_DATE_LAST_UPDATE | string        | Modification date to write in DBF header with YYYY-MM-DD format    | nan       | nan                                                                                                                                                      |
|  6 | AUTO_REPACK          | boolean       | Whether the shapefile should be automatically repacked when needed | YES       | nan                                                                                                                                                      |
|  7 | DBF_EOF_CHAR         | boolean       | Whether to write the 0x1A end-of-file character in DBF files       | YES       | nan                                                                                                                                                      |
---

### CreationOptions

---

**功能：**【创建选项】。矢量文件创建过程中使用的参数。

**返回：**`dict`。

```python
VEFormat.CreationOptions
```
> \>>>{'2GB_LIMIT': 'NO', 'ENCODING': 'UTF-8', 'RESIZE': 'NO', 'SPATIAL_INDEX': 'NO', 'AUTO_REPACK': 'YES', 'DBF_EOF_CHAR': 'YES'}

---

### Details

---

**功能：**【详细信息】。类属性，全部支持内容的详细信息。

**返回：**`dict`。

```python
VEFormat.Details
```
> \>>> {'Creation': 'Yes',
 'Copy': 'No',
 'Multiple Vector Layers': 'No',
 'Open': 'Yes',
 'Vector': 'Yes',
 'Virtualio': 'Yes',
 'Creation Field Data Types': 'Integer Integer64 Real String Date',
 'Extension': '.shp .dbf .shz .shp.zip',
 'Long Name': 'ESRI Shapefile',
 'Update': 'Yes',
 'Geo Referencing': 'Yes',
 'Short Name': 'ESRI Shapefile'}

### Extension

---

**功能：**【扩展名】。类属性，驱动格式的扩展名。

**返回：**`str`。

```python
VEFormat.Extension
```
> \>>> '.shp'
---

### GeoReferencing

---

**功能：**【地理参考支持】。类属性，是否支持地理参考。

**返回：**`str`。

```python
VEFormat.GeoReferencing
```
> \>>> 'Yes'

---

### LongName

---

**功能：**【长名称】。类属性，驱动格式的长名称。

**返回：**`str`。

```python
VEFormat.LongName
```
> \>>> 'ESRI Shapefile'

---

### MultiLayer

---

**功能：**【多图层支持】。类属性，是否支持多图层。

**返回：**`str`。

```python
VEFormat.MultiLayer
```
> \>>> 'No'

---

### SetCreationOptions(*\*\*kwargs*)

---

**功能：**【设置创建选项】。类方法，为此驱动格式修改创建选项。

**可选参数：**

&emsp; \**kwargs：需要配置的参数设置。参数名详见 CreationOptionInfo 中的 name 列。

```python
## 设置 ESRI Shapefile 字段编码为 GBK
VEFormat.SetCreationOptions(ENCODING = 'GBK')
```

---

### Transformable

---

**功能：**【转换支持】。类属性，是否支持转换。

**返回：**`str`。

```python
VEFormat.Transformable
```
> \>>> 'Yes'

---

### Updatable

---

**功能：**【更新支持】。类属性，是否支持更新（修改）。

**返回：**`str`。

```python
VEFormat.Updatable
```
> \>>> 'Yes'

---

