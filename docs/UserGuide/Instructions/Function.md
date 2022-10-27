---
title: 函数列表
date: 2022-10-29
---

**&emsp;&emsp;函数列表** 列出了 gma 包含的所有可用函数定义和说明，**可以快速了解所有的函数和功能**。

&emsp;&emsp;除了初版构建的函数之外，其他版本构建的函数会增加版本 <Badge text="标记"/>  。

## 气象气候 <Badge text="1.0.10 +"/>

 函数 | 引用（简版）| 功能 | 详细解释                          
 :----- | :----- | :----- | :-----
[SPEI](../climet/SPEI.html) | gma.climet.SPEI | 【标准化降水蒸散指数】 | 基于 Log-Logistic 分布计算标准化降水蒸散指数 
[SPI](../climet/SPI.html)| gma.climet.SPI | 【标准化降水指数】 | 基于 Gamma 分布计算标准化降水指数                            
[PAP](../climet/PAP.html)  | gma.climet.PAP | 【降水距平百分率】 | 计算降水值到多年平均值的波动情况 
| [MKMutationTest](../climet/MKMutationTest.html) <Badge text="1.0.12 +"/>| gma.math.MKMutationTest | 【Mann-Kendall 突变检验】 | 基于 Mann-Kendall 方法对时间序列数据进行突变检验。 |
***ET0*** | gma.climet.ET0 | 【蒸散】 | *日尺度或月尺度潜在蒸散量计算。支持的计算方法详见：[蒸散](Function.html#蒸散)* 

#### 蒸散 <Badge text="1.0.10 +"/>

| 函数                                                | 引用（简版）                  | 功能               | 详细解释                                             |
| :-------------------------------------------------- | :---------------------------- | :----------------- | :--------------------------------------------------- |
| [Hargreaves](../climet/ET0/Hargreaves.html)         | gma.climet.ET0.Hargreaves     | 【Hargreaves】     | 基于 哈格里夫斯（Hargreaves 1998）法计算日潜在蒸散量 |
| [PenmanMonteith](../climet/ET0/PenmanMonteith.html) | gma.climet.ET0.PenmanMonteith | 【PenmanMonteith】 | 基于 彭曼-蒙提斯法（FAO-56）计算日作物参考蒸散量     |
| [Thornthwaite](../climet/ET0/Thornthwaite.html)     | gma.climet.ET0.Thornthwaite   | 【Thornthwaite】   | 基于 桑斯维特（Thornthwaite 1948）法计算月潜在蒸散量 |

#### 其他 <Badge text="1.0.13 +"/>

| 函数                                                | 引用（简版）                  | 功能               | 详细解释                                             |
| :-------------------------------------------------- | :---------------------------- | :----------------- | :--------------------------------------------------- |
| [DaylightHours](../climet/Other/DaylightHours.html)         | gma.climet.Other.DaylightHours     | 【白昼时数】 | 基于 FAO-56 推荐的方法计算白昼时数（h） |
| [Declination](../climet/Other/Declination.html)         | gma.climet.Other.Declination     | 【赤纬】   | 基于 FAO-56 推荐的方法计算赤纬（red） |
| [HourAngle](../climet/Other/HourAngle.html)         | gma.climet.Other.HourAngle     | 【时角】   | 基于 FAO-56 推荐的方法计算时角（t） |
| [RDBSunAndEarth](../climet/Other/RDBSunAndEarth.html)         | gma.climet.Other.RDBSunAndEarth     | 【日地相对距离】 | 基于 FAO-56 推荐的方法计算日地相对距离（AU） |
| [SolarRadiationFluxOA](../climet/Other/SolarRadiationFluxOA.html)         | gma.climet.Other.SolarRadiationFluxOA     | 【大气层外太阳辐射通量】 | 基于 FAO-56 推荐的方法计算大气层外太阳辐射通量（MJ/m2）|

## 遥感指数

| 函数                                              | 引用（简版）  | 功能     | 详细解释         |
| :------------------------------------------------ | :------------ | :------- | :--------------- |
| [EVI](../rsvi/EVI.html)                           | gma.rsvi.EVI  | 【EVI】  | 增强植被指数     |
| [NDBI](../rsvi/NDBI.html)                         | gma.rsvi.NDBI | 【NDBI】 | 归一化建筑指数   |
| [NDWI](../rsvi/NDWI.html)                         | gma.rsvi.NDWI | 【NDWI】 | 归一化水指数     |
| [NDVI](../rsvi/NDVI.html)                         | gma.rsvi.NDVI | 【NDVI】 | 归一化植被指数   |
| [TVDI](../rsvi/TVDI.html) <Badge text="1.0.2 +"/> | gma.rsvi.TVDI | 【TVDI】 | 温度植被干旱指数 |

 ## 数学运算

| 函数 / *类*  | 引用（简版）                     | 功能               | 详细解释                                                     |
| :------------------ | :------------------------------- | :----------------- | :----------------------------------------------------------- |
| [FillNoData](../math/FillNoData.html) | gma.math.FillNoData | 【填充缺失值】 | 对缺失值或异常值值进行插值替换 |
| [ToNumericArray](../math/ToNumericArray.html) <Badge text="1.0.6 +"/> | gma.math.ToNumericArray | 【转换为数字型数组】 | 强制将输入数据转为数字型数组                                 |
| ***[Smooth](../math/Smooth/index.html)*** | *gma.math.Smooth* | *【数据平滑】* | *数据平滑（滤波）。支持的平滑方法详见：[数据平滑](Function.html#数据平滑)* |
| ***[Evaluation](../math/Evaluation/index.html)*** | *gma.math.Evaluation* | *【数据评估】* | *支持的重命名方法详见：[数据评估](Function.html#数据评估)* |
| ***Kernel*** <Badge text="1.0.11 +"/> | *gma.math.Kernel* | *【核运算】* | *利用卷积核或其他核对数据进行运算分析。支持的分析函数详见：[核运算](Function.html#核运算)* |

#### 数据平滑

| 方法                                                | 引用（简版）                  | 功能         | 详细解释                               |
| :-------------------------------------------------- | :---------------------------- | :----------- | :------------------------------------- |
| [MovingAverage](../math/Smooth/MovingAverage.html) | gma.math.Smooth.MovingAverage | 【滑动平均】 | 利用滑动平均法对数据进行平滑           |
| [SavitzkyGolay](../math/Smooth/SavitzkyGolay.html) | gma.math.Smooth.SavitzkyGolay | 【SG平滑】   | 利用 Savitzky-Golay 方法对数据进行平滑 |

#### 数据评估

| 方法                                    | 引用（简版）                | 功能         | 详细解释                                             |
| :-------------------------------------- | :-------------------------- | :----------- | :--------------------------------------------------- |
| [RMSE](../math/Evaluation/RMSE.html)       | gma.math.Evaluation.RMSE    | 【RMSE】     | 均方根误差                                           |
| [NRMSE](../math/Evaluation/NRMSE.html)     | gma.math.Evaluation.NRMSE   | 【NRMSE】    | 归一化均方根误差                                     |
| [D](../math/Evaluation/D.html)             | gma.math.Evaluation.D       | 【D】        | D指标                                                |
| [CORR](../math/Evaluation/CORR.html)       | gma.math.Evaluation.CORR    | 【r，P】     | 相关系数和显著性水平                                 |
| [R2](../math/Evaluation/R2.html)           | gma.math.Evaluation.R2      | 【R2】       | 决定系数                                             |
| [MaxAE](../math/Evaluation/MaxAE.html)     | gma.math.Evaluation.MaxAE   | 【MaxAE】    | 最大绝对误差                                         |
| [Select](../math/Evaluation/Select.html)   | gma.math.Evaluation.Select  | 【选择方法】 | 选择Evaluation中需要计算的一个或多个评价指标进行计算 |
| [Methods](../math/Evaluation/Methods.html) | gma.math.Evaluation.Methods | 【记录方法】 | 记录Evaluation类中所有的评估方法                     |

#### 核运算 <Badge text="1.0.11 +"/>

| 函数                                       | 引用（简版）          | 功能               | 详细解释                          |
| :----------------------------------------- | :-------------------- | :----------------- | :-------------------------------- |
| [Aggregate](../math/Kernel/Aggregate.html) | gma.math.Kernel.Aggregate | 【数组聚合】         | 生成缩小后数组        |
| [GeneralFilter](../math/Kernel/GeneralFilter.html)| gma.math.Kernel.GeneralFilter | 【普通滤波】      | 对数组进行普通滤波处理       |
| [GaussFilter](../math/Kernel/GaussFilter.html)| gma.math.Kernel.GaussFilter | 【高斯滤波】      | 利用高斯核对数组进行滤波处理       |


 ## 系统交互

| **函数 /** *类* | 引用（简版）                | 功能         | 详细解释                                         |
| :--------------- | :-------------------------- | :----------- | :----------------------------------------------- |
| [DateSeries](../osf/DateSeries.html)       | gma.osf.DateSeries        | 【日期序列】 | 构造一个日期序列列表                               |
| [GetPath](../osf/GetPath.html)          | gma.osf.GetPath           | 【获取路径】 | 获取目标路径或路径集合下满足条件的所有文件夹和文件路径                              |
| [MultiThreading](../osf/MultiThreading.html) <Badge text="1.0.3 +"/> | gma.osf.MultiThreading | 【多线程】 | 创建多个线程，实现同一函数多个参数的同步执行 |
| [UnZip](../osf/UnZip.html)            | gma.osf.UnZip             | 【解压缩】   | 解压缩 .zip 文件                                |
| [Zip](../osf/Zip.html)            | gma.osf.Zip               | 【压缩】     | 将目标路径下所有文件压缩为 .zip 文件                  |
| *[**Rename**](../osf/Rename/index.html)* | *gma.osf.Rename* | *【重命名】* | *重命名文件或文件夹。支持的重命名方法详见：[重命名](Function.html#重命名)* |

#### 重命名

| 方法                                       | 引用（简版）             | 功能     | 详细解释                                         |
| :----------------------------------------- | :----------------------- | :------- | :----------------------------------------------- |
| [Modify](../osf/Rename/Modify.html)       | gma.osf.Rename.Modify    | 【修改】 | 将原有文件（夹）名修改为新名                     |
| [Replace](../osf/Rename/Replace.html)     | gma.osf.Rename.Replace   | 【替换】 | 替换原文件（夹）名中字符串后作为新文件（夹）名   |
| [Intercept](../osf/Rename/Intercept.html) | gma.osf.Rename.Intercept | 【截取】 | 截取文件（夹）名中的部分字符串作为新文件（夹）名 |

 ## 空间杂项<Badge text="1.0.5 +"/>

| 函数 | 引用（简版）| 功能 | 详细解释|
| :----- | :----- | :----- | :-----|
| [CALArea](../smc/CALArea.html)<Badge text="1.1.0 +"/> | gma.smc.CALArea | 【计算面积】 | 计算输入多点组成多边形的面积 |
|[CALDistance](../smc/CALDistance.html) | gma.smc.CALDistance |【计算距离】|计算输入两点或多点之间依次连接后的总距离|
|[TRANCoordinate](../smc/TRANCoordinate.html) | gma.smc.TRANCoordinate |【坐标转换】|将输入点的坐标转换为目标坐标系下的坐标|
| ***Interpolate***<Badge text="1.1.0 +"/> | *gma.smc.Interpolate* | *【空间插值】* | *利用不同插值方法将点插值到面。支持的插值方法详见：[空间插值](Function.html#空间插值)* |

#### 空间插值<Badge text="1.1.0 +"/>
| 方法                                       | 引用（简版）             | 功能     | 详细解释                                         |
| :----------------------------------------- | :----------------------- | :------- | :----------------------------------------------- |
| [BSpline](../smc/Interpolate/BSpline.html)       | gma.smc.Interpolate.BSpline    | 【B-样条函数法插值】 | 使用 B-样条函数法（BSpline）将点插值成二维数组         |
| [IDW](../smc/Interpolate/IDW.html)       | gma.smc.Interpolate.IDW    | 【反距离权重插值】 | 使用反距离加权法（IDW）将点插值成二维数组           |
| [NaturalNeighbor](../smc/Interpolate/NaturalNeighbor.html) | gma.smc.Interpolate.NaturalNeighbor | 【自然邻域法插值】 | 使用自然邻域法法（NaturalNeighbor）将点插值成二维数组 |
| [Trend](../smc/Interpolate/Trend.html) | gma.smc.Interpolate.Trend | 【趋势面法插值】 | 使用趋势面法（Trend）（全局多项式插值法）将点插值成二维数组 |

 ## 栅格处理

| 函数 / *类*                                                  | 引用（简版）                  | 功能                | 详细解释                                                     |
| :----------------------------------------------------------- | :---------------------------- | :------------------ | :----------------------------------------------------------- |
| [AddColorTable](../rasp/AddColorTable.html) <Badge text="1.0.1 +"/> | gma.rasp.AddColorTable        | 【添加色彩映射表】  | 为栅格数据添加色彩映射                                       |
| [BandDecomposition](../rasp/BandDecomposition.html)  | gma.rasp.BandDecomposition    | 【波段分解】        | 将多波段文件拆分（或提取）为单波段文件                       |
| [BandSynthesis](../rasp/BandSynthesis.html)          | gma.rasp.BandSynthesis        | 【文件合并】        | 单波段文件合成多波段文件                                     |
| [ChangeDataType](../rasp/ChangeDataType.html)        | gma.rasp.ChangeDataType       | 【数据类型转换】    | 转换栅格数据的数据类型                                       |
| [Clip](../rasp/Clip.html)                            | gma.rasp.Clip                 | 【裁剪】            | 按矢量边界裁剪栅格                                           |
| [Deformation](../rasp/Deformation.html)              | gma.rasp.Deformation          | 【流程化处理】      | 完成镶嵌-裁剪-重采样-重投影-格式转换等其中一个或多个功能     |
| [GenerateOVR](../rasp/GenerateOVR.html)              | gma.rasp.GenerateOVR          | 【构建栅格金字塔】  | 为 GTiff 文件构造 .ovr 栅格金字塔，或为其他类型的栅格数据强制构造 .ovr 金字塔 |
| [Mosaic](../rasp/Mosaic.html)                        | gma.rasp.Mosaic               | 【栅格镶嵌】        | 将多个栅格数据集合并到一个新的栅格数据集中                   |
| [MultiSDSToTif](../rasp/MultiSDSToTif.html)          | gma.rasp.MultiSDSToTif        | 【多维数据转GTiff】 | 将含有子数据集的多维数据提取为 GTiff                         |
| [OrthophotoCorrection](../rasp/OrthophotoCorrection.html) | gma.rasp.OrthophotoCorrection | 【正射矫正】        | 根据有理多项式系数（RPC）对影像进行正射校正                  |
| [Reproject](../rasp/Reproject.html)                  | gma.rasp.Reproject            | 【重投影】          | 将空间数据从一种坐标系投影到另一种坐标系                     |
| [Resample](../rasp/Resample.html)                    | gma.rasp.Resample             | 【重采样】          | 更改栅格数据的空间分辨率                                     |
| [SplitImage](../rasp/SplitImage.html) <Badge text="1.0.3 +"/> | gma.rasp.SplitImage           | 【影像切片】        | 将一幅影像切分为特定行列数的小影像                           |
| [ToOtherFormat](../rasp/ToOtherFormat.html)          | gma.rasp.ToOtherFormat        | 【格式转换】        | 一种栅格格式转换为另一种栅格格式                             |
| [ToVector](../rasp/ToVector.html)                    | gma.rasp.ToVector             | 【栅格转矢量】      | 将栅格数据转换为矢量数据                                     |
| [WriteRaster](../rasp/WriteRaster.html)              | gma.rasp.WriteRaster          | 【写出栅格】        | 将数组保存为栅格                                             |
| ***Fusion***            | *gma.rasp.Fusion*             | *【数据融合】*      | *全色与多光谱数据融合。支持的融合函数详见：[数据融合](Function.html#数据融合)* |

#### 数据融合

| 函数                                          | 引用（简版）               | 功能           | 详细解释                                         |
| :-------------------------------------------- | :------------------------- | :------------- | :----------------------------------------------- |
| [Pansharpen](../rasp/Fusion/Pansharpen.html) | gma.rasp.Fusion.Pansharpen | 【Pansharpen】 | 对全色影像和多光谱影像基于Pansharpen方法进行融合 |

 ## 栅格分析

| **函数 /** *类*                         | 引用（简版）   | 功能           | 详细解释                                                     |
| --------------------------------------- | -------------- | :------------- | :----------------------------------------------------------- |
| ***DEM*** <Badge text="1.0.7 +"/> | *gma.raa.DEM* | *【DEM 分析】* | *利用 DEM 实现地形分析。支持的 DEM 分析函数详见：[DEM 分析](Function.html#dem-分析)* |
| ***Kernel*** <Badge text="1.0.11 +"/> | *gma.raa.Kernel* | *【核分析】* | *利用卷积核获取其他核对栅格数据进行运算分析。支持的分析函数详见：[核分析](Function.html#核分析)* |
| ***Extraction***<Badge text="1.0.13 +"/> | *gma.raa.Extraction* | *【提取分析 分析】* | *对栅格数据进行提取分析。函数详见：[提取分析](Function.html#提取分析)* |

#### DEM 分析 <Badge text="1.0.7 +"/>

| 函数                                       | 引用（简版）          | 功能               | 详细解释                          |
| :----------------------------------------- | :-------------------- | :----------------- | :-------------------------------- |
| [Roughness](../raa/DEM/Roughness.html) | gma.raa.DEM.Roughness | 【粗糙度】         | 从 DEM 栅格文件计算粗糙度         |
| [HillShade](../raa/DEM/HillShade.html)| gma.raa.DEM.HillShade | 【山体阴影】       | 从 DEM 栅格文件计算山体阴影       |
| [Slope](../raa/DEM/Slope.html)  | gma.raa.DEM.Slope     | 【坡度】           | 从 DEM 栅格文件计算坡度           |
| [Aspect](../raa/DEM/Aspect.html)  | gma.raa.DEM.Aspect    | 【坡向】           | 从 DEM 栅格文件计算坡向           |
| [TRI](../raa/DEM/TRI.html)   | gma.raa.DEM.TRI       | 【地形耐用度指数】 | 从 DEM 栅格文件计算地形耐用度指数 |
| [TPI](../raa/DEM/TPI.html)  | gma.raa.DEM.TPI       | 【地形位置指数】   | 从DEM 栅格文件计算地形位置指数    |

#### 核分析 <Badge text="1.0.11 +"/>

| 函数                                       | 引用（简版）          | 功能               | 详细解释                          |
| :----------------------------------------- | :-------------------- | :----------------- | :-------------------------------- |
| [Aggregate](../raa/Kernel/Aggregate.html) | gma.raa.Kernel.Aggregate | 【栅格聚合】         | 生成低分辨率栅格        |
| [GeneralFilter](../raa/Kernel/GeneralFilter.html)| gma.raa.Kernel.GeneralFilter | 【普通滤波】      | 对影像进行普通滤波处理       |
| [GaussFilter](../raa/Kernel/GaussFilter.html)| gma.raa.Kernel.GaussFilter | 【高斯滤波】      | 利用高斯核对影像进行滤波处理       |

#### 提取分析 <Badge text="1.0.13 +"/>

| 函数                                        | 引用（简版）                | 功能       | 详细解释                                 |
| :------------------------------------------ | :-------------------------- | :--------- | :--------------------------------------- |
| [Isopleth](../raa/Extraction/Isopleth.html) | gma.raa.Extraction.Isopleth | 【等值线】 | 生成数量指标值相等的各点连成的平滑曲线。 |

## 矢量处理

| 函数    | 引用（简版）             | 说明             | 解释                                     |
| :------------ | :----------------------- | :--------------- | :--------------------------------------- |
| [Check](../vesp/Check.html)         | gma.vesp.Check         | 【检查】         | 检查每个矢量要素的有效性                       |
| [Clip](../vesp/Clip.html)          | gma.vesp.Clip          | 【裁剪】         | 矢量裁剪矢量                             |
| [Erase](../vesp/Erase.html)         | gma.vesp.Erase         | 【擦除】         | 从第一个矢量中去除与第二个矢量交叉的部分 |
| [FixGeometry](../vesp/FixGeometry.html) <Badge text="1.0.6 +"/>| gma.math.FixGeometry | 【修正几何】 | 修正矢量数据中无效的几何要素 |
| [Intersection](../vesp/Intersection.html)  | gma.vesp.Intersection  | 【交集】         | 取两个矢量的交集                         |
| [Reproject](../vesp/Reproject.html)     | gma.vesp.Reproject     | 【重投影】       | 将矢量数据从一种坐标系投影到另一种坐标系                       |
| [Simplify](../vesp/Simplify.html) <Badge text="1.0.6 +"/> | gma.math.Simplify | 【简化】 | 简化矢量数据中的要素 |
| [Split](../vesp/Split.html)         | gma.vesp.Split         | 【矢量文件分解】 | 将矢量文件的每个要素拆分为单个文件       |
| [SymDifference](../vesp/SymDifference.html) <Badge text="1.0.4 +"/>    | gma.vesp.SymDifference    | 【交集取反】       | 取两个矢量不相交的部分                       |
| [ToOtherFormat](../vesp/ToOtherFormat.html) | gma.vesp.ToOtherFormat | 【格式转换】     | 一种矢量格式转换为另一种矢量格式         |
| [ToRaster](../vesp/ToRaster.html)      | gma.vesp.ToRaster      | 【矢量转栅格】   | 将矢量图层转换为栅格文件                 |
| [Union](../vesp/Union.html)         | gma.vesp.Union         | 【融合】         | 取两个矢量的并集                         |
| [Update](../vesp/Update.html)        | gma.vesp.Update        | 【更新】         | 用一个矢量更新另一个矢量                 |

## 高级配置 <Badge text="1.0.7 +"/>

| 函数 / *类*                                                  | 引用（简版）                        | 说明                   | 解释                                   |
| :----------------------------------------------------------- | :---------------------------------- | :--------------------- | :------------------------------------- |
| [GetRACreationOption](../config/GetRACreationOption.html) | gma.config.GetRACreationOption      | 【栅格创建选项】       | 获取栅格驱动格式支持的高级创建选项     |
| [GetVELayerCreationOption](../config/GetVELayerCreationOption.html) | gma.config.GetVELayerCreationOption | 【矢量图层创建选项】   | 获取矢量驱动格式支持的图层高级创建选项 |
| ***[GetRasterFormat](../config/GetRasterFormat.html)*** | *gma.config.GetRasterFormat*        | *【获取栅格格式】*     | *实现针对某一栅格驱动详细信息的获取*   |
| ***[GetVectorFormat](../config/GetVectorFormat.html)*** | *gma.config.GetVectorFormat*        | *【获取矢量格式】*     | *实现针对某一矢量驱动详细信息的获取*   |
| ***[RasterFormatInfo](../config/RasterFormatInfo.html)*** | *gma.config.RasterFormatInfo*       | *【栅格驱动格式信息】* | *获取所有栅格驱动格式分类的详细信息*   |
| ***[VectorFormatInfo](../config/VectorFormatInfo.html)*** | *gma.config.VectorFormatInfo*       | *【矢量驱动格式信息】* | *获取所有矢量驱动格式分类的详细信息*   |



## 其他函数 <Badge text="1.0.6 +"/>

| 函数                               | 引用（简版） | 说明         | 解释                                                         |
| :--------------------------------- | :----------- | :----------- | :----------------------------------------------------------- |
| [Open](../other/Open.html) | gma.Open     | 【打开文件】 | 打开栅格或矢量数据文件。*栅格或矢量数据支持的 方法/属性 详见：[打开数据](Function.html#打开数据)* |

#### **打开数据**

&emsp;&emsp;gma 对打开的矢量/栅格数据提供常用的方法和属性，不同数据集的说明和统计见下表：

| 类型         | 标识                              | 标记 | 来源                                  | 功能数量 |
| :------------ | :-------------------------------- | :--- | :------------------------------------ | :------- |
| [栅格数据集](../other/RasterOpen.html)   | <gma.algorithm.dataio.RasterOpen> | 类   | gma.Open(栅格数据)                    | 15       |
| [矢量数据集](../other/VectorOpen.html)   | <gma.algorithm.dataio.VectorOpen> | 类   | gma.Open(矢量数据)                    | 5        |
| [矢量图层](../other/Layer.html)     | <gma.algorithm.dataio.Layer>      | 子类 | gma.Open(矢量数据).GetLayer(图层序号) | 6        |
| 子数据集列表 | []                                | 列表 | gma.Open(具有子数据集的多维数据)      | -        |

#### 栅格数据集支持的方法/属性

| 功能                                                     | 引用                     | 标记 | 功能                 | 详细解释                    |
| :------------------------------------------------------- | :----------------------- | :--- | :------------------- | :-------------------------- |
| [Bands](../other/RasterOpen.html#bands)                     | gma.Open.Bands           | 属性 | 【波段数】           | 获取栅格波段数              |
| [Columns](../other/RasterOpen.html#columns)                 | gma.Open.Columns         | 属性 | 【列数】             | 获取栅格列数（X）           |
| [DataType](../other/RasterOpen.html#datatype)               | gma.Open.DataType        | 属性 | 【数据类型】         | 获取栅格数据的数据类型      |
| [Driver](../other/RasterOpen.html#driver)                   | gma.Open.Drive           | 属性 | 【栅格驱动】         | 获取栅格数据驱动            |
| [GeoTransform](../other/RasterOpen.html#geotransform)       | gma.Open.GeoTransform    | 属性 | 【仿射变换】         | 获取栅格仿射变换            |
| [GetBand](../other/RasterOpen.html#getband-band)                 | gma.Open.GetBand         | 方法 | 【获取 Band】        | 将某一波段转到 gdal.Band    |
| [GetBandMetadata](../other/RasterOpen.html#getbandmetadata) | gma.Open.GetBandMetadata | 方法 | 【波段元数据】       | 获取某一波段的元数据        |
| [GetBandToArray](../other/RasterOpen.html#getbandtoarray-band)   | gma.Open.GetBandToArray  | 方法 | 【转换波段为数组】   | 将某一波段读取为 Numpy 数组 |
| [GetGDALDataset](../other/RasterOpen.html#getgdaldataset)   | gma.Open.GetGDALDataset  | 方法 | 【获取 GDALDataset】 | 转到 gdal.GDALDataset       |
| [Info](../other/RasterOpen.html#info)                       | gma.Open.Info            | 属性 | 【栅格信息】         | 获取栅格信息                |
| [Metadata](../other/RasterOpen.html#metadata)               | gma.Open.Metadata        | 属性 | 【元数据】           | 获取栅格元数据              |
| [NoData](../other/RasterOpen.html#nodata)                   | gma.Open.NoData          | 属性 | 【无效值】           | 获取栅格无效值              |
| [Projection](../other/RasterOpen.html#projection)           | gma.Open.Projection      | 属性 | 【坐标系/投影】      | 获取栅格坐标系/投影         |
| [Rows](../other/RasterOpen.html#rows)                       | gma.Open.Rows            | 属性 | 【行数】             | 获取栅格行数（Y）           |
| [ToArray](../other/RasterOpen.html#toarray-leftrow-0-leftcolumn-0-rowsize-none-columnsize-none-bandlist-none)                 | gma.Open.ToArray         | 方法 | 【转为数组】         | 将栅格数据读取为 Numpy 数组 |

#### 矢量数据集支持的方法/属性

| 功能                                                       | 引用                      | 标记 | 功能                | 详细解释                   |
| :--------------------------------------------------------- | :------------------------ | :--- | :------------------ | :------------------------- |
| [Driver](../other/VectorOpen.html#driver)                   | gma.Open.Drive            | 属性 | 【矢量驱动】        | 获取矢量数据驱动           |
| [GetLayer](../other/VectorOpen.html#getlayer-id)                 | gma.Open.GetLayer         | 方法 | 【打开图层】        | 打开某一图层               |
| [GetOGRDataSource](../other/VectorOpen.html#getogrdatasource) | gma.Open.GetOGRDataSource | 方法 | 【获取 DataSource】 | 转到 ogr.DataSource        |
| [LayerCount](../other/VectorOpen.html#layercount)             | gma.Open.LayerCount       | 属性 | 【图层数】          | 获取矢量数据的图层数量     |
| [LayerNames](../other/VectorOpen.html#layernames)             | gma.Open.LayerNames       | 属性 | 【图层名】          | 获取矢量数据每个图层的名称 |

#### 矢量图层支持的方法/属性

| 功能                                                         | 引用                         | 标记 | 功能             | 详细解释                     |
| :----------------------------------------------------------- | :--------------------------- | :--- | :--------------- | :--------------------------- |
| [Boundary](../other/Layer.html#boundary)                   | ..GetLayer.Boundary          | 属性 | 【四至边界】     | 获取图层的左、右、下、上边界 |
| [FeatureCount](../other/Layer.html#featurecount)           | ..GetLayer.FeatureCount      | 属性 | 【要素数】       | 获取图层要素的数量           |
| [FieldDataTypes](../other/Layer.html#fielddatatypes)       | ..GetLayer.FieldDataTypes    | 属性 | 【字段数据类型】 | 获取属性表字段名数据类型     |
| [FieldNames](../other/Layer.html#fieldnames)               | ..GetLayer.FieldNames        | 属性 | 【字段名】       | 获取属性表字段名             |
| [GetAttributeTable](../other/Layer.html#getattributetable) | ..GetLayer.GetAttributeTable | 方法 | 【获取属性表】   | 获取图层属性表               |
| [Projection](../other/Layer.html#projection)             | ..GetLayer.Projection        | 属性 | 【坐标系/投影】  | 获取图层坐标系/投影          |