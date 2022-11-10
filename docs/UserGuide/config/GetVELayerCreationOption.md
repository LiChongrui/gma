---
title: GetVELayerCreationOption
date: 2022-04-17
sidebar: false
---

## gma.config.**GetVELayerCreationOption**(*Format*)

---

**功能：**【矢量图层创建选项】。获取矢量驱动格式支持的图层高级创建选项！

**参数：** 

&emsp;Format：`str`。栅格驱动格式名称。

**返回：**`DataFrame`。

---

**示例：**
```python
import gma

# 获取 gma 创建 ESRI Shapefile 文件时的高级参数及配置信息
gma.config.GetVELayerCreationOption('ESRI Shapefile')
```

|    | name                 | type          | description                                                        | default   | Value                                                                                                                                                    |
|---:|:---------------------|:--------------|:-------------------------------------------------------------------|:----------|:---------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | SHPT                 | string-select | type of shape                                                      |       | POINT ARC POLYGON MULTIPOINT POINTZ ARCZ POLYGONZ MULTIPOINTZ POINTM ARCM POLYGONM MULTIPOINTM POINTZM ARCZM POLYGONZM MULTIPOINTZM MULTIPATCH NONE NULL |
|  1 | 2GB_LIMIT            | boolean       | Restrict .shp and .dbf to 2GB                                      | NO        |                                                                                                                                                      |
|  2 | ENCODING             | string        | DBF encoding                                                       | UTF-8     |                                                                                                                                                      |
|  3 | RESIZE               | boolean       | To resize fields to their optimal size.                            | NO        |                                                                                                                                                      |
|  4 | SPATIAL_INDEX        | boolean       | To create a spatial index.                                         | NO        |                                                                                                                                                      |
|  5 | DBF_DATE_LAST_UPDATE | string        | Modification date to write in DBF header with YYYY-MM-DD format    |       |                                                                                                                                                      |
|  6 | AUTO_REPACK          | boolean       | Whether the shapefile should be automatically repacked when needed | YES       |                                                                                                                                                      |
|  7 | DBF_EOF_CHAR         | boolean       | Whether to write the 0x1A end-of-file character in DBF files       | YES       |                                                                                                                                                      |
