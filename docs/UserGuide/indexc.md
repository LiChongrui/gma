---
title: 指数计算
date: 2021-10-31
---

**&emsp;&emsp;指数计算** 为 **gma.index** 内所有遥感、气象以及其他相关指数计算函数的详细功能、参数设置和引用方法说明，如果您想了解 gma 所有函数的整体情况，请移步 [函数功能列表](/Functions/Function.html) 。


## EVI 
::: theorem

**引用：**  gma.index.EVI(Nir, Red, Blue)

**功能：** 【EVI】。计算增强植被指数。

**参数：**

&emsp;Nir：`float||array` 。近红外波段数据。

&emsp;Red：`float||array` 。红光波段数据。

&emsp;Blue：`float||array`。 蓝光波段数据。

**返回：**`float||array`。

:::

## NDBI
::: theorem
**引用：**  gma.index.NDBI(Nir, Swir)

**功能：**【NDBI】。计算归一化建筑指数。

**参数：**

&emsp;Nir：`float||array` 。近红外波段数据。

&emsp;Swir：`float||array` 。短波红光波段数据。

**返回：**`float||array`。
:::

## NDWI 
::: theorem
**引用：**  gma.index.NDWI(Nir, Green)

**功能：**【NDWI】。计算归一化水指数。

**参数：**

&emsp;Nir：`float||array` 。近红外波段数据。

&emsp;Green：`float||array` 。绿光波段数据。

**返回：** `float||array`。
:::

## NDVI
::: theorem
**引用：** gma.index.NDVI(Nir, Red)

**功能：**【NDVI】。计算归一化植被指数。

**参数：**

&emsp;Nir：`float||array` 。近红外波段数据。

&emsp;Red：`float||array`。 红光波段数据。

**返回：**`float||array`。
::: 

## PM_ET0 

::: theorem

**引用：**  gma.index.PM_ET0(Pres, Wind, MaxT, MinT, Rh, Shour, Lat, Day, Ele, AS=0.25, BS=0.5, A=0.23)

**功能：**【PM_ET0】。彭曼法（Penman Monteith）计算【日】【作物参考蒸散量（ET0）】。

**参数：**

&emsp;Pres：`float||array`。  日平均气压（hPa）。

&emsp;Wind：`float||array` 。 日平均10m风速（m/s）。

&emsp;MaxT：`float||array`。  日最高气温（℃）。

&emsp;MinT：`float||array` 。日最低气温（℃）。

&emsp;Rh：`float||array` 。日平均相对湿度（%）。

&emsp;Shour：`float||array`  日日照时数（hr）。

&emsp;Lat：`float||array` 。纬度（°）。

&emsp;Day：`int||array` 。以日序（儒略日）表示。1-365（平年）或366（闰年）。

&emsp;Ele：`float||array` 。海拔高度（m）。

**可选参数（常量）：**

&emsp; AS = 0.25。

&emsp; BS = 0.5。

&emsp; A = 0.23。

**返回：**`float||array`。

:::

## TVDI <Badge text="1.0.2 +"/>

::: theorem

**引用：**  gma.index.TVDI(VI, LST, ValidVIRange = [0.2, 0.8], ValidLSTRange = [200, 350], Delta = 0.01, VINoData = None, LSTNoData = None, OutNoData = -1)

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

<Boxx type='warning' title='注意' content='VINoData， LSTNoData 的区域在输出栅格中都将被改为 OutNoData。'/>

**返回：** TVDI（`array`），参与拟合的VI（`array`），湿边LST（`array`）， 干边LST（`array`），湿边方程[系数，常数]（`list`），干边方程[系数，常数]（`list`）。

:::
