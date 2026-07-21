# Strunk & White《The Elements of Style》与 AI 写作

## 出处

William Strunk Jr. & E. B. White, *The Elements of Style*（多版；规则编号因版而异）。下文英文短摘取通行规则表述；中文为对照说明。规则是**英文写作启发式**，不能直接当成中文语法条例。

## 短摘一：Omit needless words

> Omit needless words.

整本小书里最常被引用的一句。它不只要求「短」，要求**每个词都在负重**。对 AI 初稿：同义反复、程度副词空转、主语可替换的正确废话，都是 needless。

### 映射

- `stale-words`：词/句级可删  
- `selection`：段/材料级可删——整块「背景」若不服务判断，也是 needless  
- `qi`：删掉空转后，节奏往往自己回来

## 短摘二：具体与有力

书中反复要求用具体、确定的说法，避免含混（definite, specific, concrete）。AI 爱用升维抽象词盖住未想清的细节——评审上先问能否落到人、动作、数字、条件（见 `intent` / `proportion`）。

## 短摘三：引文与证据态度

正式引作证据时，要标明出处、忠实转述（各版在 quotations 相关规则中强调 documentary evidence 的处理）。映射 `sources`：关键论断旁要有可核线索；编造引文直接触发否决。

## 边界

- 英文规则 → 中文文档：吸收「信息量与具体性」，不吸收生搬的冠词/被动教条。  
- 「Omit needless words」若删掉必要限定，会伤 `proportion`——该留的边界不是 needless。  
- 与 Orwell 六条、韩愈「陈言务去」同族：都逼作者为自己的句子负责。

详见 `principles/stale-words.md`、`principles/selection.md`、`principles/sources.md`。
