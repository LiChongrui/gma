---
title: Open:SubDataSet
date: 2022-03-09
sidebar: false
---

&emsp;　含有子数据集的科学数据集（此处以 netCDF 数据为例）可从 [中山大学网站](http://globalchange.bnu.edu.cn/research/soil2) 下载。

```python
import gma
SDS = gma.Open('C1.nc')
```

&emsp;　打开的 **含有子数据集的科学数据集** 具有如下所列的 方法/属性：

::: warning 注意
并非所有的 netCDF 数据都含有子数据集！只具有 1 个子数据集的科学数据集可以理解为普通的栅格（例如 GTiff）。
:::

## **SubInfo** 

---

**功能：**【子数据集信息】。类属性，获取所有子数据集信息列表。

**返回：**`list`。

```python
SDS.SubInfo
```
> \>>> [('NETCDF:"C1.nc":C1', '[8x4320x7560] C1 (32-bit integer)'),
 ('NETCDF:"C1.nc":C2', '[8x4320x7560] C2 (32-bit integer)')]

---

## **GetSubDataSet**(*SUBID = 0*)

---

**功能：**【获取子数据集】。根据 ID 读取子数据集为 DataSet。

**可选参数：**

 &emsp;SUBID = `int`。子数据集序号，编号从 0 开始。默认（0）为第一个子数据集。

**返回：**[DataSet](DataSet.html)。

```python
SDS.GetSubDataSet()
```
> \>>> <gma.algorithm.core.dataio.DataSet at 0x......>

---
