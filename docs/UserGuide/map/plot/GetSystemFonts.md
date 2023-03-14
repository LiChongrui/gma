---
title: GetSystemFonts
date: 2023-01-10
sidebar: false
---

## gma.map.plot.**GetSystemFonts**()<Badge text="1.1.4 +"/> 

---

**功能：** 【获取系统字体】。读取并列出当前系统支持的所有字体名称，方便绘图时使用。

**返回：** `set`。

---

**示例：**
```python
from gma.map import plot
WorldDS = plot.GetSystemFonts()
```
> \>>> {'Agency FB', 'Algerian', 'Arial', 'Arial Rounded MT Bold', 'Bahnschrift', 'Baskerville Old Face', ...}

