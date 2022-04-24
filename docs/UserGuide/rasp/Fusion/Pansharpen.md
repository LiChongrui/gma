---
title: Pansharpen
date: 2021-10-30
sidebar: false
---

## gma.rasp.Fusion.**Pansharpen**(*InPanchromatic, InMultispectral, OutFile， ResampleMethod = None, SpatAdjust = None, Bands = None, NumThreads = None, InNoData = None, OutFormat = 'GTiff'*)

---

**功能：**【Pansharpen】。对全色影像和多光谱影像基于 Pansharpen 方法进行融合。

**参数：** 

&emsp;InPanchromatic：`str`。输入全色影像路径。

&emsp;Multispectral：`str`。输入多光谱影像数据。

&emsp;OutFile：`str`。输出栅格路径。

**可选参数：** 

&emsp;ResampleMethod = `str`。重采样方法。默认为 Cubic 法（None）。其他方法详见 Resample 函数。

&emsp;SpatAdjust = `str`。空间坐标系调整。默认为 Union（None）。

::: tip 其他空间坐标系调整方法

Intersection，NoneWithoutWarning。

:::

&emsp;Bands = `list`。融合多光谱波段列表。例如[1,2...]，波段计数从 1 开始。默认融合输入多光谱数据的所有波段（None）。

::: warning 注意

每个波段的权重值（Weights）相同，根据 Bands 数量确定，为 1 / len(Bands)。

:::

&emsp;NumThreads = `int||ALL_CPUS`。融合使用计算机 CPU 的线程数。默认不使用多线程（None）。

&emsp;InNoData = `float`。全色和多光谱影像的无效值。默认不设置无效值（None）。

::: warning 注意

所有输入数据的无效值应当相同，否则该设置无效。输出文件的无效值也为该值。

:::

&emsp;OutFormat = `str`。输出栅格文件格式。默认为 GTiff，其他格式详见 ToOtherFormat 函数。

---

