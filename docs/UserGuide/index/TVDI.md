---
title: TVDI
date: 2021-10-31
sidebar: false
---

## gma.index.**TVDI**(*VI, LST, ValidVIRange = [0.2, 0.8], ValidLSTRange = [200, 350], Delta = 0.01, VINoData = None, LSTNoData = None, OutNoData = -1*) <Badge text="1.0.2 +"/>

---

**功能：**【TVDI】。计算温度植被干旱指数。

**参数：**

&emsp;VI：`array` 。 植被指数。

&emsp;LST：`array` 。 陆表温度（K）。

**可选参数：**

&emsp; ValidVIRange = `list` 。参与干湿边拟合植被指数的有效值范围，默认 0.2 ~ 0.8。

&emsp; ValidLSTRange = `list` 。参与干湿边拟合陆表温度的有效值范围，默认 200 ~ 350（K）。

&emsp; Delta = `float` 。干湿边拟合过程中植被指数采样的样本间距。默认为 0.01。

&emsp; VINoData  = `float` 。植被指数数据中的无效值。默认不设置（None）。

&emsp; LSTNoData = `float` 。陆表温度数据中的无效值。默认不设置（None）。

&emsp; OutNoData = `float` 。TVDI结果中的无效值。默认值为 -1。

::: warning 注意

VINoData， LSTNoData 的区域在输出栅格中都将被改为 OutNoData。

:::

**返回：** TVDI（`array`），参与拟合的VI（`array`），湿边LST（`array`）， 干边LST（`array`），湿边方程[系数，常数]（`list`），干边方程[系数，常数]（`list`）。

---
