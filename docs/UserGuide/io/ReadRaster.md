---
title: ReadRaster
date: 2022-03-09
sidebar: true
---

## io.**ReadRaster**(*InFile, DataSetID = 0, \*\*kwargs*)

---

**功能：**【打开栅格文件】。

**参数：**

&emsp;InFile：`str`。输入文件路径。

**可选参数：**

&emsp;DataSetID = `int`。子数据集序号。对于普通的栅格数据，只能为 0；对于多维数据（例如 netCDF 等），可配置此参数，以打开不同的子数据集。

::: tip 提示

打开一个普通栅格时，此函数与 Open 函数等效。

:::

&emsp;\*\*kwargs: 传递给 gdal.OpenEx 的其他参数。

**返回：** `DataSet`。

---

**示例：**
```python
from gma import io

RO = io.ReadRaster('ELE_China_GEBCO_2020.tif')
print(RO)
```
> \>>> <gma.algos.dataio.rads.DataSet at 0x......>

## 类内属性/方法






