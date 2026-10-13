---
layout: post
title: "Blue Ice"
author: "J"
preview: "blue-ice.png"
homepage: "https://github.com/Jdante313/typora-blue-ice"
download: "https://github.com/Jdante313/typora-blue-ice/archive/refs/heads/main.zip"
description: "A cool blue Typora theme in light and dark, with frosted panels, deep-ink code blocks and a single restrained amber accent. Zero external dependencies, CJK-friendly typography."
tags: [light, dark, blue, cool, cjk, clean]
---
# Blue Ice for Typora

A theme in two independent variants — light and dark — built on one idea: **the blue ice of glaciers**. Deep cold blue, frosted surfaces, deep-ink code blocks, plus a single warm amber accent used in exactly one place.

## Features

- **Light and dark, fully independent** — use either one, or both
- **Zero external dependencies** — no `@import`, no web fonts, no remote images; works offline and exports cleanly to PDF
- **CJK-friendly typography** — body text at 16px with 1.82 line height, tuned for long-form Chinese reading. The stack prefers PingFang SC / Microsoft YaHei / Source Han, with Optima for display headings and SF Mono for code, falling back to Segoe UI and Consolas on Windows and Linux (no font installation required)
- **Complete element coverage** — headings, lists, task lists, blockquotes, GitHub-style alerts, code fences with syntax highlighting, tables, footnotes, table of contents, inline math, keyboard keys
- **Full interaction states** — link hover, sidebar file tree and outline hover/selection, checkbox hover and click, search highlights
- **Print / PDF adaptation** — all shadows and radii are stripped; code fences flip to a light surface in the dark theme to save ink
- **Focus mode** — non-focused paragraphs dim, sidebar fades out and restores on hover

## Design notes

Every panel — writing surface, blockquote, TOC, table, sidebar — is built from the same three-layer recipe, which is the only rule in the whole theme:

```css
background: rgba(255,255,255,.76);               /* translucent frosted surface */
box-shadow: inset 0 1px 0 rgba(255,255,255,.85), /* 1px top highlight = thickness */
            0 10px 26px rgba(14,44,60,.08);      /* cool, wide shadow = lift */
backdrop-filter: blur(20px);
```

Deliberate constraints:

- **Shadows are always cool** (`rgba(14,44,60,.08)`) — pure black shadows go muddy on a cold blue base
- **The warm accent appears exactly once**, on `==highlight==`
- **The primary colour appears in four places only**: heading ornaments, body links, checkboxes, sidebar selection
- **Heading hierarchy is expressed through position and shape**, not stacked colour: H1 centred with a fading "icicle" rule, H2 with a short ice bar on the left, H3 with a cyan dot, H4–H6 progressively desaturated

## Installation

1. Download and unzip the theme.
2. Copy `blue-ice.css` and `blue-ice-dark.css` directly into Typora's theme folder (Preferences → Appearance → Open Theme Folder).
3. Select **Blue Ice** or **Blue Ice Dark** from the theme menu — no restart needed.

> The name shown in Typora's theme list is derived from the filename: `blue-ice.css` becomes **Blue Ice**. Renaming the files renames the entries.

## Customization

All colours and metrics live in the `:root` token block at the top of each CSS file:

```css
:root {
  --ice-accent: #1e88b0;   /* primary colour */
  --ice-amber:  #c8892f;   /* the single warm accent */
  --ice-panel:  rgba(255,255,255,.76);  /* frosted surface opacity */
}
```

## License

MIT
