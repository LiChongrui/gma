---
title: GetFeature:Feature
date: 2022-11-01
sidebar: false
---

&emsp;　下载 [示例矢量](/Open/China_Province_2022.7z)。

```python
import gma
VO = gma.Open('China_Province_2022.shp')
LY = VO.GetLayer(0)
FU = LY.GetFeature(0)
```

&emsp;　打开的 **图层要素** 具有如下所列的 方法/属性：

## **Area**

---

**功能：**【面积】。类属性，获取要素（当前坐标系单位）的面积。

**返回：**`float`。

```python
FU.Area
```
> \>>> 1.7348120150624204

---

## **ExportGeom**(*Type = 'IsoWkt'*)<Badge text="1.1.1 +"/>

---

**功能：**【导出几何形状】。类方法，导出当前要素几何。

**可选参数：**

 &emsp;SUBID = `str`。导出类型。默认为 'IsoWkt'。

::: tip 所有支持的类型
'GML', 'IsoWkb', 'IsoWkt', 'Json', 'KML', 'Wkb', 'Wkt'
:::

**返回：**`str`。

```python
FU.ExportGeom()
```
> \>>> POLYGON ((117.383350145193 40.2264723149455, ...))

---

## **Fields**

---

**功能：**【字段】。类属性，获取要素的属性表字段。

**返回：**`dict`。

```python
FU.Fields
```
> \>>> {'省': '北京市',
 '省级码': 110000,
 '省类型': '直辖市',
 'ENG_NAME': 'Beijing',
 'VAR_NAME': 'Běi Jīng',
 'FIRST_GID': 110000,
 'FIRST_TYPE': 'Municipality',
 'year': 2022}

---

## **GeometryCount**

---

**功能：**【几何数量】。类属性，获取构成要素几何的数量。

**返回：**`int`。

```python
FU.GeometryCount
```
> \>>> 1

---

## **Length**

---

**功能：**【长度】。类属性，获取要素（当前坐标系单位）的长度。

**返回：**`float`。

```python
FU.Length
```
> \>>> 10.115307591455338

---

## **Points**

---

**功能：**【折点坐标】。类属性，获取组成要素所有折点的坐标。

**返回：**`list`。

```python
FU.Points
```
> \>>> [[(117.38335014519316, 40.226472314945454),
 (117.38556534536451, 40.22405173030319),
 (117.38697686459068, 40.2201720954659),
 (117.38695820995349, 40.220152554996446),
 (117.38694822028424, 40.22014282972788),
 (117.38694021991523, 40.2201355650044),
 ......],
 ......]

---



