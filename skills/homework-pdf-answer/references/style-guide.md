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

## PDF Layout Rules

- Use landscape A4 for diagram-heavy homework.
- Put a pale header band on each page with the title.
- Use large section titles: `第 4 题：...`
- Keep diagram and answer text close together.
- Split code across pages instead of shrinking it too much.
- Use a Chinese font for all text and code when code contains Chinese strings.
- Render previews after generation and inspect them visually.

## Code Formatting Rules

- Do not compress code into one line to save space.
- Use normal indentation and braces.
- For Java examples:
  - class names use PascalCase,
  - methods use camelCase,
  - use `System.out.println(...)`,
  - include a minimal `Client` or `main` only when it helps show usage.
- For design patterns, keep code minimal but structurally correct.

## What To Avoid

- Do not fabricate completed project features or implementation details.
- Do not write long textbook definitions when a pattern name plus one sentence is enough.
- Do not leave broken image links in Markdown.
- Do not deliver a PDF without rendering a preview when layout matters.
- Do not leave Chinese as black squares; register a Chinese font.

