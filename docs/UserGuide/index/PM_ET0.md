---
title: PM_ET0 
date: 2021-10-31
sidebar: false
---

## gma.index.**PM_ET0**(*Pres, Wind, MaxT, MinT, Rh, Shour, Lat, Day, Ele, AS=0.25, BS=0.5, A=0.23*)

---

**功能：**【PM_ET0】。彭曼法（Penman Monteith）计算【日】【作物参考蒸散量（ET0）】。

**参数：**

&emsp;Pres：`float||array`。  日平均气压（hPa）。

&emsp;Wind：`float||array` 。 日平均10m风速（m/s）。

&emsp;MaxT：`float||array`。  日最高气温（℃）。

&emsp;MinT：`float||array` 。日最低气温（℃）。

&emsp;Rh：`float||array` 。日平均相对湿度（%）。

&emsp;Shour：`float||array`  日日照时数（hr）。

&emsp;Lat：`float||array` 。纬度（°）。

&emsp;Day：`int||array` 。以日序（儒略日）表示。1-365（平年）或366（闰年）。

&emsp;Ele：`float||array` 。海拔高度（m）。

**可选参数（常量）：**

&emsp; AS = 0.25。

&emsp; BS = 0.5。

&emsp; A = 0.23。

**返回：**`float||array`。

---

**示例：**
```python
import gma
```
*单个值（0 维）*
```python
Pres, Wind, MaxT, MinT, Rh, Shour = 1025.3, 2.2, 5.1, -4.5, 6.3, 5.5
Lat, Day, Ele = 35.6, 350, 45
gma.index.PM_ET0(Pres, Wind, MaxT, MinT, Rh, Shour, Lat, Day, Ele)
```
> \>>> 1.680369405068718

*序列（1 维）*

```python
Pres =[1034.7, 991.8, 994.8, 1014.7]
Wind = [3.4, 2.8, 3.1, 2.9]
MaxT = [5.5, 9, 5.9, 7.6]
MinT = [-1.3, -1.4, 0.8, -0.1]
Rh = [18.8, 18.4, 7, 19.9]
Shour = [5.2, 4.6, 4.2, 6.8]
Lat = [37.1, 37.6, 35.9, 36.5]
Day = [357, 348, 352, 358]
Ele = [176, 385, 468, 412]
gma.index.PM_ET0(Pres, Wind, MaxT, MinT, Rh, Shour, Lat, Day, Ele)
```
> \>>> [2.05433147, 2.02435767, 2.31121748, 1.99324934]
::: tip 提示
Lat、Day、Ele 也支持配置单个值，以及与气象数据同形状数据进行的序列组合。
:::

```python
# 组合 1
Lat, Day, Ele = [37.1, 37.6, 35.9, 36.5], 357, 176
print('组合1', gma.index.PM_ET0(Pres, Wind, MaxT, MinT, Rh, Shour, Lat, Day, Ele))
# 组合 2
Lat, Day, Ele = [37.1, 37.6, 35.9, 36.5], [357, 348, 352, 358], 176
print('组合1', gma.index.PM_ET0(Pres, Wind, MaxT, MinT, Rh, Shour, Lat, Day, Ele))
# 组合 3
Lat, Day, Ele = [37.1, 37.6, 35.9, 36.5], 357, [176, 385, 468, 412]
print('组合1', gma.index.PM_ET0(Pres, Wind, MaxT, MinT, Rh, Shour, Lat, Day, Ele))
# 组合 4
Lat, Day, Ele = 37.1, 357, 176
print('组合1', gma.index.PM_ET0(Pres, Wind, MaxT, MinT, Rh, Shour, Lat, Day, Ele))
# 组合 5
Lat, Day, Ele = 37.1, [357, 348, 352, 358], 176
print('组合1', gma.index.PM_ET0(Pres, Wind, MaxT, MinT, Rh, Shour, Lat, Day, Ele))
# 组合 6
Lat, Day, Ele = 37.1, [357, 348, 352, 358], [176, 385, 468, 412]
print('组合1', gma.index.PM_ET0(Pres, Wind, MaxT, MinT, Rh, Shour, Lat, Day, Ele))
# 组合 7
Lat, Day, Ele = 37.1, 357, [176, 385, 468, 412]
print('组合1', gma.index.PM_ET0(Pres, Wind, MaxT, MinT, Rh, Shour, Lat, Day, Ele))
```
> \>>> 组合1 [2.05433147 2.01522148 2.3042206  1.98495581]<br>
> \>>> 组合2 [2.05433147 2.0188891  2.30384578 1.98591626]<br>
> \>>> 组合3 [2.05433147 2.02069468 2.31159229 1.99229006]<br>
> \>>> 组合4 [2.05433147 2.03178747 2.26808713 1.96110793]<br>
> \>>> 组合5 [2.05433147 2.03540336 2.26772746 1.96207709]<br>
> \>>> 组合6 [2.05433147 2.04085821 2.27514044 1.96943621]<br>
> \>>> 组合7 [2.05433147 2.0372468  2.27550011 1.96846826]

*更多维度*
```python
Pres = [[1026.4, 1037.7, 987.1, 1031.1],
        [1006.1, 1013.2, 1016.9, 1046.4],
        [1046. , 1009.3, 1004.1, 1022.9]]
Wind = [[3.2, 5.8, 5.2, 5.9],
        [5.3, 6. , 3.9, 6.4],
        [3.7, 4.1, 6.8, 4.9]]
MaxT = [[8.1, 7.1, 2.4, 5.7],
        [0.9, 3.2, 0.2, 2.9],
        [1.6, 3.7, 2.6, 6.7]]
MinT = [[-4.8, -6.1, -7.8, -9.1],
        [-8.9, -7.2, -5.8, -1.1],
        [-7.7, -2.1, -7. , -6.9]]
Rh = [[26.7, 25.6, 30.5, 17.3],
      [34.3, 15.6, 11.2, 33.7],
      [25.8, 22.1, 15.3, 28.7]]
Shour = [[3.3, 2.4, 2.4, 1.5],
         [7.8, 7.7, 5.5, 6. ],
         [6.9, 7.3, 8. , 5.6]]
Lat = [[35.2, 37. , 36.8, 35.4],
       [36.7, 36.3, 36.4, 35.6],
       [36.1, 36.6, 36.8, 36.5]]
Day = [[350, 351, 352, 353],
       [354, 355, 356, 357],
       [358, 359, 360, 361]]
Ele = [[240, 399, 168.3, 197.3],
       [233.3, 365.1, 329.4, 330.7],
       [163.2, 346.8,  57.2, 227.7]]
gma.index.PM_ET0(Pres, Wind, MaxT, MinT, Rh, Shour, Lat, Day, Ele)
```
> \>>> array([[1.96605814, 2.53089833, 1.8249439 , 2.57517405],<br>
> 　　　　　[1.60235259, 2.38994146, 1.86795955, 2.25009657],<br>
> 　　　　　[1.59021274, 2.04317504, 2.46576261, 2.17230612]])

::: tip 提示
Lat、Day、Ele 类型组合请参考 *序列（1 维）*。
:::

*基于栅格（ANUSPLIN 气象站点空间插值数据）*
```python
# 气象数据
PRSSet = gma.Open('PRS_China_ANUSPLIN_20201215.tif')
RHUSet = gma.Open('RHU_China_ANUSPLIN_20201215.tif')
SSDSet = gma.Open('SSD_China_ANUSPLIN_20201215.tif')
TMAXSet = gma.Open('TMAX_China_ANUSPLIN_20201215.tif')
TMINSet = gma.Open('TMIN_China_ANUSPLIN_20201215.tif')
WINSet = gma.Open('WIN_China_ANUSPLIN_20201215.tif')
# 高程
EleSet = gma.Open('ELE_China_GEBCO_2020.tif')
# 纬度
LatSet = gma.Open('LAT_China_GEBCO_2020.tif')

# 提取数据集的仿射变换、坐标系和无数据值
Geot = PRSSet.GeoTransform
Proj = PRSSet.Projection
NoData = PRSSet.NoData

# 读取数据到数组
Pres, Wind, MaxT = PRSSet.ToArray(), WINSet.ToArray(), TMAXSet.ToArray(),
MinT, Rh, Shour = TMINSet.ToArray(), RHUSet.ToArray(), SSDSet.ToArray()
Ele = EleSet.ToArray()
Lat = LatSet.ToArray()
Day = 350

PMET0 = gma.index.PM_ET0(Pres, Wind, MaxT, MinT, Rh, Shour, Lat, Day, Ele)

# 将结果保存为 GTiff 格式
gma.rasp.WriteRaster(r'..\0.1 预处理\PMET0_China_20201215.tif', 
                     PMET0, 
                     Projection = Proj, 
                     Transform = Geot,
                     DataType = 'Float32',
                     NoData = NoData)
```
> 对最高气温和PM_ET0 计算结果进行绘制

![](/index/PMET0.webp)

> 绘图代码示例

```python
import cartopy.crs as ccrs
import cartopy.feature as cft
import matplotlib.pyplot as plt
import matplotlib.colors as cor
import numpy as np
import gma

## 以下模块为尝鲜模块。在 gma 1.0.9 中作为非必要的扩展模块合入！！
import gma.extend.mapplottools as mpt
import gma.extend.arrayenhancement as aec

PAR = {'font.sans-serif': 'Times New Roman',
       'axes.unicode_minus': False,
      }
plt.rcParams.update(PAR)

# 需要绘制的两个文件
InFiles = ["TMAX_China_ANUSPLIN_20201215.tif", "PMET0_China_ANUSPLIN_20201215.tif"]

DataTypeNames = ['最高气温', '作物参考蒸散量']
LegendLable = ['TMax(℃)', 'ET0(mm)']
fig = plt.figure(figsize = (10, 10), dpi = 300)

# 定义一个标准中国区 ALBERS 投影
Alberts_China = ccrs.AlbersEqualArea(central_longitude = 105, standard_parallels = (25.0, 47.0))  

for i in range(len(InFiles)):
    ax = plt.subplot(1, 2, i + 1, projection = Alberts_China) 
    
    DataSet = gma.Open(InFiles[i])
    DrawData = DataSet.ToArray()
    DrawData[DrawData == DataSet.NoData] = np.nan
    # 由于数据有过大过小值，这里做一个百分比截断拉伸
    STRE = aec.Stretch(DrawData, MaxLabel = np.nanpercentile(DrawData, 95), MinLabel = np.nanpercentile(DrawData, 5))
    DrawData = STRE.Percentage()
    ############################################ 配置范围
    GEOT = DataSet.GeoTransform
    Columns = DataSet.Columns
    Rows = DataSet.Rows
    # 数据边界
    ExtentData = [GEOT[0], GEOT[0] + GEOT[1] * Columns, GEOT[3] + GEOT[-1] * Rows, GEOT[3]]
    # 绘图边界（以数据边界为基础确定）
    EL, ER, EB, ET = -0.1,-0.1,0.1, 0.01  # 左右、下上边界的扩展比例
    ExtentPLT = [ExtentData[0] - (ExtentData[1] - ExtentData[0]) * EL, 
                 ExtentData[1] + (ExtentData[1] - ExtentData[0]) * ER, 
                 ExtentData[2] - (ExtentData[3] - ExtentData[2]) * EB, 
                 ExtentData[3] + (ExtentData[3] - ExtentData[2]) * ET]    
    
    WKTCRS = DataSet.Projection
    
    # 0.控制数据显示范围
    DataCRS = mpt.GetCRS(WKTCRS)
    ax.set_extent(ExtentPLT, crs = DataCRS)

    # 1.绘制底图图层
    ## 1.1 添加行政边界
    mpt.AddGeometries(ax, r"Region\VTD_PG_Province_China.shp", EdgeColor = 'Gray', LineWidth = 0.1)
    mpt.AddGeometries(ax, r"Region\VTD_PG_China.shp", EdgeColor = 'black', LineWidth = 0.2)
    mpt.AddGeometries(ax, r"Region\南海诸岛九段线.shp", EdgeColor = 'black', LineWidth = 0.3)
    ## 1.2 添加国家 / 海洋背景 / 大型湖泊
    mpt.AddGeometries(ax, r"World\VTD_PG_World_Country.shp", EdgeColor = 'gray', LineWidth = 0.1, 
                      FaceColor = 'white', Zorder = 0)
    ax.set_facecolor('#BEE8FF')
    ax.add_feature(cft.LAKES.with_scale('110m'), color = '#BEE8FF')
    
    # 2.绘制数据图层
    im = ax.imshow(DrawData, transform = DataCRS, cmap = plt.get_cmap('jet'), extent = ExtentData, zorder = 1,
                   interpolation = 'none')        
         
    # 3.为绘制区域增加经纬网
    gl = ax.gridlines(draw_labels = True, dms = False, x_inline = False, y_inline = False, 
                      linestyle = (0, (10, 10)), 
                      linewidth = 0.2,
                      color = 'Gray',
                      rotate_labels = False,
                      xlabel_style = {'fontsize': 8},
                      ylabel_style = {'fontsize': 8})
    ## 3.1忽略相邻轴的经纬网标签
    if i % 2 == 0:
        gl.right_labels = False
    else:
        gl.left_labels = False
        
    ax.set_title(DataTypeNames[i], fontsize = 10, y = 0.92, fontdict = {'family':'SimSun'})
    
    # n.其他优化设置
    ## n.1 添加指北针
    mpt.AddCompass(ax, LOC = (0.15, 0.9), SCA = 0.04, FontSize = 10)
    ## n.2 添加比例尺
    mpt.AddScaleBar(ax, LOC = (0.4, 0.08), SCA = 0.12, FontSize = 6, UnitPad = 0.2, BarWidth = 0.6)
    ## n.3 添加并修饰图例
    leg = fig.colorbar(im, 
                       location = 'right', # 位置
                       orientation = 'vertical', # 图例方向
                       pad = -0.3, # 边距
                       ticks = [np.nanmin(DrawData), 0, np.nanmax(DrawData)],
                       shrink = 0.06, # 大小缩放
                       aspect = 2, # 长宽比
                       anchor = (-8, 0.38), # 位置
                      )
    leg.outline.set(edgecolor = 'black',linewidth = 0.1)
    leg.ax.set_title(LegendLable[i], fontsize = 8, loc = 'left')
    leg.ax.tick_params(which = 'major', direction = 'out', labelsize = 6, length = 3, color = 'black', width = 0.1)

plt.show()
```

