#!/user/bin/env python3
# -*- coding: utf-8 -*-

import os

# 配置：需要显示的隐藏文件夹
SHOW_HIDDEN = ['.venv', '.gitignore', '.env.example']


def simple_tree(path=".", depth=3, indent="", current_depth=0):
    """简化版树形输出"""
    if current_depth >= depth:
        return

    try:
        items = sorted(os.listdir(path))
    except:
        return

    # 过滤规则
    filtered = []
    for item in items:
        # 跳过大多数隐藏文件和文件夹
        if item.startswith('.') and item not in SHOW_HIDDEN:
            continue
        # 跳过特定文件夹
        if item in ['__pycache__', '.git', 'node_modules']:
            continue
        filtered.append(item)

    # 输出
    for i, item in enumerate(filtered):
        is_last = (i == len(filtered) - 1)
        connector = "└── " if is_last else "├── "

        full_path = os.path.join(path, item)
        is_dir = os.path.isdir(full_path)

        # 标记文件夹
        display = f"{item}/" if is_dir else item
        print(f"{indent}{connector}{display}")

        # 递归显示子目录（不显示隐藏文件夹内容）
        if is_dir and not item.startswith('.'):
            new_indent = indent + ("    " if is_last else "│   ")
            simple_tree(full_path, depth, new_indent, current_depth + 1)


if __name__ == "__main__":
    print("GEP-application：")
    simple_tree(".", depth=4)