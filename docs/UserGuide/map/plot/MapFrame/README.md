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
| ----- | ------------- | ------------------------------------------------------------ | ---------- |
| 1     | AddLayer      | 添加图层（可以重复添加多个图层）                             | 方法       |
| *1.1* | *AddLabel*    | *添加图层标注，为 layer 模块相关子类的功能*                  | *子类方法* |
| 2     | AddGridLines  | 添加经纬网                                                   | 方法       |
| 3     | AddCompass    | 添加指北针                                                   | 方法       |
| 4     | AddScaleBar   | 添加比例尺                                                   | 方法       |
| 5     | AddLegend     | 为绘制的矢量图层、重分类或唯一值栅格数据集添加图例           | 方法       |
| 6     | SetBackground | 设置背景颜色                                                 | 方法       |
| 7     | SetFrame      | 设置地图框（包括刻度和经纬度的标注等）                       | 方法       |
| 8     | Axes          | `<matplotlib.axes._subplots.AxesSubplot>`。matplotlib 子图，可按需补充或调整 | 属性       |
| 9     | BaseMapProj   | `<gma.map.rcs.SpatRef>` 。底图坐标系（已初始化为空间参考）   | 属性       |
| 10    | FrameFeature  | `<gma.algorithm.core.dataio.Feature>` 。地图框 Feature（ProjWKT） | 属性       |
| 11    | LATLines      | `<gma.algorithm.core.dataio.Feature>` 。纬度网 Feature       | 属性       |
| 12    | LONLines      | `<gma.algorithm.core.dataio.Feature>` 。经度网 Feature       | 属性       |
| 13    | PLengendID    | `list`。添加的图层序号列表（按图层添加顺序排序）             | 属性       |
| 14    | PlotX         | `list`。所有绘制图层的返回值                                 | 属性       |
| 15    | ProjWKT       | `str`。WKT 格式的底图坐标系                                  | 属性       |
| 16    | WorldFeature  | `<gma.algorithm.core.dataio.Feature>` 。世界 Feature（WGS84） | 属性       |

**示例：**

```python
from gma.map import plot
MapF = plot.MapFrame()
```
> \>>> <gma.map.layout.MapFrame at 0x......>

