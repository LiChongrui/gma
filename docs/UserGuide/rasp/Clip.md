---
title: Clip
date: 2021-10-30
sidebar: false
---

## gma.rasp.**Clip**(*InFile, OutFile, CutLineFile, LayerID = 0, FeatureID = None, InNoData = None, OutNoData = None, OutFormat = 'GTiff'*)

---

**功能：**【裁剪】。按矢量边界裁剪栅格。

**参数：** 

&emsp;InFile：`str`。输入栅格路径。

&emsp;OutFile：`str`。输出栅格路径。

&emsp;CutLineFile：`str`。裁剪矢量文件路径。

**可选参数：**

&emsp;LayerID = `int` <Badge text="1.0.7 +"/> 。输入裁剪矢量的图层 ID。默认第一个图层（0）。

&emsp;FeatureID = `list` <Badge text="1.0.7 +"/> 。掩膜图层的要素 ID。默认掩膜全部要素（None）。

&emsp;InNoData = `float`。输入栅格的无效值。默认不指定（None）无效值。

&emsp;OutNoData  = `float`。输出栅格的无效值。默认不指定（None）无效值。

&emsp;OutFormat  = `str`。输出栅格文件格式。默认为 GTiff，其他格式详见 ToOtherFormat 函数。

---

**示例：**

>**栅格数据：** ESA 2020年陆表覆盖数据<br>
>**矢量数据：** 河南省18个地级行政单位矢量边界

```python
import gma
InFile = r'.\0.1原始影像\ESA_Henan_2020.tif'
CutLineFile = r'.\0.2原始矢量\Henan_City.shp'
```

*按矢量全范围裁剪*
```python
# 定义裁剪结果路径并执行裁剪，并为边界外数据分配无数据值
OutFile = r'.\Clip\ESA_Henan_2020_Clip.tif'
gma.rasp.Clip(InFile, OutFile, CutLineFile, OutNoData = 0)
```

*按矢量中某个要素裁剪*

```python
# 获取矢量属性表，确定要素 ID
VEDataSet = gma.Open(CutLineFile)
LY = VEDataSet.GetLayer(0)
ATable = LY.GetAttributeTable()
# 查看前三个要素
print(ATable[:3])
```
|    |   省代码 | 省     |   市代码 | 市       | 类型     |
|---:|---------:|:-------|---------:|:---------|:---------|
|  0 |   410000 | 河南省 |   410100 | 郑州市   | 地级市   |
|  1 |   410000 | 河南省 |   410200 | 开封市   | 地级市   |
|  2 |   410000 | 河南省 |   410300 | 洛阳市   | 地级市   |

&emsp;&emsp;我们裁剪河南省洛阳市，其 FeatureID 为 2，配置参数如下：

```python
OutFileFID = r'.\Clip\ESA_Henan_2020_Clip_FID2.tif'
gma.rasp.Clip(InFile, OutFileFID, CutLineFile, FeatureID = [2], OutNoData = 0)
```
> 原始数据与裁剪结果：

![](/rasp/Clip.webp)

