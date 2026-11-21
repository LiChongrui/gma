import os, sys, tempfile, shutil
sys.path.insert(0, r'D:\github\gma\.vuepress\_gma341')
from gma import gio

SRC = r'D:\BaiduNetdiskDownload\ne\第3章'
WORK = tempfile.mkdtemp(prefix='ftprobe3_')
for f in os.listdir(SRC):
    shutil.copy(os.path.join(SRC, f), os.path.join(WORK, f))
os.chdir(WORK)

ly = gio.open_vector('Australia.shp')
a = ly.get_feature(0)
b = ly.get_feature(0)
print('same object on repeated get_feature:', a is b, '| a.fid:', a.fid, '| b.fid:', b.fid)
c = ly.get_feature(1)
print('feature1 fid:', c.fid, '| name:', c.fields['name'])
a.update(c)
d = ly.get_feature(0)
print('after a.update(c): d.fid', d.fid, '| d.name', d.fields['name'], '| a is d:', a is d)
print('get_feature(1) after:', ly.get_feature(1).fid, ly.get_feature(1).fields['name'])

# 干净 layer 的 fid
ly2 = gio.open_vector('Australia.shp')
f = ly2.get_feature(0)
print('\nfresh layer f0.fid:', f.fid, '| name:', f.fields['name'])
o = ly2.get_feature(2)
print('fresh layer f2.fid:', o.fid, '| name:', o.fields['name'])
print('f.update(f2) ->', f.update(o))
print('f after update: fid', f.fid, '| name', f.fields['name'], '| bounds', tuple(round(x,2) for x in f.geom.bounds))

# 构造：geom + values + ftypes（不传 gtype/crs）
ly3 = gio.open_vector('Australia.shp')
src = ly3.get_feature(0)
try:
    nf = gio.Feature(geom=src.geom, values=list(src.fields.values()), ftypes=src.ftypes)
    print('\nconstruct(geom, values, ftypes) OK:', type(nf).__name__, '| fid:', nf.fid,
          '| n fields:', len(nf.fields), '| name:', nf.fields.get('name'), '| crs:', repr(nf.crs))
except Exception as e:
    print('\nconstruct FAIL:', type(e).__name__, e)

# ftypes 访问方式
print('\nftypes type:', type(src.ftypes).__name__)
print('dir:', [m for m in dir(src.ftypes) if not m.startswith('_')][:40])
try:
    print('first item repr:', repr(src.ftypes[0])[:200])
except Exception as e:
    print('index FAIL:', type(e).__name__, e)
try:
    print('featurecla type:', repr(src.ftypes['featurecla'])[:200])
except Exception as e:
    print('key FAIL:', type(e).__name__, e)

# fields 选取
print('\nselected fields:', {k: src.fields[k] for k in ('name', 'iso_3166_2', 'type', 'scalerank')})
print('geom to_str head:', src.geom.to_str()[:90])
print('geom bounds:', src.geom.bounds)
print('geom area:', src.geom.get_area())
print('PROBE3 DONE')
