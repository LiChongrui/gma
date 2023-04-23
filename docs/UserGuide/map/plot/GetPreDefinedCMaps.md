---
title: GetPreDefinedCMaps
date: 2023-01-10
sidebar: false
---

## gma.map.plot.**GetPreDefinedCMaps**(PlotCMap = False)<Badge text="1.1.4 +"/> 

---

**功能：** 【获取系统字体】。读取并列出当前系统支持的所有字体名称，方便绘图时使用。

**可选参数：**

&emsp; PlotCMap = `bool`。是否绘制默认色带。默认不绘制（False）。

**返回：** `set`。

---

**示例：**

```python
from gma.map import plot
PlotCMaps = plot.GetPreDefinedCMaps(PlotCMap = True)
```
> \>>> {'Agency FB', 'Algerian', 'Arial', 'Arial Rounded MT Bold', 'Bahnschrift', 'Baskerville Old Face', ...}

![](/map/PlotCMaps.png)
