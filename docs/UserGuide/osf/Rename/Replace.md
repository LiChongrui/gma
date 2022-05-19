---
title: Replace
date: 2021-10-30
sidebar: false
---

## gma.index.Rename().**Replace**(*OldString, NewString*)

---

**功能：**【替换】。替换原文件（夹）名中字符串后作为新文件（夹）名。

**参数：** 

&emsp;OldString：`str`。需要替换的字符串。

&emsp;NewString：`str`。替换后的新字符串。

---

**示例：**
```python
import gma
SM = gma.osf.Rename('SENT_RS_LY_20220305.zip')
# 替换文件名中的 SENT 为 SENT2
SM.Replace('SENT', 'SENT2')
```
> \>>> SENT.zip
