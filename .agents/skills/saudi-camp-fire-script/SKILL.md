---
name: saudi-camp-fire-script
description: Use when generating or revising Chinese short-video口播 scripts for Saudi self-built camps, temporary camps, prefab houses, modular houses, and site accommodation when the topic involves fire safety, SBC 801, Civil Defense, Salamah, fire-resistance, fire separation, egress, alarm/firefighting systems, fire-rated materials, or fire inspection.
---

# Saudi Camp Fire Script

## Purpose

Create professional Chinese short-video口播 scripts for Saudi camp fire-safety topics. The target audience is industry professionals: Chinese EPC/general contractor project managers, procurement teams, and camp operators working in Saudi Arabia.

The script must feel like practical expert knowledge, not a generic advertisement. It should explain one concrete SBC 801 / Civil Defense requirement first. Land Eastern Camel product, delivery, or factory capability only when the user asks for it or when that capability directly answers the script's one fire-safety point.

## Required Local Sources

Before writing or revising a script, inspect the project navigation file when available:

- `AI资料导航索引.md`

For Saudi fire-safety topics, prioritize these source files:

- `沙特临建行业认知.xlsx` for SBC 801, Civil Defense / Salamah, Saudi compliance, and topic boundaries.
- `钧瀚产品优势分级分类总表_v4.xlsx` for advantages, conflict records, and information reliability.
- `拼装房屋产品介绍.txt` for prefab house / packing house product facts.
- `薄壁轻钢房屋产品介绍.txt` when the requested topic is light steel housing.
- `东方骆驼公司简介.txt` and `深圳钧瀚科技有限公司企业基础概况.docx` only when the script passes the product/company landing gate below.

If a requested fact is not in the local sources, browse official or reliable sources before using it, or mark it as a fact slot that needs confirmation.

## Core Rule

One video only explains one fire-safety point. Do not turn one script into a full SBC 801 overview.

Acceptable single points include:

- Space use and fire-risk zoning.
- Fire-resistance and fire separation.
- Material/test/report/BOQ/site consistency.
- Firestopping at joints and penetrations.
- Egress width, exit path, and signage.
- Alarm, extinguisher, fire water, or emergency lighting configuration.
- Civil Defense inspection logic.

Read `references/fire-topic-library.md` when choosing or splitting topics.

## Workflow

1. Identify the single point.
   - Rewrite broad topics into one precise question: "Which SBC 801 / Civil Defense requirement is this video proving?"
   - If the user gives multiple points, split them into a series and write only the first requested point.
   - Keep the title, opening, compliance explanation, optional product/company landing, and ending on that same fire-safety point.

2. Apply the product/company landing gate.
   - Do not mention Eastern Camel, TBOX, factory, stock, local delivery, 15000㎡, or any product unless one of these is true:
     1. The user explicitly asks to connect the topic to company/product capability.
     2. The topic is product selection, supplier selection, delivery capability, material configuration, or brand proof.
     3. The company/product fact directly answers the script's one fire-safety question.
   - If the topic can be answered by pure compliance education or project self-check, keep it product-free.
   - Factory area and `15000㎡` are only relevant when the point is local manufacturing scale, production capacity, or delivery certainty. Do not use them as a generic credibility close.

3. Verify the fact level.
   - Separate confirmed facts, likely claims, and high-risk claims.
   - High-risk claims include exact fire-resistance minutes, temperatures, material densities, UL/ASTM numbers, "must", "prohibited", "停工拆除", "绝对不能", and competitor accusations.
   - Use only confirmed high-risk facts. Otherwise, rewrite them as safer requirement directions or mark them for confirmation.
   - Read `references/fact-check-rules.md`.

4. Build the script with the four-part compliance pattern.
   - Use the structure in `references/script-pattern.md`.
   - The default skeleton is:
     1. Manufacture the crisis and break the false comfort.
     2. Pure objective code education; do not mention Eastern Camel here.
     3. Optional capability landing; map Eastern Camel capabilities to the rules only if the product/company landing gate passes.
     4. Closing hook; use a next-topic teaser, comment prompt, topic request, project self-check question, or light brand close.

5. Keep the tone.
   - Chinese口播, direct and easy to listen to.
   - Professional, concrete, and slightly sharp.
   - Avoid academic wording unless immediately translated into site language.
   - Use "先看懂", "真正卡的是", "不是看材料名字", "要能对得上" style when appropriate.

6. Self-check before returning.
   - Does the script only have one main point?
   - Does it explain the specific SBC 801 / Civil Defense requirement instead of only naming the standard?
   - Does every product claim connect to that requirement?
   - Did every company/product/factory-area mention pass the product/company landing gate?
   - If the script uses regulations, fire-resistance data, standards, test reports, product parameters, or current external facts, append a short `资料出处` footer listing only the sources actually used.
   - Are exact numbers and certifications confirmed?
   - Does it avoid writing the audience as naive?
   - Does it avoid invented competitor wrongdoing?
   - Does the ending avoid repeating one fixed slogan and instead match the script's purpose?
   - Read `.agents/skills/references/b2b-content-quality-gate.md` and confirm that the title, opening, code explanation, optional product landing, and close answer the same verified fire-safety question.
   - Confirm that any hook describes a verified decision, inspection, or configuration boundary rather than an unsupported stop-work, fine, rectification, or approval outcome.

## Output Format

Return:

```text
视频标题
...

发布文案 / SaaS风工业排版
...

视频脚本
| 场景 | 画面建议 | 硬核旁白 | 视觉特效提示 |
|---|---|---|---|
| ... | ... | ... | ... |

自检
- 单点主题：
- 已使用的规范/验收逻辑：
- 产品对应关系：
- 待核实高风险事实：
```

If the user only asks for a revision, keep the output shorter and include only the revised script plus a brief note about what changed.

## Hard Boundaries

- Do not say "used our product and it will definitely pass Civil Defense".
- Do not invent exact SBC 801 clause numbers, minutes, temperatures, material density, or certification reports.
- Do not accuse the market of common fraud or malicious material substitution unless the user provides evidence.
- Do not force a "low-end competitor exposure" paragraph when there is no evidence. Reframe it as "低价方案常见断点" or "容易被忽略的配置缺口".
- Do not write "only standard answer" literally. Use "按这套规范逻辑倒推出来的解决方案" unless the user explicitly wants a stronger advertising stance.
- Do not write "清关资料" as part of a fire approval package unless the topic is imported goods or cross-border procurement. For local delivery or local manufacturing, use "消防资料、产品规格书、材料性能资料、结构图纸/计算、BOQ、安装方法书、交付验收记录".
- Do not say "规范要求" without naming the relevant code/approval path or explaining whether it is a Civil Defense, SBC 801, owner, consultant, or drawing requirement.
- Do not use "普通填充" without explaining what it means and why it matters.
- Do not say professionals "only ask whether the material is fireproof"; instead, acknowledge that formal projects generally know fire-rated materials matter, then move to the deeper requirement.
- Do not compare by insulting Saudi local contractors, Chinese contractors, or competitors.
- Do not write a broad checklist unless the user explicitly asks for a series overview.
- Do not use Eastern Camel, local factory, or `15000㎡` as a default ending. Use them only when they directly answer this script's one point.
- Do not force the ending "关注东方骆驼，出海建营地，我们陪你把消防逻辑讲清楚。"; vary the close based on the topic and audience action.

## Reference Files

- `references/script-pattern.md`: reusable structure extracted from the accepted script.
- `references/fact-check-rules.md`: how to handle high-risk fire-safety facts.
- `references/fire-topic-library.md`: single-point topic library for future scripts.
- `references/accepted-example.md`: user-approved example. Use it as style and structure reference, not as automatically verified fact source.
- `.agents/skills/references/b2b-content-quality-gate.md`: shared title, B2B decision-value, logic-flow, and publishing-risk gate.
