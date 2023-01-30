---
title: AddLayer
date: 2023-01-10
sidebar: false
---

## **AddLegend**(*LegendName = 'Lenged', LOC = 'best', Labels = None, 
                  LabelFont = None, LabelFontSize = 7, LabelFontPROP = {},
                  LabelColor = 'black',  TitleFont = None, TitleFontSize = 9, TitleFontPROP = {},
                  TitleColor = 'black', TitleAlignment = 'center', TitleSEQ = 7, 
                  VerticalInterval = None, HorizontalInterval = None,
                  HandleLength = 3, HandleHeight = 2, HandleTextPad = 0.8,
                  MarkerFirst = True, NColumns = 1, PlotID = None*)

---

**功能：** 【添加图例】。为绘制的矢量图层、重分类或唯一值栅格数据集添加图例。

**可选参数：**

&emsp;LegendName = `str`。图例名。

&emsp;LOC = `int||tuplt||str`。 图例位置。默认为最佳位置。更多内容请参见matplotlib.legend.loc。

&emsp;EdgeColor = `str||tuplt||list||None`。多边形的边界颜色。只适用于 Polygon。其他说明同 FaceColor。

&emsp;Hatch = `str||list||None`。填充样式。只适用于 Polygon。可为 /, \\, |, -, +, x, o, O, ., * 或其组合。如果是一个列表，则为每个 Feature 指定不同的样式，默认无样式（None）。更多信息请参考：matplotlib。

&emsp;LineStyle = `str||tuplt||list||None`。线形。可为 -, --, -., :, (offset, on-off-seq), ...。如果是一个列表，则为每个 Feature 指定不同的线形，默认实线（None）。更多信息请参考：matplotlib。

&emsp;LineWidth = `float||list`。线宽。如果是一个列表，则为每个 Feature 指定不同的线宽。更多信息请参考：matplotlib。

&emsp;LineColor = `str||tuplt||list||None`。线颜色。只适用于 Line。其他说明同 FaceColor。

&emsp;PointColor = `str||tuplt||list||None`。点颜色。只适用于 Point。其他说明同 FaceColor。

&emsp;PointSize = `float||list||None`。点大小。只适用于 Point。如果是一个列表，则为每个 Feature 指定不同的大小。更多信息请参考：matplotlib。

&emsp;PointMarker = `str||list||None`。点标记。只适用于 Point。如果是一个列表，则为每个 Feature 指定不同的标记。更多信息请参考：matplotlib。

&emsp;Labels = `str||None`。为每个 Feature 添加一个标注。如果想从 矢量属性表 中添加标注，请忽略此参数，并配置 FieldName 参数。

&emsp;FieldName = `str||list||None`。字段名。从矢量字段提取标注信息，以便后续标注。

&emsp;Connector = `str`。多字段连接字符。如果 FieldName 定义了多个字段，那么字段之间用此字符连接。

&emsp;Zorder = `int`。图层顺序。如果添加了多个图层，为避免图层上下遮挡错误，请配置此参数。Zorder 越大，图层越靠上。

---

**示例：**
```python
from gma.map import plot

```
> \>>> 

