---
title: AddLayer
date: 2023-01-10
sidebar: false
---

## **AddLayer**(*GMALayer, FaceColor = '#BED2FF', LineColor = '#B2B2B2', Hatch = None, LineStyle = None, LineWidth = 0.5, PointSize = None, PointMarker = None, Labels = None, FieldName = None, Connector = '', AutoSimplify = True, Zorder = None*)

---

**功能：** 【添加矢量图层】。在地图框中添加一个图层。

**参数：**

&emsp; GMALayer: `Layer`。一个由 gma.io.ReadVector 打开的矢量图层。

**可选参数：**

&emsp; FaceColor = `str||tuplt||list||None`。多边形（包括点）的填充颜色。如果为 None，则生成随机颜色。如果是一个列表，则为每个 Feature 指定不同的颜色。详见：matplotlib。

&emsp; LineColor = `str||tuplt||list||None`。线、多边形边缘、点边缘的线颜色。其他说明同 FaceColor。

&emsp; Hatch = `str||list||None`。多边形（包括点）的填充样式。如果是一个列表，则为每个 Feature 指定不同的样式，默认无样式（None）。详见：matplotlib。

::: tip 填充样式
可为 '/'， '\\'，'|'， '-'，'+'，'x'，'o'，'O'，'.'，'*' 或其组合（例如：Hatch = '/|-+++'）。
:::

&emsp; LineStyle = `str||tuplt||list||None`。线、多边形边缘、点边缘的线样式。如果是一个列表，则为每个 Feature 指定不同的线形，默认实线（None）。详见：matplotlib。

::: tip 线形
可为 '-'，'--'，'-.'，':'，(offset, on-off-seq)，...。
:::

&emsp; LineWidth = `float||list`。线、多边形边缘、点边缘的线宽度。如果是一个列表，则为每个 Feature 指定不同的线宽。

&emsp; PointSize = `float||list||None`。点大小。只适用于 Point。如果是一个列表，则为每个 Feature 指定不同的大小。

&emsp; PointMarker = `str||list||None`。点标记。只适用于 Point。如果是一个列表，则为每个 Feature 指定不同的标记。详见：matplotlib。

::: tip 标记
'.'，','，'o'，'v'，'^'，'<'，'>'，'1'，'2'，'3'，'4'，'8'，'s'，'p'，'P'，'*'，'h'，'H'，'+'，'x'，'X'，'D'，'d'，'|'，'_'，0，1，2，3，4，5，6，7，8，9，10，11，'None',  ' '，''，'\$...\$'，Path，...。
:::

&emsp; Label = `list||None`。为每个 Feature 添加一个标注。如果想从 矢量属性表 中添加标注，请忽略此参数，并配置 FieldName 参数。

&emsp; FieldName = `str||list||None`。字段名。从矢量字段提取标注信息，以便后续标注。

&emsp; Connector = `str`。多字段连接字符。如果 FieldName 定义了多个字段，那么字段之间用此字符连接。

&emsp; AutoSimplify = `bool`<Badge text="2.0.2 +"/> 。是否自动简化图层，以提高绘图速率。默认（True）自动简化。

&emsp; Zorder = `int`。图层顺序。如果添加了多个图层，为避免图层上下遮挡错误，请配置此参数。Zorder 越大，图层越靠上。

**返回：**`gma.map.layer.PlotLayer`。

---

**示例：**
```python
from gma.map import plot, inres

# 初始化一个地图框，用于绘图
MapF = plot.MapFrame(BaseMapProj = 9311, Extent = None)

# 添加图层（可以重复添加多个图层）
MapL1 = MapF.AddLayer(inres.WorldLayer.Country, FaceColor = None, LineColor = 'gray', LineWidth = 0.1)
```
![](/map/AddLayer.png)

