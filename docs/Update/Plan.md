---
title: 更新预览
date: 2022-04-17
sidebar: false
---

&emsp;　更新预览中的新内容将在下一个 gma 版本中发布。下一版本 **1.0.8** 。

<font color="#3CB371"><i class="fab fa-superpowers"></i></font> **优化：**

&emsp;　1、重构指数计算模块 index，增加多维数据的计算支持。

&emsp;　2、重构数学计算 math 模块，增加多维数据计算支持。

&emsp;　　a、Smooth、Evaluation、FillNoData：增加轴 Axis 参数，多维数据支持定义计算轴。

&emsp;　　b、FillNoData：移除了 time 插值方法。

&emsp;　3、修改 GTiff 格式的默认压缩方式为 DEFLATE，并使用最高级别压缩（12），生成过程分块（TILED）。

&emsp;　4、MultiThreading

&emsp;　　添加 Process 参数，控制多线程进度条显示。

<font color="#FFA500"><i class="fas fa-tools"></i></font> **修复**

&emsp;　1、TVDI

&emsp;　　修复了一个引起拟合结果异常的问题。

&emsp;　2、Reproject

&emsp;　　修复了一个引起重投影结果异常的问题。