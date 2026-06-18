#!/usr/bin/env python3
"""Sync 输入法APP 设计规范引导 docs into this skill's references/rules."""

from __future__ import annotations

import shutil
import sys
from pathlib import Path


DEFAULT_SOURCE = Path("/Users/chang/Documents/Playground/输入法APP 设计规范引导")
RULE_FILES = [
    ("README.md", "README.md"),
    ("文档/00-组件与变量清单.md", "00-组件与变量清单.md"),
    ("文档/01-组件关系图谱.md", "01-组件关系图谱.md"),
    ("文档/02-组件组合规则.md", "02-组件组合规则.md"),
    ("文档/03-D2C调用准则.md", "03-D2C调用准则.md"),
    ("文档/04-变量与颜色规则.md", "04-变量与颜色规则.md"),
    ("文档/05-缺失与冲突处理.md", "05-缺失与冲突处理.md"),
    ("文档/06-画布结构与图层治理.md", "06-画布结构与图层治理.md"),
]


def main() -> int:
    source = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SOURCE
    skill_root = Path(__file__).resolve().parents[1]
    target = skill_root / "references" / "rules"
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
        print(f"synced: {src_rel} -> references/rules/{dst_name}")
    print("done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
