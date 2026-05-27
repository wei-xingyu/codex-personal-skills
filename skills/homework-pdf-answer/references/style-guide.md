# Homework PDF Answer Style Guide

## Answer Tone

- Write in Chinese unless the user asks otherwise.
- Keep answer text short. Use "答案：" and direct statements.
- For homework copying, prefer 1-3 lines per subquestion unless code or diagrams are required.
- Do not add long explanations, learning notes, or unnecessary background.
- If the user wants code, use the language they specify. If unspecified for Java backend/design-pattern homework, prefer Java.

## Diagram Rules

- Use deterministic diagrams, not AI-generated raster diagrams, when labels matter.
- Prefer SVG files or ReportLab vector drawing for UML, sequence diagrams, collaboration diagrams, flow diagrams, design-pattern diagrams, and architecture diagrams.
- Avoid Mermaid unless the user specifically says they can render Mermaid. Many Markdown viewers do not show it.
- Use large labels, simple boxes, clear arrows, and enough whitespace.
- Put one complex diagram per page if needed.
- For UML/design-pattern diagrams, include only the important classes and methods; do not overfill boxes.
- For class diagrams, prefer standard notation:
  - hollow triangle for inheritance/realization,
  - filled diamond for composition,
  - open diamond for aggregation,
  - dashed arrow for dependency.
- For sequence diagrams, keep messages horizontally aligned and do not place labels on top of participant boxes.
- For design-pattern answers, draw roles first and keep concrete class count small enough to copy by hand.

## PDF Layout Rules

- Use landscape A4 for diagram-heavy homework.
- Put a pale header band on each page with the title.
- Use large section titles: `第 4 题：...`
- Keep diagram and answer text close together.
- Split code across pages instead of shrinking it too much.
- Use a Chinese font for all text and code when code contains Chinese strings.
- Render previews after generation and inspect them visually.
- Use one page per major question when the page would otherwise feel crowded.
- Put "代码见下一页" on a diagram page when code is long.
- Give preview PNG links in the final answer when the user wants to quickly check the result.

## Code Formatting Rules

- Do not compress code into one line to save space.
- Use normal indentation and braces.
- For Java examples:
  - class names use PascalCase,
  - methods use camelCase,
  - use `System.out.println(...)`,
  - include a minimal `Client` or `main` only when it helps show usage.
- For design patterns, keep code minimal but structurally correct.
- If the user does not specify a language and the surrounding context is Java backend, use Java.
- If the first generated code page is too dense, split it into upper/lower pages.

## Copy-Ready Answer Patterns

- Pattern name: `答案：装饰模式。通过装饰类在不修改原手机类的情况下增加振动、灯光等功能。`
- Concept class list: `答案：Customer、Product、POS、Cashier。`
- UML relation: `答案：A 由 1 个 B 和 1 个或多个 C 构成，属于组合关系。`
- Sequence diagram explanation: `含义：caller 调用 E1.do(x)；若 x < 10 调用 E2，否则调用 E3。`

## What To Avoid

- Do not fabricate completed project features or implementation details.
- Do not write long textbook definitions when a pattern name plus one sentence is enough.
- Do not leave broken image links in Markdown.
- Do not deliver a PDF without rendering a preview when layout matters.
- Do not leave Chinese as black squares; register a Chinese font.
