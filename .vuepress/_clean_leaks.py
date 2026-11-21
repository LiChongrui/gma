# -*- coding: utf-8 -*-
"""重跑 docstring 泄漏星号清理（latin-1 字节安全，GBK 中文不受影响）：
  1. ;">**Optional:</p>  -> ;">Optional:</p>
  2. Optional:**</p>     -> Optional:</p>
  3. ;">**Note:</p>      -> ;">Note:</p>
  4. ;">**Other parameters(...):</p> -> 去掉 **
  5. 残留 ***word** 加粗（如 ***text**）
"""
import re
from pathlib import Path

ROOT = Path(r'D:/github/gma/docs/UserGuide')
subs = [
    (';">**Optional:</p>', ';">Optional:</p>'),
    ('Optional:**</p>', 'Optional:</p>'),
    (';">**Note:</p>', ';">Note:</p>'),
    (';">**Other parameters(', ';">Other parameters('),
]
pat_bold = re.compile(rb'\*\*\*([A-Za-z0-9_][^*<]{0,60}?)\*\*')
stats = dict(f1=0, f2=0, f3=0, f4=0, f5=0)
for p in ROOT.rglob('*.md'):
    b = p.read_bytes()
    orig = b
    for i, (a, x) in enumerate(subs, 1):
        ab, xb = a.encode('ascii'), x.encode('ascii')
        if ab in b:
            stats[f'f{i}'] += b.count(ab)
            b = b.replace(ab, xb)
    nb = pat_bold.sub(r'***\1*'.encode(), b)
    if nb != b:
        stats['f5'] += 1
        b = nb
    if b != orig:
        p.write_bytes(b)
print('APPLY' if True else 'DRY', stats)
