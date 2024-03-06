---
title: 【Layer】
sidebar: false
---

&emsp;　下载 [示例矢量](/io/China_Province_2022.7z)。

```python
from gma import io
LY = io.ReadVector('China_Province_2022.shp')
```

&emsp;　打开的 **矢量数据的图层** 具有如下所列的 方法/属性：

## **Boundary**

---

**功能：**【四至边界】。类属性，获取图层的左、右、下、上边界。

**返回：**`tuple`。

```python
LY.Boundary
```
> \>>> (73.50114210012788, 135.08851148002088, 3.837901789735838, 53.56090105044319)

---

## **FeatureCount**

---

**功能：**【要素数】。类属性，获取图层要素的数量。

**返回：**`int`。

```python
LY.FeatureCount
```
> \>>> 34

---

## **FieldsInfo**

---

**功能：**【字段信息】。类属性，获取属性表字段信息。

**返回：**`DataFrame`。

```python
LY.FieldsInfo
```
|    | Field Name   | Data Type   |   Precision |   Width |
|:---|:-------------|:------------|:------------|:--------|
|  0 | 省           | String      |           0 |     254 |
|  1 | 省级码       | Integer64   |           0 |      10 |
|  2 | 省类型       | String      |           0 |     254 |
|  3 | ENG_NAME     | String      |           0 |     254 |
|  4 | VAR_NAME     | String      |           0 |     254 |
|  5 | FIRST_GID    | Integer64   |           0 |      10 |
|  6 | FIRST_TYPE   | String      |           0 |     254 |
|  7 | year         | Integer64   |           0 |      10 |

---

## **GeomType**

---

**功能：**【几何类型】。类属性，获取图层的几何类型。

**返回：**`str`。

```python
LY.GeomType
```
> \>>> 'Polygon'

---

## **GetAttributeTable**()

---

**功能：**【获取属性表】。获取图层属性表。

**返回：**`DataFrame`。

```python
LY.GetAttributeTable()
```
|    | 省               |   省级码 | 省类型     | ENG_NAME     | VAR_NAME        |   FIRST_GID | FIRST_TYPE        |   year |
|:---|:-----------------|:---------|:-----------|:-------------|:----------------|:------------|:------------------|:-------|
|  0 | 北京市           |   110000 | 直辖市     | Beijing      | Běi Jīng        |      110000 | Municipality      |   2022 |
|  1 | 天津市           |   120000 | 直辖市     | Tianjin      | Tiān Jīn        |      120000 | Municipality      |   2022 |
|  2 | 河北省           |   130000 | 省         | Hebei        | Hé Běi          |      130000 | Province          |   2022 |
|  3 | 山西省           |   140000 | 省         | Shanxi       | Shān Xī         |      140000 | Province          |   2022 |
|  4 | 内蒙古自治区     |   150000 | 自治区     | Neimenggu    | Nèi Měng Gǔ     |      150000 | Autonomous Region |   2022 |
|  5 | 辽宁省           |   210000 | 省         | Liaoning     | Liáo Níng       |      210000 | Province          |   2022 |
|  ... | ...           |   ... | ...         | ...     | ...     |     ... | ...         |   ...|

---

## **GetFeature(FID)**

---

**功能：**【获取要素】。获取某一要素。

**参数：** 

&emsp;FID：`int`。要素编号。从 0 开始。

**返回：**[Feature](Feature.html)。

```python
LY.GetFeature(0)
```
> \>>> <gma.algorithm.core.dataio.Feature at 0x......>

---

## **Metadata**

---

**功能：**【元数据】。类属性，获取图层的元数据。

**返回：**`dict`。

```python
LY.Metadata
```
> \>>> {'DBF_DATE_LAST_UPDATE': '2022-08-28'}

---

## **Projection**

---

**功能：**【坐标系/投影】。获取图层坐标系/投影。

**返回：**`str`。

```python
LY.Projection
```
> \>>> 'GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563, AUTHORITY["EPSG","7030"]], AUTHORITY["EPSG","6326"]], PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]], UNIT["degree",0.0174532925199433, AUTHORITY["EPSG","9122"]], AXIS["Latitude",NORTH], AXIS["Longitude",EAST], AUTHORITY["EPSG","4326"]]'

---

