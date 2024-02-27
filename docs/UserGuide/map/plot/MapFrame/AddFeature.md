---
title: AddFeature
date: 2023-04-10
sidebar: false
---

## **AddFeature**(*GMAFeature, FaceColor = '#BED2FF', LineColor = '#B2B2B2', Hatch = None, LineStyle = None, LineWidth = 0.5, PointSize = 0.5, PointMarker = None, Label = None,  FieldName = None, Connector = '', Zorder = None*)<Badge text="1.1.5 +"/> 

---

**功能：** 【添加矢量要素】。在地图框中添加一个要素。

**参数：**

&emsp; GMAFeature: `Feature`。一个 gma.io.ReadVector().GetFeature() 获取的矢量要素。

**可选参数：**

&emsp; FaceColor = `str||tuplt||list||None`。多边形的填充颜色。只适用于 Polygon。如果为 None，则生成随机颜色。如果是一个列表，则为每个 Feature 指定不同的颜色。详见：matplotlib。

&emsp; EdgeColor = `str||tuplt||list||None`。多边形的边界颜色。只适用于 Polygon。其他说明同 FaceColor。

&emsp; Hatch = `str||list||None`。填充样式。只适用于 Polygon。如果是一个列表，则为每个 Feature 指定不同的样式，默认无样式（None）。详见：matplotlib。

::: tip 填充样式
可为 '/'， '\\'，'|'， '-'，'+'，'x'，'o'，'O'，'.'，'*' 或其组合（例如：Hatch = '/|-+++'）。
:::

&emsp; LineStyle = `str||tuplt||list||None`。线形。如果是一个列表，则为每个 Feature 指定不同的线形，默认实线（None）。详见：matplotlib。

::: tip 线形
可为 '-'，'--'，'-.'，':'，(offset, on-off-seq)，...。
:::

&emsp; LineWidth = `float||list`。线宽。如果是一个列表，则为每个 Feature 指定不同的线宽。

&emsp; LineColor = `str||tuplt||list||None`。线颜色。只适用于 Line。其他说明同 FaceColor。

&emsp; PointColor = `str||tuplt||list||None`。点颜色。只适用于 Point。其他说明同 FaceColor。

&emsp; PointSize = `float||list||None`。点大小。只适用于 Point。如果是一个列表，则为每个 Feature 指定不同的大小。

&emsp; PointMarker = `str||list||None`。点标记。只适用于 Point。如果是一个列表，则为每个 Feature 指定不同的标记。详见：matplotlib。

::: tip 标记
'.'，','，'o'，'v'，'^'，'<'，'>'，'1'，'2'，'3'，'4'，'8'，'s'，'p'，'P'，'*'，'h'，'H'，'+'，'x'，'X'，'D'，'d'，'|'，'_'，0，1，2，3，4，5，6，7，8，9，10，11，'None',  ' '，''，'\$...\$'，Path，...。
:::

&emsp; Label = `str||None`。为每个 Feature 添加一个标注。如果想从 矢量属性表 中添加标注，请忽略此参数，并配置 FieldName 参数。

&emsp; FieldName = `str||list||None`。字段名。从矢量字段提取标注信息，以便后续标注。

&emsp; Connector = `str`。多字段连接字符。如果 FieldName 定义了多个字段，那么字段之间用此字符连接。

&emsp; Zorder = `int`。图层顺序。如果添加了多个图层，为避免图层上下遮挡错误，请配置此参数。Zorder 越大，图层越靠上。

**返回：**`gma.map.feature.PlotFeature`。

---

**示例：**
```python
from gma.map import plot, inres

Points = [[112.5, 34.4], [30, 60], [2.3, 48.8], [47.5, -18.9], [112.5, 34.4]]
# 创建线 Feature
FPolygon = plot.CreatePlotFeature(Points, GeomType = 'Polygon')

# 1.初始化一个地图框，底图 0 定义的坐标系
MapF = plot.MapFrame(Axes = None, BaseMapProj = 4326, Extent = None)

MapL1 = MapF.AddLayer(inres.WorldLayer.Country, LineWidth = 0.1)
# 2.2 添加面
MapL1 = MapF.AddFeature(FPolygon, FaceColor = (0.2, 0.5, 0.8, 0.5), LineColor = 'gray', LineWidth = 0.5, Zorder = 2)
```
![](/map/AddFeature.png)

