---
title: 统计总览
date: 2021-10-30
---

**&emsp;&emsp;使用指南** 为 **gma** 内所有模块（7个功能模块，1个配置模块以及一些其他函数）相关函数的详细功能、参数设置和引用方法说明。

::: tip 提示

* 如果您想快速了解 gma 中每个模块所有函数的整体情况，请移步 **[函数列表](Function.html)** 。

* 如果您需要了解 gma 中规定的默认参数和数据类型，请移步 **[默认设置](/Explore/Default.html)**。

:::

## 功能统计

&emsp;&emsp;截止 <Badge text="1.0.7" vertical='middle'/>  版本，各个模块的 **函数/方法数量统计** 如下表：

|  中文名  | 模块名 | 函数 |  类  | 方法 | 属性 | 子类 | 子类方法 | 子类属性 | 合计 |
| :------- | :----: | :--: | :--: | :----: | :----: | :--: | :------: | :------: | :--: |
| 指数运算 | index  |  6   |      |        |        |      |          |          |  6   |
| 数学运算 |  math  |  2   |  2   |   10   |        |      |          |          |  14  |
| 系统交互 |  osf   |  5   |  1   |   3    |        |      |          |          |  9   |
| 空间杂项 |  smc   |  2   |      |        |        |      |          |          |  2   |
| 栅格处理 |  rasp  |  16  |  1   |   1    |        |      |          |          |  18  |
| 栅格分析 |  raa   |      |  1   |   6    |        |      |          |          |  7   |
| 矢量处理 |  vesp  |  13  |      |        |        |      |          |          |  13  |
| 高级配置 | config |  2   |  4   |        |   30   |      |          |          |  36  |
| 其他函数 |   -    |  1   |      |   7    |   13   |  1   |    1     |    5     |  28  |
|   合计   |   9    |  47  |  9   |   27   |   43   |  1   |    1     |    5     | 133  |

::: warning 注意

自 <Badge text="1.0.7" vertical='middle'/>  版本开始，gma 下各个函数生成 GTiff 文件时 **不在默认** 生成 .ovr 金字塔。

:::

## 引入模块

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
from gma import raa
from gma import vesp
from gma import config
```

::: tip 提示

1.0.5 版本后，如果 import 出现异常，可参考 **[错误解决](/Install.html#错误解决)** 中提供的方案进行处理。

:::
