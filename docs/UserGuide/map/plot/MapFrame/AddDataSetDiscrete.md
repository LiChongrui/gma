---
title: AddDataSetDiscrete
date: 2023-01-10
sidebar: false
---

## **AddDataSetDiscrete**(*GMADataSet, Bands = None, CMap = None, ForcedZoom = True, Stretch = None, StretchPROP = {}, Correction = None, CorrectionPROP = {}, UseDataRange = True, Zorder = None*)<Badge text="1.1.3 +"/> <Badge text="beta"/> 

---

**功能：** 【添加离散数据集】。添加离散型栅格数据集。

**参数：**

&emsp; GMADataSet: `gma.algorithm.core.dataio.Data`。一个由 gma.Open 打开的栅格数据集。

**可选参数：**

&emsp; Bands = `list||None`。要绘制的波段序号列表。对于多波段数据，仅支持选择 1、3（RGB）、4（RGBA）个波段。

&emsp; CMap = `str||list||matplotlib.color.Colormap||None`。色带。详见：matplotlib.color.Colormap。

::: warning 注意
1. 如果 CMap 是一个列表，那这个列表必须为 （R, G, B）或 （R, G, B, A）的格式（与 matplotlib 不同）！否则，请自行创建 matplotlib 色带！
2. 如果输入数据集带有色彩映射表，请勿配置色带，否则，数据集色彩映射表将被忽略。色彩优先级：CMap > ColorTable。
:::

&emsp; ForcedZoom = `bool`。是否进行强制缩放。默认强制缩放（True）。

::: tip 提示
当输入数据集分辨率过高或过大时，强制缩放可以极大的提高绘图效率！
:::

&emsp; Stretch = `str||None`。数据拉伸方法。默认不拉伸（None）。详见：gma.math.Stretch。

&emsp; StretchPROP = `dict`。数据拉伸参数（对应拉伸方法）。详见：gma.math.Stretch。

&emsp; Correction = `str||None`。数据变换方法。默认不变换（None）。详见：gma.math.Correction。

&emsp; StretchPROP = `dict`。数据变换参数（对应拉伸方法）。详见：gma.math.Correction。

&emsp; UseDataRange = `bool`。使用数据集的最大值、最小值作为颜色范围（True），或使用数据类型支持的最大值、最小值作为颜色范围（False）。

&emsp; Zorder = `int||None`。图层顺序。如果添加了多个图层，为避免图层上下遮挡错误，请配置此参数。Zorder 越大，图层越靠上。

**返回：**`matplotlib.image.AxesImage`。

---

**示例：** *（下载 [示例栅格](/Open/ELE_China_GEBCO_2020.tif)）*
```python
import gma
from gma.map import plot

WorldDS = plot.GetWorldDataSource()
WorldLayer = WorldDS.GetLayer(0)

DataSet = gma.Open('ELE_China_GEBCO_2020.tif')

# 初始化地图框
MapF = plot.MapFrame(BaseMapProj = 4326, Extent = None)

# 1.1添加矢量图层（可以重复添加多个图层）
MapL1 = MapF.AddLayer(WorldLayer, FaceColor = None, EdgeColor = 'gray', LineWidth = 0.1)

# 1.2 添加栅格数据集（可以重复添加多个栅格数据集）
MapL1 = MapF.AddDataSetDiscrete(DataSet)

# 2.添加经纬网
Grid = MapF.AddGridLines(LONRange = (-180, 180, 30), LATRange = (-90, 90, 15), LineWidth = 0.2)

# 3.设置地图框（包括刻度和经纬度的标注）
Frame = MapF.SetFrame(FrameWidth = 0.5, LabelFontSize = 7, TickLength = 0.008)
```
![](/map/AddDataSetDiscrete.png)

