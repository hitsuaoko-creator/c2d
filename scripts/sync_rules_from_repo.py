#!/usr/bin/env python3
"""Sync 输入法APP 设计规范引导 docs into this skill's rules directory."""

from __future__ import annotations

import shutil
import sys
from pathlib import Path


DEFAULT_SOURCE = Path("/Users/chang/Documents/Playground/输入法APP 设计规范引导")
RULE_FILES = [
    ("README.md", "00-规则索引.md"),
    ("文档/需求引导.md", "01-需求引导.md"),
    ("文档/组件使用规则.md", "02-组件使用规则.md"),
    ("文档/画布与图层规则.md", "03-画布与图层规则.md"),
    ("文档/缺失冲突与校验规则.md", "04-缺失冲突与校验规则.md"),
    ("文档/视觉产物解读规则.md", "05-视觉产物解读规则.md"),
    ("文档/组件与变量清单.md", "06-组件与变量清单.md"),
    ("文档/变量与颜色规则.md", "07-变量与颜色规则.md"),
]


def main() -> int:
    source = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SOURCE
    skill_root = Path(__file__).resolve().parents[1]
    target = skill_root / "rules"
    if not source.exists():
        print(f"ERROR: source repo not found: {source}")
        return 1
    target.mkdir(parents=True, exist_ok=True)
    for src_rel, dst_name in RULE_FILES:
        src = source / src_rel
        if not src.exists():
            print(f"ERROR: missing source file: {src}")
            return 1
        shutil.copy2(src, target / dst_name)
        if dst_name == "00-规则索引.md":
            readme = target / dst_name
            text = readme.read_text(encoding="utf-8")
            text = text.replace("./文档/", "./")
            readme.write_text(text, encoding="utf-8")
        print(f"synced: {src_rel} -> rules/{dst_name}")
    print("done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
