---
title: PM_ET0 
date: 2021-10-31
sidebar: false
---

## gma.index.**PM_ET0**(*Pres, Wind, MaxT, MinT, Rh, Shour, Lat, Day, Ele, AS=0.25, BS=0.5, A=0.23*)

---

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

---

