---
title: ChangeDataType
date: 2021-10-30
sidebar: false
---

## gma.rasp.**ChangeDataType**(*InFile, OutFile, DataType, OutFormat = 'GTiff'*)

---

**功能：**【数据类型转换】。转换栅格数据的数据类型。

**参数：** 

&emsp;InFile：`str`。输入栅格路径。

&emsp;OutFile：`str`。输出栅格路径。

&emsp;DataType：`int||str`。输出栅格数据类型的代码或字符串标记。

::: tip 支持的数据类型

Unknown:0，Byte:1，UInt16:2，Int16:3，UInt32:4，Int32:5，Float32:6，Float64:7，CInt16:8，CInt32:9，CFloat32:10，CFloat64:11。

:::

**可选参数：**

&emsp;OutFormat  = `str`。输出栅格文件格式。默认为 GTiff，其他格式详见 ToOtherFormat 函数。

---

**示例：*****（以 BandDecomposition 分解的 12 波段数据为例）***

```python
import gma
InFile = 'ELE_China_GEBCO_2020.tif'
OutFile = 'ELE_China_GEBCO_2020_Float32.tif'
print('输入栅格数据类型：', gma.Open(InFile).DataType)

gma.rasp.ChangeDataType(InFile, OutFile, 'Float32')

print('输出栅格数据类型：', gma.Open(OutFile).DataType)
```
> \>>> 输入栅格数据类型： 3<br>
> \>>> 输出栅格数据类型： 6