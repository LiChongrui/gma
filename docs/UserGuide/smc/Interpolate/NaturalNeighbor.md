---
title: NaturalNeighbor
date: 2022-10-23
sidebar: false
---

## gma.smc.Interpolate.**NaturalNeighbor**(*Points, Values, Resolution = None*)<Badge text="1.1.0 +"/>
---

**功能：** 【自然邻域法插值】。使用自然邻域法（NaturalNeighbor）将点插值成二维数组。

**参数：**

&emsp;Points：`list||tuple||array` 。插值点 X（经度），Y（纬度）坐标。可为嵌套列表或元组，至少有 2 个坐标点。

&emsp;Values：`array`。坐标点对应的数据值，与 Points 数量相同。

**可选参数：**

&emsp;Resolution = `float`。插值结果的分辨率。默认（None）为 Boundary 经度、纬度差最小值的十分之一。

**返回：** 类型：`namedtuple`。包含数据（Data）和仿射变换（Transform）。

::: warning 注意

1. NaturalNeighbor 插值不会包含输入点范围外的任何数据！

2. NaturalNeighbor 方法不会进行内部坐标转换！

:::

---

**示例：**

```python
import gma
import pandas as pd

Data = pd.read_excel("Interpolate.xlsx")
Points = Data.loc[:, ['经度','纬度']].values
Values = Data.loc[:, ['值']].values

# 插值
NND = gma.smc.Interpolate.NaturalNeighbor(Points, Values, Resolution = 0.05)

gma.rasp.WriteRaster(r'.\gma_NaturalNeighbor.tif',
                     NND.Data,
                     Projection = 'WGS84',
                     Transform = NND.Transform, 
                     NoData = np.nan,
                     DataType = 'Float32')
```

*与 ArcGIS NaturalNeighbor 插值结果（重分类后）对比：*

![fdg](/smc/NaturalNeighbor.webp)

