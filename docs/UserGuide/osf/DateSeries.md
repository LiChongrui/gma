---
title: DateSeries
date: 2021-10-30
sidebar: false
---

##  gma.osf.**DateSeries**(*StartDate, EndDate, DateDelta = 'D', Format = '%Y%m%d'*)

---

**功能：**【日期序列】。构造一个日期序列列表。

**参数：** 

&emsp;StartDate：`str`。初始日期。例如 '20200101' 。

&emsp;EndDate：`str`。结束日期。例如 '20201231' 。 

**可选参数：** 

&emsp;DateDelta = `str`。间隔时间，默认为天（'D'）。

::: tip 时间间隔
|格式|说明|示例|解释|
|:---|:---|:---|:---|
|D|天|4D|4 天|
|M|月|2M|2 个月，默认提取 月 最后一天|
|Y|年|2Y|2 年，默认提取年 最后一个月 最后一天|
|A|年|2A / A-FEB| 每 2 年 / 每年 2 月。默认提取最后一天，格式 （int）A-月份缩写|
|T|分钟|4T|4 分钟|
|S|秒|10S|10 秒|
|W|周|2W / W-FRI|2 周 / 每周的周五。格式 （int）W-星期缩写|
:::

&emsp;Format = `str`。日期序列格式。默认为 '%Y%m%d'（年月日）。

::: tip 日期序列格式
|格式|说明|格式|说明|
|:---|:---|:---|:---|
|%y|两位数的年份表示（00-99）|%Y|四位数的年份表示（000-9999）|
|%m|月份（01-12）|%d|月内中的一天（0-31）|
|%H|24小时制小时数（0-23）|%I|12小时制小时数（01-12）|
|%M|分钟数（00=59）|%S|秒（00-59）|
|%a|本地英文缩写星期名称|%A|本地英文完整星期名称|
|%b|本地缩写英文的月份名称|%B|本地完整英文的月份名称|
|%w|星期（0-6），星期天为星期的开始|%W|一年中的星期数（00-53）星期一为星期的开始|
|%x|本地相应的日期表示|%X|本地相应的时间表示|
|%Z|当前时区的名称|%U|一年中的星期数（00-53）星期天为星期的开始|
|%j|年内的一天（001-366）|%c|本地相应的日期表示和时间表示|

:::

**返回：**`DatetimeIndex`。


---

**示例：**
```python
import gma
```

*按天生成*
```python
# 按照 100 天的间隔生成日期序列
gma.osf.DateSeries('20200101', '20210101', DateDelta = '100D', Format = '%Y%m%d')
```
> \>>> DatetimeIndex(['2020-01-01', '2020-04-10', '2020-07-19', '2020-10-27'], dtype='datetime64[ns]', freq='100D')

*按月生成*
```python
# 按照 4 个月的间隔生成日期序列
gma.osf.DateSeries('20200101', '20210101', DateDelta = '4M', Format = '%Y%m%d')
```
> \>>> DatetimeIndex(['2020-01-31', '2020-05-31', '2020-09-30'], dtype='datetime64[ns]', freq='4M')

*按年生成*
```python
# 抽取每 1 年最后一天生成日期序列
gma.osf.DateSeries('20200101', '20210101', DateDelta = 'Y', Format = '%Y%m%d')
```
> \>>> DatetimeIndex(['2020-12-31'], dtype='datetime64[ns]', freq='A-DEC')

```python
# 抽取每 1 年某月最后一天生成日期序列（按照每年 2 月抽取）（A-月份名缩写）
gma.osf.DateSeries('20200101', '20210101', DateDelta = 'A-FEB', Format = '%Y%m%d')
```
> \>>> DatetimeIndex(['2020-02-29'], dtype='datetime64[ns]', freq='A-FEB')

*按小时生成*
```python
# 按照 8000 小时的间隔生成日期序列
gma.osf.DateSeries('20200101', '20210101', DateDelta = '8000H', Format = '%Y%m%d')
```
> \>>> DatetimeIndex(['2020-01-01 00:00:00', '2020-11-29 08:00:00'], dtype='datetime64[ns]', freq='8000H')

*按分钟生成*
```python
# 按照 10000 分钟的间隔生成日期序列
gma.osf.DateSeries('20200101', '20200111', DateDelta = '10000T', Format = '%Y%m%d')
```
> \>>> DatetimeIndex(['2020-01-01 00:00:00', '2020-01-07 22:40:00'], dtype='datetime64[ns]', freq='10000T')

*按秒生成*
```python
# 按照 10000 秒的间隔生成日期序列
gma.osf.DateSeries('20200101000000', '20200101040000', DateDelta = '10000S', Format = '%Y%m%d%H%M%S')
```
> \>>> DatetimeIndex(['2020-01-01 00:00:00', '2020-01-01 02:46:40'], dtype='datetime64[ns]', freq='10000S')

*按星期生成*
```python
# 提取每周的第一天（星期天）（W-星期名的缩写）
gma.osf.DateSeries('20200101', '20200121', DateDelta = 'W', Format = '%Y%m%d')
```
> \>>> DatetimeIndex(['2020-01-05', '2020-01-12', '2020-01-19'], dtype='datetime64[ns]', freq='W-SUN')


