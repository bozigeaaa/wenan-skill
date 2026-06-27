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
   - Generate 3 candidate titles internally and choose the safest, clearest one.
   - Title must include a hotspot hook, an industry relationship, and no exaggerated consequence.

5. Write or route the script.
   - Read `references/script-pattern.md`.
   - If the output is pure industry impact, write directly.
   - If it becomes a Saudi story angle, route to `$saudi-breakout-story-script`.
   - If it becomes professional科普, route to `$saudi-professional-knowledge-script`.
   - If user explicitly asks to bring product, route to `$saudi-product-seeding-script` or the relevant product skill.

6. Output rules.
   - Default output only the final script.
   - If user asks "先给选题", output 3-5 hotspot topic options with title, one impact point, and risk notes.
   - If user asks for sources, cite sources and dates.

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
