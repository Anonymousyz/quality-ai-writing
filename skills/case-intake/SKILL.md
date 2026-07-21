---
name: case-intake
description: >-
  把 AI 初稿与人工修改整理成《高质量 AI 写作》判例草稿：做 diff 归维、
  生成 cases 格式 Markdown、跑脱敏提醒。Use when the user pastes before/after
  writing samples, asks to intake a writing case, 入库案例, or 整理改稿判例.
---

# 案例入库（case-intake）

你帮助维护公开仓库 quality-ai-writing 的判例库。你输出的是**草稿**，人审校后才可移入 `cases/`。

## 硬规则

1. 默认写入本地 `inbox/`，不要直接写入 `cases/`。
2. 发现疑似真实客户、雇主、项目、内部系统名、精确内部数据时，必须列出「脱敏待处理」清单；不得假装已安全。
3. 维度标签只能使用：intent, logic, selection, sources, proportion, stale-words, qi, decorum。
4. 不复制用户的私人写作操作系统 / SOP 原文进公开文件。

## 流程

1. 读取改前、改后文本（若用户只给一段，询问缺的一侧）。
2. 列出实质改动（忽略纯空格）；每处映射 1–2 个维度。
3. 生成完整判例 Markdown（front-matter + 四节）。
4. 脱敏扫描：专名、邮箱、URL、精确百分比/金额、内部代号 → 标红建议替换为虚构名。
5. 附「修法暗示」：若现有八维接不住，说明可能要改 STANDARD 的哪一句。
6. 提醒用户：审校通过后再手动移入 `cases/YYYY-MM-DD-slug.md` 并运行 `python scripts/check_cases.py`。

## 输出模板

与 `cases/` 文件格式相同，另加章节 `## 脱敏待处理` 与 `## 修法暗示`。草稿默认保存为 `inbox/YYYY-MM-DD-slug.md`。

```markdown
---
id: YYYY-MM-DD-slug
scene: 场景一句话（可含「虚构」）
dimensions: [dimension-slug, ...]
verdict: 一句话点明改稿要害
---

## 场景

（背景、读者、用途；人物/机构/数字须已虚构或标明待脱敏）

## AI 初稿

（改前全文）

## 修改稿

（改后全文）

## 改动说明

- **dimension-slug**：实质改动与归维理由（每处 1–2 维）
- …

## 脱敏待处理

- [ ] `原文片段` → 建议替换为 `虚构名/模糊数`（原因）
- （若已全部虚构且无红线命中：写「无」）

## 修法暗示

- （八维接得住：写「无」或「现有维度已覆盖」）
- （接不住：指出可能要改 `STANDARD.md` / `principles/*.md` 的哪一句）
```

### Front-matter 字段

| 字段 | 要求 |
|---|---|
| `id` | `YYYY-MM-DD-slug`，与目标文件名一致 |
| `scene` | 短场景标签 |
| `dimensions` | 仅允许八维 slug；每条判例 1–3 个为宜 |
| `verdict` | 点明「改对了什么 / 否决了什么」 |

### 脱敏扫描清单（自检）

入库草稿交出前，逐项过一遍：

- [ ] 无真实客户 / 雇主 / 项目名
- [ ] 无内部系统名、工号、精确内部代号
- [ ] 无邮箱、可点击内网/私有 URL
- [ ] 精确百分比、金额、样本规模已虚构或模糊化（或列入「脱敏待处理」）
- [ ] 未粘贴私人写作操作系统 / SOP 原文
- [ ] `dimensions` 仅含八维 slug
- [ ] 文件写在 `inbox/`，未写入 `cases/`
- [ ] 已提醒用户：审校后移入 `cases/` 并跑 `python scripts/check_cases.py`
