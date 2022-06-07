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

