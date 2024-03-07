---
title: Primems
date: 2024-01-10
sidebar: false
---

&emsp;　gma 内置的角度单位位于 **crs.Primems** 模块下。内置子午线如下：

| 内置子午线 | 中文名     | 经度（°） |
| ---------- | ---------- | --------- |
| Athens     | 雅典       | 23.71634  |
| Bern       | 伯尔尼     | 7.439583  |
| Bogota     | 波哥大     | -74.0809  |
| Brussels   | 布鲁塞尔   | 4.367975  |
| Ferro      | 费罗       | -17.6667  |
| Greenwich  | 格林尼治   | 0         |
| Jakarta    | 雅加达     | 106.8077  |
| Lisbon     | 里斯本     | -9.13191  |
| Madrid     | 马德里     | -3.68794  |
| Oslo       | 奥斯陆     | 10.72292  |
| Paris      | 巴黎       | 2.337229  |
| Rome       | 罗马       | 12.45233  |
| Stockholm  | 斯德哥尔摩 | 18.05828  |
| Luoyang    | 洛阳       | 112.5423  |

&emsp;　不同子午线的位置如下：

![](/crs/Primems.png)

**示例：**

```python
from gma import crs

Primem = crs.Primems.Luoyang
print(Primem)
```

> \>>> 112.5522641
