# Codex Personal Skills

这是我的 Codex 个人技能库，用来保存和分享自己制作、整理或二次维护的 Codex skills。

仓库目标：

- 方便自己在不同电脑之间同步 skills。
- 方便别人 fork、参考和改造这些 skills。
- 每个 skill 都保留独立的 `SKILL.md`、脚本、参考资料和展示配置。

## Skills

### homework-pdf-answer

把拍照的作业题整理成短答案、清晰图示、Markdown 和经过渲染检查的 PDF。

适合场景：

- 计算机专业作业题整理
- 软件建模与实践、UML、顺序图、类图
- 设计模式应用题
- 需要题号清楚、答案简短、图片精细、PDF 方便查看的作业

### diagnose-answer-mode

用于后端、前端、数据库、Spring/MyBatis 等错误诊断。

特点：

- 先说原因
- 标出错误位置
- 判断严重程度
- 说明是否需要改代码
- 给出具体修改方向

### hatch-pet

用于制作、修复、验证和打包 Codex 动态宠物素材。

特点：

- 支持角色图、品牌线索、参考图
- 支持 spritesheet 和 `pet.json` 打包
- 强调视觉 QA 和可用性检查

### pdf

用于 PDF 创建、读取、渲染检查和版面验证。

特点：

- 使用 `reportlab` 生成 PDF
- 使用 `PyMuPDF` / Poppler 渲染检查
- 强调中文字体、排版、图表清晰度

## 使用方法

把需要的 skill 目录复制到本机 Codex skills 目录：

```powershell
Copy-Item -Recurse .\skills\homework-pdf-answer "$env:USERPROFILE\.codex\skills\homework-pdf-answer"
```

也可以 fork 本仓库后按自己的习惯修改。

## 同步本机 Skills 到仓库

在仓库根目录运行：

```powershell
.\scripts\sync-skills.ps1
```

默认同步这些个人 skills：

- `diagnose-answer-mode`
- `hatch-pet`
- `homework-pdf-answer`
- `pdf`

不会同步 `.system`、插件缓存、运行时目录等系统内容。

## License

MIT License. You may fork, modify, and reuse these skills.

