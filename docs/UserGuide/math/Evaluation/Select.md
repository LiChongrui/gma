---
title: Select
date: 2021-10-30
sidebar: false
---

## gma.math.Evaluation().**Select**(*Method = 'ALL'*)

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

**示例：**

```python
import gma
MEA = [15.1, 33, 88, 158.4]
SIM = [0.8, 1.7, 7.8, 7.4]
EVA = gma.math.Evaluation(MEA, SIM)
```

*一次性获取所有支持方法的结果*

```python
EVA.Select()
```
> \>>> {'r': array(0.87418731),
 'P': array(0.12581269),
 'D': 0.4857905378671188,
 'MaxAE': 136.7,
 'NRMSE': 1.1844165194382599,
 'R2': 0.7642034563762724,
 'RMSE': 87.20266624364189}

*获取其中一个或多个结果*

```python
EVA.Select(Method = ['CORR', 'RMSE'])
```
> \>>> {'r': array(0.87418731), 'P': array(0.12581269), 'RMSE': 87.20266624364189}

