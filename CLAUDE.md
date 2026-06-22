# CLAUDE.md

## Usage

When the user invokes `/c2d`, says `c2d`, says `输入法APP-C2D`, says `设计`, or asks for an input-method app MasterGo UI design, run the c2d workflow immediately.

## Required Reading

Read these files before generating UI:

1. `rules/01-需求引导.md`
2. `rules/00-规则索引.md`
3. `rules/02-组件使用规则.md`
4. `rules/03-画布与图层规则.md`
5. `rules/04-缺失冲突与校验规则.md`
6. `rules/05-视觉产物解读规则.md` if visual-insight output is provided

Read `rules/06-组件与变量清单.md` only when exact component names, props, slots, icons, or variables are needed. Read `rules/07-变量与颜色规则.md` when color or variable decisions are involved.

## Claude Code Behavior

- If `/c2d` is invoked with no arguments, start guided intake immediately.
- Ask only for missing blockers: MasterGo canvas, interaction screenshot, component library confirmation, and visual-insight output if available.
- Analyze visual-insight output into `本次视觉生成概要` before component mapping.
- Do not treat visual-insight output as final UI; use it to decide hierarchy, emphasis, states, risks, and design actions.
- Prefer MasterGo library components over custom layers.
- Run `scripts/check_mastergo_html.py` before submitting generated HTML.

## Output

Before submitting to MasterGo, briefly state:

- screenshot/OCR summary
- visual generation summary
- component shortlist
- temporary containers
- hook result
