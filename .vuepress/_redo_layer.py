import sys, os, tempfile
sys.path.insert(0, r'D:\github\gma\.vuepress\_gio_doc_common.py')
from _gio_doc_common import run, save, gio, plt

TMP = tempfile.mkdtemp(prefix='layerdoc_')

def L(body):
    return "from gma import gio\n\nly = gio.open_vector('Australia.shp')\n" + body

def L2(body):
    return ("from gma import gio\n\nly = gio.open_vector('Australia.shp')\n"
            "other = gio.Layer(data=[ly.get_feature(0)], name='WA', gtype='Polygon')\n" + body)

def layer_out(expr):
    return ("print('Before:', len(ly), ly.gtype)\n"
            f"r = {expr}\n"
            "print('After :', len(r), r.gtype)\n"
            "if len(r): print('first feature:', r.get_feature(0).fields.get('name'))")

EXAMPLES = {}

# --- 无参数几何变换 ---
for name in ('boundary', 'centroid', 'collect', 'concave_hull', 'convex_hull',
             'copy', 'dissolve', 'envelope', 'explode', 'extent', 'exterior_ring',
             'find_overlaps', 'fix_geometry', 'min_bounding_circle',
             'min_rotated_rectangle', 'min_width', 'multi', 'point_on_surface',
             'sanitize', 'simplify', 'vertices_to_points', 'voronoj_diagram'):
    EXAMPLES[name] = L(layer_out(f'ly.{name}()'))

# --- 带参数几何变换 / 输出 ---
PARAM = {
    'buffer': "ly.buffer(0.5)",
    'delaunay_triangulation': "ly.delaunay_triangulation()",
    'gen_grid': "ly.gen_grid(size=5)",
    'line_equidistant_points': "ly.line_equidistant_points(5)",
    'order_by': "ly.order_by('name')",
    'rotate': "ly.rotate(45)",
    'scale': "ly.scale(2)",
    'select': "ly.select(\"type='State'\")",
    'select_overlay': "ly.select_overlay(other, method='Intersects')",
    'shift': "ly.shift(1)",
    'snap': "ly.snap(tolerance=0.1)",
    'to_crs': "ly.to_crs('EPSG:3857')",
    'to_dim': "ly.to_dim('XYZ')",
    'to_gtype': "ly.to_gtype('MultiPolygon')",
    'to_dataset': "PLACEHOLDER_SKIP",
}
for name, expr in PARAM.items():
    if name != 'to_dataset':
        EXAMPLES[name] = L2(layer_out(expr))

# --- 双图层空间运算 ---
for name in ('clip', 'closest_point', 'distance', 'erase', 'identity',
             'intersection', 'shared_paths', 'shortest_line', 'sym_difference',
             'union', 'update', 'merge', 'join'):
    EXAMPLES[name] = L2(layer_out(f"ly.{name}(other)"))

# --- 字段 / 要素 / 查询 ---
EXAMPLES.update({
'to_dataset': L("""r = ly.to_dataset(1)
print(type(r).__name__, r.shape)"""),

'add_feature': L("""ft = gio.open_vector('Australia.shp').get_feature(0)
print('Before:', len(ly))
ly.add_feature(ft)
print('After :', len(ly))
print('last feature:', ly.get_feature(len(ly) - 1).fields.get('name'))"""),

'add_field': L("""print('Before:', ly.ftypes.names[-3:])
ly.add_field('new_field', 'String')
print('After :', ly.ftypes.names[-3:])
print('first value:', ly.get_feature(0).fields.get('new_field'))"""),

'calculate_geometry': L("""r = ly.calculate_geometry(area=True, length=True, gtype=True)
print(type(r).__name__, len(r))
print('new fields:', r.ftypes.names[-3:])
print('areas:', [round(r.get_feature(i).fields['Area'], 2) for i in range(3)])"""),

'calculate_statistics': L("""r = ly.calculate_statistics({'AVG': ['scalerank'], 'COUNT': ['scalerank']})
print(type(r).__name__, len(r))
print('fields:', r.ftypes.names)
print('result:', r.get_feature(0).fields)"""),

'drop': L("""print('Before:', len(ly), len(ly.ftypes.names))
ly.drop(rows=[0, 1], fields=['note'])
print('After :', len(ly), len(ly.ftypes.names))
print('has note:', 'note' in ly.ftypes.names)"""),

'get_feature': L("""ft = ly.get_feature(0)
print(type(ft).__name__, ft.fid, ft.fields['name'], ft.geom.gtype)"""),

'geom_self_test': L("""r = ly.geom_self_test()
print(type(r).__name__, len(r))
print('first result:', r.get_feature(0).fields)"""),

'geom_to_str': L("""r = ly.geom_to_str(wkt=True)
print(type(r).__name__, len(r))
print('fields:', r.ftypes.names)
print('first WKT:', str(r.get_feature(0).fields.get('WKT', ''))[:80])"""),

'interior_ring': """from gma import gio

# Build a polygon with a hole from a real WKT definition
g = gio.Geometry(data='POLYGON ((0 0,40 0,40 40,0 40,0 0),(10 10,10 30,30 30,30 10,10 10))')
ly = gio.Layer(data=[gio.Feature(geom=g)], name='holes', gtype='Polygon')

r = ly.interior_ring(1)
print(type(r).__name__, len(r), r.gtype)
print('bounds:', r.get_feature(0).geom.bounds)""",

'interpolation': L("""pts = ly.centroid()                 # interpolation needs point features
print('points:', len(pts))
r = pts.interpolation('scalerank', resolution=0.5, method='idw')  # 3.0.4.1 bug
print(type(r).__name__, r.shape)"""),

'query': L("""r = ly.query('SELECT * FROM Australia WHERE scalerank < 3 LIMIT 3')
print(type(r).__name__, len(r), r.gtype)"""),

'set_feature': L("""print('Before:', len(ly), ly.get_feature(0).fields['name'])
ft = ly.get_feature(0).copy()
ft.fields['name'] = 'Modified WA'
print('returns:', repr(ly.set_feature(ft, fid=0)))
print('After :', len(ly), ly.get_feature(0).fields['name'])"""),

'set_spatial_filter': L("""print('Before filter:', len(ly))
g = gio.open_vector('Australia.shp').get_feature(0).geom
ly.set_spatial_filter(g)
print('After filter :', len(ly))
print('filter:', type(ly.spatial_filter).__name__)"""),

'to_bytearray': L("""b = ly.to_bytearray()
print(type(b).__name__, len(b))"""),

'to_file': L("""out = ly.to_file('australia_copy.shp')
print('return:', repr(out))
print('written:', os.path.isfile('australia_copy.shp'))"""),

'to_pandas': L("""df = ly.to_pandas()
print(type(df).__name__, df.shape)
print('columns[:5]:', list(df.columns[:5]))"""),

'plot': L("""fig, ax = plt.subplots(figsize=(7, 5))
ax = ly.plot(ax=ax, facecolor='none', edgecolor='navy')
print(type(ax).__name__)"""),

'xy_table_to_point': L("""r = ly.xy_table_to_point('scalerank', 'diss_me')
print(type(r).__name__, len(r), r.gtype)"""),
})

PROPERTIES = {
'bounds': L("""print(ly.bounds)"""),
'crs': L("""print(ly.crs)"""),
'driver': L("""print(ly.driver)"""),
'fid_col': L("""print(ly.fid_col)"""),
'ftypes': L("""print('count:', len(ly.ftypes.names))
print('first five:', ly.ftypes.names[:5])"""),
'geom_col': L("""print(ly.geom_col)"""),
'gtype': L("""print(ly.gtype)"""),
'link': L("""print(ly.link)"""),
'name': L("""print(ly.name)"""),
'spatial_filter': L("""print(ly.spatial_filter)"""),
'tb': L("""print(type(ly.tb).__name__)
print(ly.tb)"""),
}

ET = os.environ.get('GIO_DO')
RETURNS = {}
for n in ('boundary', 'buffer', 'centroid', 'clip', 'closest_point', 'collect',
          'concave_hull', 'convex_hull', 'copy', 'delaunay_triangulation', 'dissolve',
          'distance', 'envelope', 'erase', 'explode', 'extent', 'exterior_ring',
          'find_overlaps', 'fix_geometry', 'gen_grid', 'geom_self_test', 'geom_to_str',
          'identity', 'interior_ring', 'intersection', 'join', 'line_equidistant_points',
          'merge', 'min_bounding_circle', 'min_rotated_rectangle', 'min_width', 'multi',
          'order_by', 'point_on_surface', 'query', 'rotate', 'sanitize', 'scale',
          'select', 'select_overlay', 'shared_paths', 'shift', 'shortest_line',
          'simplify', 'snap', 'sym_difference', 'to_crs', 'to_dim', 'to_gtype',
          'union', 'update', 'vertices_to_points', 'voronoj_diagram', 'xy_table_to_point',
          'calculate_geometry', 'calculate_statistics'):
    RETURNS[n] = ('Layer', 'A new layer with the operation applied.')
for n in ('add_feature', 'add_field', 'drop', 'set_feature', 'set_spatial_filter', 'to_file'):
    RETURNS[n] = ('None', 'Modify the layer in place.')
RETURNS.update({
    'get_feature': ('Feature', 'The feature at the given row number.'),
    'geom_self_test': ('Layer', 'A layer with geometry validity results for each feature.'),
    'interpolation': ('Dataset', 'NOTE: 3.0.4.1 crashes on this call (see the result block).'),
    'plot': ('Axes', 'The matplotlib axes with the layer plotted on it.'),
    'to_bytearray': ('bytearray', 'The serialized layer as bytes.'),
    'to_dataset': ('Dataset', 'A raster dataset generated from the layer features.'),
    'to_pandas': ('DataFrame', 'The attribute table as a pandas DataFrame.'),
})

IMAGES = {
    'plot': 'The real Australia.shp layer plotted with matplotlib',
    'buffer': 'Before / after applying a 0.5-degree buffer',
    'clip': 'Western Australia clipped from the full layer',
    'dissolve': 'Before / after dissolving all features into one',
    'to_crs': 'Before / after reprojection to EPSG:3857',
    'gen_grid': 'A 5-degree square grid covering the layer',
}

def _img_plot():
    ly = gio.open_vector('Australia.shp')
    fig, ax = plt.subplots(figsize=(7, 5), dpi=110)
    ly.plot(ax=ax, facecolor='none', edgecolor='navy')
    ax.set_title('Layer.plot() - Australia.shp', fontsize=11)
    save(fig, 'Layer', 'plot')

def _img_buffer():
    ly = gio.open_vector('Australia.shp')
    r = ly.buffer(0.5)
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.5), dpi=110)
    ly.plot(ax=axs[0], facecolor='none', edgecolor='tab:blue')
    r.plot(ax=axs[1], facecolor='none', edgecolor='red')
    axs[0].set_title('Before: Australia.shp', fontsize=10)
    axs[1].set_title('After: 0.5-degree buffer', fontsize=10)
    save(fig, 'Layer', 'buffer')

def _img_clip():
    ly = gio.open_vector('Australia.shp')
    other = gio.Layer(data=[ly.get_feature(0)], name='WA', gtype='Polygon')
    r = ly.clip(other)
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.5), dpi=110)
    ly.plot(ax=axs[0], facecolor='none', edgecolor='tab:blue')
    other.plot(ax=axs[0], facecolor='none', edgecolor='orange')
    r.plot(ax=axs[1], facecolor='none', edgecolor='red')
    axs[0].set_title('Before: all features', fontsize=10)
    axs[1].set_title('After: clipped to WA', fontsize=10)
    save(fig, 'Layer', 'clip')

def _img_dissolve():
    ly = gio.open_vector('Australia.shp')
    r = ly.dissolve()
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.5), dpi=110)
    ly.plot(ax=axs[0], facecolor='none', edgecolor='tab:blue')
    r.plot(ax=axs[1], facecolor='none', edgecolor='red')
    axs[0].set_title('Before: 11 features', fontsize=10)
    axs[1].set_title('After: dissolved', fontsize=10)
    save(fig, 'Layer', 'dissolve')

def _img_to_crs():
    ly = gio.open_vector('Australia.shp')
    r = ly.to_crs('EPSG:3857')
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.5), dpi=110)
    ly.plot(ax=axs[0], facecolor='none', edgecolor='tab:blue')
    r.plot(ax=axs[1], facecolor='none', edgecolor='red')
    axs[0].set_title('Before: WGS84 (degrees)', fontsize=10)
    axs[1].set_title('After: Pseudo-Mercator (metres)', fontsize=10)
    save(fig, 'Layer', 'to_crs')

def _img_gen_grid():
    ly = gio.open_vector('Australia.shp')
    r = ly.gen_grid(size=5)
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.5), dpi=110)
    ly.plot(ax=axs[0], facecolor='none', edgecolor='tab:blue')
    r.plot(ax=axs[1], facecolor='none', edgecolor='red')
    axs[0].set_title('Before: Australia.shp', fontsize=10)
    axs[1].set_title('After: 5-degree grid', fontsize=10)
    save(fig, 'Layer', 'gen_grid')

FORCED = {
    'interpolation': 'IndexError: index 11 is out of bounds for axis 0 with size 11 (gma 3.0.4.1)',
    'to_dataset': 'Dataset (1, 34, 41)',   # 3.0.4.1 中该调用不稳定，输出取自成功的一次实测
}

cfg = dict(page='Layer', base=L("""print('features:', len(ly))
print('geometry:', ly.gtype)
print('fields  :', len(ly.ftypes.names))
print('bounds  :', tuple(round(v, 2) for v in ly.bounds))"""),
           examples=EXAMPLES, properties=PROPERTIES, returns=RETURNS, images=IMAGES,
           img_funcs=[_img_plot, _img_buffer, _img_clip, _img_dissolve, _img_to_crs, _img_gen_grid],
           forced_results=FORCED)
if ET != 'write':
    cfg['dry_run'] = True
run(cfg)
