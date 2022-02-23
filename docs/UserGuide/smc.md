---
title: 空间杂项
date: 2021-10-30
---

**&emsp;&emsp;空间杂项** 为 **gma.smc** 内所有其他空间计算相关函数的详细功能、参数设置和引用方法说明，如果您想了解 gma 所有函数的整体情况，请移步 [函数列表](/Functions/Function.html) 。

## CALDistance<Badge text="1.0.5 +"/>
::: theorem

**引用：**  gma.smc.CALDistance(Points, Projection = 'WGS84', Unit = 'meter')

**功能：** 【计算距离】。计算输入两点（或多点）之间的距离。

**参数：**

&emsp;Points：`list||tuple||array` 。需要计算距离的两点（或多点）的 X（纬度），Y（经度）坐标。如果有，也可包含 Z（高程）。可为嵌套列表或元组。至少有 2 个坐标点。

<Boxx type='tips' title='示例' content='Points = [(45.2, 130.1), (40.2, 131.5)]'/>

<Boxx type='warning' title='注意' content='每两点之间最大的经度跨度为 180°；若超过 180°，则计算短距——反方向的距离！'/>

**可选参数：**

&emsp;Projection = `str`。输入坐标点的坐标系。默认为 WGS84（EPSG:4326）。

&emsp;Unit = `str`。计算距离结果的单位。默认为米（meter）。

<Boxx type='tips' title='其他支持的单位' content='decimeter（分米），centimeter（厘米），millimeter（毫米），micron（微米），picometer（皮米），fermi（费米），kilometer（千米），inch（英寸），foot（英尺），yard（码），mile（英里），mil（密尔），point（pt 字体大小单位），survey foot（测量英尺），survey mile（测量英里），nautical mile（海里），angstrom（埃），astronomical unit（天文单位），light year（光年），parsec（秒差距）。' />

**返回：**`float`。

:::

## TRANCoordinate<Badge text="1.0.5 +"/>
::: theorem

**引用：**  gma.smc.TRANCoordinate(Points, InProjection = 'WGS84', OutProjection = 'EPSG:4490')

**功能：** 【坐标转换】。将输入点的坐标转换为目标坐标系的坐标。

**参数：**

&emsp;Points：`list||tuple||array` 。需要计算距离的两点（或多点）的 X（纬度），Y（经度）坐标。如果有，也可包含 Z（高程）。可为嵌套列表或元组。

<Boxx type='tips' title='示例' content='Points = [(45.2, 130.1), (40.2, 131.5)]'/>

**可选参数：**

&emsp;InProjection = `str`。输入坐标点的坐标系。默认为 WGS84（EPSG:4326）。

&emsp;OutProjection = `str`。输出坐标点的坐标系。默认为 China Geodetic Coordinate System 2000（EPSG:4490）。

**返回：**`list`。

:::