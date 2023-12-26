---
title: GaussFilter
date: 2022-07-10
sidebar: false
---

## gma.raa.Kernel.**GaussFilter**(*InFile, OutFile, KernelSize = 3, OutFormat = 'GTiff'*)<Badge text="1.0.11 +"/>

---

**功能：** 【高斯滤波】。利用高斯核对影像进行滤波处理。

**参数：** 

&emsp;InFile：`str`。输入栅格路径。

&emsp;OutFile：`str`。输出栅格路径。

**可选参数：**

&emsp;KernelSize = `int`。滤波核大小。默认为 3（× 3）。

&emsp;OutFormat  = `str`。输出栅格文件格式。默认为 GTiff，其他格式详见 rasp.ToOtherFormat 函数。

**相关函数：**

&emsp;math.Kernel.GaussFilter

---

