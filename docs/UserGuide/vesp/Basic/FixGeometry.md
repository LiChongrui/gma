---
title: FixGeometry
date: 2021-10-30
sidebar: false
---

##  gma.vesp.Basic.**FixGeometry**(*InFile, OutFile = None*)
---

**功能：**【修正几何】。修正矢量数据中无效的几何要素。

**参数：** 

&emsp;InFile：`str`。输入矢量文件路径。

**可选参数：** 

&emsp;OutFile = str。输出矢量文件路径。如果不设置（None），则直接在输入矢量文件上修复几何错误。

---

**示例：（下载 [示例矢量](/Open/China_Province_2022.7z)）**

```python
from gma import vesp

InFile = 'China_Province_2022.shp'
OutFile = 'China_Province_2022_Fix.shp'

vesp.Basic.FixGeometry(InFile, OutFile)
```