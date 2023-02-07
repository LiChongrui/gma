---
title: AddGridLines
date: 2023-01-10
sidebar: false
---

## **AddGridLines**(*LONRange = (-180, 180, 15), LATRange = (-90, 90, 15), ShowLON = True, ShowLAT = True, LineColor = 'gray', LineStyle = (0, (6, 6)), LineWidth = 0.3*)

---

**功能：** 【添加经纬网】。在地图框中添加经纬网。

**可选参数：**

&emsp; LONRange = `tuple`。生成经纬网的初始经度、结束经度和间隔。 默认 (-180, 180, 15)。

&emsp; LATRange = `tuple`。生成经纬网的初始纬度、结束纬度和间隔。 默认 (-90, 90, 15)。

&emsp; ShowLON = `tuple`。是否显示经度网。 默认显示（True）。

&emsp; ShowLAT = `tuple`。是否显示纬度网。 默认显示（True）。

&emsp; LineColor = `str||tuple`。经纬网线颜色。如果为 None，则生成随机颜色。详见：matplotlib。

&emsp; LineStyle = `str||tuple`。经纬网线样式。详见：AddLayer 中 LineStyle。

&emsp; LineWidth = `float`。线宽。默认 0.3。

**返回：**`list`。经度网和纬度网 Feature 列表。

---

**示例：**
```python
from gma.map import plot

WorldDS = plot.GetWorldDataSource()
WorldLayer = WorldDS.GetLayer(0)

# 初始化一个地图框，用于绘图
MapF = plot.MapFrame(BaseMapProj = 2163, Extent = None)

# 添加图层（可以重复添加多个图层）
MapL1 = MapF.AddLayer(WorldLayer, FaceColor = None, EdgeColor = 'gray', LineWidth = 0.1)

# 添加经纬网
Grid = MapF.AddGridLines(LONRange = (-180, 180, 30), LATRange = (-90, 90, 15), LineWidth = 0.2)

```
![](/map/AddGridLines.png)

