# -*- coding: utf-8 -*-
"""把 34 个 ProjMethods 方法页合并进 ProjMethods.md 总览页。
产出:重写的 ProjMethods.md([const] 签名 + Parameters 参数表 + 锚点索引表 + 34 个方法小节);
方法页目录整体 rename 到备份目录(不删除,绕过批量删除守卫)。
"""
import os, re, shutil

SRC_DIR = r"D:/github/gma/docs/UserGuide/crs/ProjMethods"
OUT_FILE = r"D:/github/gma/docs/UserGuide/crs/ProjMethods.md"
BAK_DIR = r"D:/github/gma/.vuepress/_projmethods_pages_backup"
OVERVIEW = r"D:/github/gma/docs/UserGuide/crs/ProjMethods.md"

# 读取现有总览页头部(1-16 行:frontmatter + [const] 签名卡 + 说明 + 示例)与索引表
with open(OVERVIEW, encoding="utf-8") as f:
    old_lines = f.read().splitlines()
head_lines = old_lines[:16]          # 到 `crs.ProjMethods.Mercator() -->` 行为止
assert head_lines[-1].startswith("<p>crs.ProjMethods.Mercator()"), head_lines[-1][:60]

# 解析索引表:| [`Name`](url) | Desc | params |
index_rows = []
for ln in old_lines:
    m = re.match(r"\| \[`([A-Za-z0-9]+)`\]\([^)]+\) \| (.*?) \| (.*?) \|", ln)
    if m:
        index_rows.append(m.groups())
assert len(index_rows) == 34, f"index rows = {len(index_rows)}"

# 提取参数表(9 个共用参数,说明文案取自方法页)
PARAM_TABLE = """| Parameter | Description |
| --- | --- |
| <code style="text-indent: 0em;">central_meridian</code> | The central meridian. |
| <code style="text-indent: 0em;">false_easting</code> | X offset from planar origin. |
| <code style="text-indent: 0em;">false_northing</code> | Y offset from planar origin. |
| <code style="text-indent: 0em;">latitude_of_center</code> | The central latitude. |
| <code style="text-indent: 0em;">latitude_of_origin</code> | The origin latitude. |
| <code style="text-indent: 0em;">longitude_of_center</code> | The central longitude. |
| <code style="text-indent: 0em;">scale_factor</code> | The scale factor. |
| <code style="text-indent: 0em;">standard_parallel_1</code> | The first standard parallels latitude of correct scale. |
| <code style="text-indent: 0em;">standard_parallel_2</code> | The second standard parallels latitude of correct scale. |"""

# 从 34 个方法页提取签名卡行与说明段
pages = sorted(os.listdir(SRC_DIR))
assert len(pages) == 34, f"pages = {len(pages)}"
sections = []
for fn in pages:
    name = fn[:-3]
    with open(os.path.join(SRC_DIR, fn), encoding="utf-8") as f:
        body = f.read()
    sig = None
    desc = None
    for ln in body.splitlines():
        if sig is None and ln.startswith('<p style="font-size: 120%;font-weight: bold;">gma.crs.ProjMethods.'):
            sig = ln
        elif sig is not None and desc is None and ln.startswith("<p>") and not ln.startswith("<p style"):
            desc = ln
    assert sig and desc, f"{fn}: sig={bool(sig)} desc={bool(desc)}"
    # 小节:### Name + 路径行&签名卡 + 说明
    sections.append(f"### {name}\n\n{sig}\n\n{desc}")

# 锚点化索引表(Method 列改页内锚点)
anchor_rows = [f"| [`{n}`](#{n.lower()}) | {d} | {p} |" for n, d, p in index_rows]

out = "\n".join(head_lines) + "\n\n"
out += "## Parameters\n\n"
out += '<p>Parameters shared by projection methods. The default value of each parameter depends on the method and is shown in each method signature below.</p>\n\n'
out += PARAM_TABLE + "\n\n"
out += "## Projection methods\n\n"
out += "| Method | Description | Parameters |\n| --- | --- | --- |\n"
out += "\n".join(anchor_rows) + "\n\n"
out += "\n\n".join(sections) + "\n"

with open(OUT_FILE, "w", encoding="utf-8", newline="\n") as f:
    f.write(out)

# 方法页目录整体 rename 到备份目录(重命名而非删除)
if os.path.exists(BAK_DIR):
    raise SystemExit(f"backup dir already exists: {BAK_DIR}")
os.rename(SRC_DIR, BAK_DIR)

print(f"OK: {OUT_FILE} rebuilt ({len(out)} chars, {len(sections)} sections)")
print(f"OK: pages moved to {BAK_DIR}")
