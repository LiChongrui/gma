---
title: AddCompass
date: 2023-01-10
sidebar: false
---

## **AddCompass**(*LOC = (0.8, 0.8), Width = 0.05, Font = None, FontSize = None, FontPROP = {}, Color = 'black', Style = 'Compass1'*)<Badge text="1.1.2 +"/> 

---

**功能：** 【添加经纬网】。在地图框中添加经纬网。

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
import gma
from gma.map import plot

WorldDS = plot.GetWorldDataSource()
WorldLayer = WorldDS.GetLayer(0)

DataSet = gma.Open('ELE_China_GEBCO_2020.tif')

# 初始化地图框
MapF = plot.MapFrame(BaseMapProj = 3857, Extent = None)

# 1.1添加矢量图层（可以重复添加多个图层）
MapL1 = MapF.AddLayer(WorldLayer, FaceColor = None, EdgeColor = 'gray', LineWidth = 0.1)

# 1.2 添加栅格数据集（可以重复添加多个图层）
MapL1 = MapF.AddDataSetDiscrete(DataSet)

# 2.添加经纬网
Grid = MapF.AddGridLines(LONRange = (-180, 180, 30), LATRange = (-90, 90, 15), LineWidth = 0.2)

# 3.设置地图框（包括刻度和经纬度的标注）
Frame = MapF.SetFrame(FrameWidth = 0.5, LabelFontSize = 7, TickLength = 0.008)
```
![](/map/AddCompass.png)

