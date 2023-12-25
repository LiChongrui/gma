---
title: NDWI
date: 2021-10-31
sidebar: false
---

## gma.rsvi.**NDWI**(*Nir, Green*)

---

**功能：**【NDWI】。计算归一化水指数。

**参数：**

&emsp;Nir：`float||array` 。近红外波段数据。

&emsp;Green：`float||array` 。绿光波段数据。

**返回：** `float||array`。

---

**示例：**
```python
from gma import rsvi
```
*单个值（0 维）*
```python
Green = 0.1598
Nir = 0.1052
rsvi.NDWI(Green, Nir)
```
> \>>> 0.20603773584905657

*序列（1 维）*

```python
Green = [0.13174279, 0.11682527, 0.12699335, 0.10319582, 0.13458107]
Nir = [0.49998039, 0.43281425, 0.4370636 , 0.43339039, 0.42903499]
rsvi.NDWI(Green, Nir)
```
> \>>> array([-0.58290975, -0.57490222, -0.54971444, -0.61536164, -0.52243706])

*更多维度*
```python
Green = [[0.19976277, 0.15523541, 0.1801273 , 0.19935374],
        [0.18211054, 0.17035266, 0.15505663, 0.1900826 ],
        [0.1850646 , 0.1782985 , 0.16156239, 0.16757756]]
Nir = [[0.43547845, 0.4525367 , 0.48956414, 0.46418583],
        [0.43747245, 0.46524534, 0.42735143, 0.46404673],
        [0.44102187, 0.44652723, 0.44031739, 0.42079154]]
rsvi.NDWI(Green, Nir)
```
> \>>> array([[-0.37106484, -0.48916573, -0.46205883, -0.39912027],<br>
> 　　　　　[-0.41215126, -0.46396099, -0.46753268, -0.41882257],<br>
> 　　　　　[-0.40882096, -0.42928567, -0.46314066, -0.43036587]])

*基于栅格（哨兵 2 L2A/B 数据）*
```python
from gma import io
# 读取栅格文件至数据集
GreenSet = io.ReadRater('SENT_LY_B3_20220305.tif')
NirSet = io.ReadRater('SENT_LY_B8_20220305.tif')

# 提取数据集的仿射变换和坐标系
Geot = GreenSet.GeoTransform
Proj = GreenSet.Projection

# 依据反射率数据进行单位换算
Green = GreenSet.ToArray() * 1e-4
Nir = NirSet.ToArray() * 1e-4
NDWI = rsvi.NDWI(Green, Nir)

# 将结果保存为 GTiff 格式
io.SaveArrayAsRaster(NDWI, 
                     'SENT_LY_NDWI_20220305.tif', 
                     Projection = Proj, 
                     Transform = Geot,
                     DataType = 'Float32')
```
> NDWI 计算结果：

![](/rsvi/NDWI.webp)
