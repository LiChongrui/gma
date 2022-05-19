---
title: \_\_init\_\_
date: 2021-10-30
sidebar: false
---

## gma.index.**Rename**(*FilePath*)

---

**功能：**【类】。重命名文件或文件夹。

**初始化：**

&emsp;FilePath：`str`。要重命名的文件或文件夹路径。   

::: warning 注意
类内 属性/方法 引用前请先初始化 `Rename` 类！
::: 

---

**示例：**
```python
import gma
SM = gma.osf.Rename('SENT_RS_LY_20220305.zip')
## 查看类型所有的 方法/属性
print([M for M in dir(SM) if '_' not in M])
```
> \>>> ['Intercept', 'Modify', 'Replace']