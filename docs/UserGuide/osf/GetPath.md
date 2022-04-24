---
title: GetPath
date: 2021-10-30
sidebar: false
---

## gma.osf.**GetPath**(*Path,  EXT = None,  Include = None, Exclude = None, Search = 'FILE'*)

---

**功能：**【获取路径】。获取目标路径或路径集合下满足条件的所有文件夹和文件路径。

**参数：** 

&emsp;Path：`str||list`。路径或路径集合。

**可选参数：** 

&emsp;EXT = `str||list`。查找文件的扩展名或扩展名列表。默认查找所有文件（None）。

::: warning 注意

只有在 SearchPath = "FILE" 时, 此参数才生效。

:::

&emsp;Include = `str||list`。筛选包含此参数设置值的路径。默认返回全部结果（None）。其他类型的参数设置将会被强制转换为字符串。

&emsp;Exclude = `str||list`。排除包含此参数设置值的路径。默认不排除任何字符串（None）。其他类型的参数设置将会被强制转换为字符串。

::: tip 提示

1. 如果 Include（Exclude）为字符串，则包含设置值的路径才会被保留（排除）。

2. 如果 Include（Exclude）为列表，则包含列表内任意一个字符串的路径都会被保留（排除）。

:::

&emsp;Search = `str`。要查找路径的类型。可为`FILE`（文件），`DIR`（文件夹），`ALL`（文件夹和文件），默认为 FILE 。

**返回：**`list`。满足条件的所有【文件夹和文件路径】集合。重复的路径只会保留一个。

---
