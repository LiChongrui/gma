---
title: CALArea
date: 2022-10-20
sidebar: false
---

## gma.smc.Query.**CALArea**(*Points, Projection = 'WGS84', Unit = 'square meter'*)<Badge text="1.1.0 +"/>
---

**功能：** 【计算面积】。计算输入多点组成多边形的面积。

**参数：**

&emsp;Points：`list||tuple||array` 。需要计算面积多边形的顶点的 X（经度），Y（纬度）坐标。

::: tip 示例

Points = [(130.1, 45.2), (131.5, 40.2), (131.5, 45.2)]

:::

**可选参数：**

&emsp;Projection = `str`。输入坐标点的坐标系。默认为 WGS84（EPSG:4326）。

&emsp;Unit = `str`。计算距离结果的单位。默认为平方米（square meter）。

::: tip 其他支持的单位

square meter（平方米），square millimeter（平方毫米），square centimeter（平方厘米），square decimeter（平方分米），square kilometer（平方千米），hectare（公顷），acre（英亩），mu（亩）。

:::

**返回：**`float`。

---

**示例：**
```python
from gma import smc
```
*计算三个顶点的多边形面积*

```python
Points = [(130.1, 45.2), (131.5, 40.2), (131.5, 45.2)]
smc.Query.CALArea(Points)
```
> \>>> 31761406920.13275

*计算其他坐标系下三个点组成多边形的面积*

```python
Points = [(1528762.07788357, 5089353.92316552), 
          (1736214.64875059, 4552113.0446395), 
          (1638653.77538803, 5108509.49658331)]
# 输入坐标点的坐标系为 EPSG:32650（WGS 84 / UTM zone 50N）
smc.Query.CALArea(Points, Projection = 'EPSG:32650')
```
> \>>> 31506092530.98242

*获得其他面积单位的结果*
```python
# 以平方千米 square kilometer 为单位
smc.Query.CALArea(Points, Projection = 'EPSG:32650', Unit = 'square kilometer')
```
> \>>> 31506.092530982423
