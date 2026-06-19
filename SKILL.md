---
name: c2d
description: Generate or review MasterGo mobile UI designs for the iFlytek input-method app using guided requirement intake, visual-insight output summarization, the dedicated design specification, interaction screenshots, OCR/visual interpretation, and MasterGo component library. Use when the user asks to create, draw, optimize, audit, design, or c2d a design稿/界面/流程图 for 输入法APP, 皮肤制作, 键盘, 表情, 字体, 素材, 首页, tabbar; when the user says only "设计", "c2d", "使用 c2d", "$c2d", "/c2d", "输入法APP设计规范", or invokes this skill with no extra content; when they provide/mention visual skill output, visual-insight output, MasterGo component library link https://mastergo.iflytek.com/goto/TOAnEBPS, or the 输入法APP 设计规范引导 repository. Backward-compatible aliases include "input-method-app-design" and "$input-method-app-design".
---

# 输入法APP 设计规范

This skill is the trigger and execution workflow for the bundled `输入法APP 设计规范引导` rules. The canonical rules live inside this skill at `rules/`. The default component source is the MasterGo design elements and component library at `https://mastergo.iflytek.com/goto/TOAnEBPS`.

## Mandatory Workflow

1. Guide requirement intake when the request is incomplete:
   - Read `rules/需求引导.md`.
   - Give the user a concise fill-in template when they ask how to use the skill or provide only a vague goal.
   - Ask at most 3 blocking questions before generation; otherwise make safe assumptions and state them.
2. Load MasterGo generation rules first:
   - `get_guidelines(scope=["page-generate","component-import","variable-import"])`
3. Read the user-provided interaction screenshot before designing:
   - Use visual inspection/OCR.
   - Produce a short `交互截图解读`: page count, page titles, visible text, click path, states, popups, keyboard/tabbar presence.
   - If text is unreadable, zoom/crop or ask for a clearer screenshot before generating.
4. Analyze visual-insight output when provided:
   - Read `rules/视觉产物解读规则.md`.
   - Summarize the visual output into `本次视觉生成概要`: visual goal, key path, information hierarchy, primary CTA, state coverage, risks, and executable design actions.
   - Treat the summary as generation guidance, not as permission to violate component, layout, or canvas rules.
5. Read this skill's rules before generating:
   - Always read `rules/README.md` as the rules index.
   - For design generation, read `rules/03-D2C调用准则.md`, `rules/02-组件组合规则.md`, and `rules/06-画布结构与图层治理.md`.
   - For component mapping or conflicts, read the matching `rules/*.md` file.
   - Always read `rules/硬规则.md`.
   - Read `rules/组件调用.md` before selecting components.
   - Read `rules/画布结构.md` before writing MasterGo HTML.
6. Read the MasterGo component library before composing UI:
   - Use `get_component_info({ projectDir, teamLibraryName: "当前文件" })` when the component library is opened/current in MasterGo.
   - If the library is not the current file/page, ask the user to open `https://mastergo.iflytek.com/goto/TOAnEBPS` or use the available team-library flow.
   - Then read the local snapshot in `.mastergo/library/...`: `index.md`, relevant `components/*.json`, `icons.json`, and `variable.json`.
7. Build a component shortlist before drawing:
   - Map each screenshot region to candidate library components.
   - Prefer a similar component from the library when visual style or logic is close.
   - Put likely-used components into a `组件取用区` or directly instantiate them in the design before drawing custom frames.
   - Record unresolved regions as `临时容器-用途`, not anonymous freeform layers.
8. Generate the interface:
   - The `360 x 780` screen is a normal Frame/artboard container, not auto layout.
   - Inside that Frame, use flex/auto-layout for `内容区`, `top`, `卡片组`, rows, lists, bottom sheets, and toolbars.
   - Keep arrows, red boxes, notes, and flow labels outside the phone Frame.
9. Run the hook before submitting:
   - Save generated HTML to a local file.
   - Run `scripts/check_mastergo_html.py <html-file> --library <snapshot-dir>`.
   - Fix every `ERROR`; do not call `submit_page_to_canvas` until the hook passes.
10. Submit to MasterGo:
   - Use `submit_page_to_canvas(filePath=..., projectDir=..., saveCodeToLocal=true)` for large HTML.
   - If MCP times out, reduce batch size and submit per screen or per small flow-board section.

## Intake Guidance

When the user asks "怎么用这个 skill", "我该输入什么", "帮我封装一个提问模板", or provides a vague request, read `rules/需求引导.md` and respond with a short guided template. Prefer collecting:

- Target MasterGo canvas URL.
- Component library URL, defaulting to `https://mastergo.iflytek.com/goto/TOAnEBPS`.
- Uploaded interaction screenshot(s).
- Visual-insight output or visual skill artifact, if available.
- Task type: generate, optimize, or audit.
- Page count/page names/click path, if known.
- Hard constraints or known exceptions.

If one of target canvas, screenshot, or component library access is missing, ask for it before generating.

## Bare Trigger Behavior

If the request is empty after slash-invoking this skill, or only says `设计`, `c2d`, `使用 c2d`, `$c2d`, `/c2d`, `输入法APP设计规范`, or the backward-compatible alias `input-method-app-design`, immediately start the guided intake instead of waiting for a full prompt:

- Read `rules/需求引导.md`.
- Reply with the minimal template and ask only for the missing blockers.
- Ask at most 4 questions, prioritizing target MasterGo canvas, uploaded interaction screenshot, component library confirmation, and whether visual-insight output exists.
- Do not generate UI until the required target canvas and screenshot are available.

## Dead Rules

- Do not start with free drawing. First OCR/read screenshot, then read the skill rules, then read the component library.
- Treat `rules/` as the embedded `输入法APP 设计规范引导` source of truth.
- If visual-insight output is provided, summarize it into `本次视觉生成概要` before component mapping.
- Do not invent layers when a library component is close enough. Use `<ui-component>` with exact component names and exact props from `components/*.json`.
- Do not call components named like `***素材` to build product UI. In particular, do not use `1:1 图片素材`, `3 纵列图片素材`, or `placeholder_pic` as business components.
- Use `键盘组件` whenever drawing a keyboard.
- Use exactly one selected state per tab-like group.
- A `360 x 780` design screen must be a normal Frame/artboard container. It must not be auto layout.
- Inside a screen, `内容区`, `top`, `卡片组`, lists, rows, sheets, and toolbars should use flex/auto-layout.
- First-level screens use background `#FFFFFF`, include `一级界面顶部渐变` at `y=0`, and keep 状态栏 and 顶部导航栏 gap at `0`.
- `tabbar` is a floating layer, bottom safe distance `16dp`.
- Content outside nav has horizontal padding `16`; card-group gap is `8`.
- Keep component instances intact. Do not explode components into arbitrary pieces.
- If design spec, component docs, variables, or screenshot requirements conflict, add a visible `设计冲突说明` area outside the phone Frames and explain the conflict.

## Component Matching Heuristic

Use this order:

1. Exact semantic match in component library.
2. Similar visual structure and interaction logic.
3. Same parent-child pattern from `rules/组件调用.md`.
4. Temporary frame only when no suitable component exists, and name it `临时容器-用途`.
5. Ask before replacing a core component, keyboard, nav, tabbar, or business card with a temporary frame.

## Required Pre-Submit Report

Before calling `submit_page_to_canvas`, state briefly:

- Screenshot/OCR summary.
- Component shortlist and why each component is used.
- Temporary containers and why no library component was suitable.
- Hook result.

Keep this report outside the submitted HTML.
