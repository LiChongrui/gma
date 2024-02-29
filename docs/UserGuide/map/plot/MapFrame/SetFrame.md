---
title: SetFrame
date: 2023-01-10
sidebar: false
---

## **SetFrame**(*FrameColor = 'black', FrameWidth = 0.6, ShowFrame = True, ShowLeft = True, ShowBottom = True, ShowRight = True, ShowTop = True, TickColor = 'black', TickLength = 0.01, TickWidth = 0.4, LabelTickPad = 0.005, Precision = 0, Uint = 'D', UseWESN = True, LabelFont = None, LabelFontSize = 5, LabelFontPROP = {}, LabelColor = 'black'*)<Badge text="1.1.2 +"/> 

---

**功能：** 【设置地图框】。配置地图框的边框、标签和刻度。

**可选参数：**

&emsp; FrameColor = `str||tuple||None`。边框颜色。如果为 None，则生成随机颜色。详见：matplotlib。

&emsp; FrameWidth = `float`。边框线宽。默认 0.6。

::: warning 注意
以下参数在添加了经纬网（AddGridLines）之后才会生效。
:::

&emsp; ShowLeft = `bool`。是否显示左侧经纬网标签和刻度线。 默认显示（True）。

&emsp; ShowBottom = `bool`。是否显示底部经纬网标签和刻度线。 默认显示（True）。

&emsp; ShowRight = `bool`。是否显示右侧经纬网标签和刻度线。 默认显示（True）。

&emsp; ShowTop = `bool`。是否显示顶部经纬网标签和刻度线。 默认显示（True）。

&emsp; TickColor = `str||tuplt||None`。刻度线颜色。如果为 None，则生成随机颜色。详见：matplotlib。

&emsp; TickLength = `float`。刻度线的相对长度。为相对于地图框 X 方向长度的倍数。默认 0.01 倍。

&emsp; TickWidth = `float`。刻度线线宽（字体单位）。默认 0.4 。        

&emsp; LabelTickPad = `float`。刻度线与标签值之间的相对间距。为相对于地图框 X 方向长度的倍数。默认 0.005 倍。    

&emsp; Precision = `int`。经纬网标度值保留的小数位数。默认不保留小数位（0）。   
        
&emsp; Uint = `str`。经纬网标度值保留的单位。可以为 'D'（度）、 'DM'（度分）或 'DMS'（度分秒）。   

&emsp; UseWESN = `bool`。经纬网标度值是否使用 'W'（西经）、'E'（东经）、'S'（南纬）、'N'（北纬）。

&emsp; LabelFont = `str||None`。 标签字体。 默认（None）取决于 matplotlib 设置。

&emsp; LabelFontSize = `float`。 标签字体大小。默认为 7。

&emsp; LabelFontPROP = `dict`。 标签字体的其他属性。详见：matplotlib.font_manager.FontProperties。

&emsp; LabelColor = `str||tuplt||None`。标签字体的颜色。如果为 None，则生成随机颜色。详见：matplotlib。
    
**返回：**`DataFrame`。地图框绘制过程的详细数据。

---

**示例：**
```python
'''示例1'''
from gma.map import plot, inres

# 初始化地图框，并添加一个图层
MapF = plot.MapFrame(BaseMapProj = 9311, Extent = None)
MapL1 = MapF.AddLayer(inres.WorldLayer.Country, FaceColor = None, EdgeColor = 'gray', LineWidth = 0.1)

# 添加地图框
Frame = MapF.SetFrame(FrameColor = 'black', FrameWidth = 0.6)
```
![](/map/SetFrame.png)

```python
'''示例2'''
from gma.map import plot, inres

# 初始化地图框，并添加一个图层
MapF = plot.MapFrame(BaseMapProj = 2163, Extent = None)
MapL1 = MapF.AddLayer(inres.WorldLayer.Country, FaceColor = None, EdgeColor = 'gray', LineWidth = 0.1)
# 添加经纬网
Grid = MapF.AddGridLines(LONRange = (-180, 180, 30), LATRange = (-90, 90, 15), LineWidth = 0.2)

# 设置地图框（包括刻度和经纬度的标注）
Frame = MapF.SetFrame(FrameColor = 'black', FrameWidth = 0.5, LabelFontSize = 7, TickLength = 0.008)
```
![](/map/SetFrame1.png)
