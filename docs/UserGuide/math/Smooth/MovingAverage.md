---
title: MovingAverage
date: 2021-10-30
sidebar: false
---

## gma.math.Smooth().**MovingAverage**(*Mode = 'nearest'*)

---

**功能：**【滑动平均】。利用滑动平均法对数据进行平滑

**可选参数：**

&emsp;Mode = `str`。边缘数据处理方法。默认为 采用最近数据填充（nearest）。

<Boxx type='tip' title='其他方法' content='其他处理方法还包括：mirror，interp，wrap。' />

**返回：**`array`。

---
**示例：**
```python
import gma
```

*序列（1 维）*

```python
Data = [0.16359164, 0.16359164, 0.17469311, 0.20163227, 0.22857143, 0.32706435, 0.21466192, 0.10225949]
SM = gma.math.Smooth(Data, 5, Times = 1)
SM.MovingAverage()
```
> \>>> array([0.16581193, 0.17342006, 0.18641602, 0.21911056, 0.22932462,  0.21483789, 0.19496334, 0.16970095])

*不同参数结果对比*

```python
import matplotlib.pyplot as plt
# 配置参数
PAR = {'font.sans-serif': 'Times New Roman',
       'axes.unicode_minus': False
      }
plt.rcParams.update(PAR)
plt.figure(figsize = (10, 5.5), dpi = 300)
```

* *不同边缘值处理方法*
```python
Mode = ['mirror', 'nearest', 'wrap', 'interp']
for m in Mode:
    RSD = SM.MovingAverage(Mode = m)
    plt.plot(RSD, label = m)
plt.grid(True, linestyle = (0,(6,6)), linewidth = 0.4)
plt.legend(frameon = False)
plt.show()
```
![](/math/SMMovingAverageModes.svg)


* *不同平滑窗口*
```python
for ws in [3, 5, 7]:
    RSD = gma.math.Smooth(Data, ws, Times = 1).MovingAverage()
    plt.plot(RSD, label = ws)
plt.grid(True, linestyle = (0,(6,6)), linewidth = 0.4)
plt.legend(frameon = False)
plt.show()
```
![](/math/SMMovingAverageWindows.svg)

* *不同平滑次数*
```python
for ts in range(1, 5):
    RSD = gma.math.Smooth(Data, 5, Times = ts).MovingAverage()
    plt.plot(RSD, label = ts)
plt.grid(True, linestyle = (0,(6,6)), linewidth = 0.4)
plt.legend(frameon = False)
plt.show()
```
![](/math/SMMovingAverageTimes.svg)

*更多维度*

```python
Data = [[0.2775632 , 0.12230133, 0.14181635, 0.14573776, 0.26294236, 0.17534054, 0.19697314, 0.17100441],
       [0.29653988, 0.21660644, 0.27685702, 0.19734388, 0.23047971, 0.15317513, 0.14318715, 0.29095752],
       [0.10306014, 0.26547633, 0.20539848, 0.11788385, 0.20935271, 0.20853551, 0.10117026, 0.23454895],
       [0.10212869, 0.23732622, 0.29779698, 0.25204982, 0.20186597, 0.12563619, 0.12132635, 0.10949196],
       [0.24845008, 0.19504921, 0.26203447, 0.18605777, 0.15011013, 0.12348816, 0.25702251, 0.27907304],
       [0.17735726, 0.22358509, 0.30997451, 0.14726574, 0.30705883, 0.14398374, 0.12332358, 0.12161637],
       [0.10022824, 0.30212566, 0.31906632, 0.17805659, 0.28539664, 0.23701129, 0.16718833, 0.1362587 ],
       [0.12202122, 0.11896312, 0.14325725, 0.19785076, 0.22644087, 0.21387368, 0.22018365, 0.15477022]]
# 按照第一个轴平滑
SM0 = gma.math.Smooth(Data, 5, Times = 1, Axis = 0)
A0 = SM0.MovingAverage()

# 按照第二个轴平滑
SM1 = gma.math.Smooth(Data, 5, Times = 1, Axis = 1)
A1 = SM1.MovingAverage()

# 选择第一组数据制图对比
plt.plot(A0[0], label = 'Axis = 0')
plt.plot(A1[0], label = 'Axis = 1')
plt.plot(gma.math.ToNumericArray(Data)[0], label = 'Raw Data')
plt.grid(True, linestyle = (0,(6,6)), linewidth = 0.4)
plt.legend(frameon = False)
plt.show()
```

![](/math/SMMovingAverageAxis.svg)

