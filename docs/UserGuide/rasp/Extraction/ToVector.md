---
title: ToVector
date: 2021-10-30
sidebar: false
---

## gma.rasp.**ToVector**(*InFile, OutVector, FieldName = 'Value', TranBand = 1, OutFormat = 'ESRI Shapefile'*)

---

**功能：**【栅格转矢量】。将栅格数据转换为矢量数据。

**参数：** 

&emsp;InFile：`str`。输入栅格路径。

&emsp;OutVector：`str`。输出矢量路径。

**可选参数：**

&emsp;FieldName  = `str`。输出矢量字段的名称。默认为 Value。

&emsp;TranBand  = `int`。要转换的波段。默认转换第一个波段（1）。

&emsp;OutFormat   = `str`。输出矢量文件格式，默认为 ESRI Shapefile。其他格式详见 vesp.ToOtherFormat 函数。

::: tip 提示

不需要设置类型（点、线、面等），默认根据栅格数据自动确定类型。

:::

---

