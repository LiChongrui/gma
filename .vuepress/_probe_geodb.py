import os, sys, tempfile, shutil, inspect
sys.path.insert(0, r'D:\github\gma\.vuepress\_gma341')
from gma import gio

SRC = r'D:\BaiduNetdiskDownload\ne'
WORK = tempfile.mkdtemp(prefix='gdbprobe_')
for f in ('NewGDB.gpkg', '第2章/SuiTangLuoyang.gpkg'):
    shutil.copy(os.path.join(SRC, f), os.path.join(WORK, os.path.basename(f)))
os.chdir(WORK)

gdb = gio.open_file('NewGDB.gpkg')
print('=== base ===')
print('type:', type(gdb).__name__, '| driver:', gdb.driver, '| name:', gdb.name)
print('layers:', gdb.layer_names, '| count:', gdb.layer_count)
print('datasets:', gdb.dataset_names, '| count:', gdb.dataset_count)

print('\n=== iteritems ===')
for cat in (None, 'vector', 'raster'):
    try:
        it = gdb.iteritems(cat) if cat else gdb.iteritems()
        items = list(it)
        print(cat, '->', [(str(k), type(v).__name__) for k, v in items])
    except Exception as e:
        print(cat, 'FAIL:', type(e).__name__, e)

print('\n=== query ===')
try:
    q = gdb.query('SELECT * FROM Australia LIMIT 3')
    print('query ->', type(q).__name__, q.gtype, len(q), q.bounds)
except Exception as e:
    print('query FAIL:', type(e).__name__, e)

print('\n=== get_dataset ===')
try:
    d = gdb.get_dataset(0)
    print('get_dataset(0) ->', type(d).__name__, d.shape)
except Exception as e:
    print('get_dataset(0) FAIL:', type(e).__name__, e)

print('\n=== create/delete/add layer (on a fresh copy) ===')
g2 = gio.open_file('NewGDB.gpkg')
for name, fn in [
    ('create_layer', lambda: g2.create_layer('test_layer', crs='WGS84', gtype='Point')),
    ('add_layer', lambda: g2.add_layer(gio.open_vector('NewGDB.gpkg', name_or_id='Australia'), new_name='aus_copy')),
    ('delete_layer', lambda: g2.delete_layer('test_layer')),
]:
    try:
        r = fn()
        print(name, '->', repr(r), '| layers:', g2.layer_names)
    except Exception as e:
        print(name, 'FAIL:', type(e).__name__, e)

print('\n=== new empty gdb with raster ===')
try:
    g3 = gio.GeoDatabase(driver='GPKG', out_dst='empty.gpkg')
    print('new:', type(g3).__name__, g3.driver, g3.layer_names, g3.dataset_names)
except Exception as e:
    print('new FAIL:', type(e).__name__, e)
print('PROBE DONE')
