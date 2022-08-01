---
title: GaussFilter
date: 2022-07-10
sidebar: false
---

## gma.math.Kernel.**GaussFilter**(*Data, KernelSize = 3, NoData = None, Axis = None, EdgeEXPMode = 'Edge', Sigma = 1, NSRange = 1*)<Badge text="1.0.11 +"/>

---

**功能：** 【高斯滤波】。利用高斯核对数组进行滤波处理。

**参数：** 

&emsp;Data: 所有数据类型。需要计算的数据。

**可选参数：**

&emsp;KernelSize = `int`。滤波核大小。默认为 3 。

&emsp;NoData = `float`。输入数组中的无效值。此值不会参与滤波计算，默认自动设置（None）。

&emsp;Axis = `int||list`。计算轴。默认自动扩展到所有轴（None）。

&emsp;EdgeEXPMode = `str||float`。边缘数据扩展方法。默认使用边缘值扩展（'Edge'）。

::: tip 其他边缘值处理方法

str: Edge，Linear_Ramp，Maximum，Mean，Median，Minimum，Reflect，Symmetric，Wrap，Empty。
            
float: 若配置为常数，则用此常数扩展。

:::       

&emsp;Sigma = `float`。生成高斯滤波核的标准差。默认为 1。
        
&emsp;NSRange = `float`。生成高斯滤波核的范围。默认为高斯分布 ± 1 个标准差内。

**返回：**`array`。

---

