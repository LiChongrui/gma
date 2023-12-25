---
title: CORR
date: 2021-10-30
sidebar: false
---

## gma.math.Evaluation.**CORR**(*Measure, Simulation, Method = 'pearson', Axis = 0*)
---

**功能：**【r，P】。相关系数和显著性水平。

**参数：**

&emsp;Measure：`list||array`。第一组数据。

&emsp;Simulation：`list||array`。第二组数据。

**可选参数：** 

&emsp;Method = `str`。默认计算皮尔逊相关（pearson）。
        
::: tip 其他支持的方法

kendall（肯德尔秩相关），spearman（斯皮尔曼相关）。

:::

&emsp;Axis = `int` 。数据评估使用的轴。

**返回：**`nametuple`（CORR, P）。

---

**示例：**

```python
from gma import math
```

*序列（1 维）*

```python
MEA = [0.16359164, 0.16359164, 0.17469311, 0.20163227]
SIM = [0.22857143, 0.32706435, 0.21466192, 0.10225949]
EVA = math.Evaluation.CORR(MEA, SIM)
```
> \>>> CORR(CORR=array(-0.8971926), P=array(0.1028074))

*不同计算方法比较*

```python
Methods = ['pearson', 'kendall', 'spearman']
for m in Methods:
    print(m, math.Evaluation.CORR(MEA, SIM, Method = m))
```
> \>>> pearson CORR(CORR=array(-0.8971926), P=array(0.1028074))<br>
> \>>> kendall CORR(CORR=array(-0.91287093), P=array(0.07095149))<br>
> \>>> spearman CORR(CORR=array(-0.9486833), P=array(0.0513167))

*更多维度*
```python
MEA = [[ 0.05120073,  0.05444646,  0.05096978,  0.05096978],
       [ 0.16359164,  0.18061367,  0.16168582,  0.16168582],
       [-0.07699195, -0.07706093, -0.07740774, -0.07740774],
       [ 0.17469311,  0.19315895,  0.15614156,  0.15614156],
       [ 0.2006536 ,  0.18265162,  0.15587704,  0.15587704]]
SIM = [[ 0.22857143,  0.22911051,  0.1908772 ,  0.1908772 ],
       [ 0.2956548 ,  0.3080475 ,  0.22230114,  0.22230114],
       [ 0.32706437,  0.35      ,  0.29352903,  0.29352903],
       [ 0.03658536,  0.03522885,  0.03478987,  0.03478987],
       [-0.10225949, -0.07193749, -0.05467691, -0.05467691]]

## 按照第一个维度计算
EVA0 = math.Evaluation.CORR(MEA, SIM, Axis = 0)
print('"Axis = 0":', EVA0)

## 按照第二个维度计算
EVA1 = math.Evaluation.CORR(MEA, SIM, Axis = 1)
print('"Axis = 1":', EVA1)
```
> \>>> "Axis = 0": CORR(CORR=array([-0.70495502, -0.65676601, -0.69753887, -0.69753887]), P=array([0.18363032, 0.22855325, 0.19036202, 0.19036202]))<br>
> \>>> "Axis = 1": CORR(CORR=array([ 0.63613622,  0.73326187,  0.89015278,  0.40962382, -0.97075341]), P=array([0.36386378, 0.26673813, 0.10984722, 0.59037618, 0.02924659]))