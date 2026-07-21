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
| [`notes/`](notes/) | 过程短注：模式、结构、修改、一段一意、读者、场景选择 |
| [`cases/`](cases/) | 脱敏后的第一稿→定稿对照判例 |
| [`traditions/`](traditions/) | 中英名篇短摘与 AI 写作映射（9 篇） |
| [`skills/case-intake/`](skills/case-intake/) | 把改前改后整理成案例草稿的 Agent 技能 |

本地草稿放 [`inbox/`](inbox/)（gitignore，不进公开仓）。修法记录见 [`CHANGELOG.md`](CHANGELOG.md)，维护说明见 [`MAINTENANCE.md`](MAINTENANCE.md)。

### 安装 case-intake 技能

把本仓 `skills/case-intake` 目录放到对应 Agent 的 skills 路径（Windows 把 `~` 换成 `%USERPROFILE%`）：

```text
Cursor:      ~/.cursor/skills/case-intake
Claude Code: ~/.claude/skills/case-intake
Codex:       ~/.codex/skills/case-intake
```

---

## 现状

| 项 | 值 |
|---|---|
| 版本 | `0.3.0` |
| 案例数 | `3` |
| 传统篇 | `9` |
| 过程短注 | `7` |
| 上次修法 | `2026-07-21`（共识短注、修法准入、朱光潜/叶圣陶/Pinker） |

---

## 许可

- **代码与脚本：** [MIT License](LICENSE)
- **标准、原则、案例、传统等文本：** [CC BY 4.0](LICENSE-CONTENT)

英文摘要见 [`README.en.md`](README.en.md)。
