---
title: Check
date: 2021-10-30
sidebar: false
---

## gma.vesp.**Check**(*InFile*)

---

**功能：**【检查】。检查每个矢量要素的有效性。

**参数：** 

&emsp;InFile：`str`。输入矢量文件路径。

**返回：** 如果输入矢量通过检查，则返回 Pass。否则返回无效信息（dict）。无效信息组成：{ Invalid float: 无效要素的数量。Invalid layer&FID: 无效图层和图层内无效要素的FID}。

---

