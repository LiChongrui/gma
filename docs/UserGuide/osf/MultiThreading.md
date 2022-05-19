---
title: MultiThreading
date: 2021-10-30
sidebar: false
---

## gma.osf.**MultiThreading**(*Function, MTParameters, THNumber = 'ALL_CPUS', Process = True, \*args, \*\*kwargs*)<Badge text="1.0.3 +"/>

---

**功能：**【多线程】。创建多个线程，实现同一函数多个参数的同步执行。

**参数：** 

&emsp;Function：`def||接受传参的可执行程序（命令）`。需要多线程执行的函数或程序（命令）。

&emsp;MTParameters：`list`。需要分别带入 Function 的参数集合。

**可选参数：** 

&emsp;THNumber =  `int||ALL_CPUS`。线程数，默认是所有 逻辑 CPU 核心数（ALL_CPUS）。

&emsp;Process = `bool` <Badge text="1.0.8 +"/> 。是否显示多线程进度条。默认显示（True）。

&emsp;*args：`Function 的固定参数`。传递给 Function 的不变参数。从 Function 的第一个开始固定。

&emsp;**kwargs：`Function 的可选参数'`。传递给 Function 的不变可选参数。

**返回：** `list`。每个参数带入 Function 执行后的返回值列表。与 MTParameters 的顺序一致。

---

**示例：**
```python
import gma
```

*为栅格数据批量构建 .ovr 金字塔*
```python
# 获取所有栅格数据路径
InFiles = gma.osf.GetPath('.')

# 栅格金字塔函数
GenerateOVR = gma.rasp.GenerateOVR

# 批量生成
gma.osf.MultiThreading(GenerateOVR, InFiles)

# 查看生成结果
OVRFiles = gma.osf.GetPath('.', EXT = '.ovr')
print(OVRFiles)
```
> \>>> ['.\\PRE_China_ANUSPLIN_20201215.tif.ovr',<br>
 　　　'.\\PRS_China_ANUSPLIN_20201215.tif.ovr',<br>
 　　　'.\\RHU_China_ANUSPLIN_20201215.tif.ovr',<br>
 　　　'.\\SSD_China_ANUSPLIN_20201215.tif.ovr',<br>
 　　　'.\\TMAX_China_ANUSPLIN_20201215.tif.ovr',<br>
 　　　'.\\TMIN_China_ANUSPLIN_20201215.tif.ovr',<br>
 　　　'.\\WIN_China_ANUSPLIN_20201215.tif.ovr']

* *控制线程数量*
```python
import datetime as dt
T0 = dt.datetime.now()
gma.osf.MultiThreading(GenerateOVR, InFiles, THNumber = 2)
print('2 线程：', dt.datetime.now() - T0)
T1 = dt.datetime.now()
gma.osf.MultiThreading(GenerateOVR, InFiles, THNumber = 7)
print('7 线程：', dt.datetime.now() - T1)
```
> \>>> 2 线程： 0:00:06.622308<br>
 \>>> 7 线程： 0:00:04.191480

* *为 `GenerateOVR ` 传入可选参数*
```python
CM0 = gma.Open(OVRFiles[0]).Info['metadata']['IMAGE_STRUCTURE']['COMPRESSION']
print('默认压缩方式：', CM0)
# 修改金字塔文件的压缩方式
gma.osf.MultiThreading(GenerateOVR, InFiles, Compress = 'LZMA')
CM1 = gma.Open(OVRFiles[0]).Info['metadata']['IMAGE_STRUCTURE']['COMPRESSION']
print('自定义压缩方式：', CM1)
```
> \>>> 默认压缩方式： DEFLATE<br>
 \>>> 自定义压缩方式： LZMA