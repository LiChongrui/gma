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

**示例：**
```python
from gma.map import plot
PlotL = plot.MapFrame()
```
> \>>> <gma.map.layout.MapFrame at 0x......>

