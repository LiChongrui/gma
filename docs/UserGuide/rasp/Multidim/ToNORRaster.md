---
title: ToNORRaster
date: 2021-10-30
sidebar: false
---

##  gma.rasp.Multidim.**ToNORRaster**(*InFile, OutPath, Variable = None, ExtAllBands = True, Projection = None, OutFormat = 'GTiff'*)

---

**功能：**【多维数据转 GTiff】。将含有子数据集的多维数据提取为单波段的 GTiff 格式文件。

**参数：** 

&emsp;InFile：`str`。输入栅格路径。

&emsp;OutPath：`str`。输出文件夹路径。

**可选参数：**

&emsp;Variable  = `list`。要转换变量的 字符串 列表。默认转换所有变量（None）。

&emsp;ExtAllBands  = `bool`。是否将每个子数据的每个波段提取到单个文件中。

&emsp;Projection  = `str`。输入数据的 X，Y 坐标系。可配置 None，自动读取输入多维数据的坐标系。默认为 ‘WGS84’。

&emsp;OutFormat  = `str`。输出栅格文件格式。默认为 GTiff，其他格式详见 ToOtherFormat 函数。

---

**示例：**

```python
from gma import rasp

rasp.Multidim.ToNORRaster('C1.nc', '.', Variable = 'C1', Dimension = 1, Projection = 'WGS84')
```