---
title: 更新预览
date: 2022-05-08
sidebar: false
---

&emsp;　更新预览中的新内容将在下一个 gma 版本中发布。下一版本 **1.0.9** 。

<font color="#616AE5"><i class="fas fa-award"></i></font> **新增：**

&emsp;　引入 extend 扩展组。今后，尝鲜或非必要功能会合入此处。此模块功能**不提供**详细示例和说明，请自行使用 help 函数根据帮助探索应用。目前包含：

&emsp;　1、mapplottools

&emsp;　　空间绘图支持模块（依赖 cartopy）。提供 AddCompass（添加指北针）、AddScaleBar（添加比例尺）、AddGeometries（添加几何图形（.shp文件））、AddLegend（添加图例（离散型））和 GetCRS （获取支持的坐标系）功能。

&emsp;　2、arrayenhancement

&emsp;　　数组增强。提供 Stretch （数据拉伸）和 Correction （数据变换）两个类。

&emsp;　　a. Stretch

&emsp;　　提供 Percentage（百分比截断）、STD（标准差）、MaxMin（最大值最小值）、HistEqualize（直方图均衡化） 四种拉伸方式。

&emsp;　　b. Correction

&emsp;　　提供 Gamma（伽马变换）、Log（对数变换）、Sigmoid（S 型曲线函数变换）三种变换方式。

<font color="#FFA500"><i class="fas fa-tools"></i></font> **修复**

&emsp;　1、ToArray

&emsp;　　修复了一个当提取窗口边界超过栅格行列数时不能返回默认结果的错误。

&emsp;　2、其他

&emsp;　　修复了若干特殊情况下才会出现的错误。

<font color="#3CB371"><i class="fab fa-superpowers"></i></font> **优化：**

&emsp;　1、重构矢量处理模块 vesp，以实现所有的矢量处理函数在底层隶属于一个整体，而不仅仅是许多单独的函数的集合。

&emsp;　2、Open

&emsp;　　为 Open 添加 Method 参数，读取数据时可选择以 gma 定义的方式或 osgeo 原生方式打开。
