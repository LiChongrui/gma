# -*- coding: utf-8 -*-
"""4 个继承类页面：删除重复 Method/Property，替换为继承说明卡（latin-1 安全）"""
import io, re, sys

APPLY = '--apply' in sys.argv
ROOT = 'D:/github/gma/docs/UserGuide'

CARD = '''<div class="inherit-card">
<div class="inherit-card__label">Inheritance</div>
<div class="inherit-card__body">
<p style="margin: 0 0 0.35rem;">All properties and methods of <b>{child}</b> are inherited from <b>{parent}</b> - they are not repeated on this page. See the parent class documentation for details.</p>
<a class="inherit-card__btn" href="{link}">{fullname} &rarr;</a>
</div>
</div>
'''

# (rel, parent 短名, 父类全名, 父类页链接)
JOBS = [
    ('gio/VirtualVectorGeoDatabase.md', 'GeoDatabase', 'gma.gio.GeoDatabase', '/docs/UserGuide/gio/GeoDatabase.html'),
    ('gio/VirtualRasterDataset.md', 'Dataset', 'gma.gio.Dataset', '/docs/UserGuide/gio/Dataset.html'),
    ('crs/GeographicCoordinateSystem.md', 'CoordinateReferenceSystem', 'gma.crs.CoordinateReferenceSystem', '/docs/UserGuide/crs/CoordinateReferenceSystem.html'),
    ('crs/ProjectedCoordinateSystem.md', 'CoordinateReferenceSystem', 'gma.crs.CoordinateReferenceSystem', '/docs/UserGuide/crs/CoordinateReferenceSystem.html'),
]

RE_INHERITS = re.compile(
    r'<p>Inherits all properties and methods from <a href="[^"]*">CoordinateReferenceSystem</a>\.</p>\s*'
)

changed = 0
for rel, parent, fullname, link in JOBS:
    path = ROOT + '/' + rel
    s = io.open(path, encoding='latin-1').read()
    child = rel.split('/')[-1].replace('.md', '')
    card = CARD.format(child=child, parent=parent, fullname=fullname, link=link)
    orig = s

    if '\n## Method' in s:
        # gio 两页：截断到 ## Method 之前（其后全部是与父类重复的方法/属性）
        i = s.index('## Method')
        head = s[:i]
        assert '## Property' not in head, 'unexpected Property before Method: ' + rel
        s = head.rstrip('\n') + '\n\n' + card
        action = 'truncated at ## Method'
    else:
        # crs 两页：删 Inherits 尾行，原位放卡
        s2 = RE_INHERITS.sub('', s)
        assert s2 != s, 'Inherits line not found: ' + rel
        s = s2.rstrip('\n') + '\n\n' + card
        action = 'replaced Inherits line'

    # 顺手修复 docstring 重复行（相邻完全相同的 <p>）
    lines = s.split('\n')
    out = []
    dup = 0
    for l in lines:
        if out and out[-1].strip() == l.strip() and l.strip().startswith('<p>') and len(l.strip()) > 10:
            dup += 1
            continue
        out.append(l)
    if dup:
        s = '\n'.join(out)

    if s != orig:
        changed += 1
        print('%-42s %s%s' % (rel, action, ' (+%d dup line removed)' % dup if dup else ''))
        if APPLY:
            io.open(path, 'w', encoding='latin-1', newline='').write(s)

print('changed:', changed, '| APPLY:', APPLY)
