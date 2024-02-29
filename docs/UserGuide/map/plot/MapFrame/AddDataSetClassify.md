---
title: AddDataSetClassify
date: 2023-03-01
sidebar: false
---

## **AddDataSetClassify**(*GMADataSet, Bands = None, CMap = None, ForcedZoom = True, Remap = None, Method = 'Range', Labels = None, Zorder = None*)<Badge text="1.1.4 +"/>

---

**功能：** 【添加分类数据集】。添加分类后栅格数据集图层。

**参数：**

&emsp; GMADataSet: `DataSet`。一个由 gma.io.ReadRaster 打开的栅格数据集。

**可选参数：**

&emsp; Bands = `list||None`。要绘制的波段序号列表。仅支持选择 1 个波段，默认（None）为第一个波段。

&emsp; CMap = `str||list||matplotlib.color.Colormap||None`。色带。详见：matplotlib.color.Colormap。

::: warning 注意
1. 如果 CMap 是一个列表，那这个列表必须为 （R, G, B）或 （R, G, B, A）的格式（同 matplotlib ）！否则，请自行创建 matplotlib 色带！
2. 如果输入数据集带有色彩映射表，请勿配置色带，否则，数据集色彩映射表将被忽略。色彩优先级：CMap > ColorTable。
:::

&emsp; ForcedZoom = `bool`。是否进行强制缩放。默认强制缩放（True）。

::: tip 提示
当输入数据集分辨率过高或过大时，强制缩放可以极大的提高绘图效率！
:::

&emsp; Remap = `list||None`。用于将输入值或范围定义重新映射到新值。默认（None）不进行重分类映射。格式为：

&emsp;&emsp;&emsp;1、[[mapping1，value1]，[mmapping2，value2]，…]。

&emsp;&emsp;&emsp;2、[mapping1，mmapping2，…]。

&emsp; Method = `str`。重分类方法。可以为 'Range' 或 'Unique'，默认为 'Range'。

::: tip 提示

'Range':  范围映射分类。
                
'Unique': 严格一对一映射分类。

例如：

Remap = [[1000, 1],
             [2000, 2],
             [3000, 3]]

1. Method = 'Range'.

        Data <= 1000: --> 1
        1000 < Data <= 1000: --> 2
        2000 < Data <= 3000: --> 3
        Data > 3000: --> NoData

2. Method = 'Unique'.

        Data == 1000: --> 1
        Data == 2000: --> 2   
        Data == 3000: --> 3 
        Other values: --> NoData

:::

&emsp; Labels = `list||None`。为每个 分类结果 添加一个标注。其数量应与 Remap 重分类表数量相同。默认（None）无标注。

&emsp; Zorder = `int||None`。图层顺序。如果添加了多个图层，为避免图层上下遮挡错误，请配置此参数。Zorder 越大，图层越靠上。

**返回：**`gma.map.dataset.PlotDataSet`。

---

**示例：**
```python
from gma.map import plot, inres

# 1.初始化一个地图框，用于绘图
MapF = plot.MapFrame(Axes = None, BaseMapProj = 4326, Extent = None)

# 2.将内置的世界矢量图层添加到地图框
MapL1 = MapF.AddLayer(inres.WorldLayer.Country, FaceColor = 'none', LineWidth = 0.2, LineColor = 'white', Zorder = 1)

Classify = MapF.AddDataSetClassify(inres.WorldDataSet.DEM,
                                   CMap = 'rainbow',
                                   Remap = [0, 500, 1000,1500, 2000, 3000, 9000],
                                   Method = 'Range', 
                                   Labels = ['<= 0', '0 ~ 500', '500 ~ 1000','1000 ~ 1500','1500 ~ 2000','2000 ~ 3000', '> 3000'],
                                  )

MapF.AddGridLines(LONRange = (-180, 180, 30))
Frame = MapF.SetFrame()

MapF.AddLegend(TitleAlignment = 'left', PlotID = [1], LOC = (-0.2, 0.2))

```
![](/map/AddDataSetClassify.jpg)

