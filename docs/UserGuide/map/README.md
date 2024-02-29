---
title: 模块简介
date: 2024-01-20
sidebar: false
---

&emsp;&emsp; 本模块的绘图功能基于 matplotlib，依托 gma 栅格数据集（DataSet）、矢量图层（Layer）、矢量要素（Feature）和地理空间坐标参考系统（SpatRef）等 gma 基础数据类实现， 绘图流程功能设计参考了ArcGIS Pro。本模块绘图的基本成图构造如下：

![](/map/plotins.png)

&emsp;&emsp; gma 地理绘图的主要过程为：

**&emsp;&emsp; 第一步：添加一个地图框**

&emsp;&emsp; 与 ArcGIS 地图框类似，后续所有数据均在地图框内添加和绘制。

**&emsp;&emsp; 第二步：添加数据（包括** **矢量图层、矢量要素、栅格数据集等）、并配置参数（颜色、大小、宽度等）**

&emsp;&emsp; 与ArcGIS 类似，这些数据在添加到地图框后均会被重投影到地图框配置的底图坐标系上；可配置的参数类似ArcGIS的符号系统，例如矢量数据的背景色、边界色等，栅格数据的色带（颜色条）、拉伸方式（例如直方图均衡化）和数据变换（例如 gamma 变换）等。

**&emsp;&emsp; 第三步：添加地图整饰要素（例如：指北针、比例尺和图例等）。**

&emsp;&emsp; 与 ArcGIS 的地图整饰要素类似，可通过参数控制颜色、大小、样式等。

&emsp;&emsp; 本模块的主要功能分类如下：

![](/map/map.png)

 **导入此模块**

```python
from gma.map import plot, inres
```



