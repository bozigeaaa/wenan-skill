---
name: script-oralization-rewriter
description: Use when revising an existing Chinese short-video script, B2B口播稿, product script, Saudi engineering/camp script, or draft copy to make it more conversational, natural, punchy, and camera-ready while preserving verified facts and avoiding new unverified claims.
---

# Script Oralization Rewriter

## Purpose

Rewrite an existing Chinese script into natural spoken口播. Keep the business logic, single core point, and verified facts intact; improve rhythm, sentence length, transitions, and viewer-facing energy.

This is a post-processing skill. Use it after a topic/product skill has produced a draft, or when the user provides a draft and asks for "更口语化", "像真人说话", "更像短视频口播", "更有镜头感", "别太书面", or similar.

## Core Boundary

Oralization is expression work, not fact invention.

Do not add:

- New numbers, certifications, standards, legal consequences, test reports, client cases, competitor claims, prices, or performance conclusions.
- Stronger promises than the source draft supports.
- Insults toward Saudi local suppliers, Chinese contractors, competitors, or customer choices.
- Fake现场感, fake客户反馈, fake停工整改, or "听说/业内都知道" claims without evidence.

If the source draft has risky claims, keep the rewrite safer or flag internally. Do not make risky claims sound more certain just because the tone becomes more vivid.

## Workflow

1. Identify the draft's one core point.
   - Keep only the material that serves that point.
   - If the draft has multiple points, choose the most coherent one unless the user asks for diagnosis.

2. Preserve fact boundaries.
   - Read `references/fact-safety.md`.
   - Treat all numbers, regulations, certifications, fire ratings, material density, install time, loading quantity, and market comparison as locked facts.
   - Rephrase them without changing their meaning.

3. Add口播 texture.
   - Read `references/oralization-patterns.md`.
   - Replace written transitions with spoken ones.
   - Break long sentences into camera-friendly beats.
   - Add light prompts such as "你想啊", "说白了", "问题就在这", "很多人会忽略一点" only when natural.

4. Control intensity.
   - B2B口播 can be sharp, but should not become vulgar, exaggerated, or fake outrage.
   - Use contrast, questions, and scenario logic instead of shouting.

5. Output only the rewritten script by default.
   - Preserve any existing `资料出处` footer from the source draft when the rewritten script still uses those facts.
   - Follow project `AGENTS.md`: no visible diagnosis or self-check unless the user asks.

## Style Targets

Aim for:

- Like an experienced Saudi project-side operator explaining the issue on camera.
- Short, speakable sentences.
- Clear turns: problem -> why it matters -> mechanism -> product/selection implication -> ending.
- More conversational than brochure copy, but still professional enough for B2B buyers.

Avoid:

- Pure直播带货 tone.
- Overusing "老板", "兄弟", "好家伙", "绝对", "妥妥的", "没得商量".
- Turning every sentence into an exclamation.
- Making unverified facts sound vivid and therefore "true".

## Reference Files

- `references/oralization-patterns.md`: practical口语化 rewrite patterns, before/after examples, and rhythm controls.
- `references/fact-safety.md`: fact-preservation rules and unsafe amplification examples.
