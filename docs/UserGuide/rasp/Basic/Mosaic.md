---
title: Mosaic
date: 2021-10-30
sidebar: false
---

## gma.rasp.Basic.**Mosaic**(*InFiles, OutFile, InNoData = None, OutNoData = None, OutFormat = 'GTiff'*)

---

**功能：**【栅格镶嵌】。将多个栅格数据集合并到一个新的栅格数据集中。

**参数：** 

&emsp;InFiles：`list`。镶嵌影像路径集合。

&emsp;OutFile：`str`。输出栅格路径。

**可选参数：**

&emsp;InNoData = `float||list`。输入栅格的无效值。默认自动搜索每个输入栅格的无效值（None）。

&emsp;OutNoData  = `float`。输出栅格的无效值。默认根据输入栅格自动设置（None）。

&emsp;OutFormat  = `str`。输出栅格文件格式。默认为 GTiff，其他格式详见 ToOtherFormat 函数。

---

**示例：**

```python
from gma import rasp

InFiles = ['ESA_WorldCover_0.tif',
           'ESA_WorldCover_1.tif']
rasp.Basic.Mosaic(InFiles, 'ESA_WorldCover_Mosaic.tif')
```
::: tip 提示
InNoData：如果输入栅格已经定义或不含 NoData 值，则不需要配置 InNoData 值。<br>
OutNoData：如果配置了此值，输入栅格 NoData 的区域将被修改为此值。
:::

> 原始数据与镶嵌结果：

![](/rasp/Mosaic.png)