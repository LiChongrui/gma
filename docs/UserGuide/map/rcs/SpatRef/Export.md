---
title: Export
date: 2023-01-10
sidebar: false
---

## **Export**(*Format = 'Wkt'*)<Badge text="1.1.2 +"/> 

---

**功能：** 【导出坐标系】。将空间参考导出为坐标系。

**可选参数：**

&emsp; Format = `str`。坐标系格式。

::: tip 支持导出为
EPSG，MICoordSys，PCI，PROJJSON，PrettyWkt，Proj4，USGS，Wkt，XML 格式。
::: 

---

**示例：**
```python
from gma.map import rcs
SR = rcs.SpatRef('WGS84')
SR.Export(Format = 'Proj4')
```

> \>>> '+proj=longlat +datum=WGS84 +no_defs'
