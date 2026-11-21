# -*- coding: utf-8 -*-
"""
API 页成员签名合并重构（方案 A，用户已确认）：
  模式1  ### name + [F4F4F5 方法签名卡]  ->  ### name(args)   （一行成员头，去尾冒号，默认值 span 拍平）
  模式2  ### name + [裸属性签名行]        ->  ### name          （裸签名行删除）
  模式3  空描述行 <p style="margin-left: 2em;"></p>      ->  删除
  模式4  顶层路径标题 <p style="font-size: 120%;font-weight: bold;">gma.xxx.Y</p> -> 删除（同行签名卡保留）
用法：python _refactor_members.py --dry-run | --apply
读写字节经 latin-1 roundtrip，GBK 中文不受影响；被改动的内容均为 ASCII。
"""
import re, sys
from pathlib import Path

ROOT = Path(r'D:/github/gma/docs/UserGuide')
APPLY = '--apply' in sys.argv

RE_H3        = re.compile(r'^### (.+?)\s*$')
RE_CARD      = re.compile(r'^<span style="background-color:#F4F4F5[^"]*">(.*)</span>\s*$')
RE_NAME      = re.compile(r'<span style="color: #616AE5; font-weight: bold;font-size: 125%;">\.(.*?)</span>')
RE_ARGS      = re.compile(r'<span style="font-style: italic; color: black;font-size: 120%;">(.*?)</span>\s*$')
RE_DEFAULT   = re.compile(r'<span style="color:#48566B">(.*?)</span>')
RE_BARE      = re.compile(r'^<span style="">.*?<span style="color: #616AE5; font-weight: bold;font-size: 125%;">\.(.*?)</span>')
RE_EMPTY_P   = re.compile(r'^<p style="margin-left: 2em;"></p>\s*$')
RE_PATH_P    = re.compile(r'<p style="font-size: 120%;font-weight: bold;">[^<]*</p>')

ARGSPAN = '<span style="font-weight: normal;font-style: italic;color:#8a90a8;font-size: 88%;">{}</span>'
stats = dict(merged=0, prop=0, path=0, emptyp=0)
warns = []

def process(path: Path):
    text = path.read_bytes().decode('latin-1')
    lines = text.split('\n')
    out, i, n = [], 0, len(lines)
    h3_idx = None            # out 中已输出的 ### 行下标
    h3_name = None
    changed = False
    while i < n:
        line = lines[i]
        m3 = RE_H3.match(line)
        if m3:
            h3_idx, h3_name = len(out), m3.group(1).strip()
            out.append(line); i += 1; continue
        if h3_idx is not None and line.strip():
            card = RE_CARD.match(line.strip())
            bare = RE_BARE.match(line.strip())
            if card:
                mn = RE_NAME.search(card.group(1))
                ma = RE_ARGS.search(card.group(1))
                if not mn or not ma:
                    warns.append(f'{path.name}: card-not-parsed @### {h3_name}')
                else:
                    name = mn.group(1).strip()
                    if name != h3_name:
                        warns.append(f'{path.name}: name-mismatch {h3_name} vs {name}')
                    else:
                        args = RE_DEFAULT.sub(r'\1', ma.group(1)).strip()
                        if args.endswith(':'):
                            args = args[:-1]
                        out[h3_idx] = f'### {h3_name}{ARGSPAN.format(args)}'
                        stats['merged'] += 1; changed = True
                        i += 1; h3_idx = h3_name = None; continue
            elif bare:
                name = bare.group(1).strip()
                if name != h3_name:
                    warns.append(f'{path.name}: prop-mismatch {h3_name} vs {name}')
                    out.append(line)
                else:
                    stats['prop'] += 1; changed = True   # 整行删除
                i += 1; h3_idx = h3_name = None; continue
            h3_idx = h3_name = None
        if RE_EMPTY_P.match(line):
            stats['emptyp'] += 1; changed = True; i += 1; continue
        new = RE_PATH_P.sub('', line)
        if new != line:
            stats['path'] += 1; changed = True
            line = new
            if not line.strip():
                i += 1; continue     # 整行只剩路径 p -> 删行
        out.append(line); i += 1
    if changed and APPLY:
        data = '\n'.join(out).encode('latin-1')
        assert data.decode('latin-1').split('\n') == out, 'roundtrip check failed'
        path.write_bytes(data)
    return changed

files = sorted(ROOT.rglob('*.md'))
touched = [p for p in files if process(p)]
print('APPLY' if APPLY else 'DRY-RUN', '| files touched:', len(touched), '|', stats)
for w in warns[:20]:
    print('WARN:', w)
print('warn total:', len(warns))
