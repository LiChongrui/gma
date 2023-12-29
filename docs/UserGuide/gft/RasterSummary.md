---
title: RasterSummary
date: 2023-12-29
sidebar: true
---

## gma.gft.**RasterSummary**()

---

**功能：**【栅格驱动格式信息】。获取所有栅格驱动格式分类的详细信息。

**示例：**
```python
from gma import gft

RFInfo = gft.RasterSummary()
```

---

## 类内属性/方法

### AddableColorTableFormats

---

**功能：**【色彩映射表支持】。类属性，支持色彩映射表的驱动格式。

**返回：**`set`。

```python
RFInfo.AddableColorTableFormats
```
> \>>> {'AAIGrid', 'ACE2', 'ADRG', 'AIG', 'AIRSAR', 'ARG', 'BAG', ...}

---

### CompressibleFormats

---

**功能：**【压缩支持】。类属性，支持压缩的驱动格式。

**返回：**`set`。

```python
RFInfo.CompressibleFormats
```
> \>>> {'AAIGrid', 'ACE2', 'ADRG', 'AIG', 'AIRSAR', 'ARG', 'BAG', ...} 

---

### CopyableFormats

---

**功能：**【复制支持】。类属性，支持复制的驱动格式。

**返回：**`set`。

```python
RFInfo.CopyableFormats
```
> \>>> {'AAIGrid', 'ADRG', 'ARG', 'BAG', 'BLX', 'BMP', 'BT', 'BYN', ...}

---

### CreatableFormats

---

**功能：**【创建支持】。类属性，支持创建的驱动格式。

**返回：**`set`。

```python
RFInfo.CreatableFormats
```
> \>>> {'ADRG', 'ARG', 'BAG', 'BMP', 'BT', 'BYN', 'CTable2', 'EHdr', ...}

---

### MultibandFormats

---

**功能：**【多波段支持】。类属性，支持多波段的驱动格式。

**返回：**`set`。

```python
RFInfo.MultibandFormats
```
> \>>> {'CALS', 'COG', 'EHdr', 'ELAS', 'ENVI', 'ERS', 'EXR', 'FIT', ...}

---

### ReadableFormats

---

**功能：**【读取支持】。类属性，支持读取的驱动格式。

**返回：**`set`。

```python
RFInfo.ReadableFormats
```
> \>>> {'AAIGrid', 'ACE2', 'ADRG', 'AIG', 'AIRSAR', 'ARG', ...}

---

### TransformableFormats

---

**功能：**【转换支持】。类属性，支持转换的驱动格式。

**返回：**`set`。

```python
RFInfo.TransformableFormats
```
> \>>> {'AAIGrid', 'ADRG', 'ARG', 'BAG', 'BLX', 'BMP', ...}

---

### UpdatableFormats

---

**功能：**【更新支持】。类属性，支持更新的驱动格式。

**返回：**`set`。

```python
RFInfo.UpdatableFormats
```
> \>>> {'AAIGrid', 'CALS', 'COG', 'ENVI', 'GS7BG', 'GSAG', 'GSBG', 'GTiff', ...}

---

