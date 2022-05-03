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