# -*- coding: utf-8 -*-
"""图片渲染探针:验证 9 个方法的示意图渲染效果,输出到 _imgwork/ 供人工查看"""
import os, sys, shutil
sys.path.insert(0, r'D:\github\gma\.vuepress\_gma341')
import numpy as np
from gma import gio
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT = r'D:\github\gma\.vuepress\_imgwork'
shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(OUT, exist_ok=True)
os.chdir(OUT)

np.random.seed(42)
arr = np.random.randint(0, 100, (2, 6, 6)).astype('float32')
ds = gio.Dataset(data=arr, crs='WGS84', geo_transform=(110, 1, 0, 32, 0, -1))

def extent_of(d):
    gt = d.geo_transform
    return (gt[0], gt[0] + d.shape[2] * gt[1], gt[3] + d.shape[1] * gt[5], gt[3])

def two_panel(before, after, extent_b, extent_a, titles=('Before', 'After'), b_cmap='viridis', a_cmap='viridis'):
    fig, axs = plt.subplots(1, 2, figsize=(9, 3.6), dpi=110)
    axs[0].imshow(before, cmap=b_cmap, extent=extent_b, origin='upper')
    axs[0].set_title(titles[0], fontsize=10)
    axs[1].imshow(after, cmap=a_cmap, extent=extent_a, origin='upper')
    axs[1].set_title(titles[1], fontsize=10)
    for ax in axs:
        ax.tick_params(labelsize=7)
    fig.tight_layout()
    return fig

# 1) plot: ds.plot() 默认对 2 波段的行为
ax = ds.plot()
fig = ax.get_figure()
print('plot: n_axes =', len(fig.axes))
fig.savefig(os.path.join(OUT, 'test_plot.png'), bbox_inches='tight')
plt.close(fig)

# 2) clip
import os as _os
WORLD = _os.path.join(_os.environ['GMA_Data'], 'world.gdb.zip')
ly = gio.open_vector(WORLD, name_or_id='GMA_World_Country_50m')
res_c = ds.clip(ly)
arc = res_c.to_numpy()[0]
print('clip band1 min/max/nodata:', np.nanmin(arc), np.nanmax(arc), res_c.nodata)
fig = two_panel(ds.to_numpy()[0], arc, extent_of(ds), extent_of(res_c))
fig.savefig(os.path.join(OUT, 'test_clip.png'))
plt.close(fig)

# 3) resample
res_r = ds.resample(0.5)
fig = two_panel(ds.to_numpy()[0], res_r.to_numpy()[0], extent_of(ds), extent_of(res_r))
fig.savefig(os.path.join(OUT, 'test_resample.png'))
plt.close(fig)

# 4) reclassify
res_q = ds.reclassify({0: 1, 50: 2, 100: 3}, method='Range')
import matplotlib.colors as mcolors
cmap_d = mcolors.ListedColormap(['#440154', '#21918c', '#fde725'])
fig = two_panel(ds.to_numpy()[0], res_q.to_numpy()[0], extent_of(ds), extent_of(res_q),
                a_cmap=cmap_d)
fig.savefig(os.path.join(OUT, 'test_reclassify.png'))
plt.close(fig)

# 5) set_palette: 调色板映射渲染
arr_b = np.random.randint(0, 100, (6, 6)).astype('uint8')
ds_b = gio.Dataset(data=arr_b, crs='WGS84', geo_transform=(110, 1, 0, 32, 0, -1))
ds_b.set_palette({10: (200, 50, 100, 255), 20: (100, 200, 50, 255)})
pal = ds_b.get_palette()
print('palette N:', pal.N)
fig, axs = plt.subplots(1, 2, figsize=(9, 3.6), dpi=110)
axs[0].imshow(arr_b, cmap='gray'); axs[0].set_title('Before', fontsize=10)
axs[1].imshow(arr_b, cmap=pal); axs[1].set_title('After', fontsize=10)
for ax_ in axs: ax_.tick_params(labelsize=7)
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'test_set_palette.png'))
plt.close(fig)

# 6) to_crs
res_p = ds.to_crs('EPSG:3857')
print('to_crs bounds:', res_p.bounds)
fig = two_panel(ds.to_numpy()[0], res_p.to_numpy()[0], extent_of(ds), extent_of(res_p))
fig.savefig(os.path.join(OUT, 'test_to_crs.png'))
plt.close(fig)

# 7) isopleth: 左栅格 + 右叠加等值线
iso = ds.isopleth(interval=30)
fig, axs = plt.subplots(1, 2, figsize=(9, 3.6), dpi=110)
axs[0].imshow(ds.to_numpy()[0], cmap='viridis', extent=extent_of(ds), origin='upper')
axs[0].set_title('Before', fontsize=10)
axs[1].imshow(ds.to_numpy()[0], cmap='viridis', extent=extent_of(ds), origin='upper')
try:
    iso.plot(ax=axs[1], color='red')
    print('iso.plot ok on ax')
except Exception as e:
    print('iso.plot err:', e)
axs[1].set_title('After', fontsize=10)
for ax_ in axs: ax_.tick_params(labelsize=7)
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'test_isopleth.png'))
plt.close(fig)

# 8) to_layer: 左栅格 + 右叠加矢量化多边形
lay = ds.to_layer()
fig, axs = plt.subplots(1, 2, figsize=(9, 3.6), dpi=110)
axs[0].imshow(ds.to_numpy()[0], cmap='viridis', extent=extent_of(ds), origin='upper')
axs[0].set_title('Before', fontsize=10)
axs[1].imshow(ds.to_numpy()[0], cmap='viridis', extent=extent_of(ds), origin='upper')
try:
    lay.plot(ax=axs[1], facecolor='none', edgecolor='red')
    print('lay.plot ok on ax')
except Exception as e:
    print('lay.plot err:', e)
axs[1].set_title('After', fontsize=10)
for ax_ in axs: ax_.tick_params(labelsize=7)
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'test_to_layer.png'))
plt.close(fig)

# 9) gen_lonlat: 经度/纬度两面板
res_g = ds.gen_lonlat()
fig, axs = plt.subplots(1, 2, figsize=(9, 3.6), dpi=110)
axs[0].imshow(res_g.to_numpy()[0], cmap='viridis', extent=extent_of(res_g), origin='upper')
axs[0].set_title('Band 1: Longitude', fontsize=10)
axs[1].imshow(res_g.to_numpy()[1], cmap='viridis', extent=extent_of(res_g), origin='upper')
axs[1].set_title('Band 2: Latitude', fontsize=10)
for ax_ in axs: ax_.tick_params(labelsize=7)
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'test_gen_lonlat.png'))
plt.close(fig)

print('DONE ->', OUT)
