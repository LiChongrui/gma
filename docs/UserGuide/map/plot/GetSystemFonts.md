---
title: GetSystemFonts
date: 2023-01-10
sidebar: false
---

## gma.map.plot.**GetSystemFonts**(ShowFonts=False)<Badge text="1.1.4 +"/> 

---

**功能：** 【获取系统字体】。读取并列出当前系统支持的所有字体名称，方便绘图时使用。

**可选参数：**

&emsp; ShowFonts = `bool`。是否预览字体。默认不预览（False）

**返回：** `set`。

---

**示例：**

```python
from gma.map import plot
WorldDS = plot.GetSystemFonts(ShowFonts = True)
```
> \>>> {'Agency FB', 'Algerian', 'Arial', 'Arial Rounded MT Bold', 'Bahnschrift', 'Baskerville Old Face', ...}

![](/map/SystemFonts.png)
