---
title: Datum
date: 2023-01-10
sidebar: false
---

## gma.crs.**Datum**(*Name = 'WGS_1984', EllipsoidName = 'WGS84', UseDefaultEllips = True, SemiMajor = 6378137.0, InvFlattening = 298.2572236*)

---

**功能：** 创建一个自定义基准面。

**可选参数：**

&emsp; Name = `str`。基准面名称。

&emsp; EllipsoidName = `str`。椭球体名称。

&emsp; UseDefaultEllips = `bool`。是否使用内置椭球体参数。

::: tip 说明

**True**：EllipsoidName 必须为 crs.Ellips 下内置椭球体名称，且忽略 SemiMajor、InvFlattening 参数。

**False**：EllipsoidName 仅作为新椭球体自定义名称，且应用 SemiMajor、InvFlattening 参数。

::: 

&emsp; SemiMajor = `float`。椭球体长半轴（m）。

&emsp; InvFlattening = `float`。椭球体反扁率。

**返回：** `Datum`。

---

**示例：**

```python
from gma import crs

NewDatum = crs.Datum(Name = 'GMADatum', EllipsoidName = 'CGCS2000')
print(NewDatum)
```

> \>>> <gma.algos.spat.datum.Datum at 0x...>




