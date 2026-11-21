# -*- coding: utf-8 -*-
"""Bisect: 复刻 _redesign_dataset.py 的执行序列, 在 isopleth 叠加处打印诊断。"""
import os, sys, io

SRC = r'D:\github\gma\.vuepress\_redesign_dataset.py'
src = open(SRC, encoding='utf-8').read()
head = src.split("print('\\n--- images ---')")[0]
g = {'__name__': '__bisect__'}
exec(compile(head, SRC, 'exec'), g)

# 到此为止: results/prop_results 已实测, img_* 函数已定义, 但尚未生成任何图
plt = g['plt']; gio = g['gio']; IMGDIR = g['IMGDIR']
fresh = g['fresh']

print('\n=== 前置图函数(与主脚本同序) ===')
g['img_plot'](); g['img_clip'](); g['img_resample'](); g['img_reclassify']()
g['img_set_palette'](); g['img_to_crs']()

print('\n=== isopleth 诊断 ===')
ns = fresh('isopleth')
ds, res = ns['ds'], ns['res']
fig, axs = plt.subplots(1, 2, figsize=(9, 3.6), dpi=110)
ds.plot(ax=axs[0])
ds.plot(ax=axs[1])
im0 = axs[0].images[0]; im1 = axs[1].images[0]
for tag, im in (('left', im0), ('right', im1)):
    cm = im.get_cmap()
    print(f'after ds.plot[{tag}]: n={len(axs[0].images) if tag=="left" else len(axs[1].images)} '
          f'cmap_name={getattr(cm, "name", None)} N={getattr(cm, "N", None)} visible={im.get_visible()}')

res.plot(ax=axs[1], edgecolor='red')
im1 = axs[1].images[0]
cm = im1.get_cmap()
print(f'after overlay[right]: n_images={len(axs[1].images)} n_collections={len(axs[1].collections)} '
      f'cmap_name={getattr(cm, "name", None)} N={getattr(cm, "N", None)} visible={im1.get_visible()} clim={im1.get_clim()}')
print(f'  right panel: n_images_total={len(axs[1].images)}, all cmaps:',
      [getattr(i.get_cmap(), 'name', '?') for i in axs[1].images])
fig.canvas.draw()
print(f'after draw[right]: visible={im1.get_visible()} n_images={len(axs[1].images)}')

fig.savefig(os.path.join(IMGDIR, 'bisect_isopleth.png'), dpi=110)
plt.close('all')
print('SAVED bisect_isopleth.png')
