---
title: GetRasterFormat
date: 2022-04-17
sidebar: false
---

## gma.config.**GetRasterFormat**(*Format*)

---

**功能：**【类】。【获取栅格格式】，实现针对某一栅格驱动详细信息的获取。

**初始化：** 

&emsp;Format：`str`。栅格驱动格式名称。

::: warning 注意

类内 属性/方法 引用前请先初始化 `GetRasterFormat` 类！

::: 

---

## 类内属性/方法

### **ColorTableDataType**

---

**功能：**【色彩映射表数据类型】。类属性，色彩映射表支持的数据类型。

**返回：**`dict`。

---

###  **CompressMode**

---

**功能：**【压缩方式】。类属性，支持的压缩方式。

**返回：**`list`。

---

### CreationDataType

---

**功能：**【创建数据类型】。类属性，支持创建的数据类型。

**返回：**`dict`。

---

### Details

---

**功能：**【详细信息】。类属性，全部支持内容的详细信息。

**返回：**`dict`。

---

### Extension

---

**功能：**【扩展名】。类属性，驱动格式的扩展名。

**返回：**`str`。

---

### GeoReferencing

---

**功能：**【地理参考支持】。类属性，是否支持地理参考。

**返回：**`str`。

---

### LongName

---

**功能：**【长名称】。类属性，驱动格式的长名称。

**返回：**`str`。

---

### Multiband

---

**功能：**【多波段支持】。类属性，是否支持多波段或支持的波段数。

**返回：**`str||list`。

---

### Update

---

**功能：**【更新支持】。类属性，是否支持更新（修改）。

**返回：**`str||list`。

---
