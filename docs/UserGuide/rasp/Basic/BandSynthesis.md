---
title: BandSynthesis
date: 2021-10-30
sidebar: false
---

## gma.rasp.Basic.**BandSynthesis**(*InFiles, OutFile, OutFormat = 'GTiff'*)
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

**示例：**

```python
from gma import rasp, osf
OutFile = 'BandSynthesis.tif'

# 获取需要合并文件的路径列表
InFiles = osf.FindPath('TifDir', EXT = '.tif')
rasp.Basic.BandSynthesis(InFiles, OutFile)
```