---
title: NDWI
date: 2021-10-31
sidebar: false
---

## gma.index.**NDWI**(*Nir, Green*)

---

**功能：**【NDWI】。计算归一化水指数。

**参数：**

&emsp;Nir：`float||array` 。近红外波段数据。

&emsp;Green：`float||array` 。绿光波段数据。

**返回：** `float||array`。

---

**示例：**
```python
import gma
```
*单个值（0 维）*
```python
Green = 0.1598
Nir = 0.1052
gma.index.NDWI(Green, Nir)
```
> \>>> 0.20603773584905657

*序列（1 维）*

```python
Green = [0.13174279, 0.11682527, 0.12699335, 0.10319582, 0.13458107]
Nir = [0.49998039, 0.43281425, 0.4370636 , 0.43339039, 0.42903499]
gma.index.NDWI(Green, Nir)
```
> \>>> [-0.58290975, -0.57490222, -0.54971444, -0.61536164, -0.52243706]

*更多维度*
```python
Green = [[0.19976277, 0.15523541, 0.1801273 , 0.19935374],
        [0.18211054, 0.17035266, 0.15505663, 0.1900826 ],
        [0.1850646 , 0.1782985 , 0.16156239, 0.16757756]]
Nir = [[0.43547845, 0.4525367 , 0.48956414, 0.46418583],
        [0.43747245, 0.46524534, 0.42735143, 0.46404673],
        [0.44102187, 0.44652723, 0.44031739, 0.42079154]]
gma.index.NDWI(Green, Nir)
```
> \>>> [[-0.37106484, -0.48916573, -0.46205883, -0.39912027],<br>
> 　　 [-0.41215126, -0.46396099, -0.46753268, -0.41882257],<br>
> 　　 [-0.40882096, -0.42928567, -0.46314066, -0.43036587]]

*基于栅格（哨兵 2 L2A/B 数据）*
```python
# 读取栅格文件至数据集
GreenSet = gma.Open('SENT_LY_B3_20220305.tif')
NirSet = gma.Open('SENT_LY_B8_20220305.tif')

# 提取数据集的仿射变换和坐标系
Geot = GreenSet.GeoTransform
Proj = GreenSet.Projection

# 依据反射率数据进行单位换算
Green = GreenSet.ToArray() * 1e-4
Nir = NirSet.ToArray() * 1e-4
NDWI = gma.index.NDWI(Green, Nir)

# 将结果保存为 GTiff 格式
gma.rasp.WriteRaster(r'..\0.1 预处理\SENT_LY_NDWI_20220305.tif', 
                     NDWI, 
                     Projection = Proj, 
                     Transform = Geot,
                     DataType = 'Float32')
```
> NDWI 计算结果：
```python
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
# 配置参数
PAR = {'font.sans-serif': 'Times New Roman',
       'axes.unicode_minus': False,
      }
plt.rcParams.update(PAR)

# 获取色带
CMap = plt.get_cmap('RdYlGn_r')

plt.figure(figsize = (8, 5), dpi = 200)
ax = plt.subplot()
ax.set_xticks([])
ax.set_yticks([])

# 制图
im = ax.imshow(NDWI, cmap = CMap)
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size = "5%", pad = 0.2)
plt.colorbar(im, cax = cax)
plt.show()
```
![](/index/NDWI.webp)
