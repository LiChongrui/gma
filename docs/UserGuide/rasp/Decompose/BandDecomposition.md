---
title: BandDecomposition
date: 2021-10-30
sidebar: false
---

##  gma.rasp.**BandDecomposition**(*InFile, OutPath, Bands = None, OutFormat = 'GTiff'*)
---

**功能：**【波段分解】。将多波段文件拆分（或提取）为单波段文件。

**参数：** 

&emsp;InFile：`str`。输入栅格路径。

&emsp;OutPath：`str`。输出文件夹路径。

::: tip 提示
输出文件名以 **源文件名_波段序号** 的形式自动命名。
:::

**可选参数：**

&emsp;Bands = `int||list`。需要导出文件的波段，编号从 1 开始。默认全部导出（None）。

&emsp;OutFormat  = `str`。输出栅格文件格式。默认为 GTiff，其他格式详见 ToOtherFormat 函数。

---

**示例：*****（以 PM_ET0 计算的 2020 全年 12 波段 ET0 数据为例）***

```python
import gma
InFile = 'ET0_China_ANUSPLIN_2020.tif'
OutPath = r'.\BandDecomposition'
```

*提取其中一个波段*

```python
# 提取第 2 波段数据
gma.rasp.BandDecomposition(InFile, OutPath, Bands = 2)
# 提取生成文件
gma.osf.GetPath(OutPath)
```
> \>>> '.\\BandDecomposition\\ET0_China_ANUSPLIN_2020_2.tif'

*提取所有波段*

```python
gma.rasp.BandDecomposition(InFile, OutPath, Bands = None)
# 提取生成文件
gma.osf.GetPath(OutPath)
```
> \>>> ['.\\BandDecomposition\\ET0_China_ANUSPLIN_2020_1.tif',<br>
> 　　　'.\\BandDecomposition\\ET0_China_ANUSPLIN_2020_10.tif',<br>
> 　　　'.\\BandDecomposition\\ET0_China_ANUSPLIN_2020_11.tif',<br>
> 　　　'.\\BandDecomposition\\ET0_China_ANUSPLIN_2020_12.tif',<br>
> 　　　'.\\BandDecomposition\\ET0_China_ANUSPLIN_2020_2.tif',<br>
> 　　　'.\\BandDecomposition\\ET0_China_ANUSPLIN_2020_3.tif',<br>
> 　　　'.\\BandDecomposition\\ET0_China_ANUSPLIN_2020_4.tif',<br>
> 　　　'.\\BandDecomposition\\ET0_China_ANUSPLIN_2020_5.tif',<br>
> 　　　'.\\BandDecomposition\\ET0_China_ANUSPLIN_2020_6.tif',<br>
> 　　　'.\\BandDecomposition\\ET0_China_ANUSPLIN_2020_7.tif',<br>
> 　　　'.\\BandDecomposition\\ET0_China_ANUSPLIN_2020_8.tif',<br>
> 　　　'.\\BandDecomposition\\ET0_China_ANUSPLIN_2020_9.tif']



