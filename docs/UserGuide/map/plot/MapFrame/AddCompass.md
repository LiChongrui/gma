---
title: AddCompass
date: 2023-01-10
sidebar: false
---

## **AddCompass**(*LOC = (0.8, 0.8), Width = 0.05, Font = None, FontSize = None, FontPROP = {}, Color = 'black', Style = 'Compass1'*)<Badge text="1.1.2 +"/> 

---

**功能：** 【添加指北针】。在地图框中添加指北针。

**可选参数：**

&emsp; LOC = `tuple`。指北针相对（与地图框的）位置（X, Y）。 默认 (0.8, 0.8)。

&emsp; Width = `float`。指北针的相对宽度。为相对于地图框 X 方向长度的倍数。默认 0.05 倍。    

&emsp; Font= `str||None`。 指北针 'N' 字体。 默认（None）取决于 matplotlib 设置。

&emsp; FontSize = `float`。 指北针 'N' 字体大小。默认（None）根据 Width 自动缩放。

&emsp; FontPROP = `dict`。 指北针 'N' 字体的其他属性。详见：matplotlib.font_manager.FontProperties。

&emsp; Color = `str||tuplt||list||None`。指北针颜色。如果为 None，则生成随机颜色。详见：matplotlib。

::: tip 提示
如果 Color 为列表，则会为指北针的每个主体（例如字体 'N' 和指北的形状）分配不同的颜色。
:::

&emsp; Style = `str`。指北针样式。目前仅支持 'Compass1' 样式。

**返回：**`list`。指北针形状和字体样式。

---

**示例：**
```python
from gma.map import plot, inres

# 初始化地图框，并添加一个图层
MapF = plot.MapFrame(BaseMapProj = 9311, Extent = None)
MapL1 = MapF.AddLayer(inres.WorldLayer.Country, FaceColor = None, LineColor = 'gray', LineWidth = 0.1)

# 添加指北针
AddCompass = MapF.AddCompass(LOC = (0.1, 0.8), Color = 'gray')
```
![](/map/AddCompass.png)

