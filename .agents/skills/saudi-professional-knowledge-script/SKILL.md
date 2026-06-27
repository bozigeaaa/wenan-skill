---
name: saudi-professional-knowledge-script
description: Use when generating or revising Chinese B2B short-video口播 scripts that explain Saudi temporary construction, camp approval, supply chain, compliance, materials, engineering boundaries, logistics, customs, local content, or project-management knowledge. Default to pure professional education and do not include products unless the user asks.
---

# Saudi Professional Knowledge Script

## Purpose

Create professional Chinese口播 scripts that build trust by explaining Saudi engineering, temporary camp, approval, supply-chain, compliance, material, or project-boundary topics. The script should sound like an experienced practitioner simplifying a real rule or mechanism.

## Routing

Use this as the general professional科普 skill. If the topic is specifically about:

- Fire safety, SBC 801, Civil Defense, Salamah: use `$saudi-camp-fire-script`.
- Thin-walled light steel houses or G550 wall/roof systems: use `$saudi-light-steel-script`.
- TBOX/K-series toilets, showers, sanitary units: use `$saudi-sanitary-unit-script`.

## Required Sources

- Read `knowledge/AI资料导航索引.md`.
- Read `knowledge/沙特临建行业认知.xlsx` for Saudi approval, SBC, Civil Defense, SABER/SASO, tax, customs, local content, and project cognition.
- Read relevant product files only if the user explicitly asks to connect the topic to a product.
- Browse current reliable sources when discussing current policy, agencies, public programs, fines, enforcement, market changes, or latest news.

## Workflow

1. Turn the topic into one mechanism-level question.
   - Example: "Why can't every camp use one universal layout?"
   - Example: "When does local content matter, and when is it being overgeneralized?"

2. Verify facts.
   - Read `references/fact-rules.md`.
   - Exact regulation names, agency roles, approval outcomes, fines, and public program claims must be verified.

3. Build a professional explanation.
   - Read `references/script-pattern.md`.
   - Explain what most people misunderstand, what the real boundary is, and what project teams should check.

4. Keep it pure科普 by default.
   - Do not add 东方骆驼 or product capabilities unless the user asks.

5. Output only the complete script by default.

## Tone

Calm, expert, grounded, and practical. Avoid "内幕", "惊天", or exaggerated fear. The value is clarity.

## Reference Files

- `references/script-pattern.md`: professional科普 structure.
- `references/fact-rules.md`: policy, compliance, and engineering fact boundaries.
