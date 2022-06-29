---
title: \_\_init\_\_
date: 2021-10-30
sidebar: false
---

## gma.math.**Evaluation**(*Measure, Simulation, Axis = None*)

---

**功能**：【类】。数据评估。

**初始化：**

&emsp;Measure：`list||array`。实测数据。

&emsp;Simulation：`list||array`。模拟数据。

&emsp;Axis = `int` <Badge text="1.0.8 +"/> 。数据评估使用的轴。默认（None）将输入数据展开为 1 维数据，轴为 0。

::: warning 注意

类内 属性/方法 引用前请先初始化 `Evaluation` 类！

::: 

---

**示例：**
```python
import gma
MEA = [0.16359164, 0.16359164, 0.17469311, 0.20163227]
SIM = [0.22857143, 0.32706435, 0.21466192, 0.10225949]
EVA = gma.math.Evaluation(MEA, SIM)
## 查看类型所有的 方法/属性
print([M for M in dir(EVA) if '_' not in M])
```
> \>>> ['CORR', 'D', 'MaxAE', 'Methods', 'NRMSE', 'R2', 'RMSE', 'Select']

