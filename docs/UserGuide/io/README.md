---
title: 模块简介
date: 2023-08-20
sidebar: false
---

&emsp;&emsp; gma 栅格/矢量数据输入输出模块 **io** 为栅格/矢量数据支持的底层驱动，提供数据读/写、转换（与NumPy、Pandas等）等各类操作。目前主要包括 8 个函数 ，主要分类为：

![](/io/io.svg)

&emsp;&emsp; gma 栅格数据操作类主要包括**多数据集（MultiDataSets）、数据集（DataSet）**，其功能/属性的关系结构如下图所示：
![](/io/raster.svg)

&emsp;&emsp; gma 矢量数据操作逻辑继承自ogr，主要包括**数据资源（DataSource）、矢量图层（Layer）、矢量要素（Feature）**，三者的示意图如下：

![](/io/vector-type.svg)

&emsp;&emsp;矢量要素（Feature）是gma矢量数据的最小组成单元，其由一个几何体及其对应的字段构成。

&emsp;&emsp;矢量图层（Layer）是gma矢量数据的基础，其由一个或多个矢量要素构成。

&emsp;&emsp;数据资源（DataSource）由多个矢量图层组成，一般的矢量文件仅含有一个矢量图层。

&emsp;&emsp; gma 内矢量数据功能/属性的关系结构如下图所示：

![](/io/vector.svg)


 **导入此模块**

```python
from gma import io
```




