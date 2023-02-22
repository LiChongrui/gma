---
title: 快速安装
date: 2021-10-29 23:20:00
sidebar: false
---

## 依赖环境

::: theorem 系统环境

&emsp;&emsp;操作系统：64 位 (amd64) <Badge text="Windows" vertical='middle'/> 、<Badge text="Linux" vertical='middle'/>及以上

&emsp;&emsp;内存：<Badge text="8 GB" vertical='middle'/>  及以上

:::

> 注意：gma 目前**不支持** <Badge text="MacOS" type='error' vertical='middle'/> 和其他平台。

::: theorem Python 环境

&emsp; Windows： <Badge text="3.8 ~ 3.11" vertical='middle'/>

&emsp; Linux： <Badge text="3.9~3.11" vertical='middle'/>

:::

&emsp;&emsp;建议安装 **Anaconda** 创建 Python 环境。 Anaconda 是一个开源的 Python 发行版本，其包含了 180 多个科学包及其依赖项。

::: right  

 [**点击访问 Anaconda 下载网站**](https://www.anaconda.com/)

:::

## 依赖库 
&emsp;&emsp;gma 的构建依赖 gdal <Badge text="3.4.1 +"/>，numpy <Badge text="1.23.3 +"/>，pandas <Badge text="1.4.2 +"/> 和 scipy<Badge text="1.7.3 +"/> 等库，这些库是 gma 实现功能的基础。 gdal 需要手动编译或下载编译后相应版本的 whl 包手动安装。

::: right 

 [**点击访问 whl 下载网站**](https://www.lfd.uci.edu/~gohlke/pythonlibs/)

:::

&emsp;&emsp;打开  Windows 终端（或```CMD、PowerShell、conda``` 等且**已配置系统变量**），使用以下命令安装 gdal （**默认 Python 环境**）:
```bash
pip install "X:\GDAL-3.4.1-cp39-cp39-win_amd64.whl"
```
&emsp;&emsp; 或使用 **conda** 安装：

```bash
conda install gdal
```



## 安装

&emsp;&emsp;gma 已经发布至 [pypi](https://pypi.org/project/gma/)，可以在终端输入以下命令安装：

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

### 错误解决

&emsp;&emsp;从 **1.0.5** 版本开始，gma 会对引用过程中出现的错误进行追踪标记。引用过程中出现的错误可参考下表解决（其中 XXX / YYY 为发生错误的包 / 模块）：

| 错误类型            | 错误内容                                                     | 解决方法                          |
| :------------------ | :----------------------------------------------------------- | :-------------------------------- |
| ModuleNotFoundError | Missing GDAL library! See https://gdal.org/api/python_bindings.html | [安装 gdal](/Install.html#依赖库) |
| ModuleNotFoundError | The XXX library is missing, please install it with 'pip install XXX' in the terminal! | 在终端输入 `pip install XXX` 安装 |
| ImportError         | Currently installed GDAL is not supported, please update GDAL! | 升级 gdal                         |
| ImportError         | The GDAL version is too low, the current version {__gdalversion__}, the minimum version is 3.4.1, please update GDAL! | 升级 gdal                         |
