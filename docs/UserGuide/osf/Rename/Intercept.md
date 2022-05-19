---
title: Intercept
date: 2021-10-30
sidebar: false
---

## gma.index.Rename().**Intercept**(*Start, Length*)

---

**功能：**【截取】。截取文件（夹）名中的部分字符串作为新文件（夹）名。

::: warning 注意

此方法自动忽略扩展名。即：不论 Start, Length设置为多少，扩展名都将被保留。

:::

**参数：** 

&emsp;Start：`int`。截取字符串的初始位置。

&emsp;Length：`int`。截取字符串的长度。

---

**示例：**
```python
import gma
SM = gma.osf.Rename('SENT_RS_LY_20220305.zip')
# 从第 0 个字符开始截取 4 个字符做为新名
SM.Intercept(0, 4)
```
> \>>> SENT.zip