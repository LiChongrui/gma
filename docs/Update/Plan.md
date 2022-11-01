---
title: 更新预览
date: 2022-11-13
sidebar: false
---

&emsp;　更新预览中的新内容将在下一个 gma 版本中发布。下一版本 **1.1.0** 。

---

<font color="#3CB371"><i class="fab fa-superpowers"></i></font> **优化：**

&emsp;　1、smc

&emsp;　　a. 调整坐标点的设置方式为（经度，纬度），*以前为 （纬度，经度）*，以符合大多数人的使用习惯。

&emsp;　　b. 改用半正矢公式（haversine equation）进行空间计算。

&emsp;　2、MKMutationTest

&emsp;　　根据《现代气候统计诊断与预测技术》优化检验过程逻辑。

&emsp;　3、Open

&emsp;　　重构并完善数据读取操作。

&emsp;　　a. DataSet：添加 Metadata（元数据） 属性。

&emsp;　　b. Layer：添加 GeomType（几何类型）、 Metadata（元数据）、FieldsInfo（字段信息）属性，移除 FieldDataTypes、FieldNames 属性，相关信息合并至 FieldsInfo 。增加 GetFeature（获取要素） 方法。

&emsp;　　c. Feature：新增 Feature 类。添加 Area（面积）、 Fields（属性表字段）、GeometryCount（几何数量）、Length（长度）、Points（折点坐标） 属性。

&emsp;　　d. DataSource：移除了必要性不大的 GetBand、GetBandMetadata、GetBandToArray 方法。

<font color="#616AE5"><i class="fas fa-award"></i></font> **新增：**

&emsp;　1、增加【[IDW](/UserGuide/smc/Interpolate/IDW.html)】函数

&emsp;　　基于反距离权重（IDW） 法的点数据空间插值。引用：gma.smc.Interpolate.IDW。

&emsp;　2、增加【[CALArea](/UserGuide/smc/CALArea.html)】函数

&emsp;　　计算面积。计算输入多点组成多边形的面积。引用：gma.smc.CALArea。

&emsp;　3、增加【[NaturalNeighbor](/UserGuide/smc/Interpolate/NaturalNeighbor.html)】函数

&emsp;　　基于自然邻域（NaturalNeighbor）法的点数据空间插值。引用：gma.smc.Interpolate.NaturalNeighbor。

&emsp;　4、增加【[Trend](/UserGuide/smc/Interpolate/Trend.html)】函数

&emsp;　　基于趋势面法（Trend）（全局多项式插值法）的点数据空间插值。引用：gma.smc.Interpolate.Trend。

&emsp;　5、增加【[BSpline](/UserGuide/smc/Interpolate/BSpline.html)】函数

&emsp;　　基于 B-样条函数法（BSpline）的点数据空间插值。引用：gma.smc.Interpolate.BSpline。

&emsp;　6、增加【[Kriging](/UserGuide/smc/Interpolate/Kriging.html)】函数

&emsp;　　基于 克里金法（Ordinary Kriging 或 Universal Kriging）的点数据空间插值。引用：gma.smc.Interpolate.Kriging。

<font color="#FFA500"><i class="fas fa-tools"></i></font> **重大修复**

&emsp;　1、rsvi

&emsp;　　修复一个重大问题，该问题导致 rsvi 下所有函数均无法正常调用！

