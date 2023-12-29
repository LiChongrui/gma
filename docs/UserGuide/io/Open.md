---
title: Open
date: 2022-03-09
sidebar: false
---

## io.**Open**(*InFile, Mode = 0*)

---

**功能：**【打开文件】。打开栅格或矢量数据文件。

**参数：**

&emsp;InFile：`str`。输入文件路径。

**可选参数：**

&emsp;Mode = `int`。读取模式。默认为只读（0），也可为 1（可写模式）。参数设置错误则返回只读模式。

**返回：** 多维栅格：[SubDataSet](SubDataSet.html)；其他栅格：[DataSet](DataSet.html)。矢量数据：[DataSource](DataSource.html)。

---

**示例：**
```python
from gma import io
```
*打开矢量数据（下载 [示例矢量](/Open/China_Province_2022.7z)）*

```python
VO = io.Open('China_Province_2022.shp')
print(VO)
```
> \>>> <gma.algorithm.core.dataio.DataSource object at 0x......>

*打开栅格数据（下载 [示例栅格](/Open/ELE_China_GEBCO_2020.tif)）*

```python
RO = io.Open('ELE_China_GEBCO_2020.tif')
print(RO)
```
> \>>> <gma.algorithm.core.dataio.DataSet object at 0x......>




