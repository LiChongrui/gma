---
title: 更新预览
date: 2022-02-08
sidebar: false
---

## 更新前瞻

```mermaid
gantt
        dateFormat  YYYY-MM-DD
        title gma 近期完善内容

        section 库优化

        持续优化: active, des3, 2022-02-10, 2022-03-01

        section 参数检查和初始化

        为 index、math、osf 模块内未实现参数检查和初始化的函数添加参数初始化或检查: crit, after now,20d

```

## 更新测试中的新内容

&emsp;　更新测试中的新内容将在下一个 gma 版本中发布。下一版本 **1.0.6** 。

<font color="#3CB371"><i class="fab fa-superpowers"></i></font> **优化：**

&emsp;　1、FillNoData

&emsp;　　所有的插补方法支持的类型移入 key 中。（内部修改，不影响函数功能。）

&emsp;　2、TRANCoordinate

&emsp;　　优化距离计算算法。现在，即使坐标点跨度巨大，仍能准确的返回计算结果。

<font color="#616AE5"><i class="fas fa-award"></i></font> **新增：**

&emsp;　1、增加 [ToNumericArray](/UserGuide/math.html#tonumericarray) 函数

&emsp;　　强制将输入数据转为数字型数组，无法转换的值将会被修改为 nan。引用：gma.index.ToNumericArray。

<i class="far fa-trash-alt"></i> **移除：**

&emsp;　1、_DFToNumeric

&emsp;　　移除了 _DFToNumeric 函数，相关功能合并至 ToNumericArray 函数。





