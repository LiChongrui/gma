---
title: BandDecomposition
date: 2021-10-30
sidebar: false
---

##  gma.rasp.**BandDecomposition**(*InFile, OutPath, Bands = None, OutFormat = 'GTiff'*)
---

**功能：**【波段分解】。将多波段文件拆分（或提取）为单波段文件。

**参数：** 

&emsp;InFile：`str`。输入栅格路径。

&emsp;OutPath：`str`。输出文件夹路径。

**可选参数：**

&emsp;Bands = `int||list`。需要导出文件的波段，编号从 1 开始。默认全部导出（None）。

&emsp;OutFormat  = `str`。输出栅格文件格式。默认为 GTiff，其他格式详见 ToOtherFormat 函数。

---

