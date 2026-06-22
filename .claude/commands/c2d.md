---
description: "输入法APP-C2D MasterGo 高保真 UI 生成。读取交互截图、visual 产物、设计规范 rules 和组件库，进入引导式生成流程。"
argument-hint: "[目标画布/交互截图/visual产物/需求说明]"
---

Run the `c2d` workflow for input-method app MasterGo UI generation.

After `/c2d` is invoked, do not wait for another instruction. Immediately enter guided intake.

Before doing anything else:

1. Read `./CLAUDE.md` if it exists.
2. Read `./AGENTS.md` if it exists.
3. Read `./rules/01-需求引导.md`.
4. If this command is installed into another project and local `./rules/` is missing, ask the user for the c2d repository path or installed skill path.

Required materials:

1. Target MasterGo canvas URL.
2. Interaction screenshot or screenshot path.
3. MasterGo component library, defaulting to `https://mastergo.iflytek.com/file/196518374727340?file=196518374727340&page_id=1%3A6578`.
4. visual-insight output if available.

If invoked with no arguments, ask for the missing materials one at a time. Prioritize target canvas, interaction screenshot, component library confirmation, then visual-insight output.

When materials are ready:

1. OCR and summarize the screenshot.
2. Summarize visual-insight output into `本次视觉生成概要`.
3. Read `rules/00-规则索引.md`, `02-组件使用规则.md`, `03-画布与图层规则.md`, and `04-缺失冲突与校验规则.md`.
4. Read MasterGo component-library snapshot.
5. Build a component shortlist.
6. Generate MasterGo HTML.
7. Run `scripts/check_mastergo_html.py`.
8. Submit to MasterGo only after hook errors are fixed.
