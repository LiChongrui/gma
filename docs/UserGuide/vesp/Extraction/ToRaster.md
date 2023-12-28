---
title: ToRaster
date: 2021-10-30
sidebar: false
---

## gma.vesp.Extraction.**ToRaster**(*InFile, OutFile, Resolution, Attribute = None, OutNoData = None, OutFormat = 'GTiff'*)

---

**功能：**【矢量转栅格】。将矢量图层转换为栅格文件。

**参数：** 

&emsp;InFile：`str`。输入矢量文件路径。

&emsp;OutFile：`str`。输出栅格文件路径。

&emsp;Resolution：`int`。输出栅格的分辨率。

**可选参数：** 

&emsp;Attribute = `str`。进行转换的矢量数据的字段。如果未设置，则生成由 0 和 1 组成的栅格，0 是 nodata 值。

&emsp;OutNoData = `float`。输出栅格的值无效。默认不设置（None）无效值。

::: warning 注意

如果 Attribute 不为 None 且 OutNoData 未设置，则 OutNoData 修改为无穷大（inf）。

:::

&emsp;OutFormat = `str`。输出栅格文件格式，默认为 GTiff。其他格式详见 rasp.ToOtherFormat 函数。

---

**示例：（下载 [示例矢量](/Open/China_Province_2022.7z)）**

```python
from gma import vesp

InFile = 'China_Province_2022.shp'
OutFile = 'ToRaster.tif'

# 按照属性表 '省级码' 列值写入栅格
vesp.Extraction.ToRaster(InFile, OutFile, 0.3, Attribute = '省级码')
```

> 结果对比：

![](/vesp/ToRaster.png)