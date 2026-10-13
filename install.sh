#!/usr/bin/env bash
# 把「蓝冰 · Blue Ice」安装到 Typora 主题目录。
#
# 用法：bash install.sh
#
# 这个脚本只做一件事：把两个 CSS 拷进主题目录。
# 它不会删除或修改你已有的任何主题文件。
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 依次探测 macOS / Linux / Windows(WSL 及 Git Bash) 的主题目录
candidates=(
  "$HOME/Library/Application Support/abnerworks.Typora/themes"
  "${XDG_CONFIG_HOME:-$HOME/.config}/Typora/themes"
  "$HOME/.config/typora/themes"
  "${APPDATA:-}/Typora/themes"
)

TARGET=""
for dir in "${candidates[@]}"; do
  if [ -n "$dir" ] && [ -d "$dir" ]; then
    TARGET="$dir"
    break
  fi
done

if [ -z "$TARGET" ]; then
  echo "没有找到 Typora 主题目录。请手动创建后重试，或直接拷贝这两个文件："
  printf '  %s\n' "$HERE/blue-ice.css" "$HERE/blue-ice-dark.css"
  echo "Typora 菜单：文件 → 偏好设置 → 外观 → 打开主题文件夹"
  exit 1
fi

cp "$HERE/blue-ice.css" "$TARGET/"
cp "$HERE/blue-ice-dark.css" "$TARGET/"

echo "已安装到：$TARGET"
echo "接着在 Typora 里：文件 → 偏好设置 → 外观 → 主题，选择「Blue Ice」或「Blue Ice Dark」。"
echo "（重新打开一份文档即可看到效果，无需重启）"
