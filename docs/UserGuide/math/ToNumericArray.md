---
title: ToNumericArray
date: 2021-10-30
sidebar: false
---

##  gma.index.**ToNumericArray**(*Data*) <Badge text="1.0.6 +"/> 

---

**功能：**【转换为数字型数组】。强制将输入数据转为数字型数组，无法转换的值将会被修改为 nan。

**参数：**

&emsp;Data：`所有数据类型` 。需要转换的数据。

**返回：**`array`。

::: tip 提示

自 <Badge text="1.0.8" vertical='middle'/> 版本开始支持多维数据转换。

::: 


---

**示例：**
```python
import gma
```
*单个值（0 维）*

```python
Data = None
gma.math.ToNumericArray(Data)
```
> \>>> array(nan)

*更多维度（1 维及以上）*

```python
Data = [1,2,3,4,'sad',None,2,34]
gma.math.ToNumericArray(Data)
```
> \>>> array([ 1.,  2.,  3.,  4., nan, nan,  2., 34.])





