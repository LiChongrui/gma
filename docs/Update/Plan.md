---
title: 更新预览
date: 2022-10-13
sidebar: false
---

&emsp;　更新预览中的新内容将在下一个 gma 版本中发布。下一版本 **1.0.13** 。

---

<font color="#616AE5"><i class="fas fa-award"></i></font> **新增：**

&emsp;　1、为 climet 增加 Other 类组

&emsp;　　提供 DaylightHours【白昼时数】、Declination【赤纬】、HourAngle【时角】、RDBSunAndEarth【日地相对距离】、SolarRadiationFluxOA【大气层外太阳辐射通量】计算！

&emsp;　2、增加【[Isopleth](/UserGuide/raa/Extraction/Isopleth.html)】函数

&emsp;　　计算等值线，生成数量指标值相等的各点连成的平滑曲线。引用：gma.raa.Extraction.Isopleth。

<font color="#3CB371"><i class="fab fa-superpowers"></i></font> **优化：**

&emsp;　1、依赖库

&emsp;　　调整依赖库最低版本限制：**pandas >= 1.4.2，numpy >= 1.23.3，scipy >= 1.7.3，gdal >= 3.4.1**。