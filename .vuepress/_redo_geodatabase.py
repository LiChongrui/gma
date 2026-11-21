import sys
sys.path.insert(0, r'D:\github\gma\.vuepress\_gio_doc_common.py')
from _gio_doc_common import run, prepare_extra

prepare_extra([(r'D:\BaiduNetdiskDownload\ne\NewGDB.gpkg', 'NewGDB.gpkg')])

BASE = '''from gma import gio

gdb = gio.open_file('NewGDB.gpkg')       # the real GeoPackage from the sample data

print('driver:', gdb.driver)
print('layers:', gdb.layer_names)
print('count :', gdb.layer_count)'''

EXAMPLES = {
'add_layer': '''from gma import gio

gdb = gio.open_file('NewGDB.gpkg')
ly = gio.open_vector('Australia.shp')

gdb.add_layer(ly, new_name='australia_copy')
print(gdb.layer_names)''',

'create_layer': '''from gma import gio

gdb = gio.GeoDatabase(driver='GPKG', out_dst='new.gpkg')
print('Before:', gdb.layer_names)

lyr = gdb.create_layer('cities', crs='WGS84', gtype='Point')
print('After :', gdb.layer_names)
print('Name  :', lyr.name, type(lyr).__name__, lyr.gtype)''',

'delete_layer': '''from gma import gio

gdb = gio.GeoDatabase(driver='GPKG', out_dst='delete.gpkg')
gdb.create_layer('tmp_layer', crs='WGS84', gtype='Point')
print('Before:', gdb.layer_names)

gdb.delete_layer('tmp_layer')
print('After :', gdb.layer_names)''',

'get_dataset': '''from gma import gio

gdb = gio.open_file('NewGDB.gpkg')
print('datasets:', gdb.dataset_names)

try:
    ds = gdb.get_dataset(0)
except Exception as e:
    print('get_dataset(0):', type(e).__name__, e)''',

'get_layer': '''from gma import gio

gdb = gio.open_file('NewGDB.gpkg')

ly = gdb.get_layer('Australia')
print(type(ly).__name__, ly.name, ly.gtype, len(ly))
print('bounds:', tuple(round(v, 2) for v in ly.bounds))''',

'iteritems': '''from gma import gio

gdb = gio.open_file('NewGDB.gpkg')

for item in gdb.iteritems(0):            # 0 / 'Layer': vector layers
    print(type(item).__name__, item.name, item.gtype, len(item))''',

'query': '''from gma import gio

gdb = gio.open_file('NewGDB.gpkg')

res = gdb.query('SELECT * FROM Australia LIMIT 3')
print(type(res).__name__, res.gtype, len(res))
print('bounds:', tuple(round(v, 2) for v in res.bounds))''',
}

PROPERTIES = {
'dataset_count': '''from gma import gio

gdb = gio.open_file('NewGDB.gpkg')

print(gdb.dataset_count)''',
'dataset_names': '''from gma import gio

gdb = gio.open_file('NewGDB.gpkg')

print(gdb.dataset_names)''',
'driver': '''from gma import gio

gdb = gio.open_file('NewGDB.gpkg')

print(gdb.driver)''',
'files': '''from gma import gio

gdb = gio.open_file('NewGDB.gpkg')

print(gdb.files)''',
'info': '''from gma import gio

gdb = gio.open_file('NewGDB.gpkg')

print('keys:', list(gdb.info.keys()))
for key in ('description', 'driverShortName', 'driverLongName', 'size'):
    print(key, ':', gdb.info[key])''',
'layer_count': '''from gma import gio

gdb = gio.open_file('NewGDB.gpkg')

print(gdb.layer_count)''',
'layer_names': '''from gma import gio

gdb = gio.open_file('NewGDB.gpkg')

print(gdb.layer_names)''',
'link': '''from gma import gio

gdb = gio.open_file('NewGDB.gpkg')

print(gdb.link)''',
'name': '''from gma import gio

gdb = gio.open_file('NewGDB.gpkg')

print(gdb.name)''',
}

RETURNS = {
'add_layer':     ('None', 'Add the Layer in place. NOTE: gma 3.0.4.1 segfaults on this call.'),
'create_layer':  ('Layer', 'The newly created empty layer.'),
'delete_layer':  ('None', 'Delete the layer from the database in place.'),
'get_dataset':   ('Dataset', 'The raster dataset with the given name or ID.'),
'get_layer':     ('Layer', 'The vector layer with the given name or ID.'),
'iteritems':     ('iter', 'Iterate over vector layers (0 / "Layer") or raster datasets ("Dataset").'),
'query':         ('Layer', 'A new layer with the result of the SpatiaLite SQL query.'),
}

# add_layer 在 3.0.4.1 的所有 driver 上都稳定段错误，不能执行，如实记录实测现象
FORCED = {'add_layer': 'Segmentation fault (gma 3.0.4.1 terminates the process before printing)'}

run(dict(page='GeoDatabase', base=BASE, examples=EXAMPLES, properties=PROPERTIES,
         returns=RETURNS, forced_results=FORCED))
