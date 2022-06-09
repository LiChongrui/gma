---
title: GenerateOVR
date: 2021-10-30
sidebar: false
---

## gma.rasp.**GenerateOVR**(*InFile, Force = False, MINSize = 10, Compress = 'DEFLATE', Resample = 'NEAREST', BlockSize = 128*)

---

**功能：**【构建栅格金字塔】。为 GTiff 文件构造 .ovr 栅格金字塔，或为其他类型的栅格数据强制构造 .ovr 金字塔 。

**参数：** 

&emsp;InFile：`str`。栅格文件路径。

**可选参数：**

&emsp;Force  = `bool`。是否为所有类型的文件添加 .ovr 金字塔。默认（False）只为 GTiff 驱动的栅格添加金字塔。

&emsp;MINSize = `float`。需要创建金字塔的栅格文件的最小文件大小（MB）。小于此大小的栅格文件不会被创建金字塔。默认为 10 MB。

&emsp;Compress = `str` <Badge text="1.0.7 +"/> 。金字塔文件的压缩方式。默认 DEFLATE 压缩。

::: tip 可配置的压缩方式

NONE, LZW, PACKBITS, JPEG, CCITTRLE, CCITTFAX3, CCITTFAX4, DEFLATE, LZMA, ZSTD, WEBP, LERC, LERC_DEFLATE, LERC_ZSTD

:::

&emsp;Resample = `str` <Badge text="1.0.7 +"/> 。生成金字塔文件的重采样方法。默认 NEAREST 法。

::: tip 可配置的重采样方法

AVERAGE, AVERAGE_MAGPHASE, RMS, BILINEAR, CUBIC, CUBICSPLINE, GAUSS, LANCZOS, MODE, NEAREST, NONE

:::

&emsp;BlockSize = `int` <Badge text="1.0.7 +"/> 。生成金字塔过程的块大小。默认为 128。

---

**示例：**

```python
import gma
InFile = 'NASA_SRTM_DEM_China_1000m.tif'
```

*按默认配置生成金字塔*

```python
gma.rasp.GenerateOVR(InFile)
## 查看生成的金字塔信息
gma.Open(InFile).Info['bands'][0]['overviews']
```
> \>>>[{'size': [3427, 2629]},<br>
 　　{'size': [1714, 1315]},<br>
 　　{'size': [857, 658]},<br>
 　　{'size': [429, 329]},<br>
 　　{'size': [215, 165]}]

*为其他格式强制生成 .ovr 金字塔*

```python
gma.rasp.GenerateOVR('NASA_SRTM_DEM_China_1000m.img', Force = True)
## 生成的金字塔和思路 GTiff 文件一致
```

*限定只为大于 20MB 的栅格生成金字塔*

```python
gma.rasp.GenerateOVR(InFile, MINSize = 20)
## 若文件小于 设定的 MINSize 值，则会自动跳过成成过程
```

*修改金字塔文件的压缩方式*

```python
gma.rasp.GenerateOVR(InFile, Compress = 'LZW')
## 不同压缩方式的生成的金字塔文件大小不同，生成速率不同。
```

*修改金字塔文件的重采样方法*

```python
gma.rasp.GenerateOVR(InFile, Resample = 'CUBIC')
## 不同重采样方式的金字塔文件值不同，生成速率不同。
```

*修改金字塔文件生成过程的块大小（影响金字塔级别）*

```python
gma.rasp.GenerateOVR(InFile, BlockSize = 256)
## 不同的块大小对金字塔级别有影响。
gma.Open(InFile).Info['bands'][0]['overviews']
## 与默认生成方式相比（生成了 5 级金字塔），BlockSize 为 256 时生成金字塔少一级（ 生成了 4 级金字塔）。
```
> \>>>[{'size': [3427, 2629]},<br>
 　　{'size': [1714, 1315]},<br>
 　　{'size': [857, 658]},<br>
 　　{'size': [429, 329]}]


