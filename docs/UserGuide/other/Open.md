---
title: Open
date: 2022-03-09
sidebar: false
---

## gma.**Open**(*InFile, Mode = 0*)

---

**功能：**【打开文件】。打开栅格或矢量数据文件。

**参数：**

&emsp;InFile：`str`。输入文件路径。

**可选参数：**

&emsp;Mode = `int`。打开方式，默认为只读（0），也可为 1（可写模式）。参数设置错误则返回只读模式。

**返回：** 多维数据：返回子数据集列表；其他栅格：返回 [RasterOpen](RasterOpen.html)。矢量数据：返回 [VectorOpen](VectorOpen.html)。

::: tip 提示

多维数据如果需要打开子数据集，需要重新 Open 子数据集路径（一般为每个子数据集信息的第一个元素）！

:::

---

