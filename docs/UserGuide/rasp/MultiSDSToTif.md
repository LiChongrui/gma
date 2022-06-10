---
title: MultiSDSToTif
date: 2021-10-30
sidebar: false
---

##  gma.rasp.**MultiSDSToTif**(*InFile, OutPath, Variable = None, Dimension = None, Projection = 'WGS84'*)

---

**功能：**【多维数据转 GTiff】。将含有子数据集的多维数据提取为单波段的 GTiff 格式文件。

**参数：** 

&emsp;InFile：`str`。输入栅格路径。

&emsp;OutPath：`str`。输出文件夹路径。

**可选参数：**

&emsp;Variable  = `list`。要转换变量的 字符串 列表。默认转换所有变量（None）。

&emsp;Dimension  = `list`。要转换维度的 整型数 列表。默认转换所有维度（None）。

&emsp;Projection  = `str`。输入数据的 X，Y 坐标系。默认自动读取输入多维数据的坐标系（None）。

---

**示例：*（2 变量 8 维度的 netCDF 数据）***

```python
import gma
# 查看多维数据的变量信息
DataSet = gma.Open('C1.nc')
DataSet
```
> \>>> [('NETCDF:"C1.nc":C1', '[8x4320x7560] C1 (32-bit integer)'),<br>
  　　　('NETCDF:"C1.nc":C2', '[8x4320x7560] C2 (32-bit integer)')]

> *一共有两个变量 C1、C2，每个变量均为 8×4320×7560 。*

*提取第一个变量 C1 的第 1 个维度*

```python
gma.rasp.MultiSDSToTif('C1.nc', '.', Variable = 'C1', Dimension = 1, Projection = 'WGS84')
# 查看生成文件数量
len(gma.osf.GetPath('.', EXT = '.tif'))
```
> \>>> 1

*提取第一个变量 C1 的所有维度*

```python
gma.rasp.MultiSDSToTif('C1.nc', '.', Variable = 'C1', Dimension = None, Projection = 'WGS84')
len(gma.osf.GetPath('.', EXT = '.tif'))
```
> \>>> 8

*提取所有变量的所有维度*

```python
gma.rasp.MultiSDSToTif('C1.nc', '.', Variable = None, Dimension = None, Projection = 'WGS84')
len(gma.osf.GetPath('.', EXT = '.tif'))
```
> \>>> 16