# -*- coding: utf-8 -*-
"""核对 sidebar.js / navbar.js 配置与 UserGuide 文件一一对应。"""
import io
import re
import os

os.chdir('D:/github/gma')
sb = io.open('.vuepress/config/sidebar.js', encoding='utf-8').read()

sec_pat = re.compile(r"'/docs/UserGuide/([a-z]+)/':\s*\[(.*?)\n    \],", re.S)
ch_pat = re.compile(r'children:\s*\[(.*?)\]', re.S)
it_pat = re.compile(r'["\']([^"\']+)["\']')

total, missing = 0, []
for mod, seg in sec_pat.findall(sb):
    for arr in ch_pat.findall(seg):
        for it in it_pat.findall(arr):
            total += 1
            if it == '':
                if not os.path.exists('docs/UserGuide/%s/README.md' % mod):
                    missing.append('%s/README.md' % mod)
            else:
                p = 'docs/UserGuide/%s/%s.md' % (mod, it)
                if not os.path.exists(p):
                    missing.append(p)

print('模块段:', [m for m, _ in sec_pat.findall(sb)])
print('children 条目总数:', total)
print('缺失:', missing if missing else '无')

nb = io.open('.vuepress/config/navbar.js', encoding='utf-8').read()
lk_pat = re.compile(r"link:\s*'(/docs/UserGuide/[a-z]+/)'")
for link in lk_pat.findall(nb):
    p = 'docs/UserGuide/%s/README.md' % link.split('/')[-2]
    print('navbar', link, '->', 'OK' if os.path.exists(p) else 'MISSING')

# 生成文件总数
n = 0
for root, _, files in os.walk('docs/UserGuide'):
    n += len([f for f in files if f.endswith('.md')])
print('UserGuide md 总数:', n)

# 孤儿页面：存在但未进侧栏
covered = set()
for mod, seg in sec_pat.findall(sb):
    for arr in ch_pat.findall(seg):
        for it in it_pat.findall(arr):
            covered.add('docs/UserGuide/%s/README.md' % mod if it == ''
                        else 'docs/UserGuide/%s/%s.md' % (mod, it))
all_md = []
for root, _, files in os.walk('docs/UserGuide'):
    for f in files:
        if f.endswith('.md'):
            all_md.append(os.path.join(root, f).replace(os.sep, '/'))
orphans = sorted(set(all_md) - covered)
print('未进侧栏的文件:', len(orphans))
for o in orphans:
    print(' ', o)
