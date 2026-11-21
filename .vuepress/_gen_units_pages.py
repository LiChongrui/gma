# -*- coding: utf-8 -*-
"""4 个常数类页面重写：[const] 轻签名 + Constants 成员表 + 修正示例（实例直访）"""
import io, json, sys

APPLY = '--apply' in sys.argv
DATA = json.load(open('D:/github/gma/.vuepress/_units_data.json'))
ROOT = 'D:/github/gma/docs/UserGuide/crs'

# (类名, 描述, 示例属性, 值格式函数, 表头)
JOBS = [
    ('AngleUnits',
     'Angle units object. Conversion factors relative to the radian.',
     'DEGREE', lambda v: repr(v),
     ['Constant', 'Value (to radian)']),
    ('LinearUnits',
     'Linear units object. Conversion factors relative to the metre.',
     'METRE', lambda v: repr(v),
     ['Constant', 'Value (to metre)']),
    ('Primems',
     'Prime meridian object. Longitude values in degrees.',
     'Greenwich', lambda v: repr(v),
     ['Constant', 'Longitude (degrees)']),
    ('Ellips',
     'Default ellipsoids. Built from the PROJ database when created.',
     'WGS_84', lambda v: repr(v['semi_major']),
     ['Constant', 'Semi-major axis (m)', 'Inverse flattening']),
]

for name, desc, example, fmt, headers in JOBS:
    members = DATA[name]
    lines = []
    lines.append('---')
    lines.append('title: %s' % name)
    lines.append('date: 2026-11-20')
    lines.append('---')
    lines.append('')
    # 轻量 const 签名（无参数括号，[const] 标签）
    lines.append('<p style="font-size: 120%%;font-weight: bold;">gma.crs.%s</p>'
                 '<span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;">'
                 '<span style="color: gray;font-size:90%%;">[const] </span>'
                 '<span style="color: #616AE5; font-weight: bold;font-size: 150%%;">%s</span></span>' % (name, name))
    lines.append('')
    lines.append('<p>%s</p>' % desc)
    lines.append('<p>Attribute names are derived from the PROJ database and accessed directly as instance attributes:</p>')
    lines.append('')
    lines.append('```python')
    lines.append('from gma import crs')
    lines.append('crs.%s.%s' % (name, example))
    lines.append('```')
    lines.append('')
    if name == 'Ellips':
        val = members[example]
        lines.append('<p>crs.%s.%s --> <code style="text-indent: 0em;">%s</code></p>'
                     % (name, example, repr(val)))
    else:
        lines.append('<p>crs.%s.%s --> <code style="text-indent: 0em;">%s</code></p>'
                     % (name, example, repr(members[example])))
    lines.append('')
    lines.append('## Constants')
    lines.append('')
    lines.append('| ' + ' | '.join(headers) + ' |')
    lines.append('| ' + ' | '.join(['---'] * len(headers)) + ' |')
    for k in sorted(members):
        v = members[k]
        if name == 'Ellips':
            lines.append('| `%s` | %s | %s |' % (k, repr(v['semi_major']), repr(v['inv_flattening'])))
        else:
            lines.append('| `%s` | %s |' % (k, fmt(v)))
    lines.append('')

    text = '\n'.join(lines)
    path = '%s/%s.md' % (ROOT, name)
    orig = io.open(path, encoding='latin-1').read()
    assert all(ord(c) < 128 for c in text), 'non-ascii in %s' % name
    print('%-14s lines: %d -> %d, consts: %d' % (name, orig.count('\n'), text.count('\n'), len(members)))
    if APPLY:
        io.open(path, 'w', encoding='latin-1', newline='').write(text)
print('APPLY:', APPLY)
