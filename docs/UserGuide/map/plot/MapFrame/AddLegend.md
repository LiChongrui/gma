---
title: AddLegend
date: 2023-01-10
sidebar: false
---

## **AddLegend**(*LegendName = 'Lenged', LOC = 'best', Labels = None,  LabelFont = None, LabelFontSize = 7, LabelFontPROP = {}, LabelColor = 'black',  TitleFont = None, TitleFontSize = 9, TitleFontPROP = {}, TitleColor = 'black', TitleAlignment = 'center', TitleSEQ = 7, VerticalInterval = None, HorizontalInterval = None, HandleLength = 3, HandleHeight = 2, HandleTextPad = 0.8, MarkerFirst = True, NColumns = 1, PlotID = None*)<Badge text="1.1.2 +"/> 

---

**功能：** 【添加图例】。为绘制的矢量图层、重分类或唯一值栅格数据集添加图例。

**可选参数：**

&emsp; LegendName = `str`。图例名。

&emsp; LOC = `int||tuplt||str`。 图例位置。默认为最佳位置。更多内容请参见matplotlib.legend.loc。

&emsp; Labels = `None||list`。 图例标签。默认（None）使用图层标签。

&emsp; LabelFont = `str||list`。 标签字体。如果为列表，则每个标签分配不同的字体。 默认（None）取决于 matplotlib 设置。

&emsp; LabelFontSize = `float||list`。 标签字体大小。如果为列表，则每个标签分配不同的字体。 默认为 7。

&emsp; LabelFontPROP = `dict||list`。 标签字体的其他属性。如果为列表，则为每个标签分配不同的属性。详见：matplotlib.font_manager.FontProperties。

&emsp; LabelColor = `str||tuplt||list||None`。标签字体的颜色。如果为 None，则生成随机颜色。如果是一个列表，则为每个标签指定不同的颜色。详见：matplotlib。

&emsp; TitleFont = `str`。 图例名字体。 默认（None）取决于 matplotlib 设置。

&emsp; TitleFontSize  = `float`。 图例名字体大小。如果为列表，则每个标签分配不同的字体。 默认为 7。

&emsp; TitleFontPROP = `dict`。 图例名字体的其他属性。详见：matplotlib.font_manager.FontProperties。

&emsp; TitleColor = `str||tuple`。标签字体的颜色。如果为 None，则生成随机颜色。详见：matplotlib。

&emsp; TitleAlignment = `str`。图例标题的对齐方式。可为 'center', 'left' 或 'right'。默认居中（'center'）。

&emsp; TitleSEQ = `float`。图例项和标题之间的间隔。默认为 7。

&emsp; VerticalInterval = `float||None`。图例项之间的垂直间隔。默认（None）取决于 matplotlib 的设置。

&emsp; HorizontalInterval = `float||None`。图例项之间的垂直间隔。默认（None）取决于 matplotlib 的设置。

&emsp; HandleLength = `float`。图例项长度。默认为 3。

&emsp; HandleHeight = `float`。图例项宽度。默认为 2。

&emsp; HandleTextPad = `float`。图例项与图例文本之间的间距。默认为 0.8。

&emsp; MarkerFirst = `bool`。（图例项和文本）是否图例项在前。默认（True）图例项在前，文本在后。

&emsp; NColumns = `int`。图例列数。默认 1 列。

&emsp; PlotID = `list||None`。选择添加图例的图层序号（依据添加到地图框中的图层先后）。默认（None） 添加全部图层。

**返回：**`matplotlib.Figure.legend`。

---

**示例：**
```python
from gma.map import plot, inres

# 初始化一个地图框，用于绘图
MapF = plot.MapFrame(BaseMapProj = 9311, Extent = None)

# 添加图层（可以重复添加多个图层，定义标注使用 'Name'列）
MapL1 = MapF.AddLayer(inres.WorldLayer.Country, FaceColor = None, EdgeColor = 'gray', LineWidth = 0.1, 
                      FieldName = 'Name')

# 添加图例（标注属性表 'Name' 列）
Legend = MapF.AddLegend(LOC = (1, 0.1), NColumns = 1, TitleAlignment = 'left') 
```
![](/map/AddLegend.png)

