---
title: MultiSDSToTif
date: 2021-10-30
sidebar: false
---

##  gma.rasp.**MultiSDSToTif**(*InFile, OutPath, Variable = None, Dimension = None, Projection = 'WGS84'*)

---

**功能：**【多维数据转 GTiff】。将含有子数据集的多维数据提取为 GTiff。

**参数：** 

&emsp;InFile：`str`。输入栅格路径。

&emsp;OutPath：`str`。输出文件夹路径。

**可选参数：**

&emsp;Variable  = `list`。要转换变量的 字符串 列表。默认转换所有变量（None）。

&emsp;Dimension  = `list`。要转换维度的 整型数 列表。默认转换所有维度（None）。

&emsp;Projection  = `str`。输入数据的 X，Y 坐标系。默认为 WGS84。

---

