# c2d

`c2d` 是一个跨 Agent 的 Skill，用于基于交互截图、visual skill 产物、MasterGo 组件库和输入法 APP 设计规范，生成、优化、检查输入法 APP 的 MasterGo 高保真移动端 UI 设计稿。

它不是简单照搬交互截图，而是先理解 visual 产物中的设计意图，再结合组件库和 rules 生成可维护的组件化设计稿。

## 目录说明

- Skill 入口：[`SKILL.md`](./SKILL.md)
- 通用 Agent 入口：[`AGENTS.md`](./AGENTS.md)
- Claude Code 项目入口：[`CLAUDE.md`](./CLAUDE.md)
- Claude Code 斜杠命令：[`./.claude/commands/c2d.md`](./.claude/commands/c2d.md)
- Cursor 斜杠命令：[`./.cursor/commands/c2d.md`](./.cursor/commands/c2d.md)
- 设计规则源：[`rules/`](./rules/)
- 使用说明：[`docs/`](./docs/)
- 设计说明：[`docs/设计说明.md`](./docs/设计说明.md)
- 可复制 Prompt：[`prompts/c2d主Prompt.md`](./prompts/c2d主Prompt.md)
- 提交前检查脚本：[`scripts/check_mastergo_html.py`](./scripts/check_mastergo_html.py)
- rules 同步脚本：[`scripts/sync_rules_from_repo.py`](./scripts/sync_rules_from_repo.py)

## 安装

一次安装到 Codex、Cursor、Claude Code：

```bash
scripts/install_c2d.sh all
```

只安装某个平台：

```bash
scripts/install_c2d.sh codex
scripts/install_c2d.sh cursor
scripts/install_c2d.sh claude
```

安装到某个项目的 Cursor / Claude Code 斜杠命令：

```bash
scripts/install_slash_commands.sh /absolute/project both
```

## 使用方式

可以直接唤起：

```text
/c2d
c2d
设计
使用 c2d
```

如果 `/c2d` 后不输入内容直接发送，Skill 会自动进入引导流程，补齐目标画布、交互截图、组件库和 visual 产物。

推荐完整输入：

```text
/c2d

目标画布：
<MasterGo 画布链接>

组件库：
https://mastergo.iflytek.com/file/196518374727340?file=196518374727340&page_id=1%3A6578

交互截图：
我已上传截图 / 截图路径是 <path>

visual 产物：
<粘贴 visual skill 输出；没有则写暂无>
```

## 强制规则

- 生成前必须先读/OCR 交互截图。
- 如果提供 visual 产物，必须先总结为 `本次视觉生成概要`。
- 生成前必须读取 `rules/00-规则索引.md`、组件使用、画布图层、缺失冲突规则，并读取 MasterGo 组件库。
- 样式或逻辑相近时，优先抽取并使用组件库组件。
- 不要随意自创图层；临时 frame 只用于组件缺失的容器骨架。
- 单个 `360 x 780` 设计稿是普通 Frame/画板，不是自动布局。
- 画板内部的 `内容区`、`top`、`卡片组`、列表、弹层、工具栏使用 flex/自动布局。
- 画键盘时必须使用 `键盘组件`。
- 禁止把 `1:1 图片素材`、`3 纵列图片素材`、`placeholder_pic` 当业务组件使用。
- tab 类选择组只能有一个选中态。

## 提交前检查

生成 MasterGo HTML 后先运行：

```bash
scripts/check_mastergo_html.py <html-file> --library <MasterGo组件库快照目录>
```

有 `ERROR` 时不能提交到 MasterGo，需要先修复。

## 许可证

MIT
