---
title: BandSynthesis
date: 2021-10-30
sidebar: false
---

## gma.rasp.**BandSynthesis**(*InFiles, OutFile, OutFormat = 'GTiff'*)
---

**功能：**【文件合并】。将单波段文件合成多波段文件。

**参数：** 

&emsp;InFiles：`str||list`。需要合成的单波段文件路径或路径集合。

::: warning 警告
如果输入栅格为多波段数据，则仅第一个波段参与合成。
:::


&emsp;OutFile：`str`。输出栅格路径。

**可选参数：**

&emsp;OutFormat  = `str`。输出栅格文件格式。默认为 GTiff，其他格式详见 ToOtherFormat 函数。

---

**示例：*****（以 BandDecomposition 分解的 12 波段数据为例）***

```python
import gma
OutFile = r'.\ET0_China_ANUSPLIN_2020_BandSynthesis.tif'
# 获取需要合并文件的路径列表
## 为了保证顺序，在读取完所有12个波段的路径后，根据文件名长度做一个排序
InFiles = sorted(gma.osf.GetPath(OutPath), key = len)
gma.rasp.BandSynthesis(InFiles, OutFile)
# 查看合成文件的波段数
gma.Open(OutFile).Bands
```
> \>>> 12