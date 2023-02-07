---
title: SetFrame
date: 2023-01-10
sidebar: false
---

## **SetFrame**(FrameColor = 'black', FrameWidth = 0.6, ShowFrame = True, ShowLeft = True, ShowBottom = True, ShowRight = True, ShowTop = True, TickColor = 'black', TickLength = 0.01, TickWidth = 0.4, LabelTickPad = 0.005, Precision = 0, Uint = 'D', UseWESN = True, LabelFont = None, LabelFontSize = 5, LabelFontPROP = {}, LabelColor = 'black')

---

**功能：** 【设置地图框】。配置地图框的边框、标签和刻度。

**可选参数：**

&emsp; FrameColor = `str||tuple||None`。边框颜色。如果为 None，则生成随机颜色。详见：matplotlib。

&emsp; FrameWidth = `float`。边框线宽。默认 0.6。

&emsp; ShowLeft = `bool`。是否显示左侧经纬网标签和刻度线。 默认显示（True）。

&emsp; ShowBottom = `bool`。是否显示底部经纬网标签和刻度线。 默认显示（True）。

&emsp; ShowRight = `bool`。是否显示右侧经纬网标签和刻度线。 默认显示（True）。

&emsp; ShowTop = `bool`。是否显示顶部经纬网标签和刻度线。 默认显示（True）。

        TickColor = str, tuplt or None. Default 'black'.
            Ticks color. If None, a random color will be generated. For more, see matplotlib.
        
        TickLength = float. Default 0.01.
            Ticks length. It is a multiple of the length of the X-axis relative to the map frame.
        
        TickWidth = float. Default 0.4.
            Ticks width. In font-size units. 
        
        LabelTickPad = float. Default 0.005.
            Spacing of label and tick. It is a multiple of the length of the X-axis relative to the map frame.
        
        Precision = int. Default 0.  
            The number of decimal places reserved when labeling the degrees of the latitude and longitude grid.
    
        Uint = str. Default 'D'.
            The unit of the tick value. May be 'D'(degree), 'DM'(degree minute), or 'DMS'(degree minute second).
        
        UseWESN = bool. Default True.
            Whether to use 'W', 'E', 'N', 'S' after longitude or latitude.
        
        LabelFont = str, None. Default None.
            The font of the label. Default(None) depends on the matplotlib setting.
        
        LabelFontSize = float. Default 5.
            The font size of the label. For more, see matplotlib.font_manager.FontProperties.
    
        LabelFontPROP = dict. Default {}.
            The other font properties of the label. For more, see matplotlib.font_manager.FontProperties.
    
        LabelColor = str, tuple or None. Default 'black'.
            The label color. If None, a random color will be generated. For more, see matplotlib.
    
        Returns
        ----------
        A DataFrame of plot info.

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

plt.savefig(r'D:\github\gma\docs\.vuepress\public\map\SetFrame.png', transparent=True, bbox_inches = 'tight')
```
![](/map/AddGridLines.png)

