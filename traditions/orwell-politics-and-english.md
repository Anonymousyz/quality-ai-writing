# Orwell《Politics and the English Language》与 AI 写作

## 出处

George Orwell, *Politics and the English Language*（1946）。原文为英文政论/文风随笔，通行文本见 Orwell 文集与多家公域转载。下文英文短摘据该文末「六条规则」及前文对坏文风类型的分类；中文说明为本仓库转述，非官方译本。

## 来源使用原则（公开表述）

Orwell 的规则是**启发式（heuristics）**，不是科学定律。它们帮助发现病征、逼出更清楚的说法；不能当作可自动打分的公式，也不能用「违反某条」替代终审判断。遇规则与清晰表达冲突时，以不说蠢话、不虚张声势为准——Orwell 自己也把这一点写进第六条。

## 坏文风类型 ↔ AI 套话

Orwell 列举的几类病征，几乎可直接对照今日模型初稿：

| Orwell | 含义（转述） | AI 初稿对应 |
|---|---|---|
| Dying metaphors（垂死隐喻） | 用滥到不再唤起形象的比喻 | 「构建闭环」「打通抓手」「站在风口」等空转隐喻 |
| Operators / verbal false limbs（语词假肢） | 用现成动词短语撑长度，代替具体动词 | 「进行优化」「予以关注」「开展赋能」；英文 make/ensure/leverage 堆叠 |
| Pretentious diction（装腔用词） | 大词、外来词、伪科学词抬身份 | 「范式」「底层逻辑」「对齐」「落地」滥用；英文 delve、synergy |
| Meaningless words（无意义词） | 听着郑重、删了无信息 | 「值得注意的是」「在……背景下」；主体可替换句 |

垂死隐喻与语词假肢，正是「预制短语」：作者不再选择词语，只是拼装库存。模型默认输出大量库存——评审上归入 `stale-words`，常与匀速排比一并伤及 `qi`。

## 六条规则中与本仓库直接相关的几条

文末六条，此处摘与「陈言务去」「分寸」最贴的三条（原文）：

1. **陈言 / 预制比喻**  
   > Never use a metaphor, simile, or other figure of speech which you are used to seeing in print.  
   → 映射 `stale-words`：见过太多次的比喻与句式，多半已死；AI 尤其爱复读训练语料里的高频腔。

2. **能删则删**  
   > If it is possible to cut a word out, always cut it out.  
   → 映射 `stale-words`：与本库「删句测试」同向——无信息增量则删；也间接利好 `qi`（少一层空转节拍）。

3. **宁破规则，勿说蠢话**  
   > Break any of these rules sooner than say anything outright barbarous.  
   → 映射 `proportion` 与终审：机械执行「短词 / 主动 / 删字」若导致过度简化、抹掉限定或夸大确定感，就是分寸失控。规则服务于清楚与诚实的声称，不服务于「看起来干净」。

另可旁参第五条（能用日常词就不用行话）：行话本身无罪，**用行话掩盖证据不足**才伤 `proportion`。Orwell 批评的伪精密、空洞强调，常与「demo 说成结论」「个例说成规律」伴生——见 `principles/proportion.md`。

## 对 AI 写作的用法

- 把六条当**自检清单的启发**，不当自动否决器。  
- 垂死隐喻与语词假肢优先清；清完再看声称强度是否仍与证据匹配。  
- 若「去 AI 味」只换同义陈言，而未恢复具体名物、数量、条件与责任主语，则 Orwell 与韩愈「惟陈言之务去」一样，工作尚未完成。

详见 `principles/stale-words.md`、`principles/proportion.md`；文气侧面见 `principles/qi.md`。
