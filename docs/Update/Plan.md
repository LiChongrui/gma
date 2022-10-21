---
title: 更新预览
date: 2022-11-13
sidebar: false
---

&emsp;　更新预览中的新内容将在下一个 gma 版本中发布。下一版本 **1.1.0** 。

---

<font color="#3CB371"><i class="fab fa-superpowers"></i></font> **优化：**

&emsp;　1、smc

&emsp;　　a. 调整坐标点的设置方式为（经度，纬度），*以前为 （纬度，经度）*，以符合大多数人的使用习惯。

&emsp;　　b. 改用半正矢公式（haversine equation）进行空间计算。

&emsp;　2、MKMutationTest

&emsp;　　根据《现代气候统计诊断与预测技术》优化检验过程逻辑。

<font color="#616AE5"><i class="fas fa-award"></i></font> **新增：**

&emsp;　1、增加【[IDW](/UserGuide/smc/Interpolate/IDW.html)】函数

&emsp;　　基于 IDW 法的点数据空间插值。引用：gma.smc.Interpolate.IDW。

&emsp;　2、增加【[CALArea](/UserGuide/smc/CALArea.html)】函数

&emsp;　　计算面积。计算输入多点组成多边形的面积。引用：gma.smc.CALArea。