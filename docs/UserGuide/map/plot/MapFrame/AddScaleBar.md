---
title: AddScaleBar
date: 2023-01-10
sidebar: false
---

## **AddScaleBar**(*LOC = (0.1, 0.1), Width = 0.2, BarUnit = 'km', Precision = 0, Font = None, FontSize = None, FontPROP = {}, Color = 'black', SpindleWidth = 0.5, ScaleHeight = 0.05, SubSCAScaling = 0.5, Style = 'ScaleBar1'*)<Badge text="1.1.2 +"/> 

---

**功能：** 【添加比例尺】。在地图框中添加比例尺。

**可选参数：**

&emsp; LOC = `tuple`。比例尺相对（于地图框的）位置（X, Y）。 默认 (0.1, 0.1)。

&emsp; Width = `float`。比例尺的相对宽度。为相对于地图框 X 方向长度的倍数。默认 0.2 倍。    

&emsp; BarUnit = `str`。比例尺的单位。目前仅支持 'm'（米） 或 'km'（千米）。其他单位查询：gma.relation.constants.Length。
    
&emsp; Precision = `int`。比例尺标度值保留的小数位数。默认不保留小数位（0）。   

&emsp; Font= `str||None`。 比例尺字体。 默认（None）取决于 matplotlib 设置。

&emsp; FontSize = `float`。 比例尺字体大小。默认（None）根据 Width 自动缩放。

&emsp; FontPROP = `dict`。比例尺字体的其他属性。详见：matplotlib.font_manager.FontProperties。

&emsp; Color = `str||tuplt||None`。比例尺字体颜色。如果为 None，则生成一个随机颜色。详见：matplotlib。

&emsp; SpindleWidth = `float`。主轴宽度（字体单位）。默认 0.5 。    

&emsp; ScaleHeight  = `float`。主刻度缩放（相对于 Width）。默认 0.05 倍。    

&emsp; SubSCAScaling  = `float`。子刻度缩放（相对于 ScaleHeight）。默认 0.5 倍。    

&emsp; Style = `str`。比例尺样式。目前仅支持 'ScaleBar1' 样式。

**返回：**`list`。比例尺形状和字体样式。

::: warning 注意
比例尺的值根据地图坐标系和比例尺长度计算。**对于地理坐标系，比例尺的位置影响比例尺的标注值！**
:::

---

**示例：**
```python
from gma.map import plot

WorldDS = plot.GetWorldDataSource()
WorldLayer = WorldDS.GetLayer(0)

# 初始化地图框，并添加一个图层
MapF = plot.MapFrame(BaseMapProj = 2163, Extent = None)
MapL1 = MapF.AddLayer(WorldLayer, FaceColor = None, EdgeColor = 'gray', LineWidth = 0.1)

# 添加比例尺
ScaleBar = MapF.AddScaleBar(LOC = (0.1, 0.1), Width = 0.22, Color = 'black')
```
![](/map/AddScaleBar.png)

