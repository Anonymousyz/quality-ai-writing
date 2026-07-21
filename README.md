# 高质量 AI 写作

> 署名前，一篇知识工作文档怎样才算高质量？

一套可更新的评审标准，配脱敏修改判例与中英写作传统打底。不是 prompt 技巧集，不是去 AI 味插件，也不是创意写作教材。

**管辖范围：** 方案、评审、报告、决策备忘、README 与技术文档等知识工作文档；中英文通用。

---

## 边界

**本仓库是公开评审标准与示范；完整个人写作操作系统不在此开源；案例均为虚构/脱敏。**

- 公开：标准维度、评审问句、一票否决、中英传统短摘、脱敏/虚构判例
- 私有：Notion 写作体系（SOP、运行演化、真实任务）、`inbox/` 草稿、未脱敏改稿

---

## 与 humanizer 的差别

去 AI 味只覆盖辞章层的一部分。本作品覆盖立意、逻辑、来源、分寸、字句、文气、得体的完整署名前判断。

---

## 目录导航

| 路径 | 内容 |
|---|---|
| [`STANDARD.md`](STANDARD.md) | 一票否决 + 三层八维 + 终审 |
| [`principles/`](principles/) | 每维一文件：定义、问句、病征、改法 |
| [`cases/`](cases/) | 脱敏后的第一稿→定稿对照判例 |
| [`traditions/`](traditions/) | 中英名篇与 AI 写作的映射 |
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
| 版本 | `0.1.0` |
| 案例数 | `3` |
| 上次修法 | `2026-07-21`（初版） |

---

## 许可

- **代码与脚本：** [MIT License](LICENSE)
- **标准、原则、案例、传统等文本：** [CC BY 4.0](LICENSE-CONTENT)

英文摘要见 [`README.en.md`](README.en.md)。
