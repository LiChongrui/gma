---
title: Check
date: 2021-10-30
sidebar: false
---

## gma.vesp.Basic.**Check**(*InFile*)

---

**功能：**【检查】。检查每个矢量要素的有效性。

**参数：** 

&emsp;InFile：`str`。输入矢量文件路径。

**返回：** 通过：Pass；不通过：无效要素的 FID 列表（list）。

---

**示例：（下载 [示例矢量](/Open/China_Province_2022.7z)）**
```python
from gma import vesp

InFile = 'China_Province_2022.shp'
vesp.Basic.Check(InFile)
```
> \>>>  [9]