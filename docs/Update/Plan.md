---
title: 更新预览
date: 2022-08-13
sidebar: false
---

&emsp;　更新预览中的新内容将在下一个 gma 版本中发布。下一版本 **1.0.12** 。

---

<font color="#616AE5"><i class="fas fa-award"></i></font> **新增：**

&emsp;　1、增加【[MKMutationTest](/UserGuide/climet/MKMutationTest.html)】函数

&emsp;　　基于 Mann-Kendall 方法对时间序列数据进行突变检验。引用：gma.climet.MKMutationTest。

<font color="#3CB371"><i class="fab fa-superpowers"></i></font> **优化：**

&emsp;　　简化、调优多处代码，提高代码的可读性。

<font color="#FF4500"><i class="fas fa-exclamation-circle"></i></font> **已知问题：**

&emsp;　　gdal 3.4.1 等版本与 numpy 1.23.1 等版本可能存在兼容问题。若出现 numpy 相关导入错误，请尝试变更 numpy 版本。