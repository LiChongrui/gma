---
title: NDVI
date: 2021-10-31
sidebar: false
---

## gma.index.**NDVI**(*Nir, Red*)

---

**功能：**【NDVI】。计算归一化植被指数。

**参数：**

&emsp;Nir：`float||array` 。近红外波段数据。

&emsp;Red：`float||array`。 红光波段数据。

**返回：**`float||array`。

---

**示例：**
```python
import gma
```
*单个值（0 维）*
```python
Red = 0.1604
Nir = 0.4540
gma.index.NDVI(Red, Nir)
```
> \>>> 0.4778645833333333

*序列（1 维）*

```python
Red = [0.17049912, 0.18568421, 0.15712575, 0.17212352, 0.18122375]
Nir = [0.49998039, 0.43281425, 0.4370636 , 0.43339039, 0.42903499]
gma.index.NDVI(Red, Nir)
```
> \>>> [0.49141139, 0.39956452, 0.47112566, 0.43147955, 0.40607569]

*更多维度*
```python
Red = [[0.16600456, 0.18746094, 0.16713885, 0.1706692 ],
       [0.19569191, 0.18616073, 0.18538985, 0.18072001],
       [0.17289586, 0.17678199, 0.17017325, 0.1501089 ]]
Nir = [[0.43547845, 0.4525367 , 0.48956414, 0.46418583],
        [0.43747245, 0.46524534, 0.42735143, 0.46404673],
        [0.44102187, 0.44652723, 0.44031739, 0.42079154]]
gma.index.NDVI(Red, Nir)
```
> \>>> [[0.4480158 , 0.4141824 , 0.49097582, 0.46233646],<br>
> 　　 [0.38186063, 0.42843416, 0.39488376, 0.43942515],<br>
> 　　 [0.43674583, 0.43276312, 0.44250333, 0.47413283]]

*基于栅格（哨兵 2 L2A/B 数据）*
```python
# 读取栅格文件至数据集
RedSet = gma.Open('SENT_LY_B4_20220305.tif')
NirSet = gma.Open('SENT_LY_B8_20220305.tif')

# 提取数据集的仿射变换和坐标系
Geot = RedSet.GeoTransform
Proj = RedSet.Projection

# 依据反射率数据进行单位换算
Red = RedSet.ToArray() * 1e-4
Nir = NirSet.ToArray() * 1e-4
NDVI = gma.index.NDVI(Red, Nir)

# 将结果保存为 GTiff 格式
gma.rasp.WriteRaster(r'..\0.1 预处理\SENT_LY_NDVI_20220305.tif', 
                     NDVI, 
                     Projection = Proj, 
                     Transform = Geot,
                     DataType = 'Float32')
```
> NDVI 计算结果：
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
im = ax.imshow(NDVI, cmap = CMap)
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size = "5%", pad = 0.2)
plt.colorbar(im, cax = cax)
plt.show()
```

![](/index/NDVI.webp)
