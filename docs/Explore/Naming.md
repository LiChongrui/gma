---
title: 命名规定
date: 2023-08-20
---

## 基本规则

&emsp;&emsp;函数、参数的命名遵循以下规定：
::: theorem 

**单个单词：** 首字母大写，例如：Clip。

**多个单词：** 每个单词首字母大写，多个单词直接连在一起。例如：ToOtherFormat。

**缩写：** 缩写单词全部大写。例如：GenerateOVR，OVR 为 Overviews 的缩写。

:::

&emsp;&emsp;模块名的命名遵循以下规定：

::: theorem 

**不论缩写与否均使用小写**，例如：vesp（vector space processing）。

:::

## 缩写对照

&emsp;&emsp;下表为函数名中出现缩写的中英文对照解释（专有缩写，如植被指数（NDVI、EVI等）、数学评估方法（RMSE、NRMSE等）以及数据驱动等不在下表中列出）。

| 缩写 | 英文全称                            | 中文解释           | 使用条件                                                     |
| :------- | :---------------------------------- |:------------------ |:------------------------------------------------------------ |
| OVR      | Overviews                           | 概述               | 生成栅格金字塔文件，可加速栅格文件在 ArcGIS 等软件的加载显示速度 |
| PM       | Penman-Monteith                     | 彭曼-蒙提斯        | 人名（科学家）                                               |
| CORR     | Correlation                         | 相关性             | 相关分析                                                     |
| DF       | DataFrame                           | 数据帧             | 二维数据处理与分析                                           |
| CAL      | Calculate                           | 计算               | 数学计算                                                     |
| TRAN     | Transform                           | 使改变             | 数学变换                                                     |
| SDS      | Scientific Data Set                 | 科学数据集         | .nc .hdf 等科学数据集应用                                    |
| GDAL     | Geospatial Data Abstraction Library | 栅格空间数据转换库 | 栅格数据应用                                                 |
| EXT      | Extension                           | 扩展名             | 标记、查找或应用的文件类型                                   |
| VC | Vector Creation | 矢量创建 | 生成矢量文件的创建参数 |
| VE | Vector | 矢量 | 矢量处理 |
| RC | Raster Creation | 栅格创建 | 生成栅格文件的创建参数 |
| RA | Raster | 栅格 | 栅格处理 |
| DEM | Digital Elevation Model | 数字高程模型 | 零阶单纯的单项数字地貌模型 |
| TPI | Topographic Position Index | 地形位置指数 | DEM 分析 |
| TRI | Terrain Ruggedness Index | 地形耐用度指数 | DEM 分析 |

