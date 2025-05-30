---
title: Simplify
date: 2021-10-30
sidebar: false
---

##  gma.vesp.Basic.**Simplify**(*InFile, OutFile, Tolerance = 0*)<Badge text="1.0.6 +"/>

---

**功能：**【简化几何】。简化矢量数据中的要素。

**参数：** 

&emsp;InFile：`str`。输入矢量文件路径。

&emsp;OutFile：`str`。输出矢量文件路径。

**可选参数：** 

&emsp;Tolerance = float。简化几何要素时允许的几何容差。默认为 0。

---


**示例：（下载 [示例矢量](/Open/China_Province_2022.7z)）**

```python
from gma import vesp

InFile = 'China_Province_2022.shp'
OutFile = 'China_Province_2022_Simplify.shp'

vesp.Basic.Simplify(InFile, OutFile, Tolerance = 0.05)
```

> 结果对比：

![](/vesp/Simplify.png)
