---
title: Zip
date: 2021-10-30
sidebar: false
---

##  gma.osf.**Zip**(*Path,  ZipFilePath,  Mode  =  'w'*)

---

**功能：**【压缩】。将目标路径下所有文件压缩为 .zip 文件。

**参数：** 

&emsp;Path：`str`。压缩目标路径。

&emsp;ZipFilePath：`str`。压缩结果文件路径。扩展名为 .zip。

**可选参数：** 

&emsp; Mode = `str` 。压缩文件处理方法。默认为覆盖（w）。

::: tip 可接受的处理方法

w：如果目标 .zip 存在，则目标文件将会被替换。

a：如果目标 .zip 存在，则目标文件内容会被更新。

:::

---


**示例：**
```python
from gma import osf

# 压缩 SENT2_RS 文件夹及文件夹下所有文件压缩至至 SENT_RS_LY_20220305.zip
osf.Zip('SENT2_RS', 'SENT_RS_LY_20220305.zip')
```

