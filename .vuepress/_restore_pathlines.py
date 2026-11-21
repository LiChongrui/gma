# -*- coding: utf-8 -*-
"""恢复 md 里的 Python 全名路径行（gma.xxx.Yyy）：
用户要求页面开头是 gma 库位置（gma.driver.DriveStatistics），
此前误删。数据源：git HEAD（tracked 文件）+ 临时生成产物（55 个生成页）。
插入位置：第一个顶层签名卡（EFF0FC）之前，与签名卡同行相连（照 HEAD 原格式）。
"""
import io, os, re, subprocess

ROOT = 'D:/github/gma/docs/UserGuide'
TMP_OUT = 'D:/github/gma/.vuepress/_tmp_gen/out'

RE_PATHLINE = re.compile(r'^<p style="font-size: 120%;font-weight: bold;">([^<]+)</p>', re.M)
RE_SIG_CLASS = '<span style="background-color:#EFF0FC'   # 类页顶层卡
RE_SIG_FUNC = '<span style="background-color:#F4F4F5'    # 函数页顶层卡

def grab_from_text(text):
    m = RE_PATHLINE.search(text)
    return m.group(0) if m else None

# 1) 临时产物映射
mapping = {}
for dirpath, _dirs, files in os.walk(TMP_OUT):
    for f in files:
        if not f.endswith('.md'):
            continue
        full = os.path.join(dirpath, f)
        rel = os.path.relpath(full, TMP_OUT).replace('\\', '/')
        line = grab_from_text(io.open(full, encoding='utf-8').read())
        if line:
            mapping[rel] = line

# 2) git HEAD 映射（tracked 文件）
tracked = subprocess.run(['git', '-C', 'D:/github/gma', 'ls-files', 'docs/UserGuide'],
                         capture_output=True).stdout.decode('utf-8', 'replace').split()
head_hits = 0
for t in tracked:
    rel = t[len('docs/UserGuide/'):]
    if rel in mapping or not rel.endswith('.md'):
        continue
    r = subprocess.run(['git', '-C', 'D:/github/gma', 'show', 'HEAD:' + t],
                       capture_output=True)
    if r.returncode != 0:
        continue
    line = grab_from_text(r.stdout.decode('utf-8', 'replace'))
    if line:
        mapping[rel] = line
        head_hits += 1

print('mapping total: %d (tmp %d + HEAD %d)' % (len(mapping), len(mapping) - head_hits, head_hits))

# 3) 插入
applied, skipped_has, skipped_nosig, missing = 0, 0, 0, []
for rel in sorted(mapping):
    dst = os.path.join(ROOT, rel)
    if not os.path.exists(dst):
        missing.append(rel)
        continue
    cur = io.open(dst, encoding='latin-1').read()
    # 已有路径行（120%+bold 且不含 9298ED）则跳过
    for m in RE_PATHLINE.finditer(cur):
        if '9298ED' not in m.group(0):
            skipped_has += 1
            break
    else:
        # 顶层签名卡：类页 EFF0FC / 函数页 F4F4F5，取文件中最先出现的
        # （两种卡都在任何成员级卡之前，首个出现即顶层卡）
        i = cur.find(RE_SIG_CLASS)
        j = cur.find(RE_SIG_FUNC)
        cands = [x for x in (i, j) if x >= 0]
        if not cands:
            skipped_nosig += 1
            continue
        i = min(cands)
        cur = cur[:i] + mapping[rel] + cur[i:]
        io.open(dst, 'w', encoding='latin-1', newline='').write(cur)
        applied += 1

print('applied %d, already-present %d, no-sig-card %d, missing %d'
      % (applied, skipped_has, skipped_nosig, len(missing)))
if missing:
    print('missing files:', missing[:10])
