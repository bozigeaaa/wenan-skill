---
name: script-oralization-rewriter
description: Use when revising an existing Chinese short-video script, B2B口播稿, product script, Saudi engineering/camp script, or draft copy to make it more conversational, natural, punchy, and camera-ready while preserving verified facts and avoiding new unverified claims.
---

# Script Oralization Rewriter

## Purpose

Rewrite an existing Chinese script into natural spoken口播. Keep the business logic, single core point, and verified facts intact; improve rhythm, sentence length, transitions, and viewer-facing energy.

This is a post-processing skill. 所有完整口播稿都在事实与逻辑确认后默认经过本 Skill；用户提供已有稿并要求“更口语化”, “像真人说话”, “更像短视频口播”, “更有镜头感”, “别太书面”时，同样使用。

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
   - Reorder the verified information as `判断 → 原因 → 动作` when that is the clearest explanation path.

2. Preserve fact boundaries.
   - Read `references/fact-safety.md`.
   - Treat all numbers, regulations, certifications, fire ratings, material density, install time, loading quantity, and market comparison as locked facts.
   - Rephrase them without changing their meaning.

3. Add口播 texture.
   - Read `references/oralization-patterns.md`.
   - Replace written transitions with spoken ones.
   - Break long sentences into camera-friendly beats.
   - Add light prompts such as "你想啊", "说白了", "问题就在这", "很多人会忽略一点" only when natural.
   - Explain each fact or condition group once. Replace abstract written wording with concrete wording, but do not add a lay explanation for terms the B2B audience already understands.
   - Keep one main judgment or condition per sentence. Split a sentence only when that improves comprehension; do not increase the source draft's overall length.

4. Re-speak rather than decorate.
   - Reorder sentences or paragraphs when that makes the same point easier to say and hear.
   - Replace report-style explanation with a direct, viewer-facing explanation of the same verified judgment.
   - Do not treat fillers, catchphrases, or forced rhetorical questions as oralization.

5. Control intensity.
   - B2B口播 can be sharp, but should not become vulgar, exaggerated, or fake outrage.
   - Use contrast, questions, and scenario logic instead of shouting.

6. Run the professional B2B quality gate.
   - Read `.agents/skills/references/b2b-content-quality-gate.md`.
   - Read `.agents/skills/references/b2b-humanizer-expression-gate.md` and run its reinforced expression audit because the user explicitly requested an oralization rewrite.
   - Check the source draft and rewrite keep the same title question, decision value, mechanism, product implication, and ending.
   - Remove AI-sounding repetition, brochure slogans, mechanical lists, and abrupt sales turns only when doing so does not remove or alter a verified fact.
   - Do not use a more vivid hook, emotional pressure, or conversational phrasing to intensify a locked fact or imply an unsupported consequence.
   - Compare the rewrite with the source before output: keep every material conclusion, condition, comparison, cause, scope, company boundary, and source footer semantically unchanged. If a sentence cannot be made more spoken without changing meaning, keep the source sentence.
   - The Humanizer pass keeps its role of removing AI tone, making the copy natural, and adjusting expression. It may adjust word order, paragraphing, pauses, and rhythm, but must not add explanations, ineffective transitions, or new sentences; it must not make the script longer, more circuitous, or disrupt the clear information order established above.

7. Output only the rewritten script by default.
   - Preserve any existing `资料出处` footer from the source draft when the rewritten script still uses those facts.
   - Follow project `AGENTS.md`: no visible diagnosis or self-check unless the user asks.

## Style Targets

Aim for:

- Like an experienced Saudi project-side operator explaining the issue on camera.
- Short, speakable sentences.
- Use the evidence-led flow that best fits the topic; do not impose a fixed body order.
- More conversational than brochure copy, but still professional enough for B2B buyers.

Avoid:

- Pure直播带货 tone.
- Overusing "老板", "兄弟", "好家伙", "绝对", "妥妥的", "没得商量".
- Turning every sentence into an exclamation.
- Making unverified facts sound vivid and therefore "true".

## Reference Files

- `references/oralization-patterns.md`: practical口语化 rewrite patterns, before/after examples, and rhythm controls.
- `references/fact-safety.md`: fact-preservation rules and unsafe amplification examples.
- `.agents/skills/references/b2b-content-quality-gate.md`: shared title, B2B decision-value, logic-flow, and publishing-risk gate.
- `.agents/skills/references/b2b-humanizer-expression-gate.md`: shared final expression audit for AI-writing patterns and spoken rhythm.
