---
title: SavitzkyGolay
date: 2021-10-30
sidebar: false
---

### gma.math.Smooth().**SavitzkyGolay**(*Polyorder = 2, Delta = 1, Mode = 'interp'*)

---

**功能：**【Savitzky-Golay】。利用 SavitzkyGolay 方法对数据进行平滑。

**可选参数：**

&emsp;Polyorder = `int`。平滑多项式阶数。默认为 2 。

&emsp;Delta = `float`。将应用过滤器的样本间距。默认为 1。

&emsp;Mode = `str`。边缘数据处理方法。默认为 插补（interp）。

::: tip 其他方法

其他处理方法还包括：mirror，nearest，wrap。

:::

**返回：**`array`。

---
