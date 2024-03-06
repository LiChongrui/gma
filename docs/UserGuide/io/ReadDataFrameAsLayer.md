---
title: ReadDataFrameAsLayer
date: 2023-04-04
sidebar: false
---

## io.**ReadDataFrameAsLayer**(*DataFrame, Projection = 'WGS84', KeepWKT = False*)

---

**功能：** 【读取 pandas 数据帧（DataFrame） 为 Layer】。

::: tip 提示

若 DataFrame 中存在记录矢量几何体的 WKT 字符串（WKT列），则自动将此列转换为矢量几何体。

:::

**参数：**

&emsp;Array：`DataFrame`。输入 pandas 数据帧（DataFrame）。

**可选参数：**

&emsp;Projection  = `str||EPSG||WKT||Proj4||SpatRef||...` 。输出栅格坐标系。默认为 'WGS84'。

&emsp;KeepWKT  = `bool`。是否保留 DataFrame 中的几何体信息到属性表。默认不保留（False）。

**返回：**`Layer`。

***&emsp;类内属性/方法详见：[Layer](Layer.html)。***

---

**示例：**
```python
from gma import io
import pandas as pd

Data = [['Point(120 44)','Test1'],
        ['Point(121 44)','Test2']]
DF = pd.DataFrame(Data, columns = ['WKT', 'Test'], index = ['Geom1', 'Geom2'])
LY = io.ReadDataFrameAsLayer(DF, KeepWKT = True)

print(LY)
```
> \>>> <gma.algos.dataio.rads.DataSet at 0x......>

> \>>> *属性表如下：*

|    | WKT           | Test   |
|---:|:--------------|:-------|
|  0 | Point(120 44) | Test1  |
|  1 | Point(121 44) | Test2  |