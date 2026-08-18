from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
TITLE_RULES = PROJECT_ROOT / ".agents/skills/global-hotspot-industry-impact-script/references/title-selection.md"
BRAND_RULES = PROJECT_ROOT / ".agents/skills/saudi-brand-proof-script/references/fact-rules.md"
HOTSPOT_SKILL = PROJECT_ROOT / ".agents/skills/global-hotspot-industry-impact-script/SKILL.md"
BRAND_SKILL = PROJECT_ROOT / ".agents/skills/saudi-brand-proof-script/SKILL.md"
SHARED_RULES = PROJECT_ROOT / ".agents/skills/references/local-manufacturing-delivery-proof.md"
HOTSPOT_LEDGER_RULES = PROJECT_ROOT / ".agents/skills/global-hotspot-industry-impact-script/references/hotspot-ledger.md"
HOTSPOT_LEDGER = PROJECT_ROOT / "content-state/hotspot-ledger.json"
CLAIM_LEDGER = PROJECT_ROOT / "content-state/company-claim-evidence-ledger.json"
CLAIM_LEDGER_GUIDE = PROJECT_ROOT / ".agents/skills/references/company-claim-evidence-ledger.md"
HOTSPOT_SOURCING = PROJECT_ROOT / ".agents/skills/global-hotspot-industry-impact-script/references/hotspot-sourcing.md"
TOPIC_LOOP_RULES = PROJECT_ROOT / ".agents/skills/references/b2b-topic-conversion-loop.md"
KNOWLEDGE_SKILL = PROJECT_ROOT / ".agents/skills/saudi-professional-knowledge-script/SKILL.md"
WENAN_ROUTER = PROJECT_ROOT / ".agents/skills/wenan-skill/SKILL.md"
WENAN_ROUTER_UI = PROJECT_ROOT / ".agents/skills/wenan-skill/agents/openai.yaml"
PROJECT_RULES = PROJECT_ROOT / "AGENTS.md"
QUALITY_GATE = PROJECT_ROOT / ".agents/skills/references/b2b-content-quality-gate.md"
HANDOFF_DOCUMENT = PROJECT_ROOT / "docs/wenan-skill-完整交接文档_2026-08-14.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def assert_contains(content: str, expected: str, name: str) -> None:
    assert expected in content, f"Missing {name}: {expected}"


def test_local_delivery_differentiation_rules_are_connected() -> None:
    assert SHARED_RULES.exists(), "Missing shared local-delivery rule file"

    title_content = read(TITLE_RULES)
    brand_content = read(BRAND_RULES)
    hotspot_skill = read(HOTSPOT_SKILL)
    brand_skill = read(BRAND_SKILL)
    shared_content = read(SHARED_RULES)

    assert_contains(title_content, "本地交付能力", "hotspot local-delivery title trigger")
    assert_contains(title_content, "跨境采购", "cross-border exception")
    assert_contains(shared_content, "生产主体", "production check")
    assert_contains(shared_content, "常规品备货", "stock check")
    assert_contains(shared_content, "配件供应", "parts check")
    assert_contains(shared_content, "配送、安装与验收", "fulfilment check")
    assert_contains(shared_content, "后续变更和维护", "continuity check")
    assert_contains(shared_content, "二道贩子", "competitor boundary")
    assert_contains(brand_content, "稳定能力", "stable-fact classification")
    assert_contains(brand_content, "实时项目变量", "variable-fact classification")
    assert_contains(hotspot_skill, "local-manufacturing-delivery-proof.md", "hotspot rule connection")
    assert_contains(brand_skill, "local-manufacturing-delivery-proof.md", "brand rule connection")


def test_hotspot_workflow_uses_a_persistent_ledger_and_downgrade_rules() -> None:
    assert HOTSPOT_LEDGER_RULES.exists(), "Missing hotspot ledger rules"
    assert HOTSPOT_LEDGER.exists(), "Missing persistent hotspot ledger"

    hotspot_skill = read(HOTSPOT_SKILL)
    ledger_rules = read(HOTSPOT_LEDGER_RULES)
    ledger = read(HOTSPOT_LEDGER)

    assert_contains(hotspot_skill, "hotspot-ledger.md", "hotspot ledger rule connection")
    assert_contains(hotspot_skill, "hotspot-ledger.json", "persistent ledger connection")
    assert_contains(ledger_rules, "search 只负责发现候选", "search discovery boundary")
    assert_contains(ledger_rules, "scrape/打开原文", "source verification boundary")
    assert_contains(ledger_rules, "0-7 天", "strong-hotspot window")
    assert_contains(ledger_rules, "8-30 天", "ongoing-hotspot window")
    assert_contains(ledger_rules, "超过 30 天", "evergreen downgrade window")
    assert_contains(ledger_rules, "项目/政策/物流信号", "project-signal downgrade")
    assert_contains(ledger_rules, "常青决策库", "evergreen downgrade")
    assert_contains(ledger_rules, "monitor", "monitor boundary")
    assert_contains(ledger, '"schema_version": 1', "ledger schema version")
    assert_contains(ledger, '"events": [', "events collection")
    assert_contains(ledger, '"event_id": "mawani-jeddah-logistics-centres-2026-07-18"', "recent logistics signal")
    assert_contains(ledger, '"event_id": "jazan-seawater-cooling-2026-07-14"', "recent project signal")
    assert_contains(ledger, '"event_id": "mawani-shipping-services-2026-03-22"', "downgraded background event")
    assert_contains(ledger, '"source_level": "A"', "primary source level")
    assert_contains(ledger, '"write_eligibility": "eligible"', "eligible signal status")
    assert_contains(ledger, '"write_eligibility": "downgraded"', "downgraded status")


def test_company_claims_are_bound_to_sources_and_confirmation_boundaries() -> None:
    assert CLAIM_LEDGER.exists(), "Missing company claim evidence ledger"
    assert CLAIM_LEDGER_GUIDE.exists(), "Missing company claim ledger guide"

    ledger = read(CLAIM_LEDGER)
    guide = read(CLAIM_LEDGER_GUIDE)
    brand_skill = read(BRAND_SKILL)

    assert_contains(ledger, '"claim_id": "EC-001"', "company identity claim")
    assert_contains(ledger, '"claim_id": "EC-003"', "local manufacturing claim")
    assert_contains(ledger, '"claim_id": "EC-005"', "stock boundary claim")
    assert_contains(ledger, '"claim_id": "EC-007"', "capacity review claim")
    assert_contains(ledger, '"requires_project_confirmation": true', "project-confirmation boundary")
    assert_contains(ledger, '"requires_periodic_review": true', "periodic-review boundary")
    assert_contains(guide, "原始资料", "source requirement")
    assert_contains(guide, "不得延伸", "claim boundary")
    assert_contains(brand_skill, "company-claim-evidence-ledger", "brand skill ledger connection")


def test_hotspot_sources_are_dynamic_and_ranked_by_evidence_role() -> None:
    sourcing = read(HOTSPOT_SOURCING)

    assert_contains(sourcing, "A 级：事实核验源", "primary-source tier")
    assert_contains(sourcing, "B 级：交叉核验源", "wire-service tier")
    assert_contains(sourcing, "C 级：线索发现源", "discovery tier")
    assert_contains(sourcing, "不是唯一来源", "non-exclusive source boundary")
    assert_contains(sourcing, "按主题选源", "topic-to-source routing")
    assert_contains(sourcing, "新来源准入", "new-source admission")
    assert_contains(sourcing, "Mawani", "port source example")
    assert_contains(sourcing, "Reuters", "wire-service example")
    assert_contains(sourcing, "不能单独作为关键事实依据", "lead-source boundary")


def test_construction_news_feeds_a_topic_to_script_loop() -> None:
    assert TOPIC_LOOP_RULES.exists(), "Missing topic-to-script loop rules"

    sourcing = read(HOTSPOT_SOURCING)
    ledger_rules = read(HOTSPOT_LEDGER_RULES)
    hotspot_skill = read(HOTSPOT_SKILL)
    knowledge_skill = read(KNOWLEDGE_SKILL)
    loop_rules = read(TOPIC_LOOP_RULES)

    assert_contains(sourcing, "城市开发与基础设施", "construction-news candidate class")
    assert_contains(sourcing, "招标、预资格、授标、开工、施工进度", "project-action search terms")
    assert_contains(sourcing, "施工营地、临时设施、现场办公", "site-support search terms")
    assert_contains(ledger_rules, "项目阶段", "project-stage classification")
    assert_contains(ledger_rules, "临建关联判断", "temporary-facility relevance gate")
    assert_contains(ledger_rules, "项目/政策/物流信号稿", "signal-script routing")
    assert_contains(ledger_rules, "账号类型", "account routing record")
    assert_contains(ledger_rules, "发布后复盘", "post-publication review record")
    assert_contains(loop_rules, "科普账号", "education-account route")
    assert_contains(loop_rules, "营销账号", "marketing-account route")
    assert_contains(loop_rules, "品牌证据桥", "evidence-bridge rule")
    assert_contains(loop_rules, "不自然相关", "no forced product link boundary")
    assert_contains(hotspot_skill, "b2b-topic-conversion-loop.md", "hotspot loop connection")
    assert_contains(knowledge_skill, "b2b-topic-conversion-loop.md", "knowledge loop connection")


def test_wenan_skill_is_the_single_entry_router() -> None:
    assert WENAN_ROUTER.exists(), "Missing wenan-skill entry router"
    assert WENAN_ROUTER_UI.exists(), "Missing wenan-skill UI metadata"

    router = read(WENAN_ROUTER)
    router_ui = read(WENAN_ROUTER_UI)

    assert_contains(router, "name: wenan-skill", "router skill name")
    assert_contains(router, "$global-hotspot-industry-impact-script", "news route")
    assert_contains(router, "$saudi-professional-knowledge-script", "knowledge route")
    assert_contains(router, "$saudi-product-seeding-script", "product route")
    assert_contains(router, "$saudi-brand-proof-script", "brand route")
    assert_contains(router, "$script-oralization-rewriter", "rewrite route")
    assert_contains(router, "AGENTS.md", "project-rule entry")
    assert_contains(router, "AI资料导航索引.md", "knowledge-base entry")
    assert_contains(router, "不要要求用户记忆专项 Skill 名称", "single-entry boundary")
    assert_contains(router_ui, "文案 Skill", "router display name")


def test_title_handoff_value_brand_and_evidence_rules_are_connected() -> None:
    project_rules = read(PROJECT_RULES)
    router = read(WENAN_ROUTER)
    quality_gate = read(QUALITY_GATE)
    topic_loop = read(TOPIC_LOOP_RULES)

    assert_contains(router, "只生成标题候选", "title-only workflow")
    assert_contains(router, "标题交接单", "selected-title handoff")
    assert_contains(quality_gate, "低认知负荷", "low-cognitive-load gate")
    assert_contains(quality_gate, "可直接使用的判断", "immediate viewer value")
    assert_contains(topic_loop, "主题与公司业务直接相关", "company-relevance decision")
    assert_contains(topic_loop, "不强行提及公司", "no-forced-brand boundary")
    assert_contains(project_rules, "无证据，不成稿", "evidence-first rule")


def test_title_handoff_requires_a_non_basic_decision_insight_and_adaptive_structure() -> None:
    project_rules = read(PROJECT_RULES)
    router = read(WENAN_ROUTER)
    quality_gate = read(QUALITY_GATE)
    handoff = read(HANDOFF_DOCUMENT)

    assert_contains(project_rules, "受众已知的基础常识", "audience knowledge floor")
    assert_contains(project_rules, "决策张力", "decision tension")
    assert_contains(router, "non-basic conclusion", "non-basic title insight")
    assert_contains(quality_gate, "信息关系", "evidence-led structure selection")
    assert_contains(quality_gate, "最近两条", "recent-structure repetition guard")
    assert_contains(handoff, "受众已知的基础常识", "handoff knowledge floor")


def test_handoff_document_keeps_the_copy_ready_title_prompt_contract() -> None:
    handoff = read(HANDOFF_DOCUMENT)

    assert_contains(handoff, "主题（可留空）", "blank-topic input")
    assert_contains(handoff, "本条要让观众更新的判断", "title candidate insight output")
    assert_contains(handoff, "我选第 X 个", "selected-title command")


def test_current_handoff_document_is_available_from_the_single_entry() -> None:
    router = read(WENAN_ROUTER)

    assert HANDOFF_DOCUMENT.exists(), "Missing current handoff document"
    handoff = read(HANDOFF_DOCUMENT)

    assert_contains(router, "docs/wenan-skill-完整交接文档_2026-08-14.md", "current handoff entry")
    assert_contains(handoff, "标题交接单", "title handoff in current handoff document")
    assert_contains(handoff, "低认知负荷", "viewer-value rule in current handoff document")
    assert_contains(handoff, "无证据，不成稿", "evidence rule in current handoff document")
