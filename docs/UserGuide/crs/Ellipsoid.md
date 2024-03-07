---
title: Ellipsoid
date: 2023-01-10
sidebar: false
---

## gma.crs.**Ellipsoid**(*Name = 'WGS84', UseDefaultEllips = True, SemiMajor = 6378137.0, InvFlattening = 298.2572236*)

---

**功能：** 创建一个自定义椭球体。

**可选参数：**

&emsp; Name = `str`。椭球体名称。

&emsp; UseDefaultEllips = `bool`。是否使用内置椭球体参数。

::: tip 说明

**True**：EllipsoidName 必须为 crs.Ellips 下内置椭球体名称，且忽略 SemiMajor、InvFlattening 参数。

**False**：EllipsoidName 仅作为新椭球体自定义名称，且应用 SemiMajor、InvFlattening 参数。

::: 

&emsp; SemiMajor = `float`。椭球体长半轴（m）。

&emsp; InvFlattening = `float`。椭球体反扁率。

**返回：** `Ellipsoid`。


---


**示例：**

```python
from gma import crs

NewEllipsoid = crs.Ellipsoid(Name = 'CGCS2000')
print(NewEllipsoid)
```

> \>>> <gma.algos.spat.datum.Ellipsoid at 0x...>