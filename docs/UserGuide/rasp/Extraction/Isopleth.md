---
title: Isopleth
date: 2022-09-26
sidebar: false
---

## gma.rasp.Extraction.**Isopleth**(*InFile, OutFile, Band = 0, Interval = 50, Base = 0, OutFormat = 'ESRI Shapefile'*)

---

**功能：** 【等值线】。生成数量指标值相等的各点连成的平滑曲线。

**参数：** 

&emsp;InFile：`str`。输入栅格路径。

&emsp;OutFile：`str`。输出矢量路径。

**可选参数：**

&emsp;Band = `int`。需要计算的波段，编号从 0 开始。默认（0）为第一个波段。

&emsp;Interval = `float`。等值线间隔。默认为 50。

&emsp;Base = `float`。相对于间隔起始零点的偏移量。默认为 0。

&emsp;OutFormat = `str`。输出文件格式，默认为 ESRI Shapefile。其他格式详见 vesp.ToOtherFormat 函数。

---

**示例：**

```python
from gma import rasp

OutFile = 'Isopleth.shp'
rasp.Extraction.Isopleth(inres.WorldDataSet.DEM, OutFile, Interval = 1000)
```

> 原始DEM与等值线：

![](/rasp/Isopleth.png)