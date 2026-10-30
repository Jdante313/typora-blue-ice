#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成仓库根目录的 index.html —— 一个不依赖任何外部资源的在线预览页。

为什么值得做：官方主题库和 GitHub 上，别人决定要不要试一个主题只看三秒。
截图是死的，能当场切明暗的活页面说服力强得多。

页面本身会把主题 CSS 套在模拟的 Typora 窗口上（侧栏 + 写作区），
并提供一个明暗切换按钮，所以它既是预览页，也是主题的真实渲染结果。

用法：
    cd dev && python3 make_showcase.py
"""
import pathlib

from demo_content import CONTENT, SIDEBAR

HERE = pathlib.Path(__file__).resolve().parent          # dev/
ROOT = HERE.parent                                      # 仓库根

PAGE = """<!DOCTYPE html>
<html lang="zh-CN" class="theme-light" data-theme="light">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>蓝冰 Blue Ice — Typora 主题</title>
<meta name="description" content="蓝冰 Blue Ice：一套冷蓝冰面的 Typora 主题，含浅色与深色两版。雾面面板、深墨代码块、克制的暖琥珀。" />
<link id="theme-css" rel="stylesheet" href="blue-ice.css" />
<style>
  /* ---- 预览页自身的骨架。命名都带 show- 前缀，避免和主题选择器打架 ---- */
  html { scroll-behavior: smooth; }

  .show-header {
    position: sticky; top: 0; z-index: 20;
    display: flex; align-items: center; gap: 14px;
    padding: 10px 22px;
    background: color-mix(in srgb, var(--ice-panel-solid) 82%, transparent);
    backdrop-filter: saturate(1.4) blur(18px);
    -webkit-backdrop-filter: saturate(1.4) blur(18px);
    border-bottom: 1px solid var(--ice-hairline-soft);
  }
  .show-brand {
    font-family: var(--ice-font-display);
    font-weight: 600; font-size: 15px; letter-spacing: .02em;
    color: var(--ice-ink);
  }
  .show-brand span { color: var(--ice-accent); }
  .show-header .show-spacer { flex: 1 1 auto; }
  .show-btn {
    font: inherit; font-size: 13px; line-height: 1;
    padding: 7px 14px; cursor: pointer;
    color: var(--ice-ink-mid);
    background: var(--ice-panel-solid);
    border: 1px solid var(--ice-hairline);
    border-radius: 999px;
    box-shadow: var(--ice-shadow-sm);
    transition: color .18s var(--ice-ease), border-color .18s var(--ice-ease),
                background-color .18s var(--ice-ease);
  }
  .show-btn:hover {
    color: var(--ice-accent);
    border-color: var(--ice-accent-light);
    background: var(--ice-accent-soft);
  }

  /* 三个版本的分段切换器 */
  .show-seg {
    display: inline-flex; overflow: hidden;
    background: var(--ice-panel-solid);
    border: 1px solid var(--ice-hairline);
    border-radius: 999px;
    box-shadow: var(--ice-shadow-sm);
  }
  .show-seg button {
    font: inherit; font-size: 13px; line-height: 1;
    padding: 8px 15px; cursor: pointer;
    border: none; background: transparent;
    color: var(--ice-ink-mid);
    transition: color .18s var(--ice-ease), background-color .18s var(--ice-ease);
  }
  .show-seg button + button { border-left: 1px solid var(--ice-hairline-soft); }
  .show-seg button:hover:not(.active) {
    color: var(--ice-accent);
    background: var(--ice-accent-soft);
  }
  .show-seg button.active {
    color: #fff;
    background-image: linear-gradient(140deg, var(--ice-accent), #14678a);
  }

  .show-wrap { max-width: 1180px; margin: 0 auto; padding: 0 22px 72px; }

  /* ---- 头图区 ---- */
  .show-hero { padding: 68px 8px 44px; max-width: 780px; }
  .show-eyebrow {
    display: inline-block; margin-bottom: 18px;
    font-size: 12px; letter-spacing: .16em; text-transform: uppercase;
    color: var(--ice-accent);
  }
  .show-hero h1 {
    font-family: var(--ice-font-display);
    font-size: 3.1em; font-weight: 600; line-height: 1.16;
    letter-spacing: -.01em; text-align: left;
    margin: 0 0 20px; padding: 0; color: var(--ice-ink);
  }
  .show-hero h1::after { display: none; }
  .show-hero h1 em {
    font-style: normal;
    background-image: linear-gradient(100deg, var(--ice-accent-light), var(--ice-accent));
    -webkit-background-clip: text; background-clip: text;
    -webkit-text-fill-color: transparent; color: var(--ice-accent);
  }
  .show-lede {
    font-size: 1.06em; line-height: 1.85; color: var(--ice-ink-mid);
    margin: 0 0 26px; max-width: 62ch;
  }
  .show-chips { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 30px; }
  .show-chip {
    font-size: 12.5px; padding: 5px 11px; border-radius: 999px;
    color: var(--ice-ink-mid);
    background: var(--ice-accent-softer);
    border: 1px solid var(--ice-hairline-soft);
  }
  .show-actions { display: flex; flex-wrap: wrap; gap: 10px; }
  .show-cta {
    display: inline-block; text-decoration: none;
    /* 显式复位全部 background 子属性：主题给正文链接设了 background-size，
       只覆盖 background-image 的话渐变会被压成一条 */
    background-repeat: no-repeat; background-position: 0 0; background-size: auto;
    background-origin: padding-box; background-clip: border-box;
    font-size: 14px; font-weight: 600; letter-spacing: .01em;
    padding: 10px 20px; border-radius: 999px;
    /* 渐变整体压深：原来的浅冰蓝底 + 白字对比度不够，字几乎看不清 */
    background-image: linear-gradient(140deg, var(--ice-accent), #14678a);
    color: #ffffff; text-shadow: 0 1px 1px rgba(6, 32, 45, .22);
    border: 1px solid transparent;
    box-shadow: 0 4px 14px rgba(14, 44, 60, .2), inset 0 1px 0 rgba(255, 255, 255, .22);
    transition: transform .18s var(--ice-ease), box-shadow .18s var(--ice-ease);
  }
  .show-cta:hover { transform: translateY(-1px); box-shadow: 0 8px 22px rgba(14, 44, 60, .26), inset 0 1px 0 rgba(255, 255, 255, .22); }
  .show-cta:focus-visible { outline: 2px solid var(--ice-accent-light); outline-offset: 2px; }
  .show-cta.show-ghost {
    background-image: none; color: var(--ice-accent);
    background-color: var(--ice-panel-solid);
    border-color: var(--ice-hairline);
    box-shadow: var(--ice-shadow-sm);
  }
  .show-cta.show-ghost:hover { background-color: var(--ice-accent-soft); border-color: var(--ice-accent-light); }

  /* ---- 模拟的 Typora 窗口 ---- */
  .show-window {
    display: flex; overflow: hidden;
    background: var(--ice-panel);
    border: 1px solid var(--ice-hairline-soft);
    border-radius: var(--ice-radius-lg);
    box-shadow: var(--ice-shadow-lg);
  }
  .show-window #typora-sidebar {
    width: 248px; flex: 0 0 248px;
    padding: 12px 12px 24px;
    overflow-y: auto; max-height: 1180px;
    box-sizing: border-box;
    position: static;
  }
  .show-window content {
    flex: 1 1 auto; min-width: 0; display: block;
    background: transparent;
    max-height: 1180px; overflow-y: auto;
  }
  .show-window #write { box-shadow: none; border: none; border-radius: 0; margin: 0; max-width: none; }
  /* 预览页里的代码行高与真实 Typora 对齐，避免看着比实际松散 */
  .show-window .CodeMirror-line { line-height: 1.7; }
  .show-window .file-list-item { padding: 3px 6px; font-size: 13px; }
  .show-window .file-node-content { padding: 2px 6px; display: block; font-size: 13px; }
  .show-window .outline-item { padding: 1px 4px; font-size: 13px; }
  .show-window .outline-label { display: inline-block; text-decoration: none; cursor: pointer; }
  .show-window .outline-children { list-style: none; padding-left: 14px; margin: 0; }
  .show-window .outline-item-wrapper { list-style: none; padding-left: 6px; margin: 4px 0; }
  .show-window .outline-title { font-size: 12px; letter-spacing: .05em; padding: 6px 8px; opacity: .75; }
  .show-window .sidebar-tabs { display: flex; gap: 14px; padding: 2px 6px 0; }
  .show-window #file-library-search { padding: 6px 2px 10px; }
  .show-window #file-library-search-input { width: 100%; padding: 5px 9px; box-sizing: border-box; font-size: 13px; }
  .show-window table { border-collapse: separate; }

  .show-caption {
    margin: 14px 2px 0; font-size: 12.5px; color: var(--ice-ink-soft);
  }

  /* ---- 下方的安装说明 ---- */
  .show-steps { margin-top: 64px; display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; }
  .show-step {
    padding: 22px 22px 24px;
    background: var(--ice-panel);
    border: 1px solid var(--ice-hairline-soft);
    border-radius: var(--ice-radius-md);
    box-shadow: var(--ice-shadow-sm);
  }
  .show-step h3 {
    margin: 0 0 10px; padding: 0; font-size: 1.02em; color: var(--ice-ink);
    font-family: var(--ice-font-display);
  }
  .show-step h3::before { display: none; }
  .show-step p { margin: 0 0 8px; font-size: .93em; color: var(--ice-ink-mid); line-height: 1.75; }
  .show-step p:last-child { margin-bottom: 0; }
  .show-step code {
    font-size: .86em; padding: .1em .38em; border-radius: var(--ice-radius-sm);
    background: var(--ice-accent-soft); color: var(--ice-accent);
    border: 1px solid var(--ice-hairline-soft);
  }
  .show-num {
    display: inline-flex; align-items: center; justify-content: center;
    width: 22px; height: 22px; margin-right: 8px;
    border-radius: 50%; font-size: 12px;
    color: #fff; background-image: linear-gradient(140deg, var(--ice-accent-light), var(--ice-accent));
  }
  .show-foot {
    margin-top: 56px; padding-top: 20px;
    border-top: 1px solid var(--ice-hairline-soft);
    font-size: 12.5px; color: var(--ice-ink-soft);
    display: flex; flex-wrap: wrap; gap: 10px 22px;
  }
  .show-foot a { color: var(--ice-accent); background-image: none; }

  @media (max-width: 900px) {
    .show-hero { padding: 44px 4px 32px; }
    .show-hero h1 { font-size: 2.3em; }
    .show-window { flex-direction: column; }
    .show-window #typora-sidebar { width: 100%; flex: none; max-height: 260px; border-right: none; border-bottom: 1px solid var(--ice-hairline-soft); }
    .show-window content { max-height: none; }
    .show-wrap { padding: 0 14px 56px; }
  }

  /* 切到深色时，预览页自己的骨架也要跟着换（主题变量会自动生效） */
  html[data-theme="dark"] .show-header { background: color-mix(in srgb, var(--ice-panel-solid) 70%, transparent); }
</style>
</head>
<body class="typora-node os-mac">

<header class="show-header">
  <div class="show-brand">蓝冰 <span>Blue Ice</span></div>
  <div class="show-spacer"></div>
  <div class="show-seg" role="group" aria-label="主题版本">
    <button type="button" data-theme-btn="light" class="active">浅色</button>
    <button type="button" data-theme-btn="dark">深色</button>
    <button type="button" data-theme-btn="paper">纸面</button>
  </div>
</header>

<div class="show-wrap">

  <section class="show-hero">
    <span class="show-eyebrow">Typora Theme · 三个版本</span>
    <h1>蓝色的冰，<br /><em>给长时间写字的屏幕。</em></h1>
    <p class="show-lede">
      冷蓝的底、雾面的面板，外加一处被严格限制的暖琥珀色。
      代码区有两种口味：深墨面板，或者浅灰纸面（One Light 配色）。
      名字取"蓝"给颜色、"冰"给质感 —— 所有面板都由同一套语法构成：
      一层 1px 内高光（厚度）、一圈冷色扩散阴影（浮起）、一点模糊的底色。
    </p>
    <div class="show-chips">
      <span class="show-chip">浅色 / 深色 / 纸面</span>
      <span class="show-chip">零外部依赖</span>
      <span class="show-chip">中文排印友好</span>
      <span class="show-chip">打印自动翻天</span>
      <span class="show-chip">专注模式适配</span>
    </div>
    <div class="show-actions">
      <a class="show-cta" href="https://github.com/Jdante313/typora-blue-ice/releases/latest" id="dl-zip">下载主题</a>
      <a class="show-cta show-ghost" href="#install">怎么装</a>
    </div>
  </section>

  <div class="show-window">
    __SIDEBAR__
    <content>
      <div id="write">__CONTENT__</div>
    </content>
  </div>
  <p class="show-caption">
    上面就是主题的真实渲染结果（不是截图），左侧侧栏、代码块、表格、待办清单都按 Typora 的真实 DOM 结构套用。
    你会看到中文排版用的 16px / 行高 1.82 —— 这是刻意的选择，比其他主题松一档，长时间读中文更舒服。
  </p>

  <section class="show-steps" id="install">
    <div class="show-step">
      <h3><span class="show-num">1</span>下载并解压</h3>
      <p>从 Release 下载需要的 CSS 即可：<code>blue-ice.css</code>（浅色）、<code>blue-ice-dark.css</code>（深色）、<code>blue-ice-paper.css</code>（浅色 + 浅灰代码）。</p>
    </div>
    <div class="show-step">
      <h3><span class="show-num">2</span>放进主题文件夹</h3>
      <p>Typora 菜单：<strong>文件 → 偏好设置 → 外观 → 打开主题文件夹</strong>。</p>
      <p>CSS 必须直接放在该目录下，放进子文件夹不会被识别。三个文件互相独立，只装一个也可以。</p>
    </div>
    <div class="show-step">
      <h3><span class="show-num">3</span>选主题</h3>
      <p>回到 <strong>外观 → 主题</strong>，选 <code>Blue Ice</code>、<code>Blue Ice Dark</code> 或 <code>Blue Ice Paper</code>，无需重启。</p>
    </div>
  </section>

  <footer class="show-foot">
    <span>蓝冰 Blue Ice · MIT License</span>
    <span>三个版本互相独立，可各自单独使用</span>
    <span>反馈与建议：<a href="https://github.com/Jdante313/typora-blue-ice/issues" id="repo-link">仓库 Issues</a></span>
  </footer>
</div>

<script>
  (function () {
    var CSS = { light: 'blue-ice.css', dark: 'blue-ice-dark.css', paper: 'blue-ice-paper.css' };
    var root = document.documentElement;
    var css = document.getElementById('theme-css');
    var btns = document.querySelectorAll('[data-theme-btn]');

    function apply(theme) {
      if (!CSS[theme]) theme = 'light';
      css.href = CSS[theme];
      // 纸面版是浅色底，所以 html 上挂 theme-light；具体哪一版看 data-theme
      root.className = theme === 'dark' ? 'theme-dark' : 'theme-light';
      root.setAttribute('data-theme', theme);
      for (var i = 0; i < btns.length; i++) {
        btns[i].classList.toggle('active', btns[i].getAttribute('data-theme-btn') === theme);
      }
      try { localStorage.setItem('blue-ice-theme', theme); } catch (e) {}
    }

    // 优先级：URL 参数 > 上次选择 > 系统外观。
    // ?theme=light|dark|paper 让分享链接的人能指定看到哪一版。
    var forced = (location.search.match(/[?&]theme=(light|dark|paper)/) || [])[1];
    var saved = null;
    try { saved = localStorage.getItem('blue-ice-theme'); } catch (e) {}
    if (!forced && !saved) {
      saved = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    }
    apply(forced || saved);

    for (var j = 0; j < btns.length; j++) {
      btns[j].addEventListener('click', function () {
        apply(this.getAttribute('data-theme-btn'));
      });
    }
  })();
</script>
</body>
</html>
"""


def build():
    html = PAGE.replace("__SIDEBAR__", SIDEBAR).replace("__CONTENT__", CONTENT)
    out = ROOT / "index.html"
    out.write_text(html, encoding="utf-8")
    print("wrote", out, len(html), "bytes")


if __name__ == "__main__":
    build()
