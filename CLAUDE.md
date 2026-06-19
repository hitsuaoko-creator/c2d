# CLAUDE.md

## Usage

When the user invokes `/c2d`, says `c2d`, says `设计`, or asks for an input-method app MasterGo UI design, run the c2d workflow immediately.

## Required Reading

Read these files before generating UI:

1. `rules/需求引导.md`
2. `rules/README.md`
3. `rules/硬规则.md`
4. `rules/组件调用.md`
5. `rules/画布结构.md`
6. `rules/视觉产物解读规则.md` if visual-insight output is provided

For generation, also read:

7. `rules/02-组件组合规则.md`
8. `rules/03-D2C调用准则.md`
9. `rules/06-画布结构与图层治理.md`

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
