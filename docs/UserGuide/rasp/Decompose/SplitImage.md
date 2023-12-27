---
title: SplitImage
date: 2021-10-30
sidebar: false
---

## gma.rasp.Decompose.**SplitImage**(*InFile, OutPath, Size=256, Lap=0, FillValue=None*)

---

**功能：**【影像切片】。将一幅影像切分为特定行列数的小影像（切片）。

**参数：** 

&emsp;InFile：`str`。输入栅格路径。

&emsp;OutPath：`str`。输出文件夹路径。

::: tip 提示

输出切片会自动命名。命名规则：

&emsp;<输入文件名>\_<切片左边界>_<切片上边界>.<驱动扩展名>

:::

**可选参数：**

&emsp;Size = `int`。切片大小。切片结果的行列数大小。默认为 256。

&emsp;Lap = `int`。输出相邻切片的重叠度，默认不重叠（0）。

&emsp;FillValue = `None||float||'AUTO'`。边缘切片不足 Size 大小时的处理方法。默认忽略边缘值（None）。

::: tip 不同参数的含义

* None: （默认设置）忽略边缘值。不会进行扩展，不足 Size 大小的部分切片时将被舍弃。

* float: 不足 Size 的部分将用此值填充。

* AUTO: 不足 Size 的部分将用输入栅格的 NoData 值填充。若 NoData不存在，则自动尝试扩展填充值。

:::

---

**示例：**

```python
from gma import rasp

InFile = 'ESA_LC2020_Luoyang.tif'
OutPath = 'SplitImage'

rasp.Decompose.SplitImage(InFile, OutPath, Size = 2048)
```