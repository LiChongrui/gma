# -*- coding: utf-8 -*-
"""生成 crs/ProjMethods.md 总览页（常数容器形态 + 34 投影方法总表）"""
import io, json, sys

APPLY = '--apply' in sys.argv
DATA = json.load(open('D:/github/gma/.vuepress/_projmethods_data.json'))

L = []
L.append('---')
L.append('title: ProjMethods')
L.append('date: 2026-11-20')
L.append('---')
L.append('')
L.append('<p style="font-size: 120%%;font-weight: bold;">gma.crs.ProjMethods</p>'
         '<span style="background-color:#EFF0FC;display: block;line-height:1.6;border-radius: 0.3rem;">'
         '<span style="color: gray;font-size:90%%;">[const] </span>'
         '<span style="color: #616AE5; font-weight: bold;font-size: 150%%;">ProjMethods</span></span>' % ())
L.append('')
L.append('<p>The projection methods container. All supported projection methods are mounted as attributes - each attribute is a projection method class, and instantiating it creates a projection method object which holds the parameters and renders the <code style="text-indent: 0em;">PROJECTION</code> fragment of WKT (attributes: <b>name</b>, <b>pars</b>).</p>')
L.append('')
L.append('```python')
L.append('from gma import crs')
L.append('')
L.append('method = crs.ProjMethods.Mercator(central_meridian = 110)')
L.append('```')
L.append('')
L.append('<p>crs.ProjMethods.Mercator() --> <code style="text-indent: 0em;">&lt;ProjMethod:Mercator&gt;</code></p>')
L.append('')
L.append('## Projection methods')
L.append('')
L.append('| Method | Description | Parameters |')
L.append('| --- | --- | --- |')
for name in sorted(DATA):
    d = DATA[name]
    desc = d['desc'] if d['desc'] else '%s projection method.' % name
    params = ', '.join(d['params'])
    L.append('| [`%s`](/docs/UserGuide/crs/ProjMethods/%s.html) | %s | <code style="text-indent: 0em;">%s</code> |' % (name, name, desc, params))
L.append('')

text = '\n'.join(L)
assert all(ord(c) < 128 for c in text), 'non-ascii'
path = 'D:/github/gma/docs/UserGuide/crs/ProjMethods.md'
print('lines:', text.count('\n'), '| methods:', len(DATA))
if APPLY:
    io.open(path, 'w', encoding='latin-1', newline='').write(text)
    print('written', path)
