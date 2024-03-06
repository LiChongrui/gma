---
title: Open
date: 2022-03-09
sidebar: false
---

## io.**Open**(*InFile, \*args, \*\*kwargs*)

---

**功能：**【打开文件】。打开栅格或矢量数据文件。

**参数：**

&emsp;InFile：`str`。输入文件路径。

**可选参数：**

&emsp;\*args, \*\*kwargs。传递给 gdal.OpenEx 的其他参数。

**返回：** `GeoDataBase`。

***&emsp;类内属性/方法详见：[GeoDataBase](GeoDataBase.html)。***

---

**示例：**

```python
from gma import io
```
*打开矢量数据（下载 [示例矢量](/io/China_Province_2022.7z)）*

```python
GDB = io.Open('China_Province_2022.shp')
print(GDB)
```
> \>>> <gma.algos.dataio.database.GeoDataBase at 0x......>
