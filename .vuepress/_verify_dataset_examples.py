# -*- coding: utf-8 -*-
"""Dataset.md 内容级验证:类示例 + 24 个方法示例逐块执行"""
import os, re, sys, shutil, traceback

sys.path.insert(0, r'D:\github\gma\.vuepress\_gma341')
import matplotlib
matplotlib.use('Agg')

TMP = os.path.join(os.environ['TEMP'], '_gma_ds_verify')
shutil.rmtree(TMP, ignore_errors=True)
os.makedirs(TMP, exist_ok=True)
os.chdir(TMP)

import gma
import numpy as np
from gma import gio

MD = r'D:\github\gma\docs\UserGuide\gio\Dataset.md'
DP = os.environ['GMA_Data']
shutil.copy(os.path.join(DP, 'GMA_World_DEM_GEBCO.jp2'), os.path.join(TMP, 'demo.tif'))

with open(MD, 'r', encoding='utf-8') as f:
    src = f.read()

# 提取所有 python 代码块(按出现顺序)
blocks = re.findall(r'```python\n(.*?)```', src, re.S)
print(f'total python blocks: {len(blocks)}')  # 类示例1 + 说明内 agg_fun 1 + 方法24 = 26

# 底座
def make_ds():
    arr = np.random.randint(0, 100, (2, 6, 6)).astype('float32')
    return gio.Dataset(data=arr, crs='WGS84', geo_transform=(110, 1, 0, 32, 0, -1))

results = []
for i, code in enumerate(blocks):
    g = {'np': np, 'gio': gio, 'os': os, 'plt': None, 'make_ds': make_ds}
    try:
        if 'matplotlib.pyplot as plt' in code:
            import matplotlib.pyplot as plt
            g['plt'] = plt
        if 'ds = gio.Dataset' in code or 'ds2 = gio.open_raster' in code and 'ds =' not in code:
            g['ds'] = make_ds()
        else:
            g['ds'] = make_ds()
        exec(compile(code, f'block{i}', 'exec'), g)
        results.append((i, True, ''))
        print(f'[OK] block {i}')
    except Exception as e:
        results.append((i, False, f'{type(e).__name__}: {e}'))
        print(f'[FAIL] block {i}: {type(e).__name__}: {e}')
        traceback.print_exc()

ok = sum(1 for _, s, _ in results if s)
print(f'\n===== summary: {ok}/{len(blocks)} OK =====')
for i, s, e in results:
    if not s:
        print(' FAIL block', i, '->', e)
os.chdir(os.environ['USERPROFILE'])
shutil.rmtree(TMP, ignore_errors=True)
