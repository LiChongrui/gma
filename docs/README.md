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
  details: 涵盖指数运算、数学运算、系统交互、空间杂项、栅格处理、栅格分析、矢量处理等方向近百个功能函数开放使用。
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
from gma import climet # 气候气象模块
from gma import crs # 坐标参考系统
from gma import gft # 地理数据（栅格/矢量）格式
from gma import io # 输入输出模块
from gma import math # 数学模块
from gma import osf # 系统交互
from gma import rasp # 栅格处理
from gma import rsvi # 遥感指数
from gma import smc # 空间杂项
from gma import vesp # 矢量处理
from gma.map import plot, inres # 空间绘图，内置数据
```
