# -*- coding: utf-8 -*-
"""第二轮补齐：carto 模块（11 页）、sensors 模块（3 页）、crs 4 个单位类（4 页）、
更新 crs/README.md 表格。
源码以 site-packages 安装版为准（gma-code 快照缺 sensors/optical.py）。
"""
import ast
import io
import os

from _gen_missing_docs import (esc, split_doc_sections, parse_param_blocks,
                               doc_to_body_html, get_init, sig_parts, args_html,
                               infer_type, class_sig_html, method_sig_html,
                               prop_html, front, is_property, class_members,
                               write, OUT, DATE)

SP = 'C:/Users/suppe/anaconda3/Lib/site-packages/gma'

# 源码 docstring 缺失时的兜底描述（按实际代码行为编写，NumPy 风格，交给 doc_to_body_html 渲染）
FALLBACK = {
    ('carto/layout.py', 'MapFrame', 'set_border'):
        "Set the border style of the map frame.\n\nReturns\n----------\nType: MapFrame.",
    ('carto/layout.py', 'MapFrame', 'set_background'):
        "Set the background color of the map frame.\n\nReturns\n----------\nType: MapFrame.",
    ('carto/grid.py', 'Graticule', '__init__'):
        "Create a longitude and latitude grid for a map frame.\n\n"
        "Usually created via MapFrame.add_graticule().\n\n"
        "Parameters\n----------\nmap_frame: MapFrame.\n"
        "    The map frame that the grid is attached to.\n\n"
        "Returns\n----------\nType: Graticule.",
    ('carto/appearance.py', 'MapAppearance', '__init__'):
        "Add a map appearance (ScaleBar or Compass) to the map frame.\n\n"
        "Usually created via MapFrame.add_appearance().\n\n"
        "Parameters\n----------\nmap_app: str.\n"
        "    Map appearance type. Supported types include:\n\n"
        "    'ScaleBarNormal1', 'CompassNormal1', 'CompassNormal2', 'CompassNormal3'.\n\n"
        "map_frame: MapFrame.\n"
        "    The map frame that the appearance is attached to.\n\n"
        "**Optional\n----------\n"
        "loc = tuple. Default (0, 0).\n"
        "    The location of the map appearance. The coordinate system is the same as the map frame.\n\n"
        "size = float. Default 0.1.\n"
        "    The size of the map appearance. The unit is the same as the map frame.\n\n"
        "Returns\n----------\nType: MapAppearance.",
    ('carto/appearance.py', 'MapAppearance', 'plot'):
        "Plot the map appearance on the map frame.",
    ('carto/vector.py', 'PlotVector', '__init__'):
        "An object for plotting vector (Layer/Feature/Geometry).\n\n"
        "Parameters\n----------\nvector: Layer, Feature or Geometry.\n"
        "    A vector object to be plotted.\n\n"
        "map_frame: MapFrame.\n"
        "    The map frame to be plotted on.\n\n"
        "Returns\n----------\nType: PlotVector.",
    ('carto/styles.py', 'GeometryStyles', '__init__'):
        "Build point, line and polygon plotting styles for a vector.\n\n"
        "**Optional\n----------\n"
        "pointmarkers = str. Default 'o'.\n"
        "    Marker style for point geometries. For more, see matplotlib.markers.\n\n"
        "pointsizes = float, list or None. Default None.\n"
        "    Marker size for point geometries. Default(None) determined by the plotted data.\n\n"
        "ax = matplotlib.axes.Axes or None. Default None.\n"
        "    The axes used for plotting. Default(None) the axes of the map frame.\n\n"
        "Returns\n----------\nType: GeometryStyles.",
    ('carto/styles.py', 'TextStyles', '__init__'):
        "Manage text styles for labels.\n\n"
        "Usually created automatically by PlotVector.add_labels().\n\n"
        "Returns\n----------\nType: TextStyles.",
    ('carto/resources.py', 'MarkerPath', '__init__'):
        "Create custom marker shapes (SVG path markers).\n\n"
        "Built-in shapes include: Flower, Spiral, Heart, Gear, Infinity.\n\n"
        "Returns\n----------\nType: MarkerPath.",
    ('sensors/optical.py', 'GF1_PMS', '__init__'):
        "Create a GF-1 PMS sensor object.\n\n"
        "Parameters\n----------\ninfile: str.\n"
        "    The GF-1 PMS image file path.\n\n"
        "**Optional\n----------\n"
        "**kwargs:\n"
        "    Other parameters passed to gma.gio.open_raster.\n\n"
        "Returns\n----------\nType: GF1_PMS.",
    ('sensors/optical.py', 'GF1_PMS', 'radiometric_calibration'):
        "Radiometric calibration based on the XML metadata of the GF-1 PMS image.\n\n"
        "The gain and offset are read from the XML metadata ('AbsCeof' and 'AOffset') by default, "
        "and can be overridden by AGain and AOffset.\n\n"
        "**Optional\n----------\n"
        "out_file = str or None. Default None.\n"
        "    The output raster file path. If not set (None), a memory file is created.\n\n"
        "**kwargs:\n"
        "    AGain = float or list. Absolute calibration gain for each band. Default is read from XML ('AbsCeof').\n\n"
        "    AOffset = float or list. Absolute calibration offset for each band. Default is read from XML ('AOffset').\n\n"
        "Returns\n----------\nType: DataSet.",
    ('sensors/optical.py', 'GF1_PMS', 'orthorectification'):
        "Orthorectify the image based on RPC (Rational Polynomial Coefficients) metadata.\n\n"
        "**Optional\n----------\n"
        "out_file = str or None. Default None.\n"
        "    The output raster file path. If not set (None), a memory file is created.\n\n"
        "dem = str or None. Default None.\n"
        "    The DEM file path used for RPC calculations.\n\n"
        "**kwargs:\n"
        "    Other parameters passed to gma.etools.orthorectification.\n\n"
        "Returns\n----------\nType: DataSet.",
    ('sensors/optical.py', 'XMLMeta', '__init__'):
        "Parse an XML metadata file into attributes.\n\n"
        "Leaf tags become string attributes, nested tags become nested XMLMeta objects.\n\n"
        "Parameters\n----------\nxml_path: str.\n"
        "    The XML file path.\n\n"
        "Returns\n----------\nType: XMLMeta.",
}


def get_doc(file, cls, fn):
    """强制覆盖优先，其次源码 docstring，最后 FALLBACK。"""
    key = (file, cls, fn.name if fn else '__init__')
    if key in FORCE:
        return FORCE[key]
    d = ast.get_docstring(fn) if fn else None
    if d:
        return d
    return FALLBACK.get(key)


# 源码 docstring 明显有误、必须覆盖的条目
FORCE = {
    # 源码 docstring 写的是 "An object for plotting raster."（复制粘贴笔误）
    ('carto/vector.py', 'PlotVector', '__init__'):
        FALLBACK[('carto/vector.py', 'PlotVector', '__init__')],
}


def gen_module_class(rel_file, module_path, cls_name, out_path,
                     intro_note=None, extra_html=None, sig_tag='[class]'):
    """通用类页生成：签名 + intro + 完整参数 + Method/Property。"""
    src = io.open(os.path.join(SP, rel_file), encoding='utf-8').read()
    tree = ast.parse(src)
    node = next(n for n in ast.walk(tree)
                if isinstance(n, ast.ClassDef) and n.name == cls_name)
    init = get_init(node)
    doc = get_doc(rel_file, cls_name, init) or ast.get_docstring(node) or ''
    sec = split_doc_sections(doc)
    desc_first = next((x.strip() for x in sec['desc'] if x.strip()),
                      cls_name + ' object.')

    parts = sig_parts(init) if init else []
    h = [front(cls_name)]
    h.append(class_sig_html(module_path, cls_name, parts, tag=sig_tag))
    h.append('')
    # doc_to_body_html 会渲染 docstring 的描述段，非空时不再单独输出 intro
    if not any(x.strip() for x in sec['desc']):
        h.append('<p>%s</p>' % esc(desc_first.rstrip('.')))
    if intro_note:
        h.append('<p>%s</p>' % intro_note)
    h.extend(doc_to_body_html(doc))

    methods, props = class_members(node)
    if methods:
        h.append('\n## Method\n')
        for m in methods:
            h.append('### %s' % m.name)
            h.append(method_sig_html(m.name, sig_parts(m)))
            h.append('')
            h.extend(doc_to_body_html(get_doc(rel_file, cls_name, m)))
            h.append('')
    if props:
        h.append('\n## Property\n')
        for pr in props:
            h.append('### %s' % pr.name)
            h.append(prop_html(pr.name, get_doc(rel_file, cls_name, pr)))
            h.append('')
    if extra_html:
        h.append('\n' + extra_html)
    write(out_path, '\n'.join(h))


def gen_start(path, rows, intro='All items(functions/classes/consts) in this module are as follows:'):
    rd = [front('Contents'), intro, '|No.|item|type|introduce|', '|---|---|---|---|']
    rd.extend(rows)
    write(path, '\n'.join(rd) + '\n')


def main():
    # ---------------- carto ----------------
    gen_module_class('carto/layout.py', 'carto.layout.MapFrame', 'MapFrame',
                     'carto/MapFrame.md',
                     intro_note='Main entry of cartography: <code>from gma.carto.plot import MapFrame</code>.',
                     extra_html='<p>Inherits all methods from <code>MapFrameBase</code>.</p>')
    gen_module_class('carto/grid.py', 'carto.grid.Graticule', 'Graticule',
                     'carto/Graticule.md')
    gen_module_class('carto/appearance.py', 'carto.appearance.MapAppearance', 'MapAppearance',
                     'carto/MapAppearance.md')
    gen_module_class('carto/raster.py', 'carto.raster.PlotRaster', 'PlotRaster',
                     'carto/PlotRaster.md')
    gen_module_class('carto/vector.py', 'carto.vector.PlotVector', 'PlotVector',
                     'carto/PlotVector.md')
    gen_module_class('carto/styles.py', 'carto.styles.GeometryStyles', 'GeometryStyles',
                     'carto/GeometryStyles.md',
                     intro_note='Passed to <code>PlotVector.plot(style=...)</code> to customize vector plotting styles.')
    gen_module_class('carto/styles.py', 'carto.styles.TextStyles', 'TextStyles',
                     'carto/TextStyles.md')
    gen_module_class('carto/resources.py', 'carto.resources.WorldLayer', 'WorldLayer',
                     'carto/WorldLayer.md')
    gen_module_class('carto/resources.py', 'carto.resources.WorldDataset', 'WorldDataset',
                     'carto/WorldDataset.md')
    gen_module_class('carto/resources.py', 'carto.resources.MarkerPath', 'MarkerPath',
                     'carto/MarkerPath.md')

    carto_rows = [
        '|1|[carto.GeometryStyles](/docs/UserGuide/carto/GeometryStyles.html)|class|Build point, line and polygon plotting styles.|',
        '|2|[carto.Graticule](/docs/UserGuide/carto/Graticule.html)|class|Longitude and latitude grid.|',
        '|3|[carto.MapAppearance](/docs/UserGuide/carto/MapAppearance.html)|class|Map appearance (ScaleBar or Compass).|',
        '|4|[carto.MapFrame](/docs/UserGuide/carto/MapFrame.html)|class|Like ArcGIS, create a map frame to draw a map.|',
        '|5|[carto.MarkerPath](/docs/UserGuide/carto/MarkerPath.html)|class|Create custom marker shapes.|',
        '|6|[carto.PlotRaster](/docs/UserGuide/carto/PlotRaster.html)|class|An object for plotting raster.|',
        '|7|[carto.PlotVector](/docs/UserGuide/carto/PlotVector.html)|class|An object for plotting vector.|',
        '|8|[carto.TextStyles](/docs/UserGuide/carto/TextStyles.html)|class|Manage text styles for labels.|',
        '|9|[carto.WorldDataset](/docs/UserGuide/carto/WorldDataset.html)|class|Open the world Dataset provided by gma.|',
        '|10|[carto.WorldLayer](/docs/UserGuide/carto/WorldLayer.html)|class|Open the world Layer provided by gma.|',
    ]
    gen_start('carto/README.md', carto_rows)

    # ---------------- sensors ----------------
    gen_module_class('sensors/optical.py', 'sensors.optical.GF1_PMS', 'GF1_PMS',
                     'sensors/optical/GF1_PMS.md',
                     intro_note='The image must be accompanied by an XML metadata file (the same name as the image, '
                                'with a <code>.xml</code> extension, in the same path) for radiometric calibration.')
    gen_module_class('sensors/optical.py', 'sensors.optical.XMLMeta', 'XMLMeta',
                     'sensors/optical/XMLMeta.md')

    sensors_rows = [
        '|1|[sensors.optical.GF1_PMS](/docs/UserGuide/sensors/optical/GF1_PMS.html)|class|GF-1 PMS sensor. Radiometric calibration and orthorectification.|',
        '|2|[sensors.optical.XMLMeta](/docs/UserGuide/sensors/optical/XMLMeta.html)|class|Parse an XML metadata file.|',
    ]
    gen_start('sensors/README.md', sensors_rows)

    # ---------------- crs 4 个单位类 ----------------
    src = io.open(os.path.join(SP, '_algos/geo/crs.py'), encoding='utf-8').read()
    tree = ast.parse(src)
    classes = {n.name: n for n in tree.body if isinstance(n, ast.ClassDef)}

    units_doc = {
        'Ellips': ('Default ellipsoids. Built from the PROJ database when created.',
                   "from gma import crs\ncrs.Ellips().WGS_84",
                   "{'semi_major': 6378137.0, 'inv_flattening': 298.2572236}"),
        'Primems': ('Primems object. Prime meridians and their longitudes (degrees).',
                    "from gma import crs\ncrs.Primems().Greenwich",
                    "0.0"),
        'LinearUnits': ('Linear units object. Conversion factors relative to the metre.',
                        "from gma import crs\ncrs.LinearUnits().METRE",
                        "1.0"),
        'AngleUnits': ('Angle units object. Conversion factors relative to the radian.',
                       "from gma import crs\ncrs.AngleUnits().DEGREE",
                       "0.0174532925199433"),
    }
    for name, (intro, code, ret) in units_doc.items():
        node = classes[name]
        parts = sig_parts(get_init(node))
        h = [front(name)]
        h.append(class_sig_html('crs.' + name, name, parts))
        h.append('')
        h.append('<p>%s</p>' % intro)
        h.append('<p>Attribute names are derived from the PROJ database and accessed directly as instance attributes:</p>')
        h.append('\n```python\n%s\n```\n' % code)
        h.append('<p>%s --> <code style="text-indent: 0em;">%s</code></p>' % (code.split(chr(10))[-1], ret))
        write('crs/%s.md' % name, '\n'.join(h))

    # 更新 crs/README.md：追加 4 行
    crs_rd = os.path.join(OUT, 'crs/README.md')
    txt = io.open(crs_rd, encoding='utf-8').read()
    add = ('|7|[crs.AngleUnits](/docs/UserGuide/crs/AngleUnits.html)|class|Angle units object.|\n'
           '|8|[crs.Ellips](/docs/UserGuide/crs/Ellips.html)|class|Default ellipsoids.|\n'
           '|9|[crs.LinearUnits](/docs/UserGuide/crs/LinearUnits.html)|class|Linear units object.|\n'
           '|10|[crs.Primems](/docs/UserGuide/crs/Primems.html)|class|Primems object.|\n')
    if 'AngleUnits' not in txt:
        txt = txt.rstrip('\n') + '\n' + add
        io.open(crs_rd, 'w', encoding='utf-8', newline='\n').write(txt)
        print('  crs/README.md updated')

    print('DONE')


if __name__ == '__main__':
    main()
