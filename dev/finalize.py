#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""一次性收尾脚本：把仓库里的用户名占位符替换成真实账号，并设置 git remote。

用法（在仓库根目录执行）：
    python3 dev/finalize.py Jdante313
    python3 dev/finalize.py <用户名> --email <邮箱>    # 可选，覆盖提交邮箱

它会改 README.md 与 dev/gallery-post.md 里的占位符，并配置 git remote origin。
不会执行 push —— 推送需要你的令牌，由你自己跑。
"""
import subprocess
import sys
import pathlib

DEFAULT_EMAIL = "58454432+Jdante313@users.noreply.github.com"
REPO = "typora-blue-ice"


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        return 2
    user = args[0].lstrip("@")
    email = DEFAULT_EMAIL
    if "--email" in sys.argv:
        email = sys.argv[sys.argv.index("--email") + 1]

    root = pathlib.Path(__file__).resolve().parent.parent
    base = f"https://github.com/{user}/{REPO}"

    # README 里的三处：预览地址、clone 命令，以及仓库/Issues 相对链接（相对链接无需改）
    readme = root / "README.md"
    s = readme.read_text(encoding="utf-8")
    s = s.replace("https://你的用户名.github.io/typora-blue-ice/",
                  f"https://{user.lower()}.github.io/{REPO}/"  # 域名小写，仓库路径保持原样)
    s = s.replace("https://github.com/你的用户名/typora-blue-ice.git", f"{base}.git")
    readme.write_text(s, encoding="utf-8")
    print(f"  README.md             -> {base}")

    # 官方主题库投稿文案
    post = root / "dev" / "gallery-post.md"
    s = post.read_text(encoding="utf-8")
    s = s.replace("https://github.com/你的用户名/typora-blue-ice", base)
    post.write_text(s, encoding="utf-8")
    print(f"  dev/gallery-post.md   -> {base}.zip")

    # git remote
    existing = subprocess.run(["git", "remote"], cwd=root, capture_output=True, text=True).stdout.split()
    if "origin" in existing:
        subprocess.run(["git", "remote", "set-url", "origin", f"{base}.git"], cwd=root, check=True)
        print("  git remote            -> 已更新 origin")
    else:
        subprocess.run(["git", "remote", "add", "origin", f"{base}.git"], cwd=root, check=True)
        print("  git remote            -> 已添加 origin")

    print(f"\n提交身份：{subprocess.run(['git','config','user.name'], capture_output=True, text=True).stdout.strip()}"
          f" <{subprocess.run(['git','config','user.email'], capture_output=True, text=True).stdout.strip()}>")

    leftover = []
    for f in (readme, post):
        if "你的用户名" in f.read_text(encoding="utf-8") or "你的名字" in f.read_text(encoding="utf-8"):
            leftover.append(str(f.relative_to(root)))
    print("残留占位符：", leftover or "无 ✅")
    print("\n下一步（需要你自己执行，会提示输入账号与令牌）：")
    print(f"  git add -A && git commit -m 'Update repository links' && git push -u origin main")
    return 0


if __name__ == "__main__":
    sys.exit(main())
