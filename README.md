# 高质量 AI 写作

> 署名前，一篇知识工作文档怎样才算高质量？

一套可更新的评审标准，配脱敏修改判例与中英写作传统打底。不是 prompt 技巧集，不是去 AI 味插件，也不是创意写作教材。

**管辖范围：** 方案、评审、报告、决策备忘、README 与技术文档等知识工作文档；中英文通用。

---

## 本仓库包含 / 不包含

**包含：** 评审标准、原则详解、中英传统短摘、虚构或已脱敏的改稿判例。  
**不包含：** 未脱敏的真实改稿、可识别的客户/雇主/项目材料、未发表的流程台账。

判例入库前须虚构化；本地草稿放 `inbox/`（不进入版本库）。

---

## 与 humanizer 的差别

去 AI 味只覆盖辞章层的一部分。本作品覆盖立意、逻辑、来源、分寸、字句、文气、得体的完整署名前判断。

---

## 目录导航

| 路径 | 内容 |
|---|---|
| [`STANDARD.md`](STANDARD.md) | 写前模式 + 一票否决 + 三层八维 + 终审 |
| [`principles/`](principles/) | 每维一文件：定义、问句、病征、改法 |
| [`notes/`](notes/) | 过程短注：否决、证据阶梯、CARS、Warrant、MECE 等 |
| [`cases/`](cases/) | 脱敏后的第一稿→定稿对照判例 |
| [`traditions/`](traditions/) | 中英写作传统、中文文风来源索引与 AI 写作映射 |
| [`skills/pre-sign-review/`](skills/pre-sign-review/) | 署名前全检（否决→八维） |
| [`skills/ai-prose-detect/`](skills/ai-prose-detect/) | AI 腔 / 套话信号快检 |
| [`skills/mock-reader/`](skills/mock-reader/) | 模拟读者复述与追问 |
| [`skills/case-intake/`](skills/case-intake/) | 改稿判例草稿 |
| [`scripts/`](scripts/) | 判例校验、信号启发式、维度覆盖 |

本地草稿放 [`inbox/`](inbox/)（gitignore，不进版本库）。修法记录见 [`CHANGELOG.md`](CHANGELOG.md)，维护说明见 [`MAINTENANCE.md`](MAINTENANCE.md)。受版权保护的来源只保存出处、短摘录和转述；私人笔记与全文材料不进入仓库。

### 安装技能

把本仓 `skills/<技能名>` 目录放到对应 Agent 的 skills 路径（Windows 把 `~` 换成 `%USERPROFILE%`）：

```text
Cursor:      ~/.cursor/skills/pre-sign-review
             ~/.cursor/skills/ai-prose-detect
             ~/.cursor/skills/mock-reader
             ~/.cursor/skills/case-intake
Claude Code: ~/.claude/skills/...
Codex:       ~/.codex/skills/...
```

### 本地检查

```bash
python -m unittest discover -s tests -v
python scripts/check_cases.py
python scripts/case_coverage.py
```

---

## 现状

| 项 | 值 |
|---|---|
| 版本 | `0.8.0` |
| 案例数 | `11` |
| 传统篇 | `19` |
| 过程短注 | `13` |
| 技能 | `4` |
| 上次修法 | `2026-07-29`（中文文风来源索引 + 自然中文与任务文案检查） |

---

## 许可

- **代码与脚本：** [MIT License](LICENSE)
- **标准、原则、案例、传统等文本：** [CC BY 4.0](LICENSE-CONTENT)

英文摘要见 [`README.en.md`](README.en.md)。
