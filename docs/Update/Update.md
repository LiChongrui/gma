---
title: 更新日志
date: 2021-11-21
---

## 1.0.7 (2022.04.17)
---

::: warning 注意

自 <Badge text="1.0.7" vertical='middle'/>  版本开始，gma 内各个函数生成 GTiff 文件时 **不在默认** 生成 .ovr 金字塔。

:::

<i class="fas fa-box"></i> **引入 [raa](/UserGuide/Function.html#栅格分析) 函数包。** 提供栅格数据分析功能！

<i class="fas fa-box"></i> **引入 [config](/UserGuide/Function.html#高级配置) 函数包。** 提供栅格高级参数配置查询功能！

<font color="#616AE5"><i class="fas fa-award"></i></font> **新增：**

&emsp;　1、增加【[Roughness](/UserGuide/raa/DEM/Roughness.html)】函数

&emsp;　　从任何支持的 DEM 栅格文件计算粗糙度！引用：gma.raa.DEM.Roughness。

&emsp;　2、增加【[HillShade](/UserGuide/raa/DEM/HillShade.html)】函数

&emsp;　　从任何支持的 DEM 栅格文件计算山体阴影！引用：gma.raa.DEM.HillShade。

&emsp;　3、增加【[Slope](/UserGuide/raa/DEM/Slope.html)】函数

&emsp;　　从任何支持的 DEM 栅格文件计算坡度！引用：gma.raa.DEM.Slope。

&emsp;　4、增加【[Aspect](/UserGuide/raa/DEM/Aspect.html)】函数

&emsp;　　从任何支持的 DEM 栅格文件计算坡向！引用：gma.raa.DEM.Aspect。

&emsp;　5、增加【[TRI](/UserGuide/raa/DEM/TRI.html)】函数

&emsp;　　从任何支持的 DEM 栅格文件计算地形耐用度指数！引用：gma.raa.DEM.TRI。

&emsp;　6、增加【[TPI](/UserGuide/raa/DEM/TPI.html)】函数

&emsp;　　从任何支持的 DEM 栅格文件计算地形位置指数！引用：gma.raa.DEM.TPI。

&emsp;　7、增加【[GetRACreationOption](/UserGuide/config/GetRACreationOption.html)】函数

&emsp;　　获取栅格驱动格式支持的高级创建选项！引用：gma.config.GetRACreationOption。

&emsp;　8、增加【[GetRasterFormat](/UserGuide/config/GetRasterFormat.html)】类

&emsp;　　实现针对某一栅格驱动详细信息的获取！引用：gma.config.GetRasterFormat。类支持的属性包括：

&emsp;　　a. ColorTableDataType： 色彩映射表支持的数据类型。

&emsp;　　b. CompressMode：支持的压缩方式。

&emsp;　　c. CreationDataType：支持创建的数据类型。

&emsp;　　d. Details：详细信息。

&emsp;　　e. GeoReferencing：地理参考支持。

&emsp;　　f. LongName：驱动长名称。

&emsp;　　g. Multiband：多波段支持。

&emsp;　　h. Update：更新支持。

&emsp;　　i. Extension：驱动扩展名。

&emsp;　9、增加【[GetVectorFormat](/UserGuide/config/GetVectorFormat.html)】类

&emsp;　　实现针对某一矢量驱动详细信息的获取！引用：gma.config.GetVectorFormat。类支持的属性包括：

&emsp;　　a. CreationFieldDataType：支持创建属性表字段类型。

&emsp;　　b. Details：详细信息。

&emsp;　　c. Extension：驱动扩展名。

&emsp;　　d. GeoReferencing：地理参考支持。

&emsp;　　e. LongName：驱动长名称。

&emsp;　　f. MultiLayer：多图层支持。

&emsp;　　g. Update：更新支持。

&emsp;　10、增加【[GetVELayerCreationOption](/UserGuide/config/GetVELayerCreationOption.html)】函数

&emsp;　　获取矢量驱动格式支持的图层高级创建选项！引用：gma.config.GetVELayerCreationOption。

&emsp;　11、增加【[RasterFormatInfo](/UserGuide/config/RasterFormatInfo.html)】类

&emsp;　　获取所有栅格驱动格式分类的详细信息！引用：gma.config.RasterFormatInfo。类支持的属性包括：

&emsp;　　a. AddableColorTableFormats：支持色彩映射表的驱动格式。

&emsp;　　b. CompressibleFormats：支持压缩的驱动格式。

&emsp;　　c. CopyableFormats：支持复制的驱动格式。

&emsp;　　d. CreatableFormats：支持创建的驱动格式。

&emsp;　　e. MultibandFormats：支持多波段的驱动格式。

&emsp;　　f. ReadableFormats：支持读取的驱动格式。

&emsp;　　g. TransformableFormats：支持转换的驱动格式。

&emsp;　　h. UpdatableFormats：支持更新的驱动格式。

&emsp;　12、增加【[VectorFormatInfo](/UserGuide/config/VectorFormatInfo.html)】类

&emsp;　　获取所有矢量驱动格式分类的详细信息！引用：gma.config.VectorFormatInfo。类支持的属性包括：

&emsp;　　a. CopyableFormats：支持复制的驱动格式。

&emsp;　　b. CreatableFormats：支持创建的驱动格式。

&emsp;　　c. MultiLayerFormats：支持多图层的驱动格式。

&emsp;　　d. ReadableFormats：支持读取的驱动格式。

&emsp;　　e. TransformableFormats：支持转换的驱动格式。

&emsp;　　f. UpdatableFormats：支持更新的驱动格式。

<font color="#3CB371"><i class="fab fa-superpowers"></i></font> **优化：**

&emsp;　1、将 栅格/矢量 生成过程中的高级 **创建参数外置**。在未来的几个版本，栅格/矢量生成过程的高级配置参数会逐步开放设置。

&emsp;　2、基于外置的创建参数，对所有 **栅格处理函数** 进行 **第二次重构**，以实现所有的栅格处理函数在底层隶属于一个整体，而不仅仅是许多单独的函数的集合。

&emsp;　3、rasp.Clip

&emsp;　　移除 MaskBoundary 参数，增加 LayerID （掩膜矢量图层 ID）、FeatureID （掩膜图层要素 ID）参数。

&emsp;　4、rasp.GenerateOVR

&emsp;　　增加 Compress（压缩方式）、Resample（重采样方法）、BlockSize（分块大小）参数。

&emsp;　5、rasp.Fusion

&emsp;　　移除了 Fusion 类初始化参数，初始化内容合并到类内函数。

&emsp;　6、rasp.Fusion.Pansharpen

&emsp;　　承接 Fusion 初始化参数。优化内部生成逻辑，使源代码更简洁。

&emsp;　7、relation.key

&emsp;　　调整并优化了与外置的高级创建参数内容重复的内容。

&emsp;　8、vesp.FixGeometry

&emsp;　　面积或长度值小于 0.00000001 的要素将会被清除。

## 1.0.6 (2022.03.17)

---

<i class="fas fa-box"></i> **引入 [constants](/Explore/Constants.html) 常量模块。** 提供数学常量、国际单位制词头、二进制单位、长度单位、面积单位等 16 种单位的名称、值或与国际单位的代换值！

<font color="#3CB371"><i class="fab fa-superpowers"></i></font> **优化：**

&emsp;　1、FillNoData

&emsp;　　所有的插补方法支持的类型移入 key 中。（内部修改，不影响函数功能。）

&emsp;　2、TRANCoordinate

&emsp;　　优化距离计算算法。现在，即使坐标点跨度巨大，仍能准确的返回计算结果。

&emsp;　3、版本记录

&emsp;　　增加当前 gma 版本号记录。可通过 gma.\_\_version\_\_ 查看当前版本号。

&emsp;　4、Resample、ChangeDataType

&emsp;　　改进算法，提高效率。大文件处理时间缩短超过 30% 。

&emsp;　5、rasp

&emsp;　　对模块内函数进行了改造。已实现对输入栅格数据正确性的判断。

<font color="#616AE5"><i class="fas fa-award"></i></font> **新增：**

&emsp;　1、增加【[ToNumericArray](/UserGuide/math/ToNumericArray.html)】函数

&emsp;　　强制将输入数据转为数字型数组，无法转换的值将会被修改为 nan。引用：gma.math.ToNumericArray。

&emsp;　2、增加【[Simplify](/UserGuide/vesp/Simplify.html)】函数

&emsp;　　简化矢量数据中的要素。引用：gma.vesp.Simplify。

&emsp;　3、增加【[FixGeometry](/UserGuide/vesp/FixGeometry.html)】函数

&emsp;　　修正矢量数据中无效的几何要素。引用：gma.vesp.FixGeometry。

&emsp;　4、增加顶层【[Open](/UserGuide/other/Open.html)】函数

&emsp;　　以替代 gma.rasp(vesp).Open 函数（这两个函数仍可用）。引用：gma.Open。

<i class="far fa-trash-alt"></i> **移除：**

&emsp;　1、_DFToNumeric

&emsp;　　移除了 _DFToNumeric 函数，相关功能合并至 ToNumericArray 函数。

<font color="#FFA500"><i class="fas fa-tools"></i></font> **修复**

&emsp;　1、SplitImage

&emsp;　　修复了部分条件下，切片不能正常执行的问题。

&emsp;　2、ToVector

&emsp;　　修复了部分条件下，掩膜 NoData 区域异常的问题。

<font color="#FF4500"><i class="fas fa-exclamation-circle"></i></font> **已知问题：**

&emsp;　1、Float64

&emsp;　　当写出栅格的数据类型为双精度浮点数（Float64）时，数据结果可能异常。请尽量使用单精度浮点数（Float32）或半精度浮点数（Float16）来存储浮点类型的栅格数据结果！

## 1.0.5 (2022.02.10)

---

<i class="fas fa-box"></i> **增加 [smc](/UserGuide/Function.html#空间杂项) 函数包。** 提供（或未来提供）空间杂项（例如计算空间距离、面积、坐标转换等操作）计算！

<font color="#616AE5"><i class="fas fa-award"></i></font> **新增：**

&emsp;　1、增加【[CALDistance](/UserGuide/smc/CALDistance.html)】函数

&emsp;　　计算距离。计算输入两点（或多点）之间的距离。引用：gma.smc.CALDistance

&emsp;　2、增加【[TRANCoordinate](/UserGuide/smc/TRANCoordinate.html)】函数

&emsp;　　坐标转换。将输入点的坐标转换为目标坐标系的坐标。引用：gma.smc.TRANCoordinate

<font color="#3CB371"><i class="fab fa-superpowers"></i></font> **优化：**

&emsp;　1、相关系数计算函数（r）

&emsp;　　相关系数计算函数名由 r 改为 [CORR](/UserGuide/math/Evaluation/CORR.html)，并增加 pearson（皮尔逊相关）、kendall（肯德尔秩相关），spearman（斯皮尔曼相关）三种可选的相关系数计算方法。

&emsp;　2、Select

&emsp;　　参数设置错误时将会引发异常，不在默认返回 RMSE 结果。

&emsp;　3、GetPath

&emsp;　　a. 参数 String 修改为 Include，功能不变。

&emsp;　　b. 增加 Exclude 参数，用以排除包含此参数设置值的路径。

&emsp;　4、依赖包

&emsp;　　不在将 gdal 作为安装 gma 的前提。即使缺少 gdal，gma 仍可以正常安装，但无法引用。

*&emsp;　5、错误检查模块（error）*

*&emsp;　　错误检查模块由 error 修改为 initialize，增加数据初始化的内容，并对包内所有错误检查方法进行了重构。*

&emsp;　6、GenerateOVR

&emsp;　　添加 MINSize 参数，仅为文件大小大于此值的栅格文件构建金字塔。默认大小为 10 MB。

&emsp;　7、引入检查

&emsp;　　为 import gma 的过程增加检查，以方便定位引入问题。

<i class="far fa-trash-alt"></i> **移除：**

&emsp;　1、位深设置

&emsp;　　移除了 ChangeDataType 和 Pansharpen 中位深设置的相关参数。如需应用位深参数，可调用 gma.algorithm.raster 中对应的原始函数。

## 1.0.4 (2022.01.14)
---

<font color="#616AE5"><i class="fas fa-award"></i></font> **新增：**

&emsp;　1、增加【[SymDifference](/UserGuide/vesp/SymDifference.html)】函数

&emsp;　　交集取反。提取两个矢量不相交的部分组成新矢量。引用：gma.vesp.SymDifference。

<font color="#FFA500"><i class="fas fa-tools"></i></font> **修复：**

&emsp;　1、无法正常 import 

&emsp;　　分别为 Python 3.8、3.9、3.10 编译和发布对应版本的 whl 包，解决不同环境安装 gma 可能出现不能正常 import 的问题。

&emsp;　2、FillNoData

&emsp;　　修复 1.0.2 ~ 1.0.3 版本默认插值方法 `linear` 失效的问题。

&emsp;　3、MultiThreading

&emsp;　　修复 *agrs，**kwargs 传参失败的问题。

<font color="#3CB371"><i class="fab fa-superpowers"></i></font> **优化：**

&emsp;　1、坐标系检查

&emsp;　　放宽坐标系正确性的检查方式，以保证自定义坐标系可以正常引用。

<font color="#FF4500"><i class="fas fa-exclamation-circle"></i></font> **已知问题：**

&emsp;　1、ChangeDataType

&emsp;　　某些情况下，在设置了 BitDepth （位深）参数后，不能返回预期的位深结果。非必要情况下，请谨慎设置此参数。

## 1.0.3 (2021.12.16)
---

<font color="#616AE5"><i class="fas fa-award"></i></font>  **新增：**

&emsp;　1、增加【[SplitImage](/UserGuide/rasp/SplitImage.html)】函数

&emsp;　　影像切片。将一幅影像切分为特定行列数的小影像（切片）。引用：gma.rasp.SplitImage。

&emsp;　2、增加【[MultiThreading](/UserGuide/osf/MultiThreading.html)】函数

&emsp;　　多线程。自定义多线程实现同一函数多个参数的同步执行。引用：gma.osf.MultiThreading。

## 1.0.2 (2021.11.21)
---

<font color="#616AE5"><i class="fas fa-award"></i></font> **新增：**

&emsp;　1、增加【[TVDI](/UserGuide/index/TVDI.html)】函数

&emsp;　　计算温度植被干旱指数。引用：gma.index.TVDI。

<font color="#FFA500"><i class="fas fa-tools"></i></font> **修复：**

&emsp;　1、FillNoData

&emsp;　　a. 解决部分插补方法的条件下，首末端缺失值未进行处理的问题。

&emsp;　　b. 为 polynomial 和 spline 法设定了一个默认的 order ，默认值为 3 。

&emsp;　　c. 修改了部分由于拼写问题引发的异常。

<font color="#3CB371"><i class="fab fa-superpowers"></i></font> **优化：**

&emsp;　1、Smooth

&emsp;　　为输入参数的设置情况加入判断。

<i class="far fa-trash-alt"></i> **移除：**

&emsp;　1、移除了暂时未进行整合的 palmer，utils 模块。

## 1.0.1 (2021.11.18)
---

<font color="#616AE5"><i class="fas fa-award"></i></font>  **新增：**

&emsp;　1、增加【[AddColorTable](/UserGuide/rasp/AddColorTable.html)】函数

&emsp;　　为栅格数据添加色彩映射表。引用：gma.rasp.AddColorTable。

<font color="#3CB371"><i class="fab fa-superpowers"></i></font> **优化：**

&emsp;　1、GTiff 格式

&emsp;　　a. 生成 GTiff 过程使用差分预测器（若压缩支持，例如 LZW ），修改默认压缩级别为 9 级 。

&emsp;　　b. 生成 GTiff 过程调用全部 CPU 核心。

&emsp;　　c. 当读取的栅格数据未压缩大小小于系统内存时，改用 RasterIO 方法实现。

&emsp;　2、内存占用

&emsp;　　默认处理过程的最大内存占用为 **0.9 * 空闲内存**，以提高数据处理速度。

&emsp;　3、.ovr 金字塔

&emsp;　　生成 .ovr 金字塔 过程使用差分预测器（ DEFLATE 压缩）。

<font color="#FFA500"><i class="fas fa-tools"></i></font> **修复：**

&emsp;　1、修正 WKT 坐标系正确性的检查方式。


## 1.0.0 (2021.11.13)
---
&emsp;　第一版 gma 。未标注版本的函数均在第一版构建。
