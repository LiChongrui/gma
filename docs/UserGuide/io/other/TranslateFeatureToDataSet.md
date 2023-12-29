---
title: TranslateFeatureToDataSet
date: 2023-04-04
sidebar: false
---

## io.**TranslateFeatureToDataSet**(*GMAFeature, Resolution = 1, Attribute = None, Boundary = None*)<Badge text="1.1.5 +"/> 

---

**功能：** 【转换 Feature 到 DataSet】。

**参数：**

&emsp; GMAFeature: `Feature`。一个待转换的 Feature。

**可选参数：**

&emsp; Resolution = `float`。分辨率。默认 1。

&emsp; Attribute = `str||None`。属性名。如果不设置（None），则根据图层的几何边界生成 0、1 数据集。

&emsp; Boundary = `tuple`。输出栅格数据集的四至边界（左、下、右、上），默认（None）为矢量图层的四至边界。

**返回：**`DataSet`。

---

**示例**