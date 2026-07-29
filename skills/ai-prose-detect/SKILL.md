---
name: ai-prose-detect
description: >-
  扫描知识工作文稿中的 AI 腔、套话、空转逻辑与翻译腔等复查信号，引用原文并映射到
  quality-ai-writing 八维。Use when the user asks to detect AI writing, AI腔,
  套话, 陈言, humanizer-style check, prose lint, or paste a draft for stale-words
  / decorum / logic smell scan — not a full eight-dimension review.
---

# AI 文稿信号检测（ai-prose-detect）

你做的是**信号扫描**，不负责打分或决定是否发表。命中项只提示复查：追问这句话补上了什么事实或判断；没有增量可删，有内容但说不清则重写。

完整八维评审仍以 `STANDARD.md` 为准；本技能主攻辞章与浅层逻辑空转，并点名可能牵动的维度。

## 基本约束

1. **每条发现必须引用原文**（短句或短语），禁止只给抽象标签。  
2. 信号 ≠ 有罪：标【疑似】【明显】；无原文支撑不得写「明显」。  
3. 改写示例只用于说明方向，最多给 1–2 句；不要补写没有证据支撑的“更优全文”。  
4. 发现疑似真实敏感信息时提示脱敏，不要在输出里扩散。  
5. 维度标签仅用：intent, logic, selection, sources, proportion, stale-words, qi, decorum。

## 扫描清单（逐类过，可无则写「未检出」）

### A. 陈言 / AI 套话（→ stale-words）

- 中文万能词：赋能、闭环、抓手、对齐、落地、抓落实、值得注意的是、综上所述（空转时）  
- 英文预制：delve, leverage, tapestry, landscape, "It's not just X, it's Y", "in today's fast-paced…"  
- 删句测试：整句删除后信息无损失  

### B. 抽象名词与虚弱动词（→ stale-words, qi；英文旁参 Williams）

- 「进行 / 予以 / 开展 / 推动」+ 双音名词，主体不清  
- 名义化：优化的实施、赋能的落地  

### C. 逻辑空转（→ logic）

- 「因此 / 进而 / 由此可见 / 基于此」前后无推导  
- 事实、解释、建议搅在同一句，warrant 缺失（见 notes/toulmin-warrant.md）  

### D. 分寸与过度周全（→ proportion, intent）

- 语言极度周全，最终无立场  
- demo / 单次反馈写成已验证规律  

### E. 翻译腔 / 得体（→ decorum）

- 中文里欧化长定语、抽象名词串联、责任主体消失  
- 英文里中式直译腔（若文稿为英文）  

### F. 结构浅层信号（→ selection, qi；一段一意）

- 万能排比、段段同构、标题伪 MECE（见 notes/mece.md）  

## 可选：本地启发式脚本

仓库内 `scripts/detect_prose_signals.py` 用正则做**浅层**命中（套话、空「因此」、翻译腔、过强断言等）。用法：

```bash
python scripts/detect_prose_signals.py path/to/draft.md
```

脚本命中只是复查提示，**不能**替代本技能的引用原文与人工判断；无命中也不等于合格。

## 流程

1. 确认文稿语言（中/英）与场景（若未知，按知识工作文档处理）。  
2. 按 A–F 扫描；每类列出 0–N 条，优先高信号。  
3. 汇总：最伤阅读的 3 个问题；建议的修改顺序（结构 → 段落 → 句子 → 词语）。  
4. 若用户需要入库判例，指引使用 `case-intake`，不要在本技能直接写入 `cases/`。

## 输出模板

```markdown
# AI 文稿信号检测

**场景：** （已知则写；未知则「未指定」）
**扫描范围：** A–F

## 发现

| # | 信号类 | 强度 | 原文 | 可能维度 | 复查建议 |
|---|---|---|---|---|---|
| 1 | A 套话 | 明显 | 「……」 | stale-words | 删除或换成具体动作/数字 |

## 未检出

- （列出未击中的大类）

## 优先处理（最多 3 条）

1. …
2. …
3. …

## 修改顺序建议

结构 → 段落 → 句子 → 词语；事实/来源另开门，不放在最后润色。

## 说明

命中是复查信号，不是自动否决。完整署名前判断见 STANDARD 八维与终审。
```

## 自检

- [ ] 每条发现有原文  
- [ ] 未将信号写成结论  
- [ ] 维度 slug 合法  
- [ ] 未输出未脱敏敏感信息扩散  
