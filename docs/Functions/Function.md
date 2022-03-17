---
title: 函数列表
date: 2021-10-29
---

**&emsp;&emsp;函数列表** 列出了 gma 包含的所有可用函数定义和说明，**可以快速了解所有的函数和功能**。如果你需要详细的函数参数说明，请在 Python 中使用 ```help``` 获取函数帮助或移步 [使用指南](/UserGuide/index.html)。

&emsp;&emsp;除了初版构建的函数之外，其他版本构建的函数会增加版本 <Badge text="标记"/>  。

&emsp;&emsp;截止 **1.0.6**  版本，各个模块的 **函数数量统计** 如下表：

|中文名|指数运算|数学运算|系统交互|空间杂项|栅格处理|矢量处理|其他函数|  合计|
|:-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----:| :-----:|------- |
| 对应模块名 | index | math | osf | smc | rasp | vesp| * | 6|
|函数/方法 数量|6|12|8|2|17|13|1| 59 |

## 指数运算

 函数 | 引用（简版）| 功能 | 详细解释                          
 :----- | :----- | :----- | :-----
[EVI](/UserGuide/indexc.html#evi) | gma.index.EVI     | 【EVI】     | 增强植被指数                      
[NDBI](/UserGuide/indexc.html#ndbi)| gma.index.NDBI    | 【NDBI】    | 归一化建筑指数                    
[NDWI](/UserGuide/indexc.html#ndwi)  | gma.index.NDWI    | 【NDWI】    | 归一化水指数                      
[NDVI](/UserGuide/indexc.html#ndvi) | gma.index.NDVI    | 【NDVI】    | 归一化植被指数                    
[PM_ET0](/UserGuide/indexc.html#pm-et0) | gma.index.PM_ET0 | 【PM_ET0】 | 基于 FAO-56 推荐的 Penman-Monteith 法计算作物参考蒸散量（ET0） 
[TVDI](/UserGuide/indexc.html#tvdi) <Badge text="1.0.2 +"/> | gma.index.TVDI    | 【TVDI】    | 温度植被干旱指数                  

 ## 数学运算

| （类）函数          | 引用（简版）                     | 功能               | 详细解释                                                     |
| :------------------ | :------------------------------- | :----------------- | :----------------------------------------------------------- |
| [ToNumericArray](/UserGuide/math.html#tonumericarray) <Badge text="1.0.6 +"/>      | gma.math.ToNumericArray         | 【转换为数字型数组】 | 强制将输入数据转为数字型数组 |
| [FillNoData](/UserGuide/math.html#fillnodata)          | gma.math.FillNoData            | 【填充缺失值】     | 对缺失值或异常值值进行插值替换                               |
| [**Smooth.**](/UserGuide/math.html#smooth-类)[SavitzkyGolay](/UserGuide/math.html#savitzkygolay)             | gma.math.Smooth.SavitzkyGolay | 【SavitzkyGolay】  | 利用SavitzkyGolay方法对数据进行平滑                          |
| [**Smooth.**](/UserGuide/math.html#smooth-类)[MovingAverage](/UserGuide/math.html#movingaverage)       | gma.math.Smooth.MovingAverage | 【滑动平均】       | 利用滑动平均法对数据进行平滑                                 |
| [**Evaluation.**](/UserGuide/math.html#evaluation-类)[RMSE](/UserGuide/math.html#rmse)    | gma.math.Evaluation.RMSE      | 【RMSE】           | 均方根误差                                                   |
| [**Evaluation.**](/UserGuide/math.html#evaluation-类)[NRMSE](/UserGuide/math.html#nrmse)   | gma.math.Evaluation.NRMSE     | 【NRMSE】          | 归一化均方根误差                                             |
| [**Evaluation.**](/UserGuide/math.html#evaluation-类)[D](/UserGuide/math.html#d)       | gma.math.Evaluation.D         | 【D】              | D指标                                                        |
| [**Evaluation.**](/UserGuide/math.html#evaluation-类)[CORR](/UserGuide/math.html#corr)       | gma.math.Evaluation.CORR         | 【r，P】           | 相关系数和显著性水平                                         |
| [**Evaluation.**](/UserGuide/math.html#evaluation-类)[R2](/UserGuide/math.html#r2)      | gma.math.Evaluation.R2        | 【R2】             | 决定系数                                                     |
| [**Evaluation.**](/UserGuide/math.html#evaluation-类)[MaxAE](/UserGuide/math.html#maxae)   | gma.math.Evaluation.MaxAE     | 【MaxAE】          | 最大绝对误差                                                 |
| [**Evaluation.**](/UserGuide/math.html#evaluation-类)[Select](/UserGuide/math.html#select)  | gma.math.Evaluation.Select    | 【选择方法】       | 选择Evaluation中需要计算的一个或多个评价指标进行计算         |
| [**Evaluation.**](/UserGuide/math.html#evaluation-类)[Methods](/UserGuide/math.html#methods) | gma.math.Evaluation.Methods   | 【记录方法】       | 记录Evaluation类中所有的评估方法                             |

 ## 系统交互

| （类）函数       | 引用（简版）                | 功能         | 详细解释                                         |
| :--------------- | :-------------------------- | :----------- | :----------------------------------------------- |
| [GetPath](/UserGuide/osf.html#getpath)          | gma.osf.GetPath           | 【获取路径】 | 获取目标路径或路径集合下满足条件的所有文件夹和文件路径                              |
| [Zip](/UserGuide/osf.html#zip)            | gma.osf.Zip               | 【压缩】     | 将目标路径下所有文件压缩为 .zip 文件                  |
| [UnZip](/UserGuide/osf.html#unzip)            | gma.osf.UnZip             | 【解压缩】   | 解压缩 .zip 文件                                |
| [DateSeries](/UserGuide/osf.html#dateseries)       | gma.osf.DateSeries        | 【日期序列】 | 构造一个日期序列列表                               |
| [**Modify.**](/UserGuide/osf.html#rename-类)[Rename](/UserGuide/osf.html#modify)    | gma.osf.Rename.Modify    | 【修改】     | 将原有文件（夹）名修改为新名                     |
| [**Modify.**](/UserGuide/osf.html#rename-类)[Replace](/UserGuide/osf.html#replace)  | gma.osf.Rename.Replace   | 【替换】     | 替换原文件（夹）名中字符串后作为新文件（夹）名   |
| [**Modify.**](/UserGuide/osf.html#rename-类)[Intercept](/UserGuide/osf.html#intercept) | gma.osf.Rename.Intercept | 【截取】     | 截取文件（夹）名中的部分字符串作为新文件（夹）名 |
| [MultiThreading](/UserGuide/osf.html#multithreading)<Badge text="1.0.3 +"/> | gma.osf.MultiThreading | 【多线程】 | 创建多个线程，实现同一函数多个参数的同步执行 |

 ## 空间杂项

| 函数 | 引用（简版）| 功能 | 详细解释|
| :----- | :----- | :----- | :-----|
|[CALDistance](/UserGuide/smc.html#caldistance)<Badge text="1.0.5 +"/> | gma.smc.CALDistance |【计算距离】|计算输入两点或多点之间依次连接后的总距离|
|[TRANCoordinate](/UserGuide/smc.html#trancoordinate)<Badge text="1.0.5 +"/> | gma.smc.TRANCoordinate |【坐标转换】|将输入点的坐标转换为目标坐标系下的坐标|

 ## 栅格处理

| （类）函数                                                   | 引用（简版）                  | 功能                | 详细解释                                                     |
| :----------------------------------------------------------- | :---------------------------- | :------------------ | :----------------------------------------------------------- |
| [BandSynthesis](/UserGuide/rasp.html#bandsynthesis)               | gma.rasp.BandSynthesis        | 【文件合并】        | 单波段文件合成多波段文件                                     |
| [BandDecomposition](/UserGuide/rasp.html#banddecomposition)       | gma.rasp.BandDecomposition    | 【波段分解】        | 将多波段文件拆分（或提取）为单波段文件                       |
| [Clip](/UserGuide/rasp.html#clip)                                 | gma.rasp.Clip                 | 【裁剪】            | 按矢量边界裁剪栅格                                           |
| [ToOtherFormat](/UserGuide/rasp.html#tootherformat)               | gma.rasp.ToOtherFormat        | 【格式转换】        | 一种栅格格式转换为另一种栅格格式                             |
| [Mosaic](/UserGuide/rasp.html#mosaic)                             | gma.rasp.Mosaic               | 【栅格镶嵌】        | 将多个栅格数据集合并到一个新的栅格数据集中                   |
| [Resample](/UserGuide/rasp.html#resample)                         | gma.rasp.Resample             | 【重采样】          | 更改栅格数据的空间分辨率                                     |
| [Reproject](/UserGuide/rasp.html#reproject)                       | gma.rasp.Reproject            | 【重投影】          | 将空间数据从一种坐标系投影到另一种坐标系                     |
| [ChangeDataType](/UserGuide/rasp.html#changedatatype)             | gma.rasp.ChangeDataType       | 【数据类型转换】    | 转换栅格数据的数据类型                                       |
| [MultiSDSToTif](/UserGuide/rasp.html#multisdstotif)               | gma.rasp.MultiSDSToTif        | 【多维数据转GTiff】 | 将含有子数据集的多维数据提取为 GTiff                         |
| [ToVector](/UserGuide/rasp.html#tovector)                        | gma.rasp.ToVector             | 【栅格转矢量】      | 将栅格数据转换为矢量数据                                     |
| [WriteRaster](/UserGuide/rasp.html#writeraster)                  | gma.rasp.WriteRaster          | 【写出栅格】        | 将数组保存为栅格                                             |
| [GenerateOVR](/UserGuide/rasp.html#generateovr)                  | gma.rasp.GenerateOVR          | 【构建栅格金字塔】  | 为GTiff文件构造 .ovr 栅格金字塔，或为其他类型的栅格数据强制构造.ovr金字塔 |
| [OrthophotoCorrection](/UserGuide/rasp.html#orthophotocorrection) | gma.rasp.OrthophotoCorrection | 【正射矫正】        | 根据有理多项式系数（RPC）对影像进行正射校正                  |
| [Deformation](/UserGuide/rasp.html#deformation)                  | gma.rasp.Deformation          | 【流程化处理】      | 完成镶嵌-裁剪-重采样-重投影-格式转换等其中一个或多个功能     |
| [**Fusion.**](/UserGuide/rasp.html#fusion-类)[Pansharpen](/UserGuide/rasp.html#pansharpen) | gma.rasp.Fusion.Pansharpen    | 【Pansharpen】      | 对全色影像和多光谱影像基于Pansharpen方法进行融合             |
| [AddColorTable](/UserGuide/rasp.html#addcolortable)<Badge text="1.0.1 +"/> | gma.rasp.AddColorTable        | 【添加色彩映射表】  | 为栅格数据添加色彩映射                                       |
| [SplitImage](/UserGuide/rasp.html#splitimage)<Badge text="1.0.3 +"/> | gma.rasp.SplitImage           | 【影像切片】        | 将一幅影像切分为特定行列数的小影像。                         |

## 矢量处理

| 函数    | 引用（简版）             | 说明             | 解释                                     |
| :------------ | :----------------------- | :--------------- | :--------------------------------------- |
| [Split](/UserGuide/vesp.html#split)         | gma.vesp.Split         | 【矢量文件分解】 | 将矢量文件的每个要素拆分为单个文件       |
| [Check](/UserGuide/vesp.html#check)         | gma.vesp.Check         | 【检查】         | 检查每个矢量要素的有效性                       |
| [ToRaster](/UserGuide/vesp.html#toraster)      | gma.vesp.ToRaster      | 【矢量转栅格】   | 将矢量图层转换为栅格文件                 |
| [Clip](/UserGuide/vesp.html#clip)          | gma.vesp.Clip          | 【裁剪】         | 矢量裁剪矢量                             |
| [Erase](/UserGuide/vesp.html#erase)         | gma.vesp.Erase         | 【擦除】         | 从第一个矢量中去除与第二个矢量交叉的部分 |
| [Intersection](/UserGuide/vesp.html#intersection)  | gma.vesp.Intersection  | 【交集】         | 取两个矢量的交集                         |
| [Union](/UserGuide/vesp.html#union)         | gma.vesp.Union         | 【融合】         | 取两个矢量的并集                         |
| [Update](/UserGuide/vesp.html#update)        | gma.vesp.Update        | 【更新】         | 用一个矢量更新另一个矢量                 |
| [ToOtherFormat](/UserGuide/vesp.html#tootherformat) | gma.vesp.ToOtherFormat | 【格式转换】     | 一种矢量格式转换为另一种矢量格式         |
| [Reproject](/UserGuide/vesp.html#reproject)     | gma.vesp.Reproject     | 【重投影】       | 将矢量数据从一种坐标系投影到另一种坐标系                       |
| [SymDifference](/UserGuide/vesp.html#symdifference) <Badge text="1.0.4 +"/>    | gma.vesp.SymDifference    | 【交集取反】       | 取两个矢量不相交的部分                       |
| [Simplify](/UserGuide/vesp.html#simplify)<Badge text="1.0.6 +"/> | gma.math.Simplify | 【简化】 | 简化矢量数据中的要素 |
| [FixGeometry<Badge text="1.0.6 +"/>](/UserGuide/vesp.html#fixgeometry) | gma.math.FixGeometry | 【修正几何】 | 修正矢量数据中无效的几何要素 |

## 其他函数<Badge text="1.0.6 +"/>

| 函数                               | 引用（简版） | 说明         | 解释                                                         |
| :--------------------------------- | :----------- | :----------- | :----------------------------------------------------------- |
| [Open](/UserGuide/other.html#open) | gma.Open     | 【打开文件】 | 打开栅格或矢量数据文件。*栅格或矢量数据支持的 方法/属性 详见：[打开数据](Function.html#打开数据)* |

#### **打开数据**

&emsp;&emsp;gma 对打开的矢量/栅格数据提供常用的方法和属性，不同数据集的说明和统计见下表：

| 类型         | 标识                              | 标记 | 来源                                  | 功能数量 |
| :------------ | :-------------------------------- | :--- | :------------------------------------ | :------- |
| 栅格数据集   | <gma.algorithm.dataio.RasterOpen> | 类   | gma.Open(栅格数据)                    | 15       |
| 矢量数据集   | <gma.algorithm.dataio.VectorOpen> | 类   | gma.Open(矢量数据)                    | 5        |
| 矢量图层     | <gma.algorithm.dataio.Layer>      | 子类 | gma.Open(矢量数据).GetLayer(图层序号) | 6        |
| 子数据集列表 | []                                | 列表 | gma.Open(具有子数据集的多维数据)      | -        |

栅格数据集支持的方法/属性

| 功能                                                     | 引用                     | 标记 | 功能                 | 详细解释                    |
| :------------------------------------------------------- | :----------------------- | :--- | :------------------- | :-------------------------- |
| [Bands](/UserGuide/other.html#bands)                     | gma.Open.Bands           | 属性 | 【波段数】           | 获取栅格波段数              |
| [Columns](/UserGuide/other.html#columns)                 | gma.Open.Columns         | 属性 | 【列数】             | 获取栅格列数（X）           |
| [Rows](/UserGuide/other.html#rows)                       | gma.Open.Rows            | 属性 | 【行数】             | 获取栅格行数（Y）           |
| [ToArray](/UserGuide/other.html#toarray)                 | gma.Open.ToArray         | 方法 | 【转为数组】         | 将栅格数据读取为 Numpy 数组 |
| [DataType](/UserGuide/other.html#datatype)               | gma.Open.DataType        | 属性 | 【数据类型】         | 获取栅格数据的数据类型      |
| [Driver](/UserGuide/other.html#driver)                   | gma.Open.Drive           | 属性 | 【栅格驱动】         | 获取栅格数据驱动            |
| [GeoTransform](/UserGuide/other.html#geotransform)       | gma.Open.GeoTransform    | 属性 | 【仿射变换】         | 获取栅格仿射变换            |
| [GetBand](/UserGuide/other.html#getband)                 | gma.Open.GetBand         | 方法 | 【获取 Band】        | 将某一波段转到 gdal.Band    |
| [GetBandToArray](/UserGuide/other.html#getbandtoarray)   | gma.Open.GetBandToArray  | 方法 | 【转换波段为数组】   | 将某一波段读取为 Numpy 数组 |
| [GetGDALDataset](/UserGuide/other.html#getgdaldataset)   | gma.Open.GetGDALDataset  | 方法 | 【获取 GDALDataset】 | 转到 gdal.GDALDataset       |
| [NoData](/UserGuide/other.html#nodata)                   | gma.Open.NoData          | 属性 | 【无效值】           | 获取栅格无效值              |
| [Projection](/UserGuide/other.html#projection)           | gma.Open.Projection      | 属性 | 【坐标系/投影】      | 获取栅格坐标系/投影         |
| [Info](/UserGuide/other.html#info)                       | gma.Open.Info            | 属性 | 【栅格信息】         | 获取栅格信息                |
| [Metadata](/UserGuide/other.html#metadata)               | gma.Open.Metadata        | 属性 | 【元数据】           | 获取栅格元数据              |
| [GetBandMetadata](/UserGuide/other.html#getbandmetadata) | gma.Open.GetBandMetadata | 方法 | 【波段元数据】       | 获取某一波段的元数据        |

矢量数据集支持的方法/属性

| 功能                                                       | 引用                      | 标记 | 功能                | 详细解释                   |
| :--------------------------------------------------------- | :------------------------ | :--- | :------------------ | :------------------------- |
| [Driver](/UserGuide/other.html#driver-2)                   | gma.Open.Drive            | 属性 | 【矢量驱动】        | 获取矢量数据驱动           |
| [LayerCount](/UserGuide/other.html#layercount)             | gma.Open.LayerCount       | 属性 | 【图层数】          | 获取矢量数据的图层数量     |
| [LayerNames](/UserGuide/other.html#layernames)             | gma.Open.LayerNames       | 属性 | 【图层名】          | 获取矢量数据每个图层的名称 |
| [GetLayer](/UserGuide/other.html#getlayer)                 | gma.Open.GetLayer         | 方法 | 【打开图层】        | 打开某一图层               |
| [GetOGRDataSource](/UserGuide/other.html#getogrdatasource) | gma.Open.GetOGRDataSource | 方法 | 【获取 DataSource】 | 转到 ogr.DataSource        |

栅格图层支持的方法/属性

| 功能                                                         | 引用                         | 标记 | 功能             | 详细解释                     |
| :----------------------------------------------------------- | :--------------------------- | :--- | :--------------- | :--------------------------- |
| [FeatureCount](/UserGuide/other.html#featurecount)           | ..GetLayer.FeatureCount      | 属性 | 【要素数】       | 获取图层要素的数量           |
| [Projection](/UserGuide/other.html#projection-2)             | ..GetLayer.Projection        | 属性 | 【坐标系/投影】  | 获取图层坐标系/投影          |
| [Boundary](/UserGuide/other.html#boundary)                   | ..GetLayer.Boundary          | 属性 | 【四至边界】     | 获取图层的左、右、下、上边界 |
| [GetAttributeTable](/UserGuide/other.html#getattributetable) | ..GetLayer.GetAttributeTable | 方法 | 【获取属性表】   | 获取图层属性表               |
| [FieldNames](/UserGuide/other.html#fieldnames)               | ..GetLayer.FieldNames        | 属性 | 【字段名】       | 获取属性表字段名             |
| [FieldDataTypes](/UserGuide/other.html#fielddatatypes)       | ..GetLayer.FieldDataTypes    | 属性 | 【字段数据类型】 | 获取属性表字段名数据类型     |
