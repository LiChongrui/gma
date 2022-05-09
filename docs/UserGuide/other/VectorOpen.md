---
title: Open:VectorOpen
date: 2022-03-09
sidebar: false
---

&emsp;　打开的 **矢量数据** 具有如下所列的 方法/属性：

## **Driver**

---

**功能：**【矢量驱动】。类属性，获取矢量数据驱动。

**返回：**`str`。

---

## **GetLayer**(*ID*)

---

**功能：**【打开图层】。打开某一图层。

**参数：** 

&emsp;ID：`int`。矢量图层的编号。从 0 开始。

**返回：**[Layer](Layer.html)。

---

## **GetOGRDataSource**()

---

**功能：**【获取 DataSource】。读取矢量数据为 ogr.DataSource。

**返回：**`ogr.DataSource`。

---

## **LayerCount**

---

**功能：**【图层数】。类属性，获取矢量数据的图层数量。

**返回：**`int`。

---

## **LayerNames**

---

**功能：**【图层名】。类属性，获取矢量数据每个图层的名称。

**返回：**`list`。

---



