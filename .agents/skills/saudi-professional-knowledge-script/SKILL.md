---
name: saudi-professional-knowledge-script
description: Use when generating, diagnosing, revising, or selecting titles for Chinese B2B short-video口播 scripts about Saudi temporary construction, camp approval, collective housing, supply chains, compliance, materials, engineering boundaries, logistics, customs, local content, or project management. Verify the title premise and exact engineering scenario before drafting, keep every paragraph on the title's one customer question, and only add a company bridge when it is directly relevant and evidence-backed.
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

1. Run the title-premise gate before drafting.
   - Identify the title's exact subject, factual premise, customer concern, and one answer the viewer should retain.
   - Verify whether the premise matches the real engineering or approval process. Do not manufacture a late application, missing handoff, rework, rejection, extra cost, or other conflict merely to make the title dramatic.
   - If the premise is false, uncommon, or not supported, stop and explain why; recommend a fact-based angle instead of forcing a script.
   - Do not change a user-confirmed title unless the user authorizes it.
   - If the user says "先检查", "先分析", "先确认", "先判断标题", or otherwise asks for validation before generation, output only the diagnosis, recommended core conclusion, and proposed reasoning path. Do not write the script in the same turn, even when the title is viable; wait for explicit confirmation.
   - If the user asks for title candidates only, generate candidates only. Within the same topic, audience, and evidence boundary, candidates may explore different true, draftable viewer questions and topic-appropriate angles; provide each title, the question it answers, its evidence-backed non-basic conclusion, and its information relationship. After one candidate is selected, lock that question and generate a `标题交接单` before any separate script conversation writes the body.

2. Lock the exact scenario and boundaries.
   - Distinguish fixed residential buildings, residential compounds, project mobile cabins, and other temporary facilities.
   - Distinguish applicant/responsible-party identity, property or site-use relationship, product ownership, approval requirements, application documents, inspection items, and operating conditions. These are different concepts; never merge them for convenience.
   - Distinguish local manufacture/local delivery from imported or cross-border supply.
   - Do not transfer a rule from one scenario to another without an official or primary source that explicitly supports the transfer.
   - A general service page may cover multiple facility categories. Do not repeat its generic ownership/lease checklist in a mobile-cabin script unless the source explicitly states that the item applies to mobile cabins or the title directly asks about that document.

3. Verify facts to the depth needed by the title.
   - Read `references/fact-rules.md`.
   - Use an official service summary only as a routing source. If it says only "health, technical, and safety requirements," follow the linked official guide and extract concrete, relevant checks before using that phrase as the script's value.
   - Exact regulation names, thresholds, agency roles, approval outcomes, fines, timelines, documents, inspection items, and responsible parties must be verified.
   - Internally map every factual sentence to a source. If a sentence is only inference, either remove it or clearly narrow it; do not use inference to fill runtime.

4. Build around one customer question.
   - Read `references/script-pattern.md`.
   - Choose the structure from the problem: mechanism, comparison, sequence, decision rule, or checklist. Do not automatically use "first, second, third."
   - Keep only content that directly answers the title. Documents, responsibility, process, products, or consequences may appear only when they are part of that answer.
   - Translate necessary technical terms into plain spoken Chinese immediately. Give the viewer a concrete judgment, check, or action rather than abstract words.
   - In the first one or two sentences, make the scenario and the viewer's problem clear. Every paragraph must add a necessary reason, condition, comparison, or action; remove background, repetition and anxiety that do not help the viewer decide.

5. Apply the product boundary.
   - Keep the script pure科普 by default.
   - For a topic originating from construction, infrastructure, urban-development, transport, logistics, industrial-city, or project news, read `.agents/skills/references/b2b-topic-conversion-loop.md` before choosing an angle or company mention.
   - Do not add 东方骆驼 or product capabilities when the topic is not directly related to the company’s business, or when the evidence ledger cannot support a direct answer to the title. When both conditions are met, naturally use the evidence bridge and source ledger in that rule.

6. Re-audit the whole draft after every substantive revision.
   - Do not patch only the sentence the user flagged. Re-read the title, opening, every transition, conclusion, and interaction prompt as one chain.
   - Remove new repetition, concept switching, scene mixing, unsupported implications, and endings that introduce a different topic.
   - Expand runtime only by deepening verified content that answers the title; never add adjacent facts or invented project behavior to reach a target length.

7. Output the complete script by default.
   - When the user asks for a revision, return the full revised version rather than an isolated replacement unless they explicitly request one sentence only.
   - If the script uses regulations, official programs, policy facts, approval requirements, specifications, company/product facts, or current external facts, append a short `资料出处` footer listing only the sources actually used.

8. Run the professional B2B quality gate before finalizing.
   - Read `.agents/skills/references/b2b-content-quality-gate.md`.
   - Keep the verified title conclusion above hook appeal. Confirm that the title, opening, scenario boundary, explanation, optional product landing, and ending answer the same customer question.
   - Do not make an approval, document, responsibility, or inspection hook sound universal or more consequential than the evidence supports.

## Tone

Calm, expert, grounded, practical, and conversational. Write from the customer's real decision context, not from the supplier's or narrator's superior position. Avoid "内幕", "惊天", official brochure language, robotic summaries, and exaggerated fear. The value is verified clarity and usable judgment.

## Reference Files

- `references/script-pattern.md`: professional科普 structure.
- `references/fact-rules.md`: policy, compliance, and engineering fact boundaries.
- `.agents/skills/references/b2b-content-quality-gate.md`: shared title, B2B decision-value, logic-flow, and publishing-risk gate.
- `.agents/skills/references/b2b-topic-conversion-loop.md`: construction-news relevance gate, education/marketing account routing, evidence-bridge and review rules.
