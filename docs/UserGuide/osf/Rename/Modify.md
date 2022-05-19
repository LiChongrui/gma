---
title: Modify
date: 2021-10-30
sidebar: false
---

## gma.index.Rename().**Modify**(*NewName*)

---

**功能：**【修改】。将原有文件（夹）名修改为新名。

**参数：** 

&emsp;NewName：`str`。新文件或文件夹名。

---


**示例：**
```python
import gma
SM = gma.osf.Rename('SENT.zip')
# 将源文件名修改为 SENT_RS_LY_20220305.zip
SM.Modify('SENT_RS_LY_20220305.zip')
```
> \>>> SENT_RS_LY_20220305.zip
