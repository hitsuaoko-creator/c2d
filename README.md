# c2d

`c2d` is a Codex skill for generating and reviewing MasterGo mobile UI designs for the iFlytek input-method app.

The skill bundles the `输入法APP 设计规范引导` rules and enforces a workflow that reads interaction screenshots, maps UI regions to the MasterGo component library, and checks generated MasterGo HTML before submission.

中文说明见 [`README.zh-CN.md`](./README.zh-CN.md).

## Skill

- Skill entry: [`SKILL.md`](./SKILL.md)
- Rules: [`references/rules/`](./references/rules/)
- Pre-submit hook: [`scripts/check_mastergo_html.py`](./scripts/check_mastergo_html.py)

## Usage

Copy this folder into your Codex skills directory:

```bash
cp -R . ~/.codex/skills/input-method-app-design
```

Then invoke it with a prompt like:

```text
使用 input-method-app-design。
基于这张交互截图，在这个 MasterGo 画布里生成输入法APP高保真流程设计稿：
目标画布：<MasterGo 画布链接>
组件库：https://mastergo.iflytek.com/goto/TOAnEBPS
```

## What It Enforces

- Read/OCR interaction screenshots before designing.
- Read bundled rules before generating.
- Read the MasterGo component library before drawing.
- Prefer existing component instances over custom layers.
- Keep each `360 x 780` screen as a normal Frame/artboard.
- Use flex/auto-layout inside `内容区`, `top`, `卡片组`, rows, lists, sheets, and toolbars.
- Use `键盘组件` whenever drawing a keyboard.
- Reject forbidden material components such as `1:1 图片素材`, `3 纵列图片素材`, and `placeholder_pic`.

## License

MIT
