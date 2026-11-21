import os, sys, tempfile, shutil, inspect
sys.path.insert(0, r'D:\github\gma\.vuepress\_gma341')
from gma import gio
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SRC = r'D:\BaiduNetdiskDownload\ne\第3章'
WORK = tempfile.mkdtemp(prefix='ftprobe2_')
for f in os.listdir(SRC):
    shutil.copy(os.path.join(SRC, f), os.path.join(WORK, f))
os.chdir(WORK)
ly = gio.open_vector('Australia.shp')

print('=== all features ===')
for i in range(len(ly)):
    f = ly.get_feature(i)
    print(i, '| fid:', f.fid, '| name:', repr(f.fields.get('name')), '| iso:', f.fields.get('iso_3166_2'),
          '| type:', f.fields.get('type'), '| bounds:', tuple(round(x, 2) for x in f.geom.bounds))

f0 = ly.get_feature(0)
print('\n=== field repr length ===')
print('fields n=', len(f0.fields), '| repr len=', len(repr(f0.fields)))
print('ftypes repr lines=', len(str(f0.ftypes).splitlines()), '| repr len=', len(repr(f0.ftypes)))
print('geom to_str head:', f0.geom.to_str()[:160])
print('crs repr:', repr(f0.crs))

print('\n=== construct from real data ===')
try:
    fnew = gio.Feature(geom=f0.geom, values=list(f0.fields.values()), gtype='Polygon',
                       ftypes=f0.ftypes, crs=f0.crs)
    print('construct OK:', type(fnew).__name__, '| fid:', fnew.fid, '| fields n:', len(fnew.fields),
          '| gtype:', fnew.geom.gtype, '| crs:', repr(fnew.crs))
    print('new name:', fnew.fields.get('name'), '| bounds:', fnew.geom.bounds)
except Exception as e:
    print('construct FAIL:', type(e).__name__, e)

print('\n=== update details ===')
f = ly.get_feature(0)
other = ly.get_feature(1)
print('before: fid', f.fid, '| name', f.fields['name'], '| bounds', tuple(round(x,2) for x in f.geom.bounds))
print('other : fid', other.fid, '| name', other.fields['name'])
r = f.update(other)
print('after update: ret', repr(r), '| fid', f.fid, '| name', f.fields['name'], '| bounds', tuple(round(x,2) for x in f.geom.bounds))

print('\n=== copy independence ===')
a = ly.get_feature(0)
b = a.copy()
b.set_fid(777)
print('a.fid:', a.fid, '| b.fid:', b.fid, '| a name:', a.fields['name'], '| b name:', b.fields['name'])

print('\n=== set_geom detail ===')
c = ly.get_feature(0)
g = ly.get_feature(1).geom
c.set_geom(g)
print('after set_geom: bounds', c.geom.bounds, '| name (unchanged):', c.fields['name'], '| fid:', c.fid)

print('\n=== geom plot on layer background ===')
fig, axs = plt.subplots(1, 2, figsize=(11, 4.5), dpi=110)
ly.plot(ax=axs[0], facecolor='none', edgecolor='gray')
axs[0].set_title('Before: all features', fontsize=10)
ly.plot(ax=axs[1], facecolor='none', edgecolor='gray')
f0.plot(ax=axs[1], facecolor='none', edgecolor='red', linewidth=1.5)
axs[1].set_title('After: feature 0 highlighted', fontsize=10)
fig.tight_layout()
fig.savefig(os.path.join(r'D:\github\gma\.vuepress\_imgwork', 'ft_probe_context.png'), dpi=110)
plt.close('all')
print('saved ft_probe_context.png')
print('PROBE2 DONE')
