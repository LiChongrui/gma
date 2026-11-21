# -*- coding: utf-8 -*-
"""gio API 实测 v2:全部使用文档里记载的成员"""
import os, traceback
import gma

DP = os.environ['GMA_Data']
WORLD = os.path.join(DP, 'world.gdb.zip')
DEM = os.path.join(DP, 'GMA_World_DEM_GEBCO.jp2')
TMP = os.environ['TEMP']

def t(name, fn):
    print(f'\n===== {name} =====')
    try:
        fn()
        print(f'[OK] {name}')
    except Exception:
        print(f'[FAIL] {name}')
        traceback.print_exc()

def s1_geodatabase():
    from gma import gio
    gdb = gio.open_file(WORLD)
    print('layer_names:', gdb.layer_names)
    print('layer_count:', gdb.layer_count)
    print('driver:', gdb.driver)
    ly = gdb.get_layer('Country')
    print('get_layer:', type(ly).__name__, 'name:', ly.name)

def s2_layer():
    from gma import gio
    ly = gio.open_vector(WORLD, name_or_id='Country')
    print('name:', ly.name, '| gtype:', ly.gtype, '| crs:', str(ly.crs)[:50])
    print('ftypes:', ly.ftypes[:3])
    print('bounds:', ly.bounds)
    ft = ly.get_feature(0)
    print('get_feature:', type(ft).__name__)
    df = ly.to_pandas()
    print('to_pandas:', df.shape, list(df.columns)[:4])
    sel = ly.select("1=1", keep_fields=None) if False else None
    b = ly.buffer(10)
    print('buffer:', type(b).__name__, b.name)
    cg = ly.calculate_geometry(area=True)
    print('calculate_geometry:', type(cg).__name__)
    out = os.path.join(TMP, '_gma_doc_ly.shp')
    ly.to_file(out)
    print('to_file:', os.path.exists(out))
    os.remove(out)

def s3_dataset():
    from gma import gio
    ds = gio.open_raster(DEM)
    print('shape:', ds.shape, '| dtype:', ds.dtype, '| res:', ds.resolution)
    print('crs:', str(ds.crs)[:40], '| nodata:', ds.nodata)
    print('bounds:', ds.bounds)
    arr = ds.to_numpy()
    print('to_numpy:', arr.shape, arr.dtype)
    rs = ds.resample(0.5)
    print('resample:', type(rs).__name__, rs.shape)
    out = os.path.join(TMP, '_gma_doc_ds.tif')
    ds.to_file(out)
    print('to_file:', os.path.exists(out))
    os.remove(out)

def s4_geometry():
    from gma import gio
    pt = gio.Geometry('POINT (114 30)')
    print('gtype:', pt.gtype, '| dim:', pt.dim, '| bounds:', pt.bounds)
    pg = gio.Geometry('POLYGON ((110 28, 118 28, 118 32, 110 32, 110 28))')
    buf = pg.buffer(1)
    print('buffer gtype:', buf.gtype)
    print('pg.contains(pt):', pg.contains(pt))
    print('boundary gtype:', pg.boundary.gtype)
    # 从坐标列表构造
    lp = gio.Geometry([[114, 30], [115, 31]], gtype='LineString')
    print('list LineString:', lp.gtype)

def s5_feature():
    from gma import gio
    ly = gio.open_vector(WORLD, name_or_id='Country')
    ft = ly.get_feature(0)
    print('fid:', ft.fid, '| fields:', ft.fields[:3])
    print('geom gtype:', ft.geom.gtype)
    print('crs:', str(ft.crs)[:30])

def s6_read_dataframe():
    from gma import gio
    import pandas as pd
    df = pd.DataFrame({'name': ['a', 'b'], 'lon': [114.0, 118.0], 'lat': [30.0, 32.0]})
    lyr = gio.read_dataframe(df, encoding='PointFromColumns', x='lon', y='lat')
    print('Layer:', type(lyr).__name__, '| gtype:', lyr.gtype)

def s7_fieldtypes():
    from gma import gio
    ft = gio.FieldType('String')
    print('FieldType:', repr(ft)[:60], '| value:', getattr(ft, 'value', '?'))
    fts = gio.FieldTypes()
    fts.add_ftype(ft)
    print('ftypes:', fts.ftypes)
    print('names:', fts.names)
    fts.set_gtype('Point')
    print('gtype set ok')

def s8_vvgd_vrd():
    from gma import gio
    ly = gio.open_vector(WORLD, name_or_id='Country')
    vvgd = gio.VirtualVectorGeoDatabase([ly])
    print('VVGD layer_names:', vvgd.layer_names[:3])
    ds = gio.open_raster(DEM)
    vrd = gio.VirtualRasterDataset(ds)
    print('VRD:', type(vrd).__name__, '| shape:', vrd.shape)

if __name__ == '__main__':
    t('GeoDatabase', s1_geodatabase)
    t('Layer', s2_layer)
    t('Dataset', s3_dataset)
    t('Geometry', s4_geometry)
    t('Feature', s5_feature)
    t('read_dataframe', s6_read_dataframe)
    t('FieldType/FieldTypes', s7_fieldtypes)
    t('VVGD/VRD', s8_vvgd_vrd)
