import sys, os
sys.path.insert(0, r'D:\github\gma\.vuepress\_gio_doc_common.py')
from _gio_doc_common import run, save, gio, plt

def G(body):
    return "from gma import gio\n\ng = gio.open_vector('Australia.shp').get_feature(0).geom   # Western Australia\n" + body

def pair(body):
    """同一几何的两个要素：g(WA) 与 other(NT)，用于空间关系运算。"""
    return "from gma import gio\n\nly = gio.open_vector('Australia.shp')\ng = ly.get_feature(0).geom       # Western Australia\nother = ly.get_feature(1).geom   # Northern Territory\n" + body

def shape(r):
    return "print(type(r).__name__, r.gtype, len(r), tuple(round(v, 2) for v in r.bounds))"

EXAMPLES = {
'add_geometry': G("""other = gio.open_vector('Australia.shp').get_feature(9).geom
print('Before:', len(g))
g.add_geometry(other)
print('After :', len(g))"""),

'add_point': """from gma import gio

p = gio.Geometry(gtype='Point')       # an empty Point geometry
print('Before:', p.to_str())

p.add_point((115.0, -25.0))
print('After :', p.to_str())""",

'buffer': G("""print('Before:', tuple(round(v, 2) for v in g.bounds))
r = g.buffer(1)
print('After :', tuple(round(v, 2) for v in r.bounds), r.gtype)"""),

'centroid': G("""r = g.centroid()
print(r.gtype, r.to_str())"""),

'close_rings': G("""print('Before:', g.gtype, len(g))
g.close_rings()
print('After :', g.gtype, len(g))"""),

'concave_hull': G("""r = g.concave_hull(ratio=0.2)
print(r.gtype, len(r), tuple(round(v, 2) for v in r.bounds))"""),

'contains': pair("""print('WA contains NT :', g.contains(other))
print('WA contains its copy:', g.contains(g.copy()))"""),

'convex_hull': G("""r = g.convex_hull()
print(r.gtype, len(r), tuple(round(v, 2) for v in r.bounds))"""),

'copy': G("""cp = g.copy()
cp.empty()
print('original:', g.gtype, len(g), g.is_empty())
print('copy    :', cp.gtype, len(cp), cp.is_empty())
print('same object:', cp is g)"""),

'crosses': pair("""print(g.crosses(other))"""),

'delaunay_triangulation': G("""r = g.delaunay_triangulation(tolerance=0.01)
print(r.gtype, len(r))"""),

'difference': pair("""r = g.difference(other)
print(r.gtype, len(r), tuple(round(v, 2) for v in r.bounds))"""),

'disjoint': pair("""print(g.disjoint(other))"""),

'distance': pair("""d = g.distance(other)
print('type :', type(d).__name__)   # 3.0.4.1 returns an empty Geometry, not a float"""),

'empty': G("""print('Before:', g.gtype, len(g), g.is_empty())
g.empty()
print('After :', g.gtype, len(g), g.is_empty())"""),

'equals': G("""print('g equals its copy:', g.equals(g.copy()))"""),

'extent': G("""r = g.extent()
print(r.gtype, tuple(round(v, 2) for v in r.bounds))"""),

'flatten': G("""print('Before:', g.gtype, len(g))
g.flatten()
print('After :', g.gtype, len(g))"""),

'get_area': G("""print('planar  :', round(g.get_area(), 2))
print('geodesic:', round(g.get_area(geodesic=True), 2))"""),

'get_length': G("""print('planar  :', round(g.get_length(), 2))
print('geodesic:', round(g.get_length(geodesic=True), 2))"""),

'intersection': pair("""r = g.intersection(other)
print(r.gtype, r.is_empty(), 'bytes:', r.wkb_size())"""),

'intersects': pair("""print(g.intersects(other))"""),

'is_empty': G("""print(g.is_empty())"""),

'is_measured': G("""print(g.is_measured())"""),

'is_ring': G("""print(g.is_ring())"""),

'is_simple': G("""print(g.is_simple())"""),

'is_valid': G("""print(g.is_valid())"""),

'make_valid': G("""r = g.make_valid()
print(type(r).__name__, r.gtype, r.is_valid())"""),

'normalize': G("""print('Before bytes:', g.wkb_size())
g.normalize()
print('After bytes :', g.wkb_size())"""),

'overlaps': pair("""print(g.overlaps(other))"""),

'plot': G("""import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 4.5))
ax = g.plot(ax=ax, facecolor='cornflowerblue', edgecolor='navy')
print(type(ax).__name__)"""),

'point_on_surface': G("""r = g.point_on_surface()
print(r.gtype, r.to_str())"""),

'remove_geometry': G("""print('Before:', g.gtype, len(g))
g.remove_geometry(0)
print('After :', g.gtype, len(g))"""),

'remove_lower_dimension_sub_geoms': G("""print('Before:', g.gtype, len(g))
g.remove_lower_dimension_sub_geoms()
print('After :', g.gtype, len(g))"""),

'segmentize': G("""print('Before bytes:', g.wkb_size())
g.segmentize(0.5)
print('After bytes :', g.wkb_size())"""),

'set_crs': G("""print('Before:', g.crs)
g.set_crs('EPSG:3857')
print('After :', g.crs)"""),

'set_dim': G("""print('Before:', g.dim)
g.set_dim('XYZ')
print('After :', g.dim)"""),

'simplify': G("""print('Before bytes:', g.wkb_size())
r = g.simplify(0.05, preserve_topology=True)
print('After bytes :', r.wkb_size(), r.gtype)"""),

'swap': G("""print('Before:', g.to_str()[:70])
g.swap()
print('After :', g.to_str()[:70])"""),

'sym_difference': pair("""r = g.sym_difference(other)
print(r.gtype, len(r), tuple(round(v, 2) for v in r.bounds))"""),

'to_bytearray': G("""b = g.to_bytearray()
print(type(b).__name__, len(b))"""),

'to_crs': G("""print('Before:', g.crs, tuple(round(v, 2) for v in g.bounds))
r = g.to_crs('EPSG:3857')
print('After :', r.crs, tuple(round(v, 2) for v in r.bounds))"""),

'to_geom_base': G("""d = g.to_geom_base()
print(type(d).__name__, list(d.keys()))
for k, v in d.items():
    print(k, len(v))"""),

'to_points': G("""pts = g.to_points()
print(type(pts).__name__, len(pts))
print('points in first part:', len(pts[0]))
print('first two points   :', pts[0][:2])"""),

'to_precision': G("""print('Before bytes:', g.wkb_size())
g.to_precision(2)
print('After bytes :', g.wkb_size())"""),

'to_str': G("""s = g.to_str()
print('format : WKT (length %d)' % len(s))
print('starts :', s[:70])"""),

'touches': pair("""print(g.touches(other))"""),

'unary_union': G("""r = g.unary_union()
print(r.gtype, len(r), tuple(round(v, 2) for v in r.bounds))"""),

'union': pair("""r = g.union(other)
print(r.gtype, len(r), tuple(round(v, 2) for v in r.bounds))"""),

'within': G("""print(g.within(g.convex_hull()))"""),

'wkb_size': G("""print(g.wkb_size())"""),
}

PROPERTIES = {
'boundary': G("""b = g.boundary
print(b.gtype, len(b))"""),
'bounds': G("""print(g.bounds)"""),
'crs': G("""print(g.crs)"""),
'dim': G("""print(g.dim)"""),
'gtype': G("""print(g.gtype)"""),
}

RETURNS = {}
for n in ('buffer', 'centroid', 'concave_hull', 'convex_hull', 'copy', 'difference',
          'extent', 'intersection', 'make_valid', 'point_on_surface', 'sym_difference',
          'unary_union', 'union', 'delaunay_triangulation'):
    RETURNS[n] = ('Geometry', 'A new geometry with the operation applied.')
for n in ('contains', 'crosses', 'disjoint', 'equals', 'intersects', 'is_empty',
          'is_measured', 'is_ring', 'is_simple', 'is_valid', 'overlaps', 'touches', 'within'):
    RETURNS[n] = ('bool', 'Whether the spatial relation / predicate holds.')
for n in ('add_geometry', 'add_point', 'close_rings', 'empty', 'flatten', 'normalize',
          'remove_geometry', 'remove_lower_dimension_sub_geoms', 'segmentize',
          'set_crs', 'set_dim', 'swap', 'to_precision'):
    RETURNS[n] = ('None', 'Modify the geometry in place.')
RETURNS.update({
    'get_area': ('float', 'The area of the geometry (planar or geodesic).'),
    'get_length': ('float', 'The perimeter or length of the geometry.'),
    'distance': ('Geometry', 'NOTE: 3.0.4.1 returns an empty Geometry instead of a float.'),
    'plot': ('Axes', 'The matplotlib axes with the geometry plotted on it.'),
    'to_bytearray': ('bytearray', 'The WKB or WKT representation as bytes.'),
    'to_crs': ('Geometry', 'A new geometry reprojected to the given CRS.'),
    'to_geom_base': ('dict', 'Basic geometries grouped by geometry type.'),
    'to_points': ('list', 'Point coordinates grouped by component geometry.'),
    'to_str': ('str', 'The WKT or WKB string of the geometry.'),
    'wkb_size': ('int', 'Size of the WKB representation in bytes.'),
    'simplify': ('Geometry', 'A simplified copy of the geometry.'),
})

IMAGES = {
    'plot': 'A real geometry plotted with matplotlib',
    'buffer': 'Before / after applying a 1-degree buffer',
    'convex_hull': 'Original geometry and its convex hull',
    'simplify': 'Before / after simplification (tolerance 0.05)',
    'union': 'Western Australia and Northern Territory merged by union',
}

def _pair_geom():
    ly = gio.open_vector('Australia.shp')
    return ly.get_feature(0).geom, ly.get_feature(1).geom

def _img_plot():
    g, _ = _pair_geom()
    fig, ax = plt.subplots(figsize=(7, 5), dpi=110)
    g.plot(ax=ax, facecolor='cornflowerblue', edgecolor='navy')
    ax.set_title('Geometry.plot()', fontsize=11)
    save(fig, 'Geometry', 'plot')

def _img_buffer():
    g, _ = _pair_geom()
    r = g.buffer(1)
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.5), dpi=110)
    g.plot(ax=axs[0], facecolor='none', edgecolor='tab:blue')
    g.plot(ax=axs[1], facecolor='none', edgecolor='gray')
    r.plot(ax=axs[1], facecolor='none', edgecolor='red')
    axs[0].set_title('Before: original geometry', fontsize=10)
    axs[1].set_title('After: 1-degree buffer (red)', fontsize=10)
    save(fig, 'Geometry', 'buffer')

def _img_convex_hull():
    g, _ = _pair_geom()
    r = g.convex_hull()
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.5), dpi=110)
    g.plot(ax=axs[0], facecolor='none', edgecolor='tab:blue')
    g.plot(ax=axs[1], facecolor='none', edgecolor='gray')
    r.plot(ax=axs[1], facecolor='none', edgecolor='red')
    axs[0].set_title('Before: original geometry', fontsize=10)
    axs[1].set_title('After: convex hull (red)', fontsize=10)
    save(fig, 'Geometry', 'convex_hull')

def _img_simplify():
    g, _ = _pair_geom()
    r = g.simplify(0.05, preserve_topology=True)
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.5), dpi=110)
    g.plot(ax=axs[0], facecolor='none', edgecolor='tab:blue')
    r.plot(ax=axs[1], facecolor='none', edgecolor='red')
    axs[0].set_title('Before: 7082 bytes', fontsize=10)
    axs[1].set_title('After: 2714 bytes', fontsize=10)
    save(fig, 'Geometry', 'simplify')

def _img_union():
    g, other = _pair_geom()
    r = g.union(other)
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.5), dpi=110)
    g.plot(ax=axs[0], facecolor='none', edgecolor='tab:blue')
    other.plot(ax=axs[0], facecolor='none', edgecolor='orange')
    r.plot(ax=axs[1], facecolor='none', edgecolor='red')
    axs[0].set_title('Before: two geometries', fontsize=10)
    axs[1].set_title('After: union (red)', fontsize=10)
    save(fig, 'Geometry', 'union')

cfg = dict(page='Geometry', base=G("""print(g.gtype, len(g))
print(tuple(round(v, 2) for v in g.bounds))"""),
           examples=EXAMPLES, properties=PROPERTIES, returns=RETURNS, images=IMAGES,
           img_funcs=[_img_plot, _img_buffer, _img_convex_hull, _img_simplify, _img_union])
if os.environ.get('GIO_DO') != 'write':
    cfg['dry_run'] = True
run(cfg)
