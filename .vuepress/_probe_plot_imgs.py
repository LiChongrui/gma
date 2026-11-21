# -*- coding: utf-8 -*-
"""Probe: 用 ds.plot() 直接出图做前后对比的可行性验证。
注意: gma 必须先于 matplotlib 导入。
"""
import os, sys
sys.path.insert(0, r'D:\github\gma\.vuepress\_gma341')
import numpy as np
from gma import gio
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT = r'D:\github\gma\.vuepress\_imgwork'
os.makedirs(OUT, exist_ok=True)

np.random.seed(42)
arr = np.random.randint(0, 100, (2, 6, 6)).astype('float32')
ds = gio.Dataset(data=arr, crs='WGS84', geo_transform=(110, 1, 0, 32, 0, -1))

def save(fig, name):
    fig.savefig(os.path.join(OUT, f'probe_{name}.png'), dpi=110)
    plt.close('all')
    print('saved', name)

# 1. 默认 plot 出图长什么样
try:
    ax = ds.plot()
    print('default plot type:', type(ax).__name__)
    save(ax.get_figure(), 'default')
except Exception as e:
    print('default plot FAIL:', type(e).__name__, e)

# 2. ax 参数: 两个子图分别画 ds 和 res
try:
    res = ds.resample(0.5)
    fig, axs = plt.subplots(1, 2, figsize=(9, 3.6), dpi=110)
    ds.plot(ax=axs[0])
    res.plot(ax=axs[1])
    axs[0].set_title('Before', fontsize=10)
    axs[1].set_title('After', fontsize=10)
    save(fig, 'axparam')
except Exception as e:
    print('ax param FAIL:', type(e).__name__, e)

# 3. clip: 结果带 nodata, 看 plot 是否自动处理
try:
    WORLD = os.path.join(os.environ['GMA_Data'], 'world.gdb.zip')
    ly = gio.open_vector(WORLD, name_or_id='GMA_World_Country_50m')
    resc = ds.clip(ly)
    fig, axs = plt.subplots(1, 2, figsize=(11, 3.6), dpi=110)
    ds.plot(ax=axs[0])
    resc.plot(ax=axs[1])
    axs[0].set_title('Before', fontsize=10)
    axs[1].set_title('After', fontsize=10)
    save(fig, 'clip')
except Exception as e:
    print('clip plot FAIL:', type(e).__name__, e)

# 4. 调色板: 两个独立数据集(避免绘图延迟互相污染), 看 plot 是否自动应用 palette
try:
    arr_b = np.random.choice([10, 20], (6, 6)).astype('uint8')
    ds_b1 = gio.Dataset(data=arr_b, crs='WGS84', geo_transform=(110, 1, 0, 32, 0, -1))
    ds_b2 = gio.Dataset(data=arr_b, crs='WGS84', geo_transform=(110, 1, 0, 32, 0, -1))
    ds_b2.set_palette({10: (200, 50, 100, 255), 20: (100, 200, 50, 255)})
    fig, axs = plt.subplots(1, 2, figsize=(9, 3.6), dpi=110)
    ds_b1.plot(ax=axs[0])
    ds_b2.plot(ax=axs[1])
    axs[0].set_title('Before', fontsize=10)
    axs[1].set_title('After', fontsize=10)
    save(fig, 'palette')
except Exception as e:
    print('palette plot FAIL:', type(e).__name__, e)

# 5. to_crs: 度 -> 米
try:
    rest = ds.to_crs('EPSG:3857')
    fig, axs = plt.subplots(1, 2, figsize=(9, 3.6), dpi=110)
    ds.plot(ax=axs[0])
    rest.plot(ax=axs[1])
    axs[0].set_title('Before', fontsize=10)
    axs[1].set_title('After', fontsize=10)
    save(fig, 'tocrs')
except Exception as e:
    print('to_crs plot FAIL:', type(e).__name__, e)

# 6. isopleth: 在 ds.plot() 返回的 ax 上叠加
try:
    iso = ds.isopleth(interval=30)
    ax = ds.plot()
    iso.plot(ax=ax, edgecolor='red')
    save(ax.get_figure(), 'isopleth_overlay')
except Exception as e:
    print('isopleth overlay FAIL:', type(e).__name__, e)

# 7. gen_lonlat: bands=1/2 分别出图
try:
    resg = ds.gen_lonlat()
    fig, axs = plt.subplots(1, 2, figsize=(9, 3.6), dpi=110)
    resg.plot(ax=axs[0], bands=1)
    resg.plot(ax=axs[1], bands=2)
    axs[0].set_title('Band 1: Longitude', fontsize=10)
    axs[1].set_title('Band 2: Latitude', fontsize=10)
    save(fig, 'lonlat')
except Exception as e:
    print('lonlat plot FAIL:', type(e).__name__, e)

# 8. reclassify
try:
    resr = ds.reclassify({0: 1, 50: 2, 100: 3}, method='Range')
    fig, axs = plt.subplots(1, 2, figsize=(9, 3.6), dpi=110)
    ds.plot(ax=axs[0])
    resr.plot(ax=axs[1])
    axs[0].set_title('Before', fontsize=10)
    axs[1].set_title('After', fontsize=10)
    save(fig, 'reclassify')
except Exception as e:
    print('reclassify plot FAIL:', type(e).__name__, e)

# 9. to_layer: 多边形边界叠加在 ds.plot() 返回的 ax 上
try:
    lay = ds.to_layer()
    ax = ds.plot()
    lay.plot(ax=ax, facecolor='none', edgecolor='red')
    save(ax.get_figure(), 'to_layer_overlay')
except Exception as e:
    print('to_layer overlay FAIL:', type(e).__name__, e)

print('ALL DONE')
