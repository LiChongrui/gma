import os, sys, tempfile, shutil, inspect
sys.path.insert(0, r'D:\github\gma\.vuepress\_gma341')
from gma import gio

SRC = r'D:\BaiduNetdiskDownload\ne\第3章'
WORK = tempfile.mkdtemp(prefix='ftypesprobe_')
for f in os.listdir(SRC):
    shutil.copy(os.path.join(SRC, f), os.path.join(WORK, f))
os.chdir(WORK)

ly = gio.open_vector('Australia.shp')
ft0 = ly.ftypes[0]
print('=== FieldType from real data ===')
for p in ('default', 'ftype', 'name', 'precision', 'width'):
    print(p, '=', repr(getattr(ft0, p)))
print('dir:', [m for m in dir(ft0) if not m.startswith('_')])

print('\n=== constructor ===')
for args in [('String',), (None, 'String'), ('name_x', 'Integer')]:
    try:
        f = gio.FieldType(*args)
        print(args, '->', repr(f), '| name:', f.name, '| ftype:', f.ftype,
              '| precision:', f.precision, '| width:', f.width, '| default:', repr(f.default))
    except Exception as e:
        print(args, 'FAIL:', type(e).__name__, e)

print('\n=== setters ===')
f = gio.FieldType('String')
for m, a in [('set_precision', (10,)), ('set_width', (40,)), ('set_type', ('Integer',))]:
    try:
        r = getattr(f, m)(*a)
        print(m, a, '->', repr(r), '| now:', f.name, f.ftype, f.precision, f.width)
    except Exception as e:
        print(m, a, 'FAIL:', type(e).__name__, e)

print('\n=== FieldTypes ===')
fts = ly.ftypes
for p in ('ftypes', 'names'):
    print(p, '=', repr(getattr(fts, p))[:300])
print('dir:', [m for m in dir(fts) if not m.startswith('_')])
print('sig add_ftype:', inspect.signature(fts.add_ftype), '| set_gtype:', inspect.signature(fts.set_gtype))
n = gio.FieldTypes()
print('empty names:', n.names, '| ftypes:', n.ftypes)
a = gio.FieldType('String')
print('add_ftype ->', repr(n.add_ftype(a)), '| names:', n.names)
print('set_gtype ->', repr(n.set_gtype('Point')), '| names after:', n.names)
print('PROBE DONE')
