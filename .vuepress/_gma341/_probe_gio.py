# -*- coding: utf-8 -*-
"""gio API 实测:验证拟写入文档的示例调用链(每段独立 try,失败不影响后续)"""
import os, traceback
import gma

DP = os.environ['GMA_Data']
WORLD = os.path.join(DP, 'world.gdb.zip')
DEM = os.path.join(DP, 'GMA_World_DEM_GEBCO.jp2')

def t(name, fn):
    print(f'\n===== {name} =====')
    try:
        fn()
        print(f'[OK] {name}')
    except Exception:
        print(f'[FAIL] {name}')
        traceback.print_exc()

def s1_open_file():
    from gma import gio
    gdb = gio.open_file(WORLD)
    print(type(gdb).__name__, '| dataset_names:', gdb.dataset_names[:5])

def s2_open_vector():
    from gma import gio
    ly = gio.open_vector(WORLD, layer='Country')
    print(type(ly).__name__, '| feature_count:', ly.feature_count)

def s3_open_raster():
    from gma import gio
    ds = gio.open_raster(DEM)
    print(type(ds).__name__, '| bounds:', ds.bounds)

def s4_read_dataframe():
    from gma import gio
    df = gio.read_dataframe(WORLD, layer='Country')
    print(type(df).__name__, '| shape:', df.shape, '| cols:', list(df.columns)[:6])

def s5_geodatabase():
    from gma import gio
    gdb = gio.GeoDatabase(WORLD)
    print('names:', gdb.dataset_names)
    ly = gdb.get_layer('Country')
    print('layer:', type(ly).__name__, ly.feature_count)
    # query 试试
    q = gdb.query('SELECT * FROM Country LIMIT 3')
    print('query:', type(q).__name__)

def s6_vvgd():
    from gma import gio
    ly = gio.open_vector(WORLD, layer='Country')
    vvgd = gio.VirtualVectorGeoDatabase([ly, WORLD])
    print('dataset_names:', vvgd.dataset_names[:6])

def s7_vrd():
    from gma import gio
    ds = gio.open_raster(DEM)
    vrd = gio.VirtualRasterDataset(ds)
    print('VRD:', type(vrd).__name__, vrd.bounds)

def s8_dataset():
    from gma import gio
    ds = gio.open_raster(DEM)
    print('crs:', ds.crs.to_str()[:60])
    print('bounds:', ds.bounds)
    print('size:', ds.size if hasattr(ds, 'size') else '(no size)')
    arr = ds.to_numpy()
    print('to_numpy:', arr.shape, arr.dtype)
    out = os.path.join(os.environ['TEMP'], '_gma_doc_test.tif')
    ds.to_file(out)
    print('to_file ok:', os.path.exists(out))
    os.remove(out)

def s9_layer():
    from gma import gio
    ly = gio.open_vector(WORLD, layer='Country')
    print('feature_count:', ly.feature_count)
    print('fields:', ly.fields[:5])
    b = ly.buffer(10)
    print('buffer:', type(b).__name__)
    st = ly.calculate_statistics({'sum': 'Population'} ) if 'Population' in ly.fields else None
    print('statistics:', st)

def s10_feature():
    from gma import gio
    ly = gio.open_vector(WORLD, layer='Country')
    ft = ly[0] if hasattr(ly, '__getitem__') else None
    if ft is None:
        ft = next(iter(ly))
    print('feature:', type(ft).__name__)
    print('fields:', ft.fields[:4])
    print('geom:', type(ft.geom).__name__)

def s11_geometry():
    from gma import gio
    g1 = gio.Geometry('POINT (114 30)')
    print('geom1:', g1.to_wkt() if hasattr(g1, 'to_wkt') else g1)
    g2 = g1.buffer(5)
    print('buffer:', g2.to_wkt()[:50] if hasattr(g2, 'to_wkt') else type(g2))
    g3 = gio.Geometry('POLYGON ((110 28, 118 28, 118 32, 110 32, 110 28))')
    print('contains:', g3.contains(g1))
    print('area:', g3.area if hasattr(g3, 'area') else '(no area)')

def s12_fieldtypes():
    from gma import gio
    ft = gio.FieldType('String')
    print('FieldType:', ft, '| name:', getattr(ft, 'name', '?'), '| value:', getattr(ft, 'value', '?'))
    fts = gio.FieldTypes()
    fts.add_ftype(gio.FieldType('String'))
    print('FieldTypes:', fts.ftypes if hasattr(fts, 'ftypes') else fts)

if __name__ == '__main__':
    t('open_file', s1_open_file)
    t('open_vector', s2_open_vector)
    t('open_raster', s3_open_raster)
    t('read_dataframe', s4_read_dataframe)
    t('GeoDatabase', s5_geodatabase)
    t('VirtualVectorGeoDatabase', s6_vvgd)
    t('VirtualRasterDataset', s7_vrd)
    t('Dataset', s8_dataset)
    t('Layer', s9_layer)
    t('Feature', s10_feature)
    t('Geometry', s11_geometry)
    t('FieldType/FieldTypes', s12_fieldtypes)
