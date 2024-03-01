---
title: 简易说明
date: 2023-08-20
---

**&emsp;&emsp;本页** 为 **gma** 内所有模块相关函数整体统计说明。

## 功能统计

&emsp;&emsp;截至 <Badge text="2.0.0" vertical='middle'/>  版本，各个模块的 **函数/方法数量统计** 如下表：

|  模块名  | 中文名 | 对应主要功能 |  
| :------- | :----: | :--: |
|io|输入输出|栅格/矢量数据输入输出模块|
|crs|坐标系统|坐标参考系统|
|map|地图工具|地理空间制图|
|math|数学运算|数学运算模块|
|climet|气象气候|气象气候模块|
|rsvi|指数运算|遥感指数计算|
|rasp|栅格处理|栅格处理工具|
|vesp|矢量处理|矢量处理工具|
|gft|驱动格式|（地理数据格式）|
|smc|空间杂项|空间计算工具|
|osf|系统交互|其他系统工具|

## 引入模块

&emsp;&emsp;您可以通过以下形式一次引入 gma 的所有模块：

```python
import gma
```

&emsp;&emsp;或引入其中一个或多个所需模块 **（推荐）**：

```python
from gma import climet
from gma import rsvi
from gma import math
from gma import osf
from gma import smc
from gma import rasp
from gma import vesp
from gma import gft
from gma import io

# 空间绘图专用
from gma.map import plot, inres
```


