---
name: diagnose-answer-mode
description: "Use when the user asks why an error happened, whether it is serious, where the root cause is, whether code/config/data needs changing, or asks to explain logs, backend/frontend bugs, Spring/MyBatis errors, request failures, database errors, build failures, or suspicious behavior in a clear diagnosis-first style. Also use when the user asks to answer in their preferred mode with cause, exact location, severity, whether to change it, and how to change it."
---

# Diagnose Answer Mode

## Core Style

Answer in Chinese by default when the user writes in Chinese.

Use a diagnosis-first structure. Be concrete, evidence-tied, and direct. Do not give vague advice when logs, paths, SQL, request URLs, stack traces, file names, or line numbers are available.

Prefer this order:

1. **结论**: State the actual problem in one or two sentences.
2. **问题到底在哪里**: Point to the exact failing request, file, method, SQL, config key, parameter, or line when available.
3. **为什么会这样**: Explain the cause chain from symptom to root cause.
4. **严不严重**: Classify severity as low, medium, or high, and say why.
5. **需不需要改**: Say whether it must be fixed now, can be ignored, or only needs cleanup.
6. **怎么改**: Give the smallest practical fix first. Include exact code/payload/command shape when useful.
7. **怎么验证**: Give one narrow check to confirm the fix.

## Severity Guidance

Use these labels:

- **不严重**: Noise, expected framework behavior, debug logging, harmless fallback, or a failed test request that does not affect normal usage.
- **中等**: A real bug triggered by certain inputs, bad user experience, failed operation, or missing guard, but no data corruption/security risk.
- **严重**: Data loss, wrong database writes, security exposure, broken main workflow, transaction consistency issue, startup failure, or production-impacting error.

Always separate "logs look scary" from "behavior is actually broken".

## Change Guidance

If the user asks only to understand, explain first and do not edit files.

If the issue is caused by invalid input or empty parameters, recommend both:

- Frontend/caller guard: do not send invalid requests.
- Backend guard: reject or safely return on invalid input.

When proposing a fix, start with the minimal patch. Mention broader cleanup only after the minimal fix.

When there is not enough evidence, say exactly what evidence is missing and what to inspect next. Avoid pretending certainty.

## Example Answer Shape

```text
结论：这不是数据库坏了，而是请求参数为空导致 MyBatis 拼出了不完整 SQL。

问题到底在哪里：日志里是 DELETE /emps?ids=，Controller 收到 ids:{}，Mapper 最后拼成 delete from emp_expr where emp_id in。

为什么会这样：foreach 只有在 ids 有元素时才会生成括号和占位符；ids 为空时，in 后面没有内容，所以 MySQL 报 SQLSyntaxErrorException。

严不严重：中等。正常传 ids=59 时可以删除成功，但空选择也会打到后端并返回 500，属于需要补防护的真实 bug。

需不需要改：建议改。前端拦截空选择，后端也加空数组保护。

怎么改：前端没选中时不要调用 DELETE；后端 delete 方法里判断 ids == null || ids.length == 0，直接返回错误提示或 success。

怎么验证：分别测试 DELETE /emps?ids= 和 DELETE /emps?ids=59，前者不再产生坏 SQL，后者仍正常删除。
```
