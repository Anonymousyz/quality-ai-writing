# 高质量 AI 写作 · 标准

**版本：** 0.7.0  
**范围：** 知识工作文档（方案、评审、报告、决策备忘、README/技术文档）；中英文通用。

分层骨架借桐城「义理·考据·词章」相济（见 `traditions/tongcheng-yifa.md`），不是复刻古文戒律。

## 写前：模式与三问

先分清任务模式（详见 `notes/task-modes.md`）：

- **结论驱动** — 已有判断，要让读者理解、相信或行动  
- **探索驱动** — 借写作更新假说；允许未收敛，但须写清改口条件  

开始前至少问三句：这篇解决什么问题？哪些是事实、哪些是解释或选择？谁读完要理解、判断或完成什么？

动笔前试写一句话核心（写不出则先补理解，见 `notes/understanding-ceiling.md`、`traditions/lu-ji-wenfu.md`）。读者与场景见 `notes/reader-first.md`、`notes/scene-choices.md`。研究类开篇可选用 CARS（`notes/cars-intro.md`）。

## 一票否决

快扫动作见 `notes/veto-scan.md`。

1. 关键事实错误或编造（含编造引文、数据、来源）
2. 关键论断来源不可溯
3. 过度声称：demo 说成结论、个例说成规律、未验证说成已验证
4. 场合违规：敏感信息、未授权引用
5. 通篇无人的判断：AI 初稿直接交付，看不到立意与取舍痕迹

## 义理

1. 立意 (`intent`) — 有没有一个值得写下来的判断？删掉这篇，决策会不会变差？
2. 逻辑 (`logic`) — 结论是从证据里长出来的，还是先有结论再找话？（Warrant：`notes/toulmin-warrant.md`）
3. 取舍 (`selection`) — 详略是否体现观点？（MECE 启发式：`notes/mece.md`）

## 考据

4. 来源 (`sources`) — 关键事实、数据、引文是否可溯源？来源是否权威且被正确转述？
5. 分寸 (`proportion`) — 声称强度与证据强度是否匹配？（阶梯：`notes/evidence-ladder.md`）

## 辞章

6. 陈言务去 (`stale-words`) — 套话、空话、AI 腔是否已去掉？每句话是否有信息量？（辞达：`traditions/su-shi-cida.md`）
7. 文气 (`qi`) — 一口气读下来是否断气？
8. 得体 (`decorum`) — 语体与场景是否匹配？中文是否地道中文、英文是否地道英文？（英文纪律：`notes/english-knowledge-prose.md`）

详情：`principles/` · `notes/` · `traditions/` · `cases/`。

**技能：** `pre-sign-review`（署名前全检）· `ai-prose-detect`（套话信号）· `mock-reader`（模拟复述）· `case-intake`（判例草稿）。模拟读者**不能**替代真人审阅。脚本：`detect_prose_signals.py`（命中≠定罪）· `case_coverage.py`（八维判例覆盖）。

## 终审

八维查毕，清单结束。最后成不成——没有任何清单能替判断者做。

> 文章千古事，得失寸心知。

## 使用方式

1. 分清模式与写前三问；钉读者与场景。  
2. 先扫否决；触发即不合格。  
3. 按风险选深度：pre-sign-review / ai-prose-detect / mock-reader。  
4. 修改先大后小；一段一意；核心主张补 Warrant；声称对齐证据阶梯；事实核验独立成门。  
5. 脱敏后 case-intake 入库；修法见 `MAINTENANCE.md`。
