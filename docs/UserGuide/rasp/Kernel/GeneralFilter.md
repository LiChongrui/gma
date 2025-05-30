---
title: GeneralFilter
date: 2022-07-10
sidebar: false
---

## gma.rasp.Kernel.**GeneralFilter**(*InFile, OutFile, KernelSize = 3, Method = 'Median', OutFormat = 'GTiff'*)

---

**功能：** 【普通滤波】。对影像进行普通滤波处理。

**参数：** 

&emsp;InFile：`str`。输入栅格路径。

&emsp;OutFile：`str`。输出栅格路径。

**可选参数：**

&emsp;KernelSize = `int`。滤波核大小。默认为 3（× 3）。

&emsp;Method = `str`。滤波方法。默认中值滤波（Median）。

::: tip 其他滤波方法

Mean（均值滤波），Min（最小值滤波），Sum（求和滤波），Max（最大值滤波）。

:::

&emsp;OutFormat  = `str`。输出栅格文件格式。默认为 GTiff，其他格式详见 rasp.ToOtherFormat 函数。

**相关函数：**

&emsp;math.Kernel.GeneralFilter

---

**示例：**

```python
from gma import rasp

InFile = 'ESA_LC2020_Luoyang.tif'
OutFile = 'GeneralFilter.tif'
rasp.Kernel.GeneralFilter(InFile, OutFile, KernelSize = 3)
```

> 原始数据与高斯滤波结果对比：

![](/rasp/GeneralFilter.png)

