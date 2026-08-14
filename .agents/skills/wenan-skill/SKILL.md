---
name: wenan-skill
description: Use when a user asks for any Chinese B2B short-video copywriting task for the Saudi construction, temporary-building, camp, product, brand, industry-knowledge, project-news, title, revision, or oralization workflow and should not need to remember a specialist skill name.
---

# 文案 Skill

Use this as the single entry for the `Script-Copy-Skills` project. Identify the task, load the project rules and the smallest relevant specialist skill, then produce the requested output. 不要要求用户记忆专项 Skill 名称或手动选择路由。

## First Read

1. Read `AGENTS.md`.
2. Read `knowledge/AI资料导航索引.md`, then only the task-relevant original company or industry sources.
3. For a returning or handoff task, read `docs/wenan-skill-完整交接文档_2026-08-14.md` when it exists.

## Route by Request

| User request | Read and use |
| --- | --- |
| Current news, tender, project progress, construction, urban development, infrastructure, rail, logistics or international hotspot | `$global-hotspot-industry-impact-script`; also read the hotspot ledger and `b2b-topic-conversion-loop.md` |
| Saudi approval, compliance, material, engineering boundary, project-management or industry knowledge | `$saudi-professional-knowledge-script` |
| Product selection, product comparison, sales conversion or product solution | `$saudi-product-seeding-script`, or the relevant fire/light-steel/sanitary specialist skill |
| Saudi local factory, warehouse, delivery, installation, parts or company proof | `$saudi-brand-proof-script` and the company-claim evidence ledger |
| Existing script needs to sound more natural, more spoken, less AI-written or less formal | `$script-oralization-rewriter` and the Humanizer expression gate |
| A topic spans more than one row | Select one primary skill from the user’s core question; use a secondary skill only if its facts or boundaries are directly needed. Keep one script to one core question. |

## Required Decisions

Infer from the request when clear; otherwise ask only for information that changes the result:

- `account_type`: education or marketing;
- one core viewer question;
- whether current external facts need verification;
- whether a company evidence bridge is naturally relevant;
- desired runtime and output format.

For construction/project news, classify the project stage and apply the temporary-facility relevance gate. A project being in the construction industry is not proof that it needs the company’s products.

For marketing content, use one evidence-based company bridge only when it continues the same decision question. For education content, naturally use one company bridge only when the topic is directly related to the company’s products, services, delivery or after-sales capabilities and the evidence ledger supports it; otherwise do not force a company mention. Humanizer changes expression only; it never adds facts, claims, causes, numbers, cases, or promises.

## Title-Candidate Handoff

When the user asks to generate titles only, generate title candidates only. Keep every candidate on the same viewer question, but choose different topic-appropriate angles internally; do not impose a fixed category set or introduce unrelated angles to fill a quota. For each candidate, give the title, the viewer question it answers, and the recommended body logic. Do not generate the script or a full handoff for every candidate.

After the user chooses one candidate, generate a `标题交接单` for that title only. It must include: title, account type, target audience, one core viewer question, one directly usable viewer judgment or action, scenario and fact boundaries, verified materials, company-presence choice, an evidence-backed company bridge when applicable, recommended body structure, and runtime. The separate script conversation should receive this full handoff rather than the title alone.

## Output

Default to the complete final title and script. Add `资料出处` only when the project rules require it. Output diagnosis, title candidates, risks, source list, or modification notes only when the user asks.

## Prompt Contract for Colleagues

The colleague may write either `$wenan-skill` or “wenan skill”, then provide what is known:

```text
账号：营销 / 科普
主题：……
目标：……
时长：……秒
资料：已有资料 / 需要联网核验
公司露出：不带 / 自然轻带 / 转化
```

For a title-only conversation, the colleague can additionally state `本次只生成标题候选，不生成正文` and the desired candidate count. After selecting one candidate, they can state `选第 X 个。请生成标题交接单，不写正文。`

Missing fields are not a reason to demand that the user select a specialist Skill. Use safe defaults from `AGENTS.md`, or ask one concise question when the missing choice would materially change the script.
