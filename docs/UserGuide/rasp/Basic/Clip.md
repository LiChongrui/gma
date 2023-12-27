---
title: Clip
date: 2021-10-30
sidebar: false
---

## gma.rasp.Basic.**Clip**(*InFile, OutFile, CutLineFile, LayerID = 0, FeatureID = None, InNoData = None, OutNoData = None, OutFormat = 'GTiff'*)

---

**功能：**【裁剪】。按矢量边界裁剪栅格。

**参数：** 

&emsp;InFile：`str`。输入栅格路径。

&emsp;OutFile：`str`。输出栅格路径。

&emsp;CutLineFile：`str`。裁剪矢量文件路径。

**可选参数：**

&emsp;LayerID = `int` <Badge text="1.0.7 +"/> 。输入裁剪矢量的图层 ID。默认第一个图层（0）。

&emsp;FeatureID = `list` <Badge text="1.0.7 +"/> 。掩膜图层的要素 ID。默认掩膜全部要素（None）。

&emsp;InNoData = `float`。输入栅格的无效值。默认不指定（None）无效值。

&emsp;OutNoData  = `float`。输出栅格的无效值。默认不指定（None）无效值。

&emsp;OutFormat  = `str`。输出栅格文件格式。默认为 GTiff，其他格式详见 ToOtherFormat 函数。

---

**示例：**

```python
from gma import rasp

InFile = 'ESA_LC2020_Luoyang.tif'
CutLineFile = 'Chanhe.shp'
OutFile = 'ESA_LC2020_Luoyang_Chanhe.tif'

# 定义裁剪结果路径并执行裁剪，并为边界外数据分配无数据值
rasp.Basic.Clip(InFile, OutFile, CutLineFile, OutNoData = 0)
```

> 原始数据与裁剪结果：

![](/rasp/Clip.png)

