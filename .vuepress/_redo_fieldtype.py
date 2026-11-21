import sys
sys.path.insert(0, r'D:\github\gma\.vuepress\_gio_doc_common.py')
from _gio_doc_common import run, gio

BASE = '''from gma import gio

ly = gio.open_vector('Australia.shp')
ftype = ly.ftypes[0]        # first field of the real vector data

print(ftype)'''

EXAMPLES = {
'set_precision': '''from gma import gio

src = gio.open_vector('Australia.shp').ftypes[0]
ftype = gio.FieldType(src.name, src.ftype)     # a modifiable copy of a real field

print('Before:', ftype)
ftype.set_precision(10)
print('After :', ftype)''',

'set_type': '''from gma import gio

src = gio.open_vector('Australia.shp').ftypes[0]
ftype = gio.FieldType(src.name, src.ftype)     # a modifiable copy of a real field

print('Before:', ftype)
ftype.set_type('Integer')
print('After :', ftype)''',

'set_width': '''from gma import gio

src = gio.open_vector('Australia.shp').ftypes[0]
ftype = gio.FieldType(src.name, src.ftype)     # a modifiable copy of a real field

print('Before:', ftype)
ftype.set_width(40)
print('After :', ftype)''',
}

PROPERTIES = {
'default': '''from gma import gio

ftype = gio.open_vector('Australia.shp').ftypes[0]

print(ftype.default)''',
'ftype': '''from gma import gio

ftype = gio.open_vector('Australia.shp').ftypes[0]

print(ftype.ftype)''',
'name': '''from gma import gio

ftype = gio.open_vector('Australia.shp').ftypes[0]

print(ftype.name)''',
'precision': '''from gma import gio

ftype = gio.open_vector('Australia.shp').ftypes[0]

print(ftype.precision)''',
'width': '''from gma import gio

ftype = gio.open_vector('Australia.shp').ftypes[0]

print(ftype.width)''',
}

RETURNS = {
'set_precision': ('None', 'Modify the precision in place.'),
'set_type':      ('None', 'Modify the field data type in place.'),
'set_width':     ('None', 'Modify the field width in place.'),
}

run(dict(page='FieldType', base=BASE, examples=EXAMPLES, properties=PROPERTIES, returns=RETURNS))
