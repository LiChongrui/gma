---
title: UnZip
date: 2021-10-30
sidebar: false
---

##  gma.osf.**UnZip**(*ZipFilePath,  OutPath*)

---

**功能：**【解压缩】。解压缩 .zip 文件。

**参数：** 

&emsp;ZipFilePath：`str`。需要解压缩的 .zip 文件路径。

&emsp;OutPath：`str`。解压后存储文件的路径。

---

**示例：**
```python
import gma
# 压缩 SENT_RS_LY_20220305.zip 文件至 SENT2_RS_UNZip 文件夹
gma.osf.UnZip('SENT_RS_LY_20220305.zip', 'SENT2_RS_UNZip')
```
