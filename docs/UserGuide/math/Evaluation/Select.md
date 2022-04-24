---
title: Select
date: 2021-10-30
sidebar: false
---

## gma.index.Evaluation().**Select**(*Method = 'ALL'*)

---

**功能：**【选择方法】。按选择的方法返回结果。

**可选参数：** 

&emsp;Method = `str||list||tuple||set`。默认为输出所有方法的结果（ALL）。

::: tip 其他参数设置

1. list、tuple 或 set: 列表、元组或集合内所有方法（ Evaluation 已经定义过算法）的结果。
2. str: 单个评价方法（Evaluation 已经定义过算法，例如 RMSE ）的结果。

:::

::: warning 注意 

选择的方法只支持默认的可选参数。例如 CORR，其计算相关系数的方法只能为 pearson，不能传入其他方法。

:::

**返回：**`dict`。

---
