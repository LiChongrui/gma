---
title: 使用指南
date: 2021-10-30
---

**&emsp;&emsp;用户指南** 为 **gma** 内 6 大模块所有相关函数的详细功能、参数设置和引用方法说明，如果您想快速了解 gma 中每个模块所有函数的整体情况，请移步 [函数功能列表](/Functions/Function.html) 。

&emsp;&emsp;6 大模块包括：

>+ [指数运算](indexc.html) == gma.index
>+ [数学运算](math.html) == gma.math
>+ [系统交互](osf.html) == gma.osf
>+ [空间杂项](smc.html) == gma.smc
>+ [栅格处理](rasp.html) == gma.rasp
>+ [矢量处理](vesp.html) == gma.vesp

&emsp;&emsp;您可以通过以下形式一次引入 gma 的所有模块：

```python
 import gma
```
&emsp;&emsp;或引入其中一个或多个所需模块：

```python
from gma import index
from gma import math
from gma import osf
from gma import smc
from gma import rasp
from gma import vesp
```

&emsp;&emsp;如果您需要了解 gma 中默认的参数、定义和约定，请移步 [默认设置](/Functions/Default.html)。