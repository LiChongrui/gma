---
title: 安装引用
date: 2021-10-29 23:20:00
sidebar: false
---

## 依赖环境

::: theorem 系统环境

&emsp;&emsp;操作系统：<Badge text="Winows 10 +" vertical='middle'/> 及以上

&emsp;&emsp;内存：<Badge text="8 GB" vertical='middle'/>  及以上

:::

> 注意：gma 目前**不支持** <Badge text="Linux" type='error' vertical='middle'/><Badge text="MacOS" type='error' vertical='middle'/> 和其他平台。

::: theorem Python 环境

&emsp; Python 版本应为 <Badge text="3.8、3.9 或 3.10" vertical='middle'/>

:::

&emsp;&emsp;建议安装 **Anaconda** 创建 Python 环境。 Anaconda 是一个开源的 Python 发行版本，其包含了 180 多个科学包及其依赖项。

::: right  

 [**点击下载 Anaconda3 (Python 3.8.8 64-bit)**](https://repo.anaconda.com/archive/Anaconda3-2021.05-Windows-x86_64.exe)

:::

## 依赖库 
&emsp;&emsp;gma 的构建依赖 gdal <Badge text="3.3.1 +"/>，numpy <Badge text="1.20.3 +"/>，pandas <Badge text="1.3.3 +"/> 和 scipy<Badge text="1.7.1 +"/> 等库，这些库是 gma 实现功能的基础。由于 gdal 不是一个纯 Python 库，需要手动编译或下载编译后对应版本的 whl 包手动安装。

::: right 

 [**点击访问 whl 下载网站**](https://www.lfd.uci.edu/~gohlke/pythonlibs/)

:::

&emsp;&emsp;打开  Windows 终端（或```CMD、PowerShell、conda``` 等且**已配置系统变量**），使用以下命令安装 gdal （**默认 Python 环境**）:
```bash
pip install "X:\XXX\GDAL-3.3.3-cp38-cp38-win_amd64.whl"
```

&emsp;&emsp; 其中```X:\XXX\GDAL-3.3.3-cp38-cp38-win_amd64.whl``` 为下载的编译后 whl 格式 gdal 包的绝对路径。其他 whl 包也可以按此方法安装。

## 手动安装

&emsp;&emsp;gma 已经上传至 [pypi](https://pypi.org/project/gma/)，可以在终端输入以下命令安装：

```bash
pip install gma
```
&emsp;&emsp;在安装 gma 时，依赖的 numpy，pandas 和 scipy 等库如果不存在则会自动安装（需联网）。

## 引用

&emsp;&emsp;打开 Python 的 IDE（数据处理推荐 **Spyder**，工程开发推荐 **Pycharm**，分步测试推荐 **Jupter Notebook**）直接导入库。

```python
import gma
```

&emsp;&emsp; 下一步，请试试 gma 的函数吧。
