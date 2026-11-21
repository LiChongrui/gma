# -*- coding: utf-8 -*-
"""内容级验证:提取各页 Example 代码真实运行(输出文件重定向到临时目录)"""
import os, re, shutil, traceback, sys

# gma 3.0.4.1 解压环境(导入后 GMA_Data 环境变量才会被设置)
sys.path.insert(0, r'D:\github\gma\.vuepress\_gma341')
import gma

DOCS = r'D:\github\gma\docs\UserGuide\gio'
TMP = os.path.join(os.environ['TEMP'], '_gma_doc_verify')
os.makedirs(TMP, exist_ok=True)

PAGES = ['open_file.md', 'open_vector.md', 'open_raster.md', 'read_dataframe.md',
         'GeoDatabase.md', 'Layer.md', 'Feature.md', 'Geometry.md',
         'VirtualVectorGeoDatabase.md', 'VirtualRasterDataset.md',
         'FieldType.md', 'FieldTypes.md', 'Dataset.md']

# 输出文件重定向:示例里的输出文件名 -> 临时目录
OUT_RE = re.compile(r"(to_file\(')([^']+?)(?:'\))")
# Dataset.md 的 demo.tif 用真实文件替代
DP = os.environ['GMA_Data']
shutil.copy(os.path.join(DP, 'GMA_World_DEM_GEBCO.jp2'), os.path.join(TMP, 'demo.tif'))

ok, fail = [], []
for fname in PAGES:
    with open(os.path.join(DOCS, fname), 'r', encoding='utf-8') as f:
        src = f.read()
    m = re.search(r'## Example\n\n```python\n(.*?)```', src, re.S)
    if not m:
        fail.append((fname, 'no Example block'))
        continue
    code = m.group(1)
    # 输出文件重定向到临时目录(正斜杠避免 \U 转义)
    def redirect(mm):
        return f"{mm.group(1)}{os.path.join(TMP, mm.group(2)).replace(chr(92), '/')}')"
    code_run = OUT_RE.sub(redirect, code)
    # 忌 exec 里的 print 汇总;保持原样执行
    try:
        g = {'__name__': '__main__'}
        cwd = os.getcwd()
        os.chdir(TMP)  # 相对路径(demo.tif/输出文件)都在临时目录解析
        try:
            exec(compile(code_run, fname, 'exec'), g)
        finally:
            os.chdir(cwd)
        ok.append(fname)
        print(f'[OK] {fname}')
    except Exception as e:
        fail.append((fname, f'{type(e).__name__}: {e}'))
        print(f'[FAIL] {fname}: {type(e).__name__}: {e}')
        traceback.print_exc()

print(f'\n===== summary: {len(ok)} OK, {len(fail)} FAIL =====')
for f_, e_ in fail:
    print(' ', f_, '->', e_)
shutil.rmtree(TMP, ignore_errors=True)
