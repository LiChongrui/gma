---
title: ReadArrayAsDataSet
date: 2023-04-04
sidebar: false
---

## io.**ReadArrayAsDataSet**(*Array, Projection = None, Transform = None, DataType = None, NoData = None*)

---

**功能：** 【读取 NumPy 数组 为 DataSet】。

**参数：**

&emsp;Array：`array`。输入数组。

**可选参数：**

&emsp;Projection  = `str||EPSG||WKT||Proj4||SpatRef||...` 。输出栅格坐标系。默认不指定坐标系（None）。

&emsp;Transform  = `tuple`。输出栅格的仿射变换。默认不指定仿射变换（None）。

&emsp;Format   = `str`。输出栅格文件格式。默认为 GTiff。其他格式详见 ToOtherFormat 函数。

&emsp;DataType  = `int||str`。输出栅格数据类型的代码或字符串标记。默认根据写出数组的数据类型确定（None），其他类型详见 ChangeDataType 函数。

&emsp;NoData = `float`。输出栅格的无效值。默认不设置无效值（None）。

**返回：**`DataSet`。

---

**示例：**
```python
from gma import io
import numpy as np

np.random.seed(1992)
Data = np.random.uniform(0, 100, size = (50, 100))
DataSet = io.ReadArrayAsDataSet(Data, Projection = 3857)
```
> \>>> <gma.algos.dataio.rads.DataSet at 0x......>

![](/io/ReadArrayAsDataSet.png)
