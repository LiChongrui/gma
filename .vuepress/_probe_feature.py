import os, sys, tempfile, shutil, inspect
sys.path.insert(0, r'D:\github\gma\.vuepress\_gma341')
from gma import gio          # gma 必须第一个导入（不然 matplotlib/hashlib 的 DLL 冲突）
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SRC = r'D:\BaiduNetdiskDownload\ne\第3章'
WORK = tempfile.mkdtemp(prefix='ftprobe_')
for f in ('HYP_50M_SR_W.tif', 'Australia.shp'):
    shutil.copy(os.path.join(SRC, f), os.path.join(WORK, f))
for ext in ('.dbf', '.shx', '.prj', '.cpg'):
    p = os.path.join(SRC, 'Australia' + ext)
    if os.path.exists(p):
        shutil.copy(p, os.path.join(WORK, 'Australia' + ext))
os.chdir(WORK)

ly = gio.open_vector('Australia.shp')
print('layer:', ly.gtype, len(ly))
print('layer attrs:', [m for m in dir(ly) if not m.startswith('_')][:45])
ft = ly.get_feature(0)
print('\n=== feature base ===')
print('fid:', ft.fid)
print('fields:', repr(ft.fields)[:300])
print('ftypes:', repr(ft.ftypes)[:200])
print('geom:', type(ft.geom).__name__, '| gtype:', ft.geom.gtype)
print('geom attrs:', [m for m in dir(ft.geom) if not m.startswith('_')][:60])
print('crs:', repr(ft.crs)[:200])

print('\n=== method signatures / returns ===')
for name in ('copy', 'plot', 'set_fid', 'set_geom', 'update'):
    m = getattr(ft, name)
    try:
        sig = inspect.signature(m)
    except Exception as e:
        sig = 'ERR ' + str(e)
    print(name, sig, '| doc:', (inspect.getdoc(m) or '')[:160].replace('\n', ' '))

# 返回值实测
r = ft.copy()
print('copy ->', type(r).__name__, '| fid:', r.fid, '| is self:', r is ft)
r2 = ft.set_fid(999)
print('set_fid ->', repr(r2), '| ft.fid:', ft.fid)
g2 = ly.get_feature(1).geom
r3 = ft.set_geom(g2)
print('set_geom ->', repr(r3), '| new gtype:', ft.geom.gtype, '| bounds:', ft.geom.bounds)
other = ly.get_feature(2)
r4 = ft.update(other)
print('update ->', repr(r4), '| ft.fid:', ft.fid, '| fields:', repr(ft.fields)[:150])

print('\n=== plot ===')
ft0 = ly.get_feature(0)
print('plot sig:', inspect.signature(ft0.plot))
print('plot doc:', (inspect.getdoc(ft0.plot) or '')[:350].replace('\n', ' '))
fig, ax = plt.subplots(figsize=(6, 5), dpi=110)
try:
    ret = ft0.plot(ax=ax, facecolor='none', edgecolor='red')
    print('plot(ax=) ->', type(ret).__name__, '| collections:', len(ax.collections), '| patches:', len(ax.patches))
    fig.savefig(os.path.join(r'D:\github\gma\.vuepress\_imgwork', 'ft_probe_plot.png'), dpi=110)
    plt.close('all')
except Exception as e:
    print('plot(ax=) FAIL:', type(e).__name__, e)

fig, ax = plt.subplots(figsize=(6, 5), dpi=110)
try:
    ret = ft0.plot(ax=ax)
    print('plot(ax= default) ->', type(ret).__name__, '| collections:', len(ax.collections))
    fig.savefig(os.path.join(r'D:\github\gma\.vuepress\_imgwork', 'ft_probe_plot_default.png'), dpi=110)
    plt.close('all')
except Exception as e:
    print('plot default FAIL:', type(e).__name__, e)

print('PROBE DONE')
