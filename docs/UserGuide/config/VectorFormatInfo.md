---
title: VectorFormatInfo
date: 2022-04-17
sidebar: false
---

## gma.config.**VectorFormatInfo**()

---

**功能：**【矢量驱动格式信息】。获取所有矢量驱动格式分类的详细信息。

**示例：**
```python
import gma
VFInfo = gma.config.VectorFormatInfo()
```
---

## 类内属性/方法

### CopyableFormats

---

**功能：**【复制支持】。类属性，支持复制的驱动格式。

**返回：**`set`。

```python
VFInfo.CopyableFormats
```
> \>>> {'GPKG', 'NGW', 'PDF', 'netCDF'}

---

### CreatableFormats

---

**功能：**【创建支持】。类属性，支持创建的驱动格式。

**返回：**`set`。

```python
VFInfo.CreatableFormats
```
> \>>> {'AmigoCloud', 'CARTO', 'CSV', 'DGN', 'DGNv8', 'DXF', 'ESRI Shapefile', ...}

---

### MultiLayersFormats

---

**功能：**【多图层支持】。类属性，支持多图层的驱动格式。

**返回：**`set`。

```python
VFInfo.MultiLayersFormats
```
> \>>> {'AVCBIN', 'CAD', 'DGN', 'DXF', 'EDIGEO', 'GML', 'GPKG', ...}

---

### ReadableFormats

---

**功能：**【读取支持】。类属性，支持读取的驱动格式。

**返回：**`set`。

```python
VFInfo.ReadableFormats
```
> \>>> {'AVCBIN', 'AVCE00', 'AmigoCloud', 'CAD', 'CARTO', 'CSV', ...}

---

### TransformableFormats

---

**功能：**【转换支持】。类属性，支持转换的驱动格式。

**返回：**`set`。

```python
VFInfo.TransformableFormats
```
> \>>> {'AmigoCloud', 'CARTO', 'CSV', 'DGN', 'DGNv8', 'DXF', 'ESRI Shapefile', ...}

---

### UpdatableFormats

---

**功能：**【更新支持】。类属性，支持更新的驱动格式。

**返回：**`set`。

```python
VFInfo.UpdatableFormats
```
> \>>> {'CSV', 'DGN', 'DXF', 'ESRI Shapefile', 'GMT', 'GPKG', 'GeoJSON', ...}

---
