#!/usr/bin/env python3
"""Pre-submit checks for input-method-app MasterGo HTML."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


FORBIDDEN_COMPONENTS = {
    "1:1 图片素材",
    "3 纵列图片素材",
    "placeholder_pic",
}

REQUIRED_COMPONENTS_WHEN_PRESENT = {
    "键盘": "键盘组件",
}


def load_component_names(library: Path | None) -> set[str]:
    if not library:
        return set()
    components_dir = library / "components"
    names: set[str] = set()
    if not components_dir.exists():
        return names
    for path in components_dir.glob("*.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        name = data.get("name")
        if isinstance(name, str):
            names.add(name)
    return names


def iter_tag_classes(html: str):
    pattern = re.compile(r"<(?P<tag>[a-zA-Z0-9-]+)(?P<attrs>[^>]*)>", re.S)
    for match in pattern.finditer(html):
        attrs = match.group("attrs")
        class_match = re.search(r'class="([^"]*)"', attrs)
        data_name_match = re.search(r'data-name="([^"]*)"', attrs)
        name_match = re.search(r'name="([^"]*)"', attrs)
        yield {
            "tag": match.group("tag"),
            "attrs": attrs,
            "class": class_match.group(1) if class_match else "",
            "data_name": data_name_match.group(1) if data_name_match else "",
            "name": name_match.group(1) if name_match else "",
        }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("html_file", type=Path)
    parser.add_argument("--library", type=Path, help="MasterGo snapshot directory containing components/")
    args = parser.parse_args()

    html = args.html_file.read_text(encoding="utf-8")
    errors: list[str] = []
    warnings: list[str] = []
    component_names = load_component_names(args.library)

    if "<main" not in html:
        errors.append("Missing <main> root fragment.")
    if re.search(r"<(html|head|body|script|style|link|meta|title)\b", html):
        errors.append("HTML contains forbidden document/script/style tags.")
    if re.search(r"\bgrid\b|grid-cols-|grid-rows-", html):
        errors.append("Grid layout is forbidden.")
    if re.search(r"\b(m|mx|my|mt|mr|mb|ml)-", html):
        errors.append("Margin classes are forbidden.")
    if re.search(r"<\s*(button|input|form|select|textarea)\b", html):
        errors.append("Native form/button tags are forbidden.")

    ui_component_names = re.findall(r"<ui-component[^>]*\bname=\"([^\"]+)\"", html)
    for name in ui_component_names:
        if name in FORBIDDEN_COMPONENTS:
            errors.append(f"Forbidden material component used: {name}")
        if component_names and name not in component_names:
            errors.append(f"Component not found in library snapshot: {name}")

    for keyword, required in REQUIRED_COMPONENTS_WHEN_PRESENT.items():
        if keyword in html and required not in ui_component_names:
            errors.append(f"'{keyword}' appears, but required component '{required}' is not used.")

    has_artboard = False
    for item in iter_tag_classes(html):
        cls = item["class"]
        data_name = item["data_name"]
        if "w-[360px]" in cls and "h-[780px]" in cls:
            has_artboard = True
            if " flex " in f" {cls} " or cls.startswith("flex "):
                errors.append(f"360x780 artboard must not be flex: {data_name or item['tag']}")
        if any(key in data_name for key in ("内容区", "卡片组", "top")):
            if "flex" not in cls:
                warnings.append(f"Semantic container should use flex/auto-layout: {data_name}")

    if not has_artboard:
        warnings.append("No w-[360px] h-[780px] artboard detected.")

    if "一级界面顶部渐变" not in html:
        warnings.append("Missing 一级界面顶部渐变.")
    if "状态栏" not in html:
        warnings.append("Missing 状态栏.")

    selected_markers = re.findall(r"data-name=\"([^\"]*(?:选中|checked|selected)[^\"]*)\"", html)
    tab_like = [name for name in selected_markers if "Tab" in name or "tab" in name or "导航" in name]
    if len(tab_like) > 12:
        warnings.append("Many selected tab-like markers detected; manually verify one selected state per group.")

    for message in errors:
        print(f"ERROR: {message}")
    for message in warnings:
        print(f"WARN: {message}")

    if errors:
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s).")
        return 1
    print(f"PASSED: 0 errors, {len(warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
