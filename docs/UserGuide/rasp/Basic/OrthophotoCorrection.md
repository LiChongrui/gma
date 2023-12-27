---
title: OrthophotoCorrection
date: 2021-10-30
sidebar: false
---

## gma.rasp.Basic.**OrthophotoCorrection**(*InFile, OutFile, DEM = None, Resample = 0, OutFormat = 'GTiff'*)

---

**功能：**【正射校正】。根据有理多项式系数（RPC）对影像进行正射校正。

**参数：** 

&emsp;InFile：`str`。输入栅格路径。

::: warning 注意

输入栅格必须有内部 RPC（有理多项式系数）元数据或同路径下描述 RPC 的外部 .rpb 或 _RPC.txt 文件。

:::

&emsp;OutFile：`str`。输出栅格路径。

**可选参数：**

&emsp;DEM  = `float||str`。用于 RPC 计算的 固定海拔 或 DEM 文件的名称。默认不设置此参数（None）。

&emsp;Resample  = `int||str`。重采样方法。默认为 Nearest Neighbour 法（0）。其他重采样方法详见 Resample 函数。

&emsp;OutFormat   = `str`。输出栅格文件格式。默认为 GTiff，其他格式详见 ToOtherFormat 函数。

---

