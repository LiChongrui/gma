---
title: FillNoData
date: 2021-10-30
sidebar: false
---

## gma.index.**FillNoData**(*Data, FillValue = None, Method = 'linear', Axis = None, \*\*kwargs*)

---

**功能：**【填充缺失值】。对缺失值或异常值值进行插值替换。

**参数：**

&emsp;Data：`list||tuple||Series||DataFrame||array` 。需要插补的数据。

**可选参数：**

&emsp;FillValue = `float||list`。 需要进行插补的缺失值。默认不设置（None）。

::: warning 注意

1. 当 FillValue 为列表时，列表内所有值都将被插补。

2. 数据内原有的NAN、INF以及不能被转化为数字的字符串等异常值也将被插补。

:::

&emsp;Method = `str`。 插补方法。默认线性插值（linear）。

::: tip 其他插补方法

 index（索引）, values（序列值），pad（前向填充），nearest（最邻近），zero（零值），slinear（滑动线性），quadratic（2次方），cubic（3次方），spline（样条函数），barycentric（重心），polynomial（分段多项式），from_derivatives（衍生），krogh（克罗格），piecewise_polynomial（分段多项式），pchip（分段三次 Hermite 多项式插值），akima（akima 光滑插值），cubicspline（3次样条）等。

:::

&emsp;Axis = `int` <Badge text="1.0.8"/> 。数据插补使用的轴。默认（None）数据小于 3 维以第 1 个维度为轴，高于 3 维以倒数第 3 个维度为轴。

&emsp;**kwargs。传递给插值函数的其他参数。例如：Method 为 polynomial 或 spline 需要设置 order（阶数），默认阶数为 3。

**返回：** Series，DataFrame 返回 `输入类型`；list，tuple，array 返回 `array`。

---

**示例：**
```python
import gma
```

*序列（1 维）*

```python
Data = [None, 0.16359164, 0.17469311, 'NULL', 0.22857143, 0.32706435, 10, 0.10225949]
# 未定义需要被填充的值则仅插值序列中的非数据值以及无穷值
gma.math.FillNoData(Data)
```
> \>>> array([0.16359164, 0.16359164, 0.17469311, 0.20163227, 0.22857143, 0.32706435, 10.0, 0.10225949])

::: tip 提示

不能处理边缘缺失值的插补方法（例如 linear 等）函数默认采用邻近值填充边缘缺失值！如有特定需求，请在插补前自行处理！

:::

```python
# 定义了需要被填充的值后此值也会被填充。不存在的值则自动忽略
gma.math.FillNoData(Data, FillValue = 10)
```

> \>>> array([0.16359164, 0.16359164, 0.17469311, 0.20163227, 0.22857143, 0.32706435, 0.21466192, 0.10225949])

*不同插补方法插值结果对比*

```python
import matplotlib.pyplot as plt
# 配置参数
PAR = {'font.sans-serif': 'Times New Roman',
       'axes.unicode_minus': False
      }
plt.rcParams.update(PAR)
plt.figure(figsize = (8, 4.5), dpi = 300)
# 所有支持的插补方法
Metheds = gma.relation.key.FillingMethod
for m in Metheds:
    RS = gma.math.FillNoData(Data, FillValue = 10, Method = m)
    plt.plot(RS, label = m)
plt.grid(True, linestyle = (0,(6,6)), linewidth = 0.4)
plt.legend(ncol = 3, frameon = False)
plt.show()
```
![](/math/FillNoData.svg)

*基于栅格（多维）（10 波段哨兵2 L2A/B 计算的 NDVI 结果）*

```python
NDVISet = gma.Open('SENT_LY_NDVI_20220303-20220417.tif')

# 提取数据集的仿射变换和坐标系
Geot = NDVISet.GeoTransform
Proj = NDVISet.Projection
## print(NDVISet.NoData) >>> None # 栅格文件未配置 NoData 值
NDVI = NDVISet.ToArray()
## print(NDVI.max()) >>> nan  # 数据中存在无数据值 nan，也可根据最大值、最小值确定异常值。

# 按照第一个维度，也就是波段（相当于时间序列）进行 linear 插补。
# 无数据值为 nan 且栅格未配置 NoData 值，插补时不在需要配置 FillValue 参数；否则可配置为栅格 NoData 值或自行指定 FillValue 值。
NDVIFill = gma.math.FillNoData(NDVI, Axis = 0)

## NDVIFill.min() >>> -1.0
## NDVIFill.max() >>> 1.0 # 确定插补完数据不含异常值

# 将结果保存为 GTiff 格式
gma.rasp.WriteRaster(r'..\0.1 预处理\SENT_LY_NDVI_FillNoData_20220303-20220417.tif', 
                     NDVIFill, 
                     Projection = Proj, 
                     Transform = Geot,
                     DataType = 'Float32')
```
> \>>> 绘制其中的一个波段

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
im = ax.imshow(NDVIFill[7], cmap = CMap)
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size = "5%", pad = 0.2)
plt.colorbar(im, cax = cax)
```
![](/math/FillNoData.webp)
