---
title: 更新预览
date: 2022-02-08
sidebar: false
---

## 更新前瞻

```mermaid
gantt
        dateFormat  YYYY-MM-DD
        title gma 近期完善内容

        section 库优化

        持续优化: active, des3, 2022-02-10, 2022-03-01
  
        section 参数检查和初始化

        为 index、math、osf 模块内未实现参数检查和初始化的函数添加参数初始化或检查: crit, after now,30d

```

## 更新测试中的新内容

&emsp;　更新测试中的新内容将在下一个 gma 版本中发布。下一版本 **1.0.6** 。

<font color="#3CB371"><i class="fab fa-superpowers"></i></font> **优化：**

&emsp;　1、FillNoData

&emsp;　　所有的插补方法支持的类型移入 key 中。（内部修改，不影响函数功能。）

