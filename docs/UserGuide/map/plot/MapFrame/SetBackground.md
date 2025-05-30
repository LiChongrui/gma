---
title: SetBackground
date: 2023-01-10
sidebar: false
---

## **SetBackground**(*Color = '#BEE8FF'*)<Badge text="1.1.2 +"/> 

---

**功能：** 【设置背景颜色】。设置绘图区域的背景颜色。

**可选参数：**

&emsp; Color = `str||tuplt||None`。背景色。如果为 None，则生成随机颜色。详见：matplotlib。

**返回：**`gma.map.layer.PlotLPolygon`。

---

**示例：**
```python
from gma.map import plot, inres

# 初始化一个地图框，用于绘图
MapF = plot.MapFrame(BaseMapProj = 9311, Extent = None)

# 添加图层（可以重复添加多个图层）
MapL1 = MapF.AddLayer(inres.WorldLayer.Country, FaceColor = None, LineColor = 'gray', LineWidth = 0.1)

# 设置底图颜色
Background = MapF.SetBackground(Color = '#BEE8FF')
```
![](/map/SetBackground.png)

