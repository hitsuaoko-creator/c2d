# c2d

`c2d` 是一个 Codex Skill，用于基于交互截图和 MasterGo 组件库生成、优化、检查输入法 APP 的移动端 UI 设计稿。

这个 Skill 已经内置了「输入法APP 设计规范引导」rules，会在生成设计稿前先读取交互截图并做 OCR/视觉解读，再读取组件库和规范，优先抽取相近组件，最后用 hook 检查生成的 MasterGo HTML。

## 目录说明

- Skill 入口：[`SKILL.md`](./SKILL.md)
- 规范 rules：[`references/rules/`](./references/rules/)
- 提交前检查脚本：[`scripts/check_mastergo_html.py`](./scripts/check_mastergo_html.py)
- rules 同步脚本：[`scripts/sync_rules_from_repo.py`](./scripts/sync_rules_from_repo.py)

## 安装

将仓库复制到 Codex skills 目录：

```bash
cp -R . ~/.codex/skills/input-method-app-design
```

## 使用方式

可以直接发送下面任意一种触发语进入引导：

```text
c2d
```

```text
设计
```

也可以斜杠唤起 `$input-method-app-design` 后，不输入其他内容直接发送。Skill 会自动进入引导流程，补齐目标画布、交互截图和组件库。

推荐的完整请求如下：

```text
使用 input-method-app-design。
基于这张交互截图，在这个 MasterGo 画布里生成输入法APP高保真流程设计稿：
目标画布：<MasterGo 画布链接>
组件库：https://mastergo.iflytek.com/goto/TOAnEBPS
```

如果你不知道怎么写完整需求，也可以直接说：

```text
使用 input-method-app-design，告诉我该输入哪些信息。
```

Skill 会引导你补齐目标画布、组件库、交互截图、页面数量、点击路径和特殊约束。

## 强制规则

- 生成前必须先读/OCR 交互截图。
- 生成前必须读取内置 rules 和 MasterGo 组件库。
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

## 同步 rules

如果外部「输入法APP 设计规范引导」仓库有更新，可以运行：

```bash
scripts/sync_rules_from_repo.py
```

它会把本机默认路径 `/Users/chang/Documents/Playground/输入法APP 设计规范引导` 的规范同步到 `references/rules/`。

也可以指定来源路径：

```bash
scripts/sync_rules_from_repo.py <输入法APP设计规范引导目录>
```

## 许可证

MIT
