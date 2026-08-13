---
name: saudi-light-steel-script
description: Generate or revise Chinese B2B short-video口播 scripts for Saudi thin-walled light steel houses, long-term camps, office/dormitory units, wall/roof/envelope systems, G550/C-shaped steel, glass wool, cement fiber board, PVC windows, steel doors, insulation, wind/sand/high-temperature performance, and comparisons with packing containers, ordinary prefab, or current Saudi market alternatives. Use when the user wants one reliable, single-point, expert-style script about light-steel product logic, parameters, selection, application scenarios, or competitor/market comparison for Eastern Camel.
---

# Saudi Light Steel Script

## Purpose

Create professional Chinese口播 scripts about thin-walled light steel houses in Saudi project scenarios. The speaker should sound like someone who understands Saudi engineering delivery: practical, specific, and calm, not like a brochure or salesperson.

This skill is for single-point product logic. It should explain one concrete question about light steel, then connect Eastern Camel's material, design, delivery, or local service capability only when it naturally answers that question.

## Required Local Sources

Before writing or revising a light-steel script, inspect the project navigation file when available:

- `knowledge/AI资料导航索引.md`

Prioritize these source files:

- `knowledge/薄壁轻钢房屋产品介绍.txt` for product structure, materials, wall/roof/envelope system, door/window, and house-type facts.
- `knowledge/沙特临建行业认知.xlsx` for Saudi light-steel industry cognition, approval, site, climate, and compliance boundaries.
- `knowledge/钧瀚产品优势分级分类总表_v4.xlsx` for advantages, reliability level, and conflict records.
- `knowledge/深圳钧瀚科技有限公司企业基础概况.docx` for company role, sales cognition, delivery logic, and Saudi project boundaries.
- `knowledge/东方骆驼公司简介.txt` for Eastern Camel local factory, brand positioning, and Saudi local delivery.

If a requested light-steel parameter is not confirmed in local sources, do not invent it. Use a safer professional explanation or mark it internally as a confirmation slot.

## Scope

Use this skill for topics such as:

- Why light steel is more suitable than packing containers for medium/long-term camps, office areas, or higher-image projects.
- How wall systems, glass wool, cement fiber board, PVC windows, steel doors, and roof systems work together.
- How Saudi heat, sand, corrosion, AC load, and site management affect product selection.
- How to explain G550, C-shaped steel, wall thickness, insulation, fire resistance, wind resistance, or seismic claims without overclaiming.
- How Eastern Camel's local factory, stock, Chinese coordination, or delivery team supports light-steel project certainty.
- How to compare light steel with current market alternatives without fake competitor accusations.

If the topic is mainly SBC 801, Civil Defense, Salamah, fire separation, egress, or fire inspection, prefer `$saudi-camp-fire-script`.

## Core Rule

One video explains one light-steel point. Do not turn one script into a full product catalog.

Title, opening, parameters, product landing, and ending must answer the same question. If the title is about G550/C-shaped steel, do not drift into transport cost, wind/seismic rating, local mass production, or SBC approval in the same script. Those are separate episodes.

Rewrite broad topics into one precise question:

- "Why does this wall system matter in a Saudi camp?"
- "What problem does glass wool solve here: insulation, sound, or fire direction?"
- "Why is light steel different from packing containers for long-term use?"
- "Which parameter actually answers the customer's concern?"

Every parameter, scenario, and product claim must answer that one question. If it answers another question, remove it.

## Workflow

1. Identify the single point.
   - Convert the user's topic into one mechanism-level question.
   - If the topic includes multiple selling points, choose the strongest one and leave the others out.
   - Decide the intended ending before drafting. If the ending does not answer the title, split the topic or change the title.

2. Verify facts.
   - Read `references/fact-check-rules.md`.
   - Treat steel grade, wall thickness, glass-wool thickness, wind resistance, seismic grade, fire performance, install time, capacity, and cost as high-risk facts.
   - Check each parameter one by one against local sources, conflict records, user-provided facts, or reliable current sources before writing it.
   - Do not avoid parameters merely because they are high-risk. If a parameter is real, relevant, and verified, use it precisely.
   - If a parameter cannot be verified, do not write it as fact.

3. Check market comparison needs.
   - If the script mentions current competitors, Saudi market alternatives, or mainstream local solutions, browse current reliable sources first.
   - Do not name competitors, prices, or performance conclusions without current evidence.
   - Compare risk structures and suitable scenarios, not by insulting competitors.

4. Build the script.
   - Read `references/script-pattern.md`.
   - Default structure:
     1. Point out one common selection mistake.
     2. Explain the light-steel mechanism in plain Chinese.
     3. Translate it into a Saudi project scene.
     4. Land Eastern Camel's corresponding capability only if relevant.
     5. End with a natural question, topic request, next-video hook, or light brand close.

5. Follow project output rules.
   - By default, output the complete script text.
   - When the script uses regulations, specifications, company/product parameters, material data, competitor/current-market facts, or other external facts, append a short `资料出处` footer listing only the sources actually used.
   - Do not show self-check or risk notes unless the user asks.

6. Run the professional B2B quality gate before finalizing.
   - Read `.agents/skills/references/b2b-content-quality-gate.md`.
   - Confirm that the title, opening, mechanism, Saudi project scene, optional product landing, and ending answer the same verified light-steel selection question.
   - Do not use a hook to imply unverified structural, fire, approval, cost, or market consequences.

## Tone

- Professional, direct, and grounded.
- Like a Saudi engineering practitioner explaining one real selection issue.
- Default to a senior Saudi local supplier / project delivery perspective. Do not unnecessarily expose a China-to-Saudi shipment angle.
- Do not sound cheerful, promotional, or brochure-like.
- Use short spoken sentences.
- Explain technical terms immediately in plain Chinese.
- Prefer "在沙特现场真正卡人的不是...", "这个参数要看它回答什么问题", "长期营地不能只看搭得快", "墙体不是越厚越好，关键是整套围护系统能不能对上使用场景".

## Hard Boundaries

- Do not dump all light-steel parameters into one script.
- Do not remove useful parameters just because they require verification; verify them and keep the ones that directly support the single point.
- Do not say "best", "only answer", "perfect", "100% safe", or "guaranteed approval".
- Do not invent G550/Q235B decisions, wall thickness, glass-wool thickness, wind/seismic ratings, fire ratings, install time, cost, or production capacity.
- Do not claim Saudi regulations force a specific material unless sourced.
- Do not say "规范要求" without naming the relevant code, owner requirement, drawing requirement, or calculation boundary. For light steel, distinguish SBC 308/309/301/306/303 when relevant; if not verified, say "按项目图纸和结构计算确认".
- Do not write "清关资料" for Saudi local factory/local manufacturing/local delivery unless the script is explicitly about imported goods or cross-border procurement. Use "项目资料包、产品规格书、材料参数表、结构计算、消防资料、安装方法书、交付验收记录" instead.
- Do not write "照搬国内现成配置" as a general market fact. If needed, frame narrowly as "刚进入沙特市场的新供应商容易按熟悉配置套用" and only with evidence or user approval.
- Do not guarantee "15-20 years" or any lifecycle/warranty/corrosion period unless confirmed in source material; use safer long-term-use language if unresolved.
- Do not write "local Saudi options are bad" or insult local contractors, Chinese contractors, or competitors.
- Do not use old generic competitor stereotypes. Current market claims require current research.
- Do not use a fire-safety compliance frame when the topic is actually insulation, structure, delivery, or usage scenario.

## Reference Files

- `references/script-pattern.md`: structure and language patterns for light-steel single-point scripts.
- `references/fact-check-rules.md`: parameter, competitor, and high-risk claim handling.
- `.agents/skills/references/b2b-content-quality-gate.md`: shared title, B2B decision-value, logic-flow, and publishing-risk gate.
