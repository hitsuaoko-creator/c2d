# c2d 主 Prompt

请使用 c2d 流程生成输入法 APP MasterGo 高保真 UI。

先读取：

1. `rules/01-需求引导.md`
2. `rules/00-规则索引.md`
3. `rules/02-组件使用规则.md`
4. `rules/03-画布与图层规则.md`
5. `rules/04-缺失冲突与校验规则.md`
6. `rules/05-视觉产物解读规则.md`，如提供 visual 产物
7. `rules/06-组件与变量清单.md`，仅在确认组件名、props、slots、变量名时读取
8. `rules/07-变量与颜色规则.md`，仅在处理颜色或变量时读取

输入材料：

```text
目标 MasterGo 画布：
【粘贴链接】

组件库：
https://mastergo.iflytek.com/file/196518374727340?file=196518374727340&page_id=1%3A6578

交互截图：
【上传截图或粘贴路径】

visual-insight 产物：
【粘贴 visual skill 输出；没有则写暂无】

需求说明：
【说明要生成的页面、流程和特殊要求】
```

执行要求：

1. 先 OCR / 解读交互截图。
2. 如果提供 visual 产物，先总结为 `本次视觉生成概要`。
3. 读取 MasterGo 组件库并做组件候选清单。
4. 优先使用组件库组件，不要随意自创图层。
5. 每个页面是 `360 x 780` 普通 Frame，Frame 内部用 flex / 自动布局。
6. 画键盘必须调用 `键盘组件`。
7. 提交前运行 `scripts/check_mastergo_html.py`。
