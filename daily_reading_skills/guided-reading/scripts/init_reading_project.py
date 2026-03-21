#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path
import re


def load_paths_config() -> dict:
    skill_dir = Path(__file__).resolve().parent.parent
    candidates = [
        skill_dir.parent / "_shared" / "user_config.py",
        Path.home() / ".codex" / "skills" / "_shared" / "user_config.py",
    ]
    user_config_path = next((path for path in candidates if path.exists()), None)
    if user_config_path is None:
        raise FileNotFoundError("Cannot locate _shared/user_config.py")

    namespace = {"__file__": str(user_config_path)}
    exec(user_config_path.read_text(encoding="utf-8"), namespace)
    return namespace["paths_config"]()


def safe_name(title: str) -> str:
    title = re.sub(r'[\\/:*?"<>|]+', "-", title).strip()
    title = re.sub(r"\s+", " ", title)
    return title or "未命名项目"


def ensure_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def book_map_template(title: str) -> str:
    return f"""# {title} - 总学习地图

## 材料信息

- 书名：{title}
- 当前状态：未开始

## 为什么读这本书

- 想解决的问题：
- 和当前方向的关系：
- 预期收获：

## 全书主线

- 核心问题：
- 关键方法：
- 章节依赖：

## 当前方向联系

- 直接可用：
- 方法近邻：
- 背景地基：
- 后续线索：
"""


def chapter_map_template(title: str) -> str:
    return f"""# {title} - 章节地图

## 章节总览

| 章节 | 主题 | 在全书里的作用 | 是否优先 |
|------|------|----------------|----------|
| 1 |  |  | 是 / 否 |

## 当前阅读策略

- 精读：
- 略读：
- 暂时跳过：
"""


def paper_intro_template(title: str) -> str:
    return f"""# {title} - 导读

## 为什么读这篇

- 想回答的问题：
- 和当前方向的关系：
- 最希望从这篇拿到什么：

## 先看什么

- 摘要：
- 引言：
- 方法：
- 实验：
- 附录：

## 当前方向联系

- 直接可用：
- 方法近邻：
- 背景地基：
- 后续线索：
"""


def session_template() -> str:
    return """# Session 共读记录

## 基本信息

- 日期：
- 本次范围：
- 本次目标：

## 原文理解

- 

## 你的原始笔记

- 

## 纠正后的版本

- 

## 当前方向联系

- 直接可用：
- 方法近邻：
- 背景地基：
- 后续线索：

## 小测结果

- 复述题：
- 判断题：
- 迁移题：
- 当前掌握度：不会 / 模糊 / 会复述 / 会迁移

## 下次阅读计划

- 
"""


def test_template() -> str:
    return """# 小测

## 复述题

- 

## 判断题

- 

## 迁移题

- 

## 评分

- 复述：不会 / 模糊 / 会复述 / 会迁移
- 判断：不会 / 模糊 / 会复述 / 会迁移
- 迁移：不会 / 模糊 / 会复述 / 会迁移
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Initialize a guided reading project.")
    parser.add_argument("--mode", choices=("book", "paper"), required=True)
    parser.add_argument("--title", required=True)
    args = parser.parse_args()

    paths = load_paths_config()
    vault_path = Path(paths["obsidian_vault"]).expanduser()
    reading_root_name = paths.get("guided_reading_folder", "共读精读")
    reading_root = vault_path / reading_root_name
    category = "书籍" if args.mode == "book" else "论文"
    project_dir = reading_root / category / safe_name(args.title)

    for subdir in ("sessions", "tests", "draft-notes", "sources"):
        (project_dir / subdir).mkdir(parents=True, exist_ok=True)

    if args.mode == "book":
        ensure_file(project_dir / "00-总学习地图.md", book_map_template(args.title))
        ensure_file(project_dir / "01-章节地图.md", chapter_map_template(args.title))
    else:
        ensure_file(project_dir / "00-导读.md", paper_intro_template(args.title))

    ensure_file(project_dir / "sessions" / "README.md", session_template())
    ensure_file(project_dir / "tests" / "README.md", test_template())

    print(project_dir)


if __name__ == "__main__":
    main()
