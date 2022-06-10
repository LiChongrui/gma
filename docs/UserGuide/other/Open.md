---
title: Open
date: 2022-03-09
sidebar: false
---

## gma.**Open**(*InFile, Mode = 0, Methed = 'gma'*)

---

**功能：**【打开文件】。打开栅格或矢量数据文件。

**参数：**

&emsp;InFile：`str`。输入文件路径。

**可选参数：**

&emsp;Mode = `int`。读取模式。默认为只读（0），也可为 1（可写模式）。参数设置错误则返回只读模式。

&emsp;Methed = str <Badge text="1.0.9 +"/> 。打开方式（gma 或 osgeo）。默认以 gma 定义的方式打开。参数设置错误则以 gma 的方式打开。

**返回：** 多维数据：返回子数据集列表；其他栅格：返回 [RasterOpen](RasterOpen.html)。矢量数据：返回 [VectorOpen](VectorOpen.html)。

::: warning 注意

1、gma 暂不支持直接读取子数据集。

2、如果需要打开多维数据的子数据集，请以 osgeo 方式打开子数据集路径（一般为每个子数据集信息的第一个元素）！

:::

---

