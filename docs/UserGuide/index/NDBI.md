---
title: NDBI
date: 2021-10-31
sidebar: false
---

## gma.index.**NDBI**(*Nir, Swir*)

---

**功能：**【NDBI】。计算归一化建筑指数。

**参数：**

&emsp;Nir：`float||array` 。近红外波段数据。

&emsp;Swir：`float||array` 。短波红光波段数据。

**返回：**`float||array`。

---

**示例：**
```python
import gma
```
*单个值（0 维）*
```python
Nir = 0.1052
Swir = 0.1598
gma.index.NDBI(Nir, Swir)
```
> \>>> 0.20603773584905657

*序列（1 维）*

```python
Nir = [0.49998039, 0.43281425, 0.4370636 , 0.43339039, 0.42903499]
Swir = [0.57939615, 0.5364073 , 0.56272019, 0.56820692, 0.50563094]
gma.index.NDBI(Nir, Swir)
```
> \>>> array([0.07357558, 0.10688273, 0.12568376, 0.13460153, 0.08195008])

*更多维度*
```python
Nir = [[0.43547845, 0.4525367 , 0.48956414, 0.46418583],
        [0.43747245, 0.46524534, 0.42735143, 0.46404673],
        [0.44102187, 0.44652723, 0.44031739, 0.42079154]]
Swir = [[0.52987932, 0.53247515, 0.59122501, 0.50296513],
       [0.51291895, 0.55736167, 0.50249297, 0.50782207],
       [0.5959599 , 0.52399249, 0.59509758, 0.54306701]]
gma.index.NDBI(Nir, Swir)
```
> \>>> array([[0.09778848, 0.08115481, 0.0940617 , 0.04009643],<br>
> 　　　　　[0.07938466, 0.09007989, 0.08081088, 0.04504244],<br>
> 　　　　　[0.14941249, 0.07981833, 0.14948614, 0.12686039]])

*基于栅格（哨兵 2 L2A/B 数据）*
```python
# 读取栅格文件至数据集
NirSet = gma.Open('SENT_LY_B8_20220305.tif')
SwirSet = gma.Open('SENT_LY_B11_20220305.tif')

# 提取数据集的仿射变换和坐标系
Geot = NirSet.GeoTransform
Proj = NirSet.Projection

# 依据反射率数据进行单位换算
Nir = NirSet.ToArray() * 1e-4
Swir = SwirSet.ToArray() * 1e-4
NDBI = gma.index.NDBI(Nir, Swir)

# 将结果保存为 GTiff 格式
gma.rasp.WriteRaster(r'..\0.1 预处理\SENT_LY_NDBI_20220305.tif', 
                     NDBI, 
                     Projection = Proj, 
                     Transform = Geot,
                     DataType = 'Float32')
```
> NDBI 计算结果：

![](/index/NDBI.webp)