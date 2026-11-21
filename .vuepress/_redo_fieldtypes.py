import sys
sys.path.insert(0, r'D:\github\gma\.vuepress\_gio_doc_common.py')
from _gio_doc_common import run

BASE = '''from gma import gio

ly = gio.open_vector('Australia.shp')
fts = ly.ftypes               # real field definitions of the vector data

print('number of fields :', len(fts.names))
print('first five names :', fts.names[:5])
print('first field type :', fts[0])'''

EXAMPLES = {
'add_ftype': '''from gma import gio

fts = gio.FieldTypes()
print('Before:', fts.names)

fts.add_ftype(gio.FieldType('name', 'String'))
print('After :', fts.names)''',

'set_gtype': '''from gma import gio

fts = gio.FieldTypes()
fts.add_ftype(gio.FieldType('name', 'String'))

print('Before:', fts.names)
fts.set_gtype('Point')
print('After :', fts.names)''',
}

PROPERTIES = {
'ftypes': '''from gma import gio

fts = gio.open_vector('Australia.shp').ftypes

print('number of types:', len(fts.ftypes))
print('first five     :', fts.ftypes[:5])''',

'names': '''from gma import gio

fts = gio.open_vector('Australia.shp').ftypes

print('number of names:', len(fts.names))
print('first five     :', fts.names[:5])''',
}

RETURNS = {
'add_ftype': ('None', 'Add the FieldType in place.'),
'set_gtype': ('None', 'Set the geometry type in place; field names are unchanged.'),
}

run(dict(page='FieldTypes', base=BASE, examples=EXAMPLES, properties=PROPERTIES, returns=RETURNS))
