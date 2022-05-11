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

**示例：（以 gma 库内文件为例，文件详情见 [文件组织](/Explore/Structure.html#文件组织)）**
```python
import gma
# 确定 gma 库的位置
Path = gma.__path__[0]
# gma 内关联参数和函数 relation 路径
PathA = f'{Path}\\relation'
```

*获取所有文件*
```python
gma.osf.GetPath(PathA)
```
> \>>> ['D:\\github\\gma-code\\gma-pyd\\dist\\gma\\relation\\constants.pyd',<br>
 　　　'D:\\github\\gma-code\\gma-pyd\\dist\\gma\\relation\\driver.pyd',<br>
 　　　'D:\\github\\gma-code\\gma-pyd\\dist\\gma\\relation\\initialize.pyd',<br>
 　　　'D:\\github\\gma-code\\gma-pyd\\dist\\gma\\relation\\key.pyd',<br>
 　　　'D:\\github\\gma-code\\gma-pyd\\dist\\gma\\relation\\\_\_init\_\_.py',<br>
 　　　'D:\\github\\gma-code\\gma-pyd\\dist\\gma\\relation\\\_\_pycache\_\_\\_\_init__.cpython-38.pyc']

*获取指定扩展名的文件*
```python
gma.osf.GetPath(PathA, EXT = '.pyd')
```
> \>>> ['D:\\github\\gma-code\\gma-pyd\\dist\\gma\\relation\\constants.pyd',<br>
 　　　'D:\\github\\gma-code\\gma-pyd\\dist\\gma\\relation\\driver.pyd',<br>
 　　　'D:\\github\\gma-code\\gma-pyd\\dist\\gma\\relation\\initialize.pyd',<br>
 　　　'D:\\github\\gma-code\\gma-pyd\\dist\\gma\\relation\\key.pyd']

*获取指定扩展名且包含特定字符的文件*
```python
gma.osf.GetPath(PathA, EXT = '.pyd', Include = 'init')
```
> \>>> ['D:\\github\\gma-code\\gma-pyd\\dist\\gma\\relation\\initialize.pyd']

*获取指定扩展名且排除特定字符的文件*
```python
gma.osf.GetPath(PathA, EXT = '.pyd', Exclude = 'init')
```
> \>>> ['D:\\github\\gma-code\\gma-pyd\\dist\\gma\\relation\\constants.pyd',<br>
　　　'D:\\github\\gma-code\\gma-pyd\\dist\\gma\\relation\\driver.pyd',<br>
　　　'D:\\github\\gma-code\\gma-pyd\\dist\\gma\\relation\\key.pyd']

*仅获取文件夹（含输入路径）*
```python
gma.osf.GetPath(PathA, Search = 'DIR')
```
> \>>> ['D:\\github\\gma-code\\gma-pyd\\dist\\gma\\relation\\',<br>
　　　'D:\\github\\gma-code\\gma-pyd\\dist\\gma\\relation\\\_\_pycache\_\_\\']

*获取文件和文件夹*
```python
gma.osf.GetPath(PathA, Search = 'ALL')
```
> \>>> ['D:\\github\\gma-code\\gma-pyd\\dist\\gma\\relation\\constants.pyd',<br>
　　　'D:\\github\\gma-code\\gma-pyd\\dist\\gma\\relation\\driver.pyd',<br>
　　　'D:\\github\\gma-code\\gma-pyd\\dist\\gma\\relation\\initialize.pyd',<br>
　　　'D:\\github\\gma-code\\gma-pyd\\dist\\gma\\relation\\key.pyd',<br>
　　　'D:\\github\\gma-code\\gma-pyd\\dist\\gma\\relation\\\_\_init\_\_.py',<br>
　　　'D:\\github\\gma-code\\gma-pyd\\dist\\gma\\relation\\\_\_pycache\_\_',<br>
　　　'D:\\github\\gma-code\\gma-pyd\\dist\\gma\\relation\\\_\_pycache\_\_\\\_\_init\_\_.cpython-38.pyc']


