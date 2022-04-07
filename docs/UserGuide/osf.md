---
title: 系统交互
date: 2021-10-30
---

**&emsp;&emsp;系统交互** 为 **gma.osf** 内所有文件系统操作相关函数的详细功能、参数设置和引用方法说明，如果您想了解 gma 所有函数的整体情况，请移步 [函数列表](/Functions/Function.html) 。

## GetPath
::: theorem

**引用：** gma.osf.GetPath(Path, EXT = None, Include = None, Exclude = None, Search = 'FILE')

**功能：**【获取路径】。获取目标路径或路径集合下满足条件的所有文件夹和文件路径。

**参数：** 

&emsp;Path：`str||list`。路径或路径集合。

<Boxx type='tips' title='示例' content='1. Path = "C:/SP"</br>2. Path = ["C:/SD", "C:/SP"]'/>

**可选参数：** 

&emsp;EXT = `str||list`。查找文件的扩展名或扩展名列表。默认查找所有文件（None）。

<Boxx type='warning' title='注意' content='只有在 SearchPath = "FILE" 时, 此参数才生效。'/>

&emsp;Include = `str||list`。筛选包含此参数设置值的路径。默认返回全部结果（None）。其他类型的参数设置将会被强制转换为字符串。

&emsp;Exclude = `str||list`。排除包含此参数设置值的路径。默认不排除任何字符串（None）。其他类型的参数设置将会被强制转换为字符串。

<Boxx type='tips' title='提示' content='1. 如果 Include（Exclude）为字符串，则包含设置值的路径才会被保留（排除）。<br>2. 如果 Include（Exclude）为列表，则包含列表内任意一个字符串的路径都会被保留（排除）。'/>

&emsp;Search = `str`。要查找路径的类型。可为`FILE`（文件），`DIR`（文件夹），`ALL`（文件夹和文件），默认为 FILE 。

**返回：**`list`。满足条件的所有【文件夹和文件路径】集合。重复的路径只会保留一个。
::: 

## Zip

::: theorem

**引用：** gma.osf.Zip(Path, ZipFilePath, Mode = 'w')

**功能：**【压缩】。将目标路径下所有文件压缩为 .zip 文件。

**参数：** 

&emsp;Path：`str`。压缩目标路径。

&emsp;ZipFilePath：`str`。压缩结果文件路径。扩展名为 .zip。

**可选参数：** 

&emsp; Mode = `str` 。压缩文件处理方法。默认为覆盖（w）。

<Boxx type='tips' title='可接受的处理方法' content='w：如果目标 .zip 存在，则目标文件将会被替换。<br>a：如果目标 .zip 存在，则目标文件内容会被更新。'/>

:::

## UnZip

::: theorem

**引用：** gma.osf.UnZip(ZipFilePath, OutPath)

**功能：**【解压缩】。解压缩 .zip 文件。

**参数：** 

&emsp;ZipFilePath：`str`。需要解压缩的 .zip 文件路径。

&emsp;OutPath：`str`。解压后存储文件的路径。

:::

## DateSeries

::: theorem

**引用：** gma.osf.DateSeries(StartDate, EndDate, DateDelta, Format = '%Y%m%d')

**功能：**【日期序列】。构造一个日期序列列表。

**参数：** 

&emsp;StartDate：`str`。初始日期。例如 '20200101' 。

&emsp;EndDate：`str`。结束日期。例如 '20201231' 。 

&emsp;DateDelta：`int`。间隔日期（天）。

**可选参数：** 

&emsp;Format = `str`。日期序列格式。默认为 '%Y%m%d'（年月日）。

**返回：**`list`。

:::

## Rename 类

::: theorem

**引用：** gma.index.Rename(FilePath)

**功能：**【重命名】文件或文件夹。

**初始化：**

&emsp;FilePath：`str`。要重命名的文件或文件夹路径。   

::: 

::: warning 注意
类内函数引用前请先初始化 `Rename` 类！
::: 

### Modify
::: theorem

**引用：** gma.index.Rename().Modify(NewName):

&emsp;  注意：*引用前请先初始化 `Rename` 类。*

**功能：**【修改】。将原有文件（夹）名修改为新名。

**参数：** 

&emsp;NewName：`str`。新文件或文件夹名。

::: 

### Replace

::: theorem

**引用：** gma.index.Rename().Replace(OldString, NewString)

&emsp;  注意：*引用前请先初始化 `Rename` 类。*

**功能：**【替换】。替换原文件（夹）名中字符串后作为新文件（夹）名。

**参数：** 

&emsp;OldString：`str`。需要替换的字符串。

&emsp;NewString：`str`。替换后的新字符串。

::: 

### Intercept

::: theorem

**引用：** gma.index.Rename().Intercept(Start, Length)

&emsp;  注意：*引用前请先初始化 `Rename` 类。*

**功能：**【截取】。截取文件（夹）名中的部分字符串作为新文件（夹）名。

&emsp;  注意：*此方法自动忽略扩展名。即：不论 Start, Length设置为多少，扩展名都将被保留。*

**参数：** 

&emsp;Start：`int`。截取字符串的初始位置。

&emsp;Length：`int`。截取字符串的长度。

::: 

## MultiThreading<Badge text="1.0.3 +"/>

::: theorem

**引用：** gma.osf.MultiThreading(Function, MTParameters, THNumber='ALL_CPUS', *args, **kwargs)

**功能：**【多线程】。创建多个线程，实现同一函数多个参数的同步执行。

**参数：** 

&emsp;Function：`def||接受传参的可执行程序（命令）`。需要多线程执行的函数或程序（命令）。

&emsp;MTParameters：`list`。需要分别带入 Function 的参数集合。

**可选参数：** 

&emsp;THNumber =  `int||ALL_CPUS`。线程数，默认是所有 逻辑 CPU 核心数（ALL_CPUS）。

&emsp;*args：`Function 的固定参数`。传递给 Function 的不变参数。从 Function 的第一个开始固定。

&emsp;**kwargs：`Function 的可选参数'`。传递给 Function 的不变可选参数。

**返回：** `list`。每个参数带入 Function 执行后的返回值列表。与 MTParameters 的顺序一致。

::: 