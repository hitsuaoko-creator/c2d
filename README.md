# c2d

`c2d` is a cross-agent skill for generating and reviewing high-fidelity MasterGo mobile UI designs for the iFlytek input-method app.

It reads interaction screenshots, visual-insight output, the MasterGo component library, and the bundled `输入法APP 设计规范引导` rules before generating UI. The goal is not to copy screenshots blindly, but to turn design intent into maintainable MasterGo component-based screens.

中文说明见 [`README.zh-CN.md`](./README.zh-CN.md).

## Structure

- Codex/Cursor/Claude Skill entry: [`SKILL.md`](./SKILL.md)
- Generic agent entry: [`AGENTS.md`](./AGENTS.md)
- Claude Code project entry: [`CLAUDE.md`](./CLAUDE.md)
- Claude slash command: [`.claude/commands/c2d.md`](./.claude/commands/c2d.md)
- Cursor slash command: [`.cursor/commands/c2d.md`](./.cursor/commands/c2d.md)
- Rules: [`rules/`](./rules/)
- Docs: [`docs/`](./docs/)
- Design explanation: [`docs/设计说明.md`](./docs/设计说明.md)
- Copyable prompt: [`prompts/c2d主Prompt.md`](./prompts/c2d主Prompt.md)
- Pre-submit hook: [`scripts/check_mastergo_html.py`](./scripts/check_mastergo_html.py)

## Install

Install to Codex, Cursor, and Claude Code:

```bash
scripts/install_c2d.sh all
```

Install one platform only:

```bash
scripts/install_c2d.sh codex
scripts/install_c2d.sh cursor
scripts/install_c2d.sh claude
```

Install project-level Cursor/Claude slash commands:

```bash
scripts/install_slash_commands.sh /absolute/project both
```

## Invoke

Use:

```text
/c2d
c2d
设计
使用 c2d
```

If `/c2d` is invoked with no arguments, c2d starts guided intake for the target canvas, interaction screenshot, component library, and visual-insight output.

## What It Enforces

- Read/OCR interaction screenshots before designing.
- Summarize visual-insight output into `本次视觉生成概要` when provided.
- Read bundled rules before generating.
- Read the MasterGo component library before drawing.
- Prefer existing component instances over custom layers.
- Keep each `360 x 780` screen as a normal Frame/artboard.
- Use flex/auto-layout inside `内容区`, `top`, `卡片组`, rows, lists, sheets, and toolbars.
- Use `键盘组件` whenever drawing a keyboard.
- Reject forbidden material components such as `1:1 图片素材`, `3 纵列图片素材`, and `placeholder_pic`.

## License

MIT
