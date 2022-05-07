---
title: TVDI
date: 2021-10-31
sidebar: false
---

## gma.index.**TVDI**(*VI, LST, ValidVIRange = [0.2, 0.8], ValidLSTRange = [200, 350], Delta = 0.01, VINoData = None, LSTNoData = None, OutNoData = -1*) <Badge text="1.0.2 +"/>

---

**功能：**【TVDI】。计算温度植被干旱指数。

**参数：**

&emsp;VI：`array` 。 植被指数。

&emsp;LST：`array` 。 陆表温度（K）。

**可选参数：**

&emsp; ValidVIRange = `list` 。参与干湿边拟合植被指数的有效值范围，默认 0.2 ~ 0.8。

&emsp; ValidLSTRange = `list` 。参与干湿边拟合陆表温度的有效值范围，默认 200 ~ 350（K）。

&emsp; Delta = `float` 。干湿边拟合过程中植被指数采样的样本间距。默认为 0.01。

&emsp; VINoData  = `float` 。植被指数数据中的无效值。默认不设置（None）。

&emsp; LSTNoData = `float` 。陆表温度数据中的无效值。默认不设置（None）。

&emsp; OutNoData = `float` 。TVDI结果中的无效值。默认值为 -1。

::: warning 注意

VINoData， LSTNoData 的区域在输出栅格中都将被改为 OutNoData。

:::

**返回：** TVDI（`array`），参与拟合的VI（`array`），湿边LST（`array`）， 干边LST（`array`），湿边方程[系数，常数]（`list`），干边方程[系数，常数]（`list`）。

---

**示例：**
```python
import gma
```

*基于数组（1 维或多维）*

```python
NDVI = [0.5251, 0.5092, 0.4618, 0.4304, 0.4494, 0.4544, 0.4982, 0.6308, 0.5271, 0.4489]
LST = [302.72, 302.98, 303.64, 304.68, 303.7 , 302.94, 302.78, 300.64, 301.98, 302.12]
gma.index.TVDI(NDVI, LST)
```
> \>>> (array([ 1.93649901,  1.79681104,  1.2003987 ,  2.40119038,  0.79481429,<br>
> 　　　　　　-1.04221242,  0.37934697, -2.2399279 , -1.1514285 , -3.38829638]),<br>
> 　　 array([0.435, 0.445, 0.455, 0.465, 0.495, 0.505, 0.525, 0.635]),<br>
> 　　 array([304.68, 303.7 , 302.94, 303.64, 302.78, 302.98, 302.72, 300.64]),<br>
> 　　 array([304.68, 302.12, 302.94, 303.64, 302.78, 302.98, 301.98, 300.64]),<br>
> 　　  [-16.835616438356006, 311.3436301369862],<br>
 > 　　 [-14.890410958904331, 310.0907534246576])

::: danger 警告

计算 TVDI 时值过少会引起拟合结果较差或异常！要保证 TVDI 的结果质量需保证足够数量的有效数据！

:::


*基于栅格（MODIS VI/LST）*
```python
# 读取栅格文件至数据集
NDVISet = gma.Open("MOD13Q1_LY_NDVI_20220407.tif")
LSTSet = gma.Open("MOD11A2_LY_LST_20220407.tif")

# 提取数据集的仿射变换和坐标系
Proj = NDVISet.Projection
Geot = NDVISet.GeoTransform
# 记录不参与拟合和计算的 VI 值和 LST 值（ ValidVIRange，ValidLSTRange 范围外的数据不参与拟合）
VINoData = NDVISet.NoData
LSTNoData = LSTSet.NoData

# 依据数据单位进行单位换算
NDVI = NDVISet.ToArray() * 1e-4 
LST = LSTSet.ToArray() * 0.02

TVDI = gma.index.TVDI(NDVI, LST, VINoData = VINoData, LSTNoData = LSTNoData, OutNoData = VINoData)

# 将结果保存为 GTiff 格式
gma.rasp.WriteRaster(r'..\0.1 预处理\MODIS_LY_TVDI_20220407.tif', 
                     TVDI[0], 
                     Projection = Proj,
                     Transform = Geot,
                     DataType = 'Float32',
                     NoData = VINoData)
```
> TVDI 计算结果：

![](/index/TVDI.png)

> TVDI 干湿边拟合：

``` python 
import matplotlib.pyplot as plt
# 配置参数
PAR = {'font.sans-serif': 'Times New Roman',
       'axes.unicode_minus': False,
       'mathtext.default': 'default',
      }
plt.rcParams.update(PAR)
plt.figure(figsize = (8, 5), dpi = 300)

# 干边散点图、拟合图和方程
plt.scatter(TVDI[1], TVDI[3], c = 'pink', s = 10)
DryP = TVDI[5]
PolyfitD = TVDI[1] * DryP[0] + DryP[1]
plt.plot(TVDI[1], PolyfitD, c = 'red')
DryR2 = gma.math.Evaluation(PolyfitD, TVDI[3]).R2()
DryInfo = f'Dry: y = {"{:.4f}".format(DryP[0])} * VI + {"{:.4f}".format(DryP[1])}\n{" " * 8}$R^2$ = {DryR2}'
plt.text(0.58, 305, DryInfo, c = 'red', linespacing = 1.5)

# 湿边散点图、拟合图和方程
plt.scatter(TVDI[1], TVDI[2], c = 'lightblue', s = 10)
WetP = TVDI[4]
PolyfitW = TVDI[1] * WetP[0] + WetP[1]
plt.plot(TVDI[1], PolyfitW, c = 'blue')
WetR2 = gma.math.Evaluation(PolyfitW, TVDI[2]).R2()
WetInfo = f'Wet: y = {"{:.4f}".format(WetP[0])} * VI + {"{:.4f}".format(WetP[1])}\n{" " * 8}$R^2$ = {WetR2}'
plt.text(0.58, 291, WetInfo, c = 'blue', linespacing = 1.5)

# 其他配置
plt.grid(True, linestyle = (0,(6,6)), linewidth = 0.4)
plt.ylim(280, 310)
plt.xlabel('VI', loc = 'right', fontsize = 12)
plt.ylabel('LST(K)', loc = 'top', fontsize = 12)
plt.show()
```

![](/index/TVDIWDF.svg)

