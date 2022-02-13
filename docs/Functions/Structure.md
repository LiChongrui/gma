---
title: 组织方式
date: 2021-10-29
---

&emsp;&emsp;不同的类型的函数在 gma 中分类构建，**库组织方式**列出了 gma 库的整体组织和构造，供大家了解和参考。

<!-- more -->

::: theorem 函数包和依赖文件的组织关系和说明

- **algorithm** *&emsp;&emsp; &emsp;&emsp; == 栅格、矢量操作的**基础算法***
	* raster *&emsp;&emsp; &emsp;&emsp; &emsp;&emsp; ==== 栅格处理， rasp 调用的**算法*** 
	* vector *&emsp;&emsp; &emsp;&emsp; &emsp;&emsp; ==== 矢量处理，vesp 调用的**算法***
- **relation** *&emsp;&emsp; &emsp;&emsp; ==  **关联参数和函数***
	* initialize *&emsp;&emsp; &emsp;&emsp; &emsp;&emsp; ==== **初始化**输入参数，错误检查*
	* [**key**](Default.html#默认参数) *&emsp;&emsp; &emsp;&emsp; &emsp;&emsp; ==== 栅格 / 矢量 处理的内置参数，例如**压缩**，**超大 TIFF 支持**等*
- [**index**](Function.html#index-指数运算) *&emsp;&emsp; &emsp;&emsp; == 遥感、气象的**指数运算**的相关算法*
- [**math**](Function.html#math-数学运算) *&emsp;&emsp; &emsp;&emsp; == **数学运算**相关算法*
- [**osf**](Function.html#osf-系统交互) *&emsp;&emsp;&emsp; &emsp;&emsp; == **系统交互**操作*
- [**smc**](Function.html#smc-空间杂项) *&emsp;&emsp;&emsp; &emsp;&emsp; == **空间杂项**计算*
- [**rasp**](Function.html#rasp-栅格处理) *&emsp;&emsp; &emsp;&emsp; == **栅格处理**函数包*
- [**vesp**](Function.html#vesp-矢量处理) *&emsp;&emsp; &emsp;&emsp; == **矢量处理**函数包*

:::

