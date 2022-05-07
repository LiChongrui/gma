---
title: EVI
date: 2021-10-31
sidebar: false
---

## gma.index.**EVI**(*Nir, Red, Blue*)

---

**功能：** 【EVI】。计算增强植被指数。

**参数：**

&emsp;Nir：`float||array` 。近红外波段数据。

&emsp;Red：`float||array` 。红光波段数据。

&emsp;Blue：`float||array`。 蓝光波段数据。

**返回：**`float||array`。

---
**示例：**
```python
import gma
```
*单个值（0 维）*
```python
Blue = 0.1302
Red = 0.1604
Nir = 0.4540
gma.index.EVI(Blue, Red, Nir)
```
> \>>> 0.5097576220570874

*序列（1 维）*

```python
Blue =[0.1572414, 0.17303503, 0.17937252, 0.18422147, 0.17526136]
Red = [0.17049912, 0.18568421, 0.15712575, 0.17212352, 0.18122375]
Nir = [0.49998039, 0.43281425, 0.4370636 , 0.43339039, 0.42903499]
gma.index.EVI(Blue, Red, Nir)
```
> \>>> [0.61302736, 0.49459372, 0.67648937, 0.60229133, 0.51544986]

*更多维度*
```python
Blue = [[0.18552341, 0.16901705, 0.18855329, 0.15960997],
        [0.17417957, 0.19806264, 0.16436113, 0.15814385],
        [0.17763388, 0.18464873, 0.15400542, 0.17487925]]
Red = [[0.16600456, 0.18746094, 0.16713885, 0.1706692 ],
       [0.19569191, 0.18616073, 0.18538985, 0.18072001],
       [0.17289586, 0.17678199, 0.17017325, 0.1501089 ]]
Nir = [[0.43547845, 0.4525367 , 0.48956414, 0.46418583],
        [0.43747245, 0.46524534, 0.42735143, 0.46404673],
        [0.44102187, 0.44652723, 0.44031739, 0.42079154]]
gma.index.EVI(Blue, Red, Nir)
```
> \>>> [[0.6477238 , 0.50599551, 0.74756786, 0.56833448],<br>
> 　　 [0.46308277, 0.63616862, 0.46282498, 0.51994648],<br>
> 　　 [0.58484418, 0.60084722, 0.51699606, 0.67010568]]

*基于栅格（哨兵 2 L2A/B 数据）*
```python
# 读取栅格文件至数据集
BlueSet = gma.Open('SENT_LY_B2_20220305.tif')
RedSet = gma.Open('SENT_LY_B4_20220305.tif')
NirSet = gma.Open('SENT_LY_B8_20220305.tif')

# 提取数据集的仿射变换和坐标系
Geot = BlueSet.GeoTransform
Proj = BlueSet.Projection

# 依据反射率数据进行单位换算
Blue = BlueSet.ToArray() * 1e-4
Red = RedSet.ToArray() * 1e-4
Nir = NirSet.ToArray() * 1e-4
EVI = gma.index.EVI(Blue, Red, Nir)

# 将结果保存为 GTiff 格式
gma.rasp.WriteRaster(r'..\0.1 预处理\SENT_LY_EVI_20220305.tif', 
                     EVI, 
                     Projection = Proj, 
                     Transform = Geot,
                     DataType = 'Float32')
```
> EVI 计算结果制图：
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
im = ax.imshow(EVI, cmap = CMap)
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size = "5%", pad = 0.2)
plt.colorbar(im, cax = cax)
plt.show()
```
![](/index/EVI.webp)

