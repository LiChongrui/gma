---
title: ReadRaster
date: 2022-03-09
sidebar: false
---

## io.**ReadRaster**(*InFile, DataSetID = 0, \*\*kwargs*)

---

**功能：**【打开栅格文件】。

**参数：**

&emsp;InFile：`str`。输入文件路径。

**可选参数：**

&emsp;DataSetID = `int`。子数据集序号。对于普通的栅格数据，只能为 0；对于多维数据（例如 netCDF 等），可配置此参数，以打开不同的子数据集。


&emsp;\*\*kwargs: 传递给 gdal.OpenEx 的其他参数。

**返回：** `DataSet`。

***&emsp;类内属性/方法详见：[DataSet](DataSet.html)。***

---

**示例：** *（下载 [示例栅格](/io/ELE_China_GEBCO_2020.tif)）*

```python
from gma import io

RO = io.ReadRaster('ELE_China_GEBCO_2020.tif')
print(RO)
```
> \>>> <gma.algos.dataio.rads.DataSet at 0x......>







