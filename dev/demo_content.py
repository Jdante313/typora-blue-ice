"""演示内容（测试页与在线预览页共用）。

这里刻意手写 Typora 的真实 DOM 结构与类名，而不是用 Markdown 解析器生成 ——
这样主题里每个选择器命中的对象，跟真实编辑器里一致。
"""

CODE_PY = '''<div class="md-fences md-end-block ty-contain-cm modeLoaded" lang="python"><pre class="md-fences-content"><span class="cm-s-inner"><span class="CodeMirror-code">
<div class="CodeMirror-line"><span class="CodeMirror-gutter-wrapper"><span class="CodeMirror-linenumber">1</span></span><span class="cm-keyword">from</span> <span class="cm-variable">dataclasses</span> <span class="cm-keyword">import</span> <span class="cm-variable">dataclass</span>, <span class="cm-variable">field</span></div>
<div class="CodeMirror-line"><span class="CodeMirror-gutter-wrapper"><span class="CodeMirror-linenumber">2</span></span>&nbsp;</div>
<div class="CodeMirror-line"><span class="CodeMirror-gutter-wrapper"><span class="CodeMirror-linenumber">3</span></span><span class="cm-meta">@dataclass</span></div>
<div class="CodeMirror-line"><span class="CodeMirror-gutter-wrapper"><span class="CodeMirror-linenumber">4</span></span><span class="cm-keyword">class</span> <span class="cm-def">Glass</span>:</div>
<div class="CodeMirror-line"><span class="CodeMirror-gutter-wrapper"><span class="CodeMirror-linenumber">5</span></span>    <span class="cm-string">"""一块蓝冰：冷底、磨砂、圆角。"""</span></div>
<div class="CodeMirror-line"><span class="CodeMirror-gutter-wrapper"><span class="CodeMirror-linenumber">6</span></span>    <span class="cm-variable">hue</span>: <span class="cm-builtin">str</span> = <span class="cm-string">"#1e88b0"</span></div>
<div class="CodeMirror-line"><span class="CodeMirror-gutter-wrapper"><span class="CodeMirror-linenumber">7</span></span>    <span class="cm-variable">blur</span>: <span class="cm-builtin">int</span> = <span class="cm-number">20</span></div>
<div class="CodeMirror-line"><span class="CodeMirror-gutter-wrapper"><span class="CodeMirror-linenumber">8</span></span>    <span class="cm-variable">layers</span>: <span class="cm-builtin">list</span> = <span class="cm-variable">field</span>(<span class="cm-variable">default_factory</span>=<span class="cm-builtin">list</span>)</div>
<div class="CodeMirror-line"><span class="CodeMirror-gutter-wrapper"><span class="CodeMirror-linenumber">9</span></span>&nbsp;</div>
<div class="CodeMirror-line"><span class="CodeMirror-gutter-wrapper"><span class="CodeMirror-linenumber">10</span></span>    <span class="cm-keyword">def</span> <span class="cm-def">frost</span>(<span class="cm-variable">self</span>, <span class="cm-variable">opacity</span>: <span class="cm-builtin">float</span> = <span class="cm-number">0.76</span>) -&gt; <span class="cm-builtin">str</span>:</div>
<div class="CodeMirror-line"><span class="CodeMirror-gutter-wrapper"><span class="CodeMirror-linenumber">11</span></span>        <span class="cm-comment"># 透明度越低，冰面越厚</span></div>
<div class="CodeMirror-line"><span class="CodeMirror-gutter-wrapper"><span class="CodeMirror-linenumber">12</span></span>        <span class="cm-keyword">return</span> <span class="cm-string">f"rgba(255,255,255,{opacity})"</span></div>
</span></span></pre><div class="code-tooltip">python</div></div>'''

CODE_BASH = '''<div class="md-fences md-end-block ty-contain-cm modeLoaded" lang="bash"><pre class="md-fences-content"><span class="cm-s-inner"><span class="CodeMirror-code">
<div class="CodeMirror-line"><span class="CodeMirror-gutter-wrapper"><span class="CodeMirror-linenumber">1</span></span><span class="cm-comment"># 把两套主题放进 Typora 主题目录</span></div>
<div class="CodeMirror-line"><span class="CodeMirror-gutter-wrapper"><span class="CodeMirror-linenumber">2</span></span><span class="cm-variable">cp</span> <span class="cm-string">blue-ice*.css</span> <span class="cm-string">"$HOME/Library/Application Support/abnerworks.Typora/themes/"</span></div>
</span></span></pre><div class="code-tooltip">bash</div></div>'''

CODE_HTML = '''<div class="md-fences md-end-block ty-contain-cm modeLoaded" lang="html"><pre class="md-fences-content"><span class="cm-s-inner"><span class="CodeMirror-code">
<div class="CodeMirror-line"><span class="CodeMirror-gutter-wrapper"><span class="CodeMirror-linenumber">1</span></span><span class="cm-operator">&lt;</span><span class="cm-tag">section</span> <span class="cm-attribute">class</span>=<span class="cm-string">"glass"</span><span class="cm-operator">&gt;</span></div>
<div class="CodeMirror-line"><span class="CodeMirror-gutter-wrapper"><span class="CodeMirror-linenumber">2</span></span>  <span class="cm-operator">&lt;</span><span class="cm-tag">h2</span><span class="cm-operator">&gt;</span>蓝冰<span class="cm-operator">&lt;/</span><span class="cm-tag">h2</span><span class="cm-operator">&gt;</span></div>
<div class="CodeMirror-line"><span class="CodeMirror-gutter-wrapper"><span class="CodeMirror-linenumber">3</span></span><span class="cm-operator">&lt;/</span><span class="cm-tag">section</span><span class="cm-operator">&gt;</span></div>
</span></span></pre><div class="code-tooltip">html</div></div>'''

SIDEBAR = '''<aside id="typora-sidebar">
  <div class="sidebar-tabs">
    <div class="sidebar-tab active"><span class="info-panel-tab-title active">文件</span></div>
    <div class="sidebar-tab"><span class="info-panel-tab-title">大纲</span></div>
  </div>
  <div id="file-library-search"><input id="file-library-search-input" placeholder="搜索文件…" /></div>
  <div class="file-list">
    <div class="file-list-item"><span class="file-list-item-file-name-part">蓝冰</span><span class="file-list-item-file-ext-part">.md</span></div>
    <div class="file-list-item active"><span class="file-list-item-file-name-part">README</span><span class="file-list-item-file-ext-part">.md</span></div>
    <div class="file-library-node file-tree-node file-library-directory-node active">
      <span class="file-node-content"><span class="file-node-title">notes</span></span>
      <div class="file-library-node file-tree-node file-library-file-node active"><span class="file-node-background"></span><span class="file-node-content"><span class="file-node-title">风格笔记.md</span></span></div>
      <div class="file-library-node file-tree-node file-library-file-node"><span class="file-node-content"><span class="file-node-title">深色模式.md</span></span></div>
    </div>
  </div>
  <div class="outline-content">
    <div class="outline-title-wrapper"><span class="outline-title">大纲</span></div>
    <ul class="outline-item-wrapper">
      <li class="outline-item outline-h1"><a class="outline-label">蓝冰</a></li>
      <li class="outline-item outline-h2"><a class="outline-label">冷调画布</a></li>
      <li class="outline-item outline-h2 outline-item-open"><a class="outline-label">磨砂面板</a><ul class="outline-children"><li class="outline-item outline-h3 outline-item-active"><a class="outline-label">表格也是雾面</a></li></ul></li>
      <li class="outline-item outline-h3"><a class="outline-label">圆角与厚度</a></li>
      <li class="outline-item outline-h3"><a class="outline-label">待办与清单</a></li>
    </ul>
  </div>
</aside>'''

CONTENT = '''<h1>蓝冰</h1>
<p>同样的文字，<strong>蓝冰</strong>让层级更轻。这一套主题只做三个动作：<em>冷调的底</em>、<em>磨砂的面</em>、<em>克制的暖色</em>，其余全部交给字距与留白。</p>
<p>正文里偶尔需要一点强调 —— 比如 <mark>这样一条琥珀纸带</mark>，或者按下 <kbd>⌘</kbd> + <kbd>K</kbd> 唤出快捷面板，也可以用 <code>inline code</code> 标注一个小片段，剩下的交给 <a href="#">链接</a> 与 <del>被划掉的旧结论</del>。</p>

<h2>冷调画布</h2>
<p>底色不能是纯白。纯白太硬，雾面会失去厚度。这一版的画布从顶部的 <code>#dfeaf2</code> 极缓地过渡到 <code>#f4f9fc</code>，写作区则是一张半透明的磨砂纸浮在上面。段落之间的关系由留白说明，而不是靠边框。</p>
<blockquote><p>冰的本质不是透明，而是<strong>厚度</strong>：一层 1px 的高光、一圈冷色阴影、一点模糊的底色，三者缺一，面板就会塌成一张色卡。</p></blockquote>

<h3>圆角与厚度</h3>
<ul>
  <li>大圆角（14–20px）负责“轻”，阴影负责“浮”。</li>
  <li>阴影必须是冷色：<code>rgba(14,44,60,.08)</code>，用纯黑会脏。
    <ul><li>嵌套一层换空心圆点</li><li>再深一层换成实心方点</li></ul>
  </li>
  <li>唯一的高对比留给代码块 —— 独立面板，边框带一点冰蓝。</li>
</ul>

<ol>
  <li>先定画布与墨色，再定强调色。</li>
  <li>强调色只出现在三个地方：标题、链接、勾选框。</li>
  <li>暖色只允许出现一次。</li>
</ol>

<h2>磨砂面板</h2>
''' + CODE_PY + '''
<p>代码面板是页面上最“实”的一块，也是唯一的强对比。它不参与雾面的透明游戏，而是作为独立区块存在：让代码与正文一眼分开。</p>
''' + CODE_BASH + '''
<h3>表格也是雾面</h3>
<table><thead><tr><th>层</th><th>颜色</th><th>作用</th><th>透明度</th></tr></thead>
<tbody>
<tr><td>画布</td><td><code>#e9f1f7</code></td><td>冷白底，托住所有面板</td><td>100%</td></tr>
<tr><td>写作区</td><td><code>#ffffff</code></td><td>磨砂纸，正文所在</td><td>76%</td></tr>
<tr><td>引用 / 目录</td><td><code>#eef7fc</code></td><td>次级雾面，退后一层</td><td>72%</td></tr>
<tr><td>代码块</td><td><code>#0d1b25</code> / <code>#fafafa</code></td><td>独立面板，最强对比</td><td>100%</td></tr>
<tr><td>强调</td><td><code>#1e88b0</code></td><td>标题、链接、勾选</td><td>—</td></tr>
</tbody></table>

<hr />

<h2>待办与清单</h2>
<ul class="ul-list">
  <li class="md-list-item task-list-item md-task-list-item task-list-done"><input type="checkbox" checked=""></input><p>确定冰蓝主色 <code>#1e88b0</code></p></li>
  <li class="md-list-item task-list-item md-task-list-item task-list-done"><input type="checkbox" checked=""></input><p>给代码块做独立面板</p></li>
  <li class="md-list-item task-list-item md-task-list-item task-list-not-done"><input type="checkbox"></input><p>把暖色限制在荧光笔一处</p></li>
  <li class="md-list-item task-list-item md-task-list-item task-list-not-done"><input type="checkbox"></input><p>深色模式同步一版 <code>blue-ice-dark.css</code></p></li>
  <li class="md-list-item task-list-item md-task-list-item task-list-not-done"><input type="checkbox"></input><p>复选框要和普通列表一眼分开：未勾选是白底冰蓝描边，勾选是实心冰蓝加白勾</p></li>
</ul>

<h3>普通无序列表（作为对照）</h3>
<ul class="ul-list">
  <li class="md-list-item"><p>普通条目的冰晶符号</p></li>
  <li class="md-list-item"><p>它不应该和复选框长得像</p></li>
</ul>

<h4>原码片段</h4>
''' + CODE_HTML + '''
<p>写到这里，一条分隔线上的那枚小圆点，就是整套主题里最不重要、也最必要的装饰。<sup>[1]</sup></p>
<p class="md-footnote">[1] 装饰的作用是提示节奏，而不是提示存在感。</p>
'''
