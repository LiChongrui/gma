# -*- coding: utf-8 -*-
"""Dataset 24 个方法逐个实测:统一底座 + 记录真实返回值"""
import os, sys, traceback
sys.path.insert(0, r'D:\github\gma\.vuepress\_gma341')
import gma
import numpy as np
from gma import gio

DP = os.environ['GMA_Data']
WORLD = os.path.join(DP, 'world.gdb.zip')
TMP = os.environ['TEMP']

import matplotlib
matplotlib.use('Agg')

def base_ds():
    """统一示例底座:2 波段 6x6,带 WGS84 地理坐标"""
    arr = np.random.randint(0, 100, (2, 6, 6)).astype('float32')
    return gio.Dataset(data=arr, crs='WGS84', geo_transform=(110, 1, 0, 32, 0, -1))

def t(name, fn):
    print(f'\n===== {name} =====')
    try:
        fn()
    except Exception:
        print(f'[FAIL] {name}')
        traceback.print_exc()

def s1_algebraic():
    ds = base_ds()
    def func(in_ar):
        return in_ar[0] * 2.1
    res = ds.algebraic(func)
    print(type(res).__name__, res.shape, res.dtype)

def s2_clip():
    ds = gio.open_raster(os.path.join(DP, 'GMA_World_DEM_GEBCO.jp2'))
    ly = gio.open_vector(WORLD, name_or_id='GMA_World_Country_50m')
    res = ds.clip(ly)
    print(type(res).__name__, res.shape, res.bounds)

def s3_extent():
    ds = base_ds()
    res = ds.extent()
    print(type(res).__name__, '| gtype:', res.gtype, '| bounds:', res.bounds)

def s4_gen_lonlat():
    ds = base_ds()
    res = ds.gen_lonlat()
    print(type(res).__name__, res.shape, res.dtype)

def s5_get_palette():
    ds = base_ds()
    print(ds.get_palette())

def s6_isopleth():
    ds = base_ds()
    res = ds.isopleth(interval=30)
    print(type(res).__name__, '| gtype:', res.gtype, '| count:', res.get_feature(0).fid if hasattr(res, 'get_feature') else '?')

def s7_plot():
    ds = base_ds()
    ax = ds.plot()
    print(type(ax).__name__)

def s8_reclassify():
    ds = base_ds()
    res = ds.reclassify({0: 1, 50: 2, 100: 3}, method='Range')
    print(type(res).__name__, '| dtype:', res.dtype, '| unique:', np.unique(res.to_numpy()))

def s9_resample():
    ds = base_ds()
    res = ds.resample(0.5)
    print(type(res).__name__, res.shape, res.resolution)

def s10_set_crs():
    ds = base_ds()
    ds.set_crs('EPSG:4326')
    print(ds.crs)

def s11_set_gcps():
    ds = base_ds()
    gcps = [(110.0, 32.0, 0.0, 0.0, 0.0, 'GCP1', '1'), (111.0, 31.0, 0.0, 3.0, 3.0, 'GCP2', '2')]
    ds.set_gcps(gcps, crs='EPSG:4326')
    print(ds.gcps)

def s12_set_geo_transform():
    ds = base_ds()
    ds.set_geo_transform((110, 1, 0, 32, 0, -1))
    print(ds.geo_transform)

def s13_set_metadata():
    ds = base_ds()
    ds.set_metadata({'author': 'gma'})
    print(ds.metadata)

def s14_set_nodata():
    ds = base_ds()
    ds.set_nodata(-9999)
    print(ds.nodata)

def s15_set_palette():
    ds = base_ds()
    ds.set_palette({10: (200, 50, 100, 255), 20: (100, 200, 50, 255)})
    print(ds.get_palette())

def s16_set_statistics():
    ds = base_ds()
    ds.set_statistics([(0, 100, 50, 10)])
    print(ds.stats)

def s17_shift():
    ds = base_ds()
    print('before bounds:', ds.bounds)
    res = ds.shift(0.5)
    print('after bounds:', res.bounds, '| type:', type(res).__name__)

def s18_to_bytearray():
    ds = base_ds()
    ba = ds.to_bytearray()
    print(type(ba).__name__, '| len:', len(ba))

def s19_to_crs():
    ds = base_ds()
    res = ds.to_crs('EPSG:3857')
    print(type(res).__name__, '| crs:', res.crs, '| bounds:', res.bounds)

def s20_to_dtype():
    ds = base_ds()
    res = ds.to_dtype('Byte')
    print(type(res).__name__, '| dtype:', res.dtype)

def s21_to_file():
    ds = base_ds()
    out = os.path.join(TMP, 'doc_dataset_test.tif')
    ds.to_file(out)
    ds2 = gio.open_raster(out)
    print('reopened:', ds2.shape, ds2.dtype)
    os.remove(out)

def s22_to_layer():
    ds = base_ds()
    res = ds.to_layer()
    print(type(res).__name__, '| gtype:', res.gtype)

def s23_to_numpy():
    ds = base_ds()
    ar = ds.to_numpy()
    print(ar.shape, ar.dtype)

def s24_write_array():
    ds = base_ds()
    ds.write_array(np.zeros((2, 6, 6), dtype='float32'))
    print('after write unique:', np.unique(ds.to_numpy()))

if __name__ == '__main__':
    t('algebraic', s1_algebraic)
    t('clip', s2_clip)
    t('extent', s3_extent)
    t('gen_lonlat', s4_gen_lonlat)
    t('get_palette', s5_get_palette)
    t('isopleth', s6_isopleth)
    t('plot', s7_plot)
    t('reclassify', s8_reclassify)
    t('resample', s9_resample)
    t('set_crs', s10_set_crs)
    t('set_gcps', s11_set_gcps)
    t('set_geo_transform', s12_set_geo_transform)
    t('set_metadata', s13_set_metadata)
    t('set_nodata', s14_set_nodata)
    t('set_palette', s15_set_palette)
    t('set_statistics', s16_set_statistics)
    t('shift', s17_shift)
    t('to_bytearray', s18_to_bytearray)
    t('to_crs', s19_to_crs)
    t('to_dtype', s20_to_dtype)
    t('to_file', s21_to_file)
    t('to_layer', s22_to_layer)
    t('to_numpy', s23_to_numpy)
    t('write_array', s24_write_array)
