---
name: homework-pdf-answer
description: Create concise homework answers from photographed or pasted assignment questions, especially CS/software-engineering/modeling/design-pattern exercises, with clean deterministic diagrams, copy-friendly text, Markdown, and visually verified PDF output. Use when the user asks to solve homework from images and wants polished PDFs, clear question numbering, short answers, UML/sequence/class diagrams, or "same quality as last time" outputs.
---

# Homework PDF Answer

## Goal

Turn assignment photos or pasted homework questions into a polished deliverable:

- concise copy-ready answers,
- clear question numbering,
- deterministic diagrams that do not blur or hallucinate text,
- Markdown source,
- PDF output rendered and visually checked before delivery.

## Typical Requests

Use this skill for requests like:

- "把这些作业题整理成短答案和 PDF，图要清楚"
- "和上次一样，题号标清楚，答案少写点"
- "软件建模与实践作业，类图/顺序图要精致"
- "设计模式应用题，给我 Java 代码和类图"
- "不要 Mermaid，直接做成能看的 PDF"

## Required Style

Read `references/style-guide.md` when the task includes diagrams, PDF layout, or resume-quality formatting. The default user preference is: answer text should be short, direct, and easy to copy; diagrams should be clean enough to redraw by hand or view in a PDF.

## Workflow

1. Extract the questions from the provided image(s). If the photo is rotated, mentally rotate it; only ask for clarification if the problem text is unreadable or missing.
2. Identify each question number and subquestion. Preserve numbering exactly, for example `第 4 题`, `第 2 题(1)`.
3. Write answers in the shortest form that still hits the point. Avoid textbook filler.
4. For diagram questions, create deterministic diagrams using SVG, ReportLab drawing, Mermaid only if the user explicitly wants Mermaid, or structured text as fallback.
5. Do not use AI image generation for diagrams containing important text. The `imagegen` skill itself says simple diagrams are better produced as SVG/code-native assets. Use generated raster images only for decorative or non-textual visuals.
6. Generate a Markdown file and, when requested or implied, a PDF under the current workspace:
   - Markdown: `<topic>简答.md`
   - PDF: `output/pdf/<topic>整理.pdf`
   - Preview PNGs: `tmp/pdfs/<topic>/page-1.png`, etc.
7. Render the PDF to PNG with PyMuPDF or Poppler and visually inspect at least the pages most likely to have layout issues. Fix overlap, clipped text, unreadable Chinese, tiny code, or arrows crossing labels.
8. Final response should give direct links to the PDF, Markdown, and preview PNGs if useful.

## Diagram Decision Table

- UML class diagram: use boxes with class names, attributes/methods, inheritance triangles, dependency arrows, aggregation/composition diamonds.
- Sequence diagram: use participant boxes, dashed lifelines, horizontal message arrows, dashed return arrows, and guard labels such as `[x < 10]`.
- Collaboration/communication diagram: use object boxes and numbered arrows, for example `1: do(x)`.
- Flow/process diagram: use left-to-right or top-to-bottom boxes with numbered arrows.
- Design pattern diagram: include only roles needed by the pattern, then put concise code on a separate page if it would crowd the diagram.
- Code-heavy answer: split code across pages instead of shrinking below readable size.

## Implementation Notes

- Prefer `reportlab` for PDF creation and `pymupdf`/`fitz` for rendering previews.
- Use a real Chinese font on Windows, preferably `C:\Windows\Fonts\simhei.ttf` or `C:\Windows\Fonts\Deng.ttf`.
- If Python packages are missing, install normal packages with `python -m pip install reportlab pymupdf pillow`; do not present them as lesser tools.
- Keep outputs in the workspace, not only under temp locations.
- Use `apply_patch` for creating or editing reusable scripts and Markdown.
- If a repository named `codex-personal-skills` exists in the workspace, run its `scripts/sync-skills.ps1` after improving this skill so the public copy stays current.

## Reusable Script

Use `scripts/homework_pdf_template.py` as a starting point for generating PDFs with:

- registered Chinese font,
- landscape A4 layout,
- reusable `box`, `line`, `diamond`, `triangle`, `lifeline`, `code_block`, `wrap_text`, and rendering helpers,
- output and preview directory conventions.

Copy or adapt it into the workspace for each assignment instead of modifying the skill script directly.

## Quality Gate

Before final delivery, verify:

- every question has a visible number,
- every diagram has readable labels,
- no diagram/text overlaps,
- code is language-appropriate and normally formatted,
- PDF opens and renders to preview PNGs,
- any unfinished or inferred content is not presented as completed fact.
