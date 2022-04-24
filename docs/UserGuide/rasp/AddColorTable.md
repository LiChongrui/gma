---
title: AddColorTable
date: 2021-10-30
sidebar: false
---

## gma.rasp.**AddColorTable**(*InFile, TemplateFile = None, ColorTable = None*)<Badge text="1.0.1 +"/>

---

**功能：**【添加色彩映射表】。为栅格数据添加色彩映射。

**参数：** 

&emsp;InFile：`str`。输入栅格路径。

**可选参数：**

&emsp;TemplateFile = `str`。模板栅格文件路径。默认不设置（None）。若设置模板栅格，则将模板栅格的色彩映射表添加到输入栅格。

&emsp;ColorTable = `dict`。色彩映射表。格式为 {值: (R,G,B,A)}。默认不设置（None）。

::: tip 示例

ColorTable = {10:(200,50,100,255), 20:(200,50,100,255)}。
:::

::: warning 注意

若设置了 ColorTable，则：

&emsp;1、若 TemplateFile 未设置（None），则用 ColorTable 更新输入栅格的色彩映射表。

&emsp;2、若设置了 TemplateFile，则以 TemplateFile 色彩映射表为基础，并用 ColorTable 更新该基础色彩映射表，然后将更新后的色彩映射表添加到输入栅格中。

:::

---

