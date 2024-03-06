---
title: ReadVector
date: 2022-03-09
sidebar: true
---

## io.**ReadVector**(*InFile, LayerID = 0, Encoding = None, \*\*kwargs*)

---

**功能：**【读取矢量文件】。

**参数：**

&emsp;InFile：`str`。输入文件路径。

**可选参数：**

&emsp;LayerID = `int`。子图层序号。对于普通的矢量数据，只能为 0；对于多维矢量（例如 GPKG  等），可配置此参数，以打开不同的子图层。

&emsp;Encoding = `str||None` 。属性表字段的字符编码，默认自动（None）解码。

::: tip 提示

当属性表乱码时，可以配置此参数，gma 会按照新的编码方式重新解码矢量属性表。

:::

&emsp;\*\*kwargs：传递给 gdal.OpenEx 的其他参数。

**返回：** `Layer`。

***&emsp;类内属性/方法详见：[Layer](Layer.html)。***

---

**示例：***（下载 [示例矢量](/io/China_Province_2022.7z)）*
```python
from gma import io

VO = io.ReadVector('China_Province_2022.shp')
print(VO)
```
> \>>> <gma.algos.dataio.vesd.Layer at 0x......>



