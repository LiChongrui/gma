---
title: AddColorTable
date: 2021-10-30
sidebar: false
---

## gma.rasp.**AddColorTable**(*InFile, TemplateFile = None, ColorTable = None*)<Badge text="1.0.1 +"/>

---

**功能：**【添加色彩映射表】。为栅格数据添加色彩映射。

**参数：** 

&emsp;InFile：`str`。输入栅格路径。

**可选参数：**

&emsp;TemplateFile = `str`。模板栅格文件路径。默认不设置（None）。若设置模板栅格，则将模板栅格的色彩映射表添加到输入栅格。

&emsp;ColorTable = `dict`。色彩映射表。格式为 {值: (R,G,B,A)}。默认不设置（None）。

::: tip 示例

ColorTable = {10:(200,50,100,255), 20:(200,50,100,255)}。
:::

::: warning 注意

若设置了 ColorTable，则：

&emsp;1、若 TemplateFile 未设置（None），则用 ColorTable 更新输入栅格的色彩映射表。

&emsp;2、若设置了 TemplateFile，则以 TemplateFile 色彩映射表为基础，并用 ColorTable 更新该基础色彩映射表，然后将更新后的色彩映射表添加到输入栅格中。

:::

---

**示例：**

```python
import gma
```

*根据定义更新*

```python
## 待更新的色彩映射表
ColorTable = {10:(0,112,255,255),
              20:(255,211,127,255),
              30:(76,230,0,255),
              40:(123,104,238,255),
              50:(230,230,0,255),
              60:(205,245,122,255),
              70:(156,200,121,255),
              80:(245,162,122,255),
              90:(190,210,255,255),
              95:(109,150,178,255),
              100:(223,198,142,255)}
## 将定义的色彩映射表更新到文件
gma.rasp.AddColorTable("地表覆盖_河南_ESA_2020 - 副本.tif",
                       ColorTable = ColorTable)
```

*根据模板栅格更新*

```python
## 将定义的色彩映射表更新到文件
gma.rasp.AddColorTable("地表覆盖_河南_ESA_2020 - 副本 (2).tif",
                       "地表覆盖_河南_ESA_2020 - 副本.tif")
```

*根据模板栅格和定义更新*

```python
## 将定义的色彩映射表更新到文件
gma.rasp.AddColorTable("地表覆盖_河南_ESA_2020 - 副本 (3).tif",
                       "地表覆盖_河南_ESA_2020 - 副本.tif",
                       ColorTable = {10:(100,100,100,255), 40:(200,200,200,255)})
```

> \>>> 绘制原始数据及三个更新后的副本

```python
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import matplotlib.colors as cor
import numpy as np
## 此模块为地理制图图例、比例尺等的尝鲜模块。在下一版 gma 中会作为非必要的扩展模块合入！！
import gma.extend.mapplottools as mpt
PAR = {'font.sans-serif': 'Times New Roman',
       'axes.unicode_minus': False,
      }
plt.rcParams.update(PAR)
```
* *第一步：读取需绘制文件的色彩映射表信息*
```python
InFiles = ["地表覆盖_河南_ESA_2020.tif", "地表覆盖_河南_ESA_2020 - 副本.tif", 
           "地表覆盖_河南_ESA_2020 - 副本 (2).tif", "地表覆盖_河南_ESA_2020 - 副本 (3).tif"]
#### 读取四组数据色彩信息
CMap = []
Colors = []
for InFile in InFiles:
    DataSet = gma.Open(InFile)
    Color = DataSet.GetGDALDataset().GetRasterBand(1).GetColorTable()
    ColorTable = [Color.GetColorEntry(i) for i in range(Color.GetCount())]
    # 转换 色彩映射表 为 Matplotlib 可识别的格式
    CMapV = tuple(tuple(np.array(CT) / 255) for CT in ColorTable)
    # 生成色带
    CMap.append(cor.ListedColormap(CMapV))
    Colors.append([CMapV[i] for i in range(10, 110, 10)] + [CMapV[95]])
#### 为四组数据分配名称
Method = ['原始配色', '根据定义更新', '根据模板栅格更新', '根据模板栅格和定义更新']
#### 为颜色值定义含义
ColorName = ['林地', '灌木', '草地', '耕地', '建筑', '裸地/稀疏植被区', '雪和冰', '开阔水域', 
             '草本湿地', '红树林', '苔藓和地衣']
```

* *第二步：定义数据分块 —— 用于数据分块绘制（节约内存）*
```python
BlockSize = 8000
Columns = DataSet.Columns
Rows = DataSet.Rows
Blocks = [(r, c) for r in range(0, Rows, BlockSize) for c in range(0, Columns, BlockSize)]
```

* *第三步：配置制图范围*
```python
GEOT = DataSet.GeoTransform
Columns = DataSet.Columns
Rows = DataSet.Rows
# 数据边界
ExtentData = [GEOT[0], GEOT[0] + GEOT[1] * Columns, GEOT[3] + GEOT[-1] * Rows, GEOT[3]]
# 绘图边界（以数据边界为基础确定）
EL, ER, EB, ET = 0.2, 0.1, 0.15, 0.05  # 左右、下上边界的扩展比例
ExtentPLT = [ExtentData[0] - (ExtentData[1] - ExtentData[0]) * EL, 
             ExtentData[1] + (ExtentData[1] - ExtentData[0]) * ER, 
             ExtentData[2] - (ExtentData[3] - ExtentData[2]) * EB, 
             ExtentData[3] + (ExtentData[3] - ExtentData[2]) * ET]
```

* *第四步：绘图*
```python
WKTCRS = DataSet.Projection
fig = plt.figure(figsize = (10, 10), dpi = 600)

# 定义一个标准中国区 ALBERS 投影
Alberts_China = ccrs.AlbersEqualArea(central_longitude = 105, standard_parallels = (25.0, 47.0))  

for i in range(4):
    ax = plt.subplot(2, 2, i + 1, projection = Alberts_China) 

    ## 0.控制数据显示范围
    DataCRS = mpt.GetCRS(WKTCRS)
    ax.set_extent(ExtentPLT, crs = DataCRS)

    # 1.绘制底图图层（应用自有高精度数据做地图）
    ## 1.1 添加行政边界
    mpt.AddGeometries(ax, r"Region\VTD_PG_PLCity_China.shp", EdgeColor = 'LightGrey', LineWidth = 0.1)
    mpt.AddGeometries(ax, r"Region\VTD_PG_Province_China.shp", EdgeColor = 'Gray', LineWidth = 0.2)
    mpt.AddGeometries(ax, r"Region\VTD_PG_China.shp", EdgeColor = 'black', LineWidth = 0.4)
    mpt.AddGeometries(ax, r"Region\南海诸岛九段线.shp", EdgeColor = 'black', LineWidth = 0.4)

    ## 1.2 添加河流湖泊
    mpt.AddGeometries(ax, r"river\1级河流.shp", EdgeColor = 'RoyalBlue', LineWidth = 0.4)
    mpt.AddGeometries(ax, r"river\2级河流.shp", EdgeColor = 'DodgerBlue', LineWidth = 0.3)
    mpt.AddGeometries(ax, r"river\3级河流.shp", EdgeColor = 'DeepSkyBlue', LineWidth = 0.2)
    mpt.AddGeometries(ax, r"river\4级河流.shp", EdgeColor = 'SkyBlue', LineWidth = 0.15)
    mpt.AddGeometries(ax, r"river\5级河流.shp", EdgeColor = 'LightSkyBlue', LineWidth = 0.05)
    mpt.AddGeometries(ax, r"river\主要湖泊.shp", EdgeColor = 'none', LineWidth = 0, FaceColor = '#BEE8FF')

    # 2.绘制数据图层
    ## 分块绘制（节约内存）
    for Block in Blocks:
        # 数据都一样，读取一个文件的数据即可
        DrawData = DataSet.ToArray(*Block, BlockSize, BlockSize)
        ExtentBlock = [GEOT[0] + Block[1] * GEOT[1],  GEOT[0] + (DrawData.shape[1] + Block[1]) * GEOT[1], 
                       GEOT[3] - (DrawData.shape[0] + Block[0]) * GEOT[1], GEOT[3] - Block[0] * GEOT[1]]
        im = ax.imshow(DrawData, transform = DataCRS, cmap = CMap[i], extent = ExtentBlock, zorder = 2,
                       interpolation = 'none', vmin = 0, vmax = 255)

    # 3.为绘制区域增加经纬网
    gl = ax.gridlines(draw_labels = True, dms = False, x_inline = False, y_inline = False, 
                      linestyle = (0, (10, 10)), 
                      linewidth = 0.2,
                      color = 'Gray',
                      rotate_labels = False,
                      xlabel_style = {'fontsize': 8},
                      ylabel_style = {'fontsize': 8})
    # 3.1忽略相邻轴的经纬网标签
    if i % 2 == 0:
        gl.right_labels = False
    else:
        gl.left_labels = False
    if i < 2:
        gl.bottom_labels = False
    else:
        gl.top_labels = False        
           
    ax.set_title(Method[i], fontsize = 10, y = 0.92, fontdict = {'family':'SimSun'})
    
    # n.其他优化设置
    # n.1 添加指北针
    mpt.AddCompass(ax, LOC = (0.2, 0.85), SCA = 0.04, FontSize = 10)
    # n.2 添加比例尺
    mpt.AddScaleBar(ax, LOC = (0.8, 0.08), SCA = 0.1, FontSize = 6, PROJType = 'PROJCS', UnitPad = 0.25, BarWidth = 0.6)
    ## n.3 添加并修饰图例
    mpt.AddLegend(ax, Colors[i], LegendName = '分类', LengedInterval = 0.4, LabelList = ColorName, 
                  LegendSize = 8, TextInterval = 0.1, LOC = (0.05, 0.32), SCA = 0.03, AspectRatio = 1.5, 
                  Columns = 2, ColumnWide = 0.15, RowInterval = 0.015, FontSize = 6, EdgeColor = 'k', EdgeWidth = 0.1)    
plt.subplots_adjust(wspace = 0.05, hspace = -0.05)
plt.show()
```
![](/rasp/AddColorTable.webp)
