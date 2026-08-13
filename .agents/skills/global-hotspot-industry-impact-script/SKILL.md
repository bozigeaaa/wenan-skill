---
name: global-hotspot-industry-impact-script
description: Use when generating or revising Chinese short-video口播 scripts based on current international hot topics, global news, Middle East political/economic events, shipping disruptions, energy markets, trade, policy, or supply-chain changes, where Codex must verify the latest facts, identify one impact point for Saudi temporary construction/camps/engineering practitioners, decide a title, and write an industry-impact script. Default to no product mention.
---

# Global Hotspot Industry Impact Script

## Purpose

Turn current international hotspots into one-point industry-impact scripts for people doing Saudi temporary construction, camps, prefabricated buildings, logistics, procurement, or site delivery. The value is not "chasing news"; it is explaining how one verified hotspot may affect Saudi engineering work.

Default output is a complete script with a finalized title. Do not mention 东方骆驼, TBOX, light steel, sanitary units, or any product unless the user explicitly asks.

## Core Positioning

This is an upstream topic and title skill:

1. Find or verify a current hotspot.
2. Decide whether it truly matters to this industry.
3. Select one impact point only.
4. Finalize a title.
5. Write the script or route to a suitable script skill.

It is not a product conversion skill, market panic generator, or news summary.

## Required Sources

Always browse for current hotspot facts. Use current date and absolute dates when comparing "latest", "today", "recently", or "now".

Also inspect project sources when industry framing is needed:

- `knowledge/AI资料导航索引.md`
- `knowledge/沙特临建行业认知.xlsx`
- `knowledge/钧瀚产品优势分级分类总表_v4.xlsx` only if the user explicitly asks to connect to company/product capabilities.

## Workflow

1. Verify the hotspot.
   - Read `references/hotspot-sourcing.md`.
   - Read `references/hotspot-ledger.md` and `content-state/hotspot-ledger.json` before looking for a topic.
   - Treat search results only as candidates. Open or scrape the original source before confirming its date, actor, status, and source link.
   - Confirm what happened, where, when, and what is still uncertain.
   - Never treat rumor, social media speculation, or one sensational headline as fact.

2. Test industry relevance.
   - Read `references/impact-filter.md`.
   - Keep only hotspots that affect Saudi projects through a concrete chain: shipping, port access, customs, insurance, material cost, energy price, approval, labor, safety, project schedule, procurement, or camp operation.

3. Choose one impact point.
   - One video explains one impact, not the entire geopolitical event.
   - Examples: delivery time, freight risk, war-risk insurance, material cost, site expansion schedule, procurement planning, local compliance, or labor/camp management.

4. Finalize the title.
   - Read `references/title-selection.md`.
   - When the hotspot is about shipping, ports, imports, cross-border procurement, or delivery responsibility, read `.agents/skills/references/local-manufacturing-delivery-proof.md` before choosing the title.
   - Generate 3 candidate titles internally and choose the safest, clearest one.
   - Title must include a hotspot hook, an industry relationship, and no exaggerated consequence.

5. Write or route the script.
   - Read `references/script-pattern.md`.
   - For Saudi construction, urban development, infrastructure, industrial-city, transport, logistics, or project news, read `.agents/skills/references/b2b-topic-conversion-loop.md` before selecting the script angle. Record the project stage and reject any product link that is not naturally supported by a site-support, delivery, or operation question.
   - If the output is pure industry impact, write directly.
   - If it becomes a Saudi story angle, route to `$saudi-breakout-story-script`.
   - If it becomes professional科普, route to `$saudi-professional-knowledge-script`.
   - If user explicitly asks to bring product, or explicitly selects the marketing account, route to `$saudi-product-seeding-script` or the relevant product skill. A company mention remains optional unless its evidence-backed capability directly continues the same customer question.

6. Prevent repetition and downgrade stale news.
   - Before drafting, use the ledger to check whether the same event or angle has already been used.
   - A 0-7 day event may be a current hotspot only after status verification. An 8-30 day event needs a material ongoing development. News older than 30 days must be treated as background, not recent news.
   - If no eligible hotspot remains, route in this order: verified official project/policy/logistics signal -> evergreen decision topic -> local-manufacturing proof topic supported by company materials.
   - Do not force a news script just because the user asks for a hotspot.

7. Output rules.
   - Default output the final script with a short `资料出处` footer because hotspot scripts always rely on current external facts.
   - If user asks "先给选题", output 3-5 hotspot topic options with title, one impact point, and risk notes.
   - Cite only sources used for the selected hotspot facts and the industry-impact chain; include source name, publication/access date when available, and link.

8. Run the professional B2B quality gate before finalizing.
   - Read `.agents/skills/references/b2b-content-quality-gate.md`.
   - Keep the verified hotspot and its one concrete industry impact above title appeal or urgency.
   - Check that the title, opening, impact chain, and ending answer the same procurement, delivery, camp-operation, or project-management question.

## Hard Boundaries

- Do not use war, disaster, sanctions, or diplomatic conflict to hard-sell products.
- Do not write "closed", "blocked", "shutdown", "停关", "全面中断", or "项目停摆" unless current reliable sources prove that exact status.
- Do not turn "possible impact" into "has already caused".
- Do not claim price increases, delays, insurance changes, fines, or route changes without current evidence.
- Do not discuss sensitive military or diplomatic conclusions beyond what reliable sources establish.
- Do not mention company/product by default.

## Reference Files

- `references/hotspot-sourcing.md`: current-news sourcing and verification rules.
- `references/impact-filter.md`: one-point industry impact filter and scoring.
- `references/title-selection.md`: title drafting and finalization rules.
- `references/script-pattern.md`: script structure, routing, and example using Strait of Hormuz.
- `.agents/skills/references/b2b-content-quality-gate.md`: shared title, B2B decision-value, logic-flow, and publishing-risk gate.
- `.agents/skills/references/local-manufacturing-delivery-proof.md`: conditional local manufacturing and delivery-responsibility differentiation rule.
- `references/hotspot-ledger.md`: candidate discovery, original-source verification, freshness, deduplication, and monitor boundaries.
- `content-state/hotspot-ledger.json`: shared local event and usage ledger; read before drafting and update after a script is finalized.
- `.agents/skills/references/b2b-topic-conversion-loop.md`: construction-news classification, temporary-facility relevance gate, account routing, evidence bridge, and post-publication review fields.
