---
title: Reclassify
date: 2022-12-01
sidebar: false
---

## gma.rasp.Extraction.**Reclassify**(*InFile, OutFile, Remap, Method = 'Range', OutFormat = 'GTiff'*)<Badge text="1.1.1 +"/>

---

**功能：** 【重分类】。重新分类或修改栅格数据值。

**参数：** 

&emsp;InFile：`str`。输入栅格路径。

&emsp;OutFile：`str`。输出矢量路径。

&emsp;Remap： `list`。重分类表。

&emsp;&emsp;用于将输入值或范围定义重新映射到新值。格式为：

&emsp;&emsp;&emsp;[[mapping1，value1]，[mmapping2，value2]，…]。

**可选参数：**

&emsp;Method = `str`。重分类方法。可以为 'Range' 或 'Unique'，默认为 'Range'。

::: tip 提示

'Range':  范围映射分类。
                
'Unique': 严格一对一映射分类。

例如：

Remap = [[1000, 1],
             [2000, 2],
             [3000, 3]]

1. Method = 'Range'.

        Data <= 1000: --> 1
        1000 < Data <= 1000: --> 2
        2000 < Data <= 3000: --> 3
        Data > 3000: --> NoData

2. Method = 'Unique'.

        Data == 1000: --> 1
        Data == 2000: --> 2   
        Data == 3000: --> 3 
        Other values: --> NoData

:::

&emsp;OutFormat  = `str`。输出栅格文件格式。默认为 GTiff，其他格式详见 rasp.ToOtherFormat 函数。

---

**示例：**

```python
from gma import rasp

OutFile = 'Reclassify.tif'
Remap = [[0, 0],
         [500, 1],
         [1000, 2],
         [1500, 3],
         [2000, 5],
        ]
rasp.Extraction.Reclassify(inres.WorldDataSet.DEM, OutFile, Remap = Remap)
```

> 原始DEM与重分类结果：

![](/rasp/Reclassify.png)
