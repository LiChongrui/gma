---
title: Aggregate
date: 2022-07-10
sidebar: false
---

## gma.rasp.Kernel.**Aggregate**(*InFile, OutFile, KernelSize = 3, Method = 'Max', OutFormat = 'GTiff'*)

---

**功能：** 【栅格聚合】。生成低分辨率栅格。

**参数：** 

&emsp;InFile：`str`。输入栅格路径。

&emsp;OutFile：`str`。输出栅格路径。

**可选参数：**

&emsp;KernelSize = `int`。像元系数。输出栅格分辨率会缩小 KernelSize 倍。默认为 3 。

&emsp;Method = `str`。聚合方法。指出确定每个输出像元值的方式。默认取最大值（Max）。

::: tip 其他聚合方法

Mean（均值） ， Min（最小值），Sum（求和），Median（中值）。

:::

&emsp;OutFormat  = `str`。输出栅格文件格式。默认为 GTiff，其他格式详见 rasp.ToOtherFormat 函数。

**相关函数：**

&emsp;rasp.Basic.Resample

&emsp;math.Kernel.Aggregate

---

**示例：**

```python
from gma import rasp

InFile = 'ESA_LC2020_Luoyang.tif'
OutFile = 'Aggregate.tif'
rasp.Kernel.Aggregate(InFile, OutFile, KernelSize = 3)
```

> 原始数据与聚合结果对比：

![](/rasp/Aggregate.png)