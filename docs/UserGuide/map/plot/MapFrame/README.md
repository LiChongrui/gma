---
title: 初始化
date: 2023-01-10
sidebar: false
---

## gma.map.plot.**MapFrame**(*Axes = None, BaseMapProj = 'WGS84', Extent = None*)<Badge text="1.1.2 +"/> 

---

**功能：** 【类】。初始化一个地图框。

**初始化：**

&emsp;Axes = `None||matplotlib.~.AxesSubplot`。一个 matplotlib 子图。默认（None）自动创建子图。

::: warning 注意
gma 会自动禁用大部分的 matplotlib 子图配置功能！如有需求请反馈！
:::

&emsp;BaseMapProj = `str||EPSG||WKT||Proj4||SpatRef||...` 。底图坐标系，默认为 WGS84。

::: tip 提示
后续添加的所有数据都会被重投影到此坐标系。
:::

&emsp;Extent = `tuple` 。WGS84 坐标系下的绘图范围（左、下、右、上）。默认为底图坐标系所支持的最大范围。

---

**已包含的类方法/属性：**

| 序号  | 名称          | 描述                                                         | 类型       |
| :----- | :------------- | :------------------------------------------------------------ | :---------- |
| M.1     | [AddLayer](/UserGuide/map/plot/MapFrame/AddLayer.html)      | 添加图层（可以重复添加多个图层）                             | 方法       |
| *M.1.1* | *AddLabel*    | *添加图层标注，为 layer 模块相关子类的功能*                  | *子类方法* |
| M.2     | [AddCompass](/UserGuide/map/plot/MapFrame/AddCompass.html)    | 添加指北针                                                   | 方法       |
| M.3     | [AddGridLines](/UserGuide/map/plot/MapFrame/AddGridLines.html)   | 添加经纬网（仅经纬网线）                             | 方法       |
| M.4     | [AddLegend](/UserGuide/map/plot/MapFrame/AddLegend.html)      | 为绘制的矢量图层、重分类或唯一值栅格数据集添加图例           | 方法       |
| M.5     | [AddScaleBar](/UserGuide/map/plot/MapFrame/AddScaleBar.html)    | 添加比例尺                                                   | 方法       |
| M.6     | [AddDataSetClassify](/UserGuide/map/plot/MapFrame/AddDataSetClassify.html)    | 添加重分类栅格数据集图层                                               | 方法       |
| M.7     | [AddDataSetDiscrete](/UserGuide/map/plot/MapFrame/AddDataSetDiscrete.html)    | 添加离散型栅格数据集图层                                               | 方法       |
| M.7     | [SetBackground](/UserGuide/map/plot/MapFrame/SetBackground.html)  | 设置背景颜色                                                 | 方法       |
| M.8     | [SetFrame](/UserGuide/map/plot/MapFrame/SetFrame.html)       | 设置地图框（包括刻度和经纬度的标注等）                       | 方法       |
| P.1     | Axes          | `<matplotlib.axes._subplots.AxesSubplot>`。matplotlib 子图，可按需补充调整 | 属性       |
| P.2     | BaseMapProj   | `<gma.map.rcs.SpatRef>` 。底图坐标系（已初始化为空间参考）   | 属性       |
| P.3    | FrameFeature  | `<gma.algorithm.core.dataio.Feature>` 。地图框 Feature（ProjWKT） | 属性       |
| P.4    | LATLines      | `<gma.algorithm.core.dataio.Feature>` 。纬度网 Feature       | 属性       |
| P.5    | LONLines      | `<gma.algorithm.core.dataio.Feature>` 。经度网 Feature       | 属性       |
| P.6    | PLengendID    | `list`。添加的图层序号列表（按图层添加顺序排序）             | 属性       |
| P.7    | PlotX         | `list`。所有绘制图层的返回值                                 | 属性       |
| P.8    | ProjWKT       | `str`。WKT 格式的底图坐标系                                  | 属性       |
| P.9    | WorldFeature  | `<gma.algorithm.core.dataio.Feature>` 。底图坐标系的最大范围 Feature（WGS84） | 属性       |

**示例：**

```python
from gma.map import plot
MapF = plot.MapFrame(BaseMapProj = 2163, Extent = None)
```
> \>>> <gma.map.layout.MapFrame at 0x......>

**绘图流程的简单示例：**
```python
WorldDS = plot.GetWorldDataSource()
WorldLayer = WorldDS.GetLayer(0)

# 1.添加图层（可以重复添加多个图层）
MapL1 = MapF.AddLayer(WorldLayer, FaceColor = None, EdgeColor = 'gray', LineWidth = 0.1)
## 1.1 为此图层添加标注(标注属性表 'Name' 列)
MapL1.AddLabel(FieldName = 'Name', FontSize = 4)

# 2.添加经纬网
Grid = MapF.AddGridLines(LONRange = (-180, 180, 30), LATRange = (-90, 90, 15), LineWidth = 0.2)

# 3.设置地图框（包括刻度和经纬度的标注）
Frame = MapF.SetFrame(FrameWidth = 0.5, LabelFontSize = 7, TickLength = 0.008)

# 4.设置底图颜色
Background = MapF.SetBackground(Color = '#BEE8FF')

# *5.地图整饰要素
## 5.1 添加指北针
Compass = MapF.AddCompass(LOC = (0.06, 0.86), Width = 0.05, Color = 'black')
## 5.2 添加比例尺
ScaleBar = MapF.AddScaleBar(LOC = (0.02, 0), Width = 0.22, Color = 'black')
## 5.3 添加图例
Legend = MapF.AddLegend(LOC = (1, 0.1), NColumns = 1, TitleAlignment = 'left')
```
![](/map/MapFrame.png)
