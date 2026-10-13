#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""开发用测试页生成器 —— 不参与主题使用，纯粹用来截图自检。

复刻 Typora 的真实 DOM 选择器（含 `md-task-list-item` 这类易错标记），
把主题套在静态页面上渲染，再用 headless Chrome 截图检查。

用法：
    cd dev && python3 make_harness.py        # 用仓库根目录的 blue-ice*.css
"""
import pathlib

from demo_content import CONTENT, SIDEBAR

HERE = pathlib.Path(__file__).resolve().parent          # dev/
ROOT = HERE.parent                                      # 仓库根
OUT = HERE / "out"
SHOTS = ROOT / "screenshots"

TPL = """<!DOCTYPE html>
<html lang="zh-CN" class="{htmlcls}">
<head><meta charset="utf-8" /><title>Blue Ice harness ({theme})</title>
<link rel="stylesheet" href="../../{css}" />
<style>
  /* 仅 harness 自身的窗口骨架，不属于主题 */
  html, body {{ height: 100%; }}
  body {{ display: flex; flex-direction: row; margin: 0; overflow: hidden; }}
  #typora-sidebar {{ width: 268px; flex: 0 0 268px; height: 100%; overflow-y: auto; padding: 10px 12px 60px; box-sizing: border-box; }}
  content {{ flex: 1 1 auto; height: 100%; overflow-y: auto; box-sizing: border-box; display: block; }}
  /* flat 模式：整页展开，方便一次性截全 */
  body.flat {{ display: block; overflow: visible; height: auto; }}
  body.flat #typora-sidebar {{ position: fixed; top: 0; left: 0; bottom: 0; }}
  body.flat content {{ margin-left: 268px; height: auto; overflow: visible; display: block; }}
  footer.ty-footer {{ position: fixed; left: 268px; right: 0; bottom: 0; height: 28px; display: flex; align-items: center; gap: 18px; padding: 0 18px; font-size: 12px; z-index: 5; }}
  .file-list-item {{ padding: 3px 6px; font-size: 13px; }}
  .file-node-content {{ padding: 2px 6px; display: block; font-size: 13px; }}
  .outline-item {{ padding: 1px 4px; font-size: 13px; }}
  .outline-label {{ cursor: pointer; text-decoration: none; display: inline-block; }}
  .outline-children {{ list-style: none; padding-left: 14px; margin: 0; }}
  .outline-item-wrapper {{ list-style: none; padding-left: 6px; margin: 4px 0; }}
  .outline-title {{ font-size: 12px; letter-spacing: .05em; padding: 6px 8px; opacity: .75; }}
  #file-library-search {{ padding: 6px 2px 10px; }}
  #file-library-search-input {{ width: 100%; padding: 5px 9px; box-sizing: border-box; font-size: 13px; }}
  .sidebar-tabs {{ display: flex; gap: 14px; padding: 2px 6px 0; }}
  .CodeMirror-line {{ line-height: 1.7; }}
  .outline-label {{ display: inline-block; }}
  table {{ border-collapse: separate; }}
</style>
</head>
<body class="typora-node os-mac show-footer">
{sidebar}
<content>
  <div id="write">{content}</div>
</content>
<footer class="ty-footer">
  <div class="footer-item">1,204 词</div>
  <div class="footer-item">6,318 字符</div>
  <div class="footer-item">蓝冰 · {theme}</div>
</footer>
</body></html>"""


def build(theme, flat=False):
    css = "blue-ice.css" if theme == "light" else "blue-ice-dark.css"
    html = TPL.format(theme=theme, css=css,
                      htmlcls="theme-light" if theme == "light" else "theme-dark",
                      sidebar=SIDEBAR, content=CONTENT)
    if flat:
        html = html.replace('class="typora-node os-mac show-footer"',
                            'class="typora-node os-mac show-footer flat"')
    name = f"harness-{theme}{'-flat' if flat else ''}.html"
    OUT.mkdir(exist_ok=True)
    (OUT / name).write_text(html, encoding="utf-8")
    print("wrote", OUT / name, len(html), "bytes")


if __name__ == "__main__":
    for t in ("light", "dark"):
        build(t, flat=False)
        build(t, flat=True)
