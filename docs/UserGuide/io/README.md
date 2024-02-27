---
title: 模块简介
date: 2023-08-20
sidebar: false
---

&emsp;&emsp; gma 栅格/矢量数据输入输出模块 **io** 为栅格/矢量数据支持的底层驱动，提供数据读/写、转换（与NumPy、Pandas等）等各类操作。目前主要包括 9 个函数 ，主要分类为：

![](/io/io.svg)

 **导入此模块**

```python
from gma import io
```

&emsp;&emsp; gma栅格数据操作类为数据集（DataSet），其功能/属性的关系结构如下图所示：

![](/io/raster.svg)

&emsp;&emsp; gma 矢量数据操作类主要包括矢量图层（Layer）、矢量要素（Feature）。矢量要素（Feature）是gma矢量数据的最小组成单元，其由一个几何体及其对应的字段构成。矢量图层（Layer）是 gma 矢量数据的基础，其由一个或多个矢量要素构成。其功能/属性的关系结构如下图所示：

![](/io/vector.svg)