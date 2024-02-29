---
home: true

heroText: 地理与气象分析库
tagline: 一个基于 Python 的地理、气象数据快速处理分析和地理制图函数包（Geographic and Meteorological Analysis，gma）


heroImage: /images/Logo-gma.svg

actionText: 开始探索 →
actionLink: /Introduce.md
features:
- title: 易用至上
  details: 以 Python 语法为基础，以最清晰用户指南帮助你快速实现功能应用。
- title: 开放共享
  details: 涵盖气候气象指数、遥感指数、空间绘图、栅格/矢量处理等方向近百个功能函数开放使用。
- title: 效率更新
  details: 针对算法函数不断优化升级，以最大限度提高运行效率。
---

---
## <strong>快速入手</strong>

### 安装（终端）
```bash
pip install gma
```
### 引用（IDE）
```python
## 完整引入
import gma
## 引用部分模块
## 气候气象模块，坐标参考系统，地理数据（栅格/矢量）格式， 输入输出模块，数学模块，系统交互，
## 栅格处理，遥感指数，空间杂项，矢量处理
from gma import climet, crs ,gft, io, math, osf, rasp, rsvi, smc, vesp 
## 空间绘图和内置数据
from gma.map import plot, inres 
```

### 绘图（示例）

```python
from gma import crs
from gma.map import plot, inres

# 创建一个 中央经线为 112°E 的 Bonne 投影坐标系
Proj = crs.ProjCS(ProjMethod = crs.ProjMethod.Bonne(CentralMeridian = 112))

# 0.创建一个地图框，用于制图
MapF = plot.MapFrame(BaseMapProj = Proj)

# 1.添加内置的世界国家和政区矢量
MapL1 = MapF.AddLayer(inres.WorldLayer.Country, FaceColor = None, LineColor = 'gray', LineWidth = 0.1)

# 2.添加经纬网
GridLines = MapF.AddGridLines(LONRange = (-180, 180, 30), LATRange = (-90, 90, 15), LineWidth = 0.2)

# 3.设置地图边框
Frame = MapF.SetFrame(ShowBottom = False, ShowLeft = False, ShowRight = False, ShowTop = False, FrameWidth = 0.4)
```
![](/images/Bonne.png)
