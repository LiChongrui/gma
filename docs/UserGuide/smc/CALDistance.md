---
title: CALDistance
date: 2021-10-30
sidebar: false
---

## gma.smc.**CALDistance**(*Points, Projection = 'WGS84', Unit = 'meter'*)<Badge text="1.0.5 +"/>
---

**功能：** 【计算距离】。计算输入两点（或多点）之间的距离。

**参数：**

&emsp;Points：`list||tuple||array` 。需要计算距离的两点（或多点）的 X（纬度），Y（经度）坐标。如果有，也可包含 Z（高程）。可为嵌套列表或元组。至少有 2 个坐标点。

::: warning 注意

每两点之间最大的经度跨度为 180°；若超过 180°，则计算短距——反方向的距离！

:::

**可选参数：**

&emsp;Projection = `str`。输入坐标点的坐标系。默认为 WGS84（EPSG:4326）。

&emsp;Unit = `str`。计算距离结果的单位。默认为米（meter）。

::: tip 其他支持的单位

decimeter（分米），centimeter（厘米），millimeter（毫米），micron（微米），picometer（皮米），fermi（费米），kilometer（千米），inch（英寸），foot（英尺），yard（码），mile（英里），mil（密尔），point（pt 字体大小单位），survey foot（测量英尺），survey mile（测量英里），nautical mile（海里），angstrom（埃），astronomical unit（天文单位），light year（光年），parsec（秒差距）。

:::

**返回：**`float`。

---

**示例：**
```python
import gma
```
*计算两点之间的距离*
```python
Points = [(45.2, 130.1), (40.2, 131.5)]
gma.smc.CALDistance(Points)
```
> \>>> 567068.6613355379

*计算其他坐标系下两点的距离*

```python
Points = [(1528762.0778835732, 5089353.9231655225),(1482994.7191603119, 4968227.359572877)]
# 输入坐标点的坐标系为 EPSG:32650（WGS 84 / UTM zone 50N）
gma.smc.CALDistance(Points, Projection = 'EPSG:32650')
```
> \>>> 129484.73088463691

*获得其他距离单位的结果*
```python
# 以千米 kilometer 为单位
gma.smc.CALDistance(Points, Projection = 'EPSG:32650', Unit = 'kilometer')
```
> \>>> 129.48473088463692
