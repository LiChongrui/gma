---
title: 常量单位
date: 2021-10-29
---

&emsp;&emsp;  从 **1.0.6** 版本开始，gma 定义和引用的常量名称、值等内置在 gma.relation.constants 模块中。各个常量或单位的类型均为**字典**，以下列出了 gma 中引定义的常量或单位。

## 数学常量

| 名称（key） | 值（value）       | 解释     |
| :---------- | :---------------- | :------- |
| pi          | 3.141592653589793 | 圆周率   |
| golden      | 1.618033988749895 | 黄金分割 |
| e           | 2.718281828459045 | 自然常数 |

## 国际单位制词头

| 名称（key） | 值（value） | 名称（key） | 值（value） | 名称（key） | 值（value） |
| :---------- | :---------- | ----------- | ----------- | ----------- | ----------- |
| yotta       | $10^{24}$   | kilo        | $10^{3}$    | micro       | $10^{-6}$   |
| zetta       | $10^{21}$   | hecto       | $10^{2}$    | nano        | $10^{-9}$   |
| exa         | $10^{18}$   | deka        | $10^{1}$    | pico        | $10^{-12}$  |
| peta        | $10^{15}$   | deci        | $10^{-1}$   | femto       | $10^{-12}$  |
| tera        | $10^{12}$   | centi       | $10^{-2}$   | atto        | $10^{-18}$  |
| giga        | $10^{9}$    | milli       | $10^{-3}$   | zepto       | $10^{-21}$  |
| mega        | $10^{6}$    |             |             |             |             |

## 二进制单位

| 名称（key）                     | B    | KB       | MB       | GB       | TB       | PB       | EB       | ZB       | YB       |
| :------------------------------ | :--- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 值（value）-- 每单位比特数（B） | 1    | $2^{10}$ | $2^{20}$ | $2^{30}$ | $2^{40}$ | $2^{50}$ | $2^{60}$ | $2^{70}$ | $2^{80}$ |

## 物理常量

| 物理量（key） | 值（2018年修订）       | 误差     | 单位                    | 长名称                                    | 长名称对照           |
| :------------ | :--------------------- | :------- | :---------------------- | :---------------------------------------- | :------------------- |
| c             | 299792458              | 0        | $m · s^{-1}$            | Vacuum Speed Of Light                     | 真空光速             |
| mu_0          | 1.25663706212e-6       | 1.9e-16  | $N · A^{-2}$            | Vacuum Magnetic Permeability              | 真空磁导率           |
| ε0            | 8.8541878128e-12       | 1.3e-21  | $F · m^{-1}$            | Vacuum Electric Permittivity              | 真空介电常数         |
| h             | 6.62607015e-34         | 0        | $J · Hz^{-1}$           | Planck Constant                           | 普朗克常数           |
| hbar          | 1.0545718176461565e-34 | 0        | -                       | Reduced Planck Constant                   | 约化普朗克常数       |
| G             | 6.67430e-11            | 1.5e-15  | $m^3 · kg^{-1}· s^{-2}$ | Gravitational Constant                    | 万有引力常量         |
| g             | 9.80665                | 0        | $m · s^{-2}$            | Acceleration Of Gravity                   | 标准重力加速度       |
| e             | 1.602176634e-19        | 0        | $C$                     | Elementary Charge                         | 基本电荷             |
| R             | 8.314462618            | 0        | $J · mol^{-1} · K^{-1}$ | Molar Gas Constant                        | 摩尔气体常数         |
| α             | 7.2973525693e-3        | 1.1e-12  | -                       | Fine Structure Constant                   | 精细结构常数         |
| N_A           | 6.02214076e23          | 0        | $mol^{-1}$              | Avogadro Constant                         | 阿伏伽德罗常数       |
| k             | 1.380649e-23           | 0        | $J · K^{-1}$            | Boltzmann Constant                        | 玻尔兹曼常数         |
| σ             | 5.670374419e-8         | 0        | $W · m^{-2} · K^{-4}$   | Stefan Boltzmann Constant                 | 斯蒂芬-玻尔兹曼常数  |
| b             | 2.897771955e-3         | 0        | $m · K$                 | Wien Wavelength Displacement Law Constant | 维恩波长位移定律常数 |
| Ry            | 10973731.568160        | 0.000021 | $m^{-1}$                | Rydberg Constant                          | 里德堡常数           |

## 质量单位

| 名称（key） | 值（value）-- 每单位千克（kg）数 | 简写  | 对照           |
| :---------- | :------------------------------- | :---- | :------------- |
| kilogram    | 1                                | kg    | 千克           |
| gram        | 0.001                            | g     | 克             |
| milligram   | 1e-6                             | mg    | 毫克           |
| microgram   | 1e-9                             | μg    | 微克           |
| ton         | 1000.0                           | t     | 吨             |
| kintal      | 100                              | g     | 公担           |
| pound       | 0.45359236999999997              | lb    | 磅，英国常衡磅 |
| ounce       | 0.028349523124999998             | oz    | 盎司           |
| carat       | 0.0002                           | ct    | 克拉           |
| grain       | 0.0000648                        | gr    | 格令           |
| long ton    | 1016.0469088                     | lt    | 长吨           |
| short ton   | 907.1847399999999                | stone | 英石           |
| troy ounce  | 0.031103476799999998             | toz   | 金衡盎司       |
| troy pound  | 0.37324172159999996              | tp    | 金衡制磅       |
| electron    | 9.1093837015e-31                 | m_e   | 电子质量       |
| proton      | 1.67262192369e-27                | m_p   | 质子质量       |
| neutron     | 1.67492749804e-27                | m_n   | 中子质量       |
| atomic      | 1.66053906660e-27                | m_a   | 原子质量       |

## 角度单位

| 名称（key） | 值（value）-- 每单位弧度（rad） | 简写 | 对照 |
| :---------- | :------------------------------ | ---- | :--- |
| radian      | 1.0                             | rad  | 弧度 |
| degree      | 0.017453292519943295            | °    | 度   |
| arcmin      | 0.000290888208665               | ′    | 弧分 |
| arcsec      | 4.84813681109536e-06            | ″    | 弧秒 |

## 时间单位

| 名称（key） | 值（value）-- 每单位秒（s）数 | 简写 | 对照   |
| :---------- | :---------------------------- | ---- | :----- |
| second      | 1.0                           | s    | 秒     |
| minute      | 60.0                          | m    | 分     |
| hour        | 3600.0                        | h    | 时     |
| day         | 86400.0                       | d    | 日     |
| week        | 604800.0                      | w    | 周     |
| year        | 31536000.0                    | y    | 年     |
| Julian year | 31557600.0                    | j    | 儒略年 |

## 长度单位

| 名称（key）       | 值（value）-- 每单位米（m）数 | 简写 | 对照             |
| :---------------- | :---------------------------- | ---- | :--------------- |
| meter             | 1.0                           | m    | 米               |
| decimeter         | 0.1                           | dm   | 分米             |
| centimeter        | 0.01                          | cm   | 厘米             |
| millimeter        | 0.001                         | mm   | 毫米             |
| micron            | 1e-6                          | μm   | 微米             |
| picometer         | 1e-12                         | pm   | 皮米             |
| fermi             | 1e-15                         | fm   | 费米             |
| kilometer         | 1000.0                        | km   | 千米             |
| inch              | 0.0254                        | in   | 英寸             |
| foot              | 0.30479999999999996           | ft   | 英尺             |
| yard              | 0.9143999999999999            | yd   | 码               |
| mile              | 1609.3439999999998            | mi   | 英里             |
| mil               | 2.5399999999999997e-05        | mil  | 密尔             |
| point             | 0.00035277777777777776        | pt   | 点，字体大小单位 |
| survey foot       | 0.3048006096012192            | sft  | 测量英尺         |
| survey mile       | 1609.3472186944373            | smi  | 测量英里         |
| nautical mile     | 1852.0                        | nmi  | 海里             |
| angstrom          | 1e-10                         | a    | 埃，埃格斯特朗   |
| astronomical unit | 149597870691.0                | au   | 天文单位         |
| light year        | 9460730472580800.0            | ly   | 光年             |
| parsec            | 3.0856775813057292e+16        | pc   | 秒差距           |

## 压强单位

| 名称（key） | 值（value）-- 每单位帕斯卡（Pa）数 | 简写 | 对照          |
| :---------- | :--------------------------------- | ---- | :------------ |
| pascal      | 1.0                                | Pa   | 帕斯卡        |
| hectopascal | 100.0                              | hPa  | 百帕          |
| kilopascal  | 1000.0                             | kPa  | 千帕          |
| megapascal  | 1000000.0                          | mPa  | 兆帕          |
| atmosphere  | 101325.0                           | atm  | 标准大气压    |
| bar         | 100000.0                           | b    | 巴            |
| mmHg        | 133.32236842105263                 | mmHg | 毫米汞柱      |
| psi         | 6894.757293168361                  | psi  | 磅力/平方英寸 |

## 面积单位

| 名称（key）       | 值（value）-- 每单位平方米（$m^2$）数 | 简写   | 对照     |
| :---------------- | :------------------------------------ | ------ | :------- |
| square meter      | 1.0                                   | $m^2$  | 平方米   |
| square millimeter | 1e-6                                  | $mm^2$ | 平方毫米 |
| square centimeter | 0.0001                                | $cm^2$ | 平方厘米 |
| square decimeter  | 0.01                                  | $dm^2$ | 平方分米 |
| square kilometers | 1000000.0                             | $km^2$ | 平方千米 |
| hectare           | 1e4                                   | ha     | 公顷     |
| acre              | 4046.8564223999992                    | acre   | 英亩     |
| mu                | 666.6666667                           | mu     | 亩       |

## 体积单位

| 名称（key）      | 值（value）-- 每单位立方米（$m^3$）数 | 简写      | 对照         |
| :--------------- | :------------------------------------ | --------- | :----------- |
| cubic meter      | 1.0                                   | $m^3$     | 立方米       |
| cubic kilometer  | 1000000000                            | $km^3$    | 立方千米     |
| cubic decimeter  | 0.001                                 | $dm^3$    | 立方分米     |
| cubic centimeter | 1e-6                                  | $cm^3$    | 立方厘米     |
| cubic millimeter | 1e-9                                  | $mm^3$    | 立方毫米     |
| liter            | 0.001                                 | l         | 升           |
| milliliter       | 1e-6                                  | ml        | 毫升         |
| gallon           | 0.0037854117839999997                 | gal       | 加仑         |
| fluid ounce      | 2.9573529562499998e-05                | fl oz     | 液量盎司     |
| barrel           | 0.15898729492799998                   | bbl       | （原油）桶   |
| gallon imp       | 0.00454609                            | gla imp   | 英制加仑     |
| fluid ounce imp  | 2.84130625e-05                        | fl oz imp | 英制液量盎司 |

## 速度单位

| 名称（key） | 值（value）-- 每单位等于多少米每秒（m/s） | 简写 | 对照       |
| :---------- | :---------------------------------------- | ---- | :--------- |
| mps         | 1.0                                       | mps  | 米每秒     |
| kmh         | 0.2777777777777778                        | kmh  | 千米每小时 |
| mph         | 0.44703999999999994                       | mph  | 英里每小时 |
| sound       | 340.5                                     | sos  | 音速       |
| knot        | 0.5144444444444445                        | kn   | 节         |

## 温度单位

| 名称（key）                  | 值（value）-- 每单位开尔文（K）数 | 简写 | 对照       |
| :--------------------------- | :-------------------------------- | ---- | :--------- |
| Kelvin                       | 1.0                               | K    | 开氏度     |
| Kelvin per degree Celsius    | 1.0                               | ℃    | 单位摄氏度 |
| Kelvin per degree Fahrenheit | 0.5555555555555556                | ℉    | 单位华氏度 |
| zero Celsius                 | 273.15                            | -    | 0 摄氏度   |
| zero Fahrenheit              | 255.3722222                       | -    | 0 华氏度   |

## 能量单位

| 名称（key）    | 值（value）-- 每单位焦耳（J）数 | 简写   | 对照         |
| :------------- | :------------------------------ | ------ | :----------- |
| Joule          | 1.0                             | J      | 焦耳         |
| electron Volt  | 1.602176634e-19                 | eV     | 电子伏特     |
| calorie        | 4.184                           | cal    | 卡路里       |
| calorie IT     | 4.1868                          | cal IT | 国际蒸汽表卡 |
| erg            | 1e-7                            | erg    | 尔格         |
| ton TNT        | 4184000000.0                    | t TNT  | 吨 TNT       |
| btu th         | 1054.3502644888888              | btu th | 英热单位     |
| kilowatt hours | 3600000.0                       | kWh    | 千瓦时       |
| watt hour      | 3600.0                          | Wh     | 瓦时         |

## 功率单位

| 名称（key） | 值（value）-- 每单位瓦特（W）数 | 简写 | 对照 |
| :---------- | :------------------------------ | ---- | :--- |
| watt        | 1.0                             | W    | 瓦特 |
| horsepower  | 745.6998715822701               | hp   | 马力 |
| kilowatt    | 1000.0                          | kW   | 千瓦 |

## 力单位

| 名称（key）    | 值（value）-- 每单位牛顿（N）数 | 简写 | 对照   |
| :------------- | :------------------------------ | ---- | :----- |
| Newton         | 1.0                             | N    | 牛顿   |
| dyn            | 1e-5                            | dyn  | 达因   |
| pound force    | 4.4482216152605                 | lbf  | 磅力   |
| kilogram force | 9.80665                         | kgf  | 千克力 |