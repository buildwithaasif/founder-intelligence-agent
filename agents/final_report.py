def generate_final_report(
    startup_idea: str = "",
    assumptions: dict = None,
    evidence: dict = None,
    validation: dict = None,
    recommendation: dict = None,
    opportunity_score: dict = None,
    customer_discovery_data: dict = None,
    founder_fit: dict = None,
    interview_questions: str = "",
) -> str:
    # Safe getters
    rec = recommendation or {}
    score = opportunity_score or {}
    cust = customer_discovery_data or {}
    fit = founder_fit or {}

    decision = rec.get("decision", "UNKNOWN")
    overall = score.get("overall_score", "N/A")
    verdict_emoji = {"BUILD": "🟢", "PIVOT": "🟡", "ABANDON": "🔴", "MAYBE": "🟡"}.get(decision, "⚪")

    # ── Split assumptions by verdict ──
    supported = []
    rejected = []
    partial = []
    unclear = []
    
    if evidence:
        for item in evidence.get("assumptions", []):
            v = item.get("verdict", "UNCLEAR")
            if v == "SUPPORTED":
                supported.append(item.get("assumption", ""))
            elif v == "REJECTED":
                rejected.append(item.get("assumption", ""))
            elif v == "PARTIALLY SUPPORTED":
                partial.append(item.get("assumption", ""))
            else:
                unclear.append(item.get("assumption", ""))

    # ── Key insights ──
    evidence_overall = evidence.get("overall", {}) if evidence else {}
    blind_spot = evidence_overall.get("biggest_blind_spot", "")
    most_validated = evidence_overall.get("most_validated", "")
    revised = evidence_overall.get("revised_direction", "")

    # ── Best action ──
    angle = rec.get("best_startup_angle", "")
    mvp = rec.get("first_mvp", "")
    next_steps = rec.get("next_30_days", [])
    risk = rec.get("biggest_risk", "")
    pricing = rec.get("pricing_strategy", "")

    # ── YC Advice (shortened) ──
    yc_advice = rec.get("yc_advice", [])
    top_advice = yc_advice[:3] if len(yc_advice) > 3 else yc_advice

    # ── Validation summary ──
    val_summary = validation.get("summary", {}) if validation else {}
    first_task = val_summary.get("recommended_first_task", "")
    est_time = val_summary.get("estimated_total_time", "")

    # ── ICP ──
    icp = cust.get("icp", "")
    biggest_pain = cust.get("biggest_pain", "")

    # ── Founder summary ──
    fit_summary = fit.get("summary", "")
    cofounder_rec = fit.get("co_founder_recommendation", "")
    solo = fit.get("solo_viability", "")

    # ── Build sections ──

    # WHAT'S WRONG section
    wrong_items = []
    for r in rejected:
        wrong_items.append(f"❌ {r[:120]}...")
    for p in partial:
        wrong_items.append(f"⚠️ {p[:120]}...")
    for u in unclear:
        wrong_items.append(f"❓ {u[:120]}...")
    if not wrong_items:
        wrong_items.append("✅ No critical issues found")
    wrong_str = "\n".join(wrong_items)

    # WHAT'S RIGHT section
    right_items = []
    for s in supported:
        right_items.append(f"✅ {s[:120]}...")
    if not right_items:
        right_items.append("Nothing strongly validated yet — test your assumptions")
    right_str = "\n".join(right_items)

    # NEXT STEPS section
    steps_str = ""
    for i, step in enumerate(next_steps[:3], 1):
        steps_str += f"\n  {i}. {step}"
    if not steps_str:
        steps_str = "\n  1. Talk to 10 potential customers before building anything"

    # YC ADVICE section
    advice_str = ""
    for advice in top_advice:
        short = advice[:150] + "..." if len(advice) > 150 else advice
        advice_str += f"\n  💬 \"{short}\""

    # INTERVIEW QUESTIONS — first question only
    first_question = ""
    if interview_questions:
        lines = interview_questions.split("\n")
        for line in lines:
            stripped = line.strip()
            if stripped and (stripped.startswith("1.") or stripped.startswith("1 ")):
                first_question = stripped
                break

    # ── Build the report ──
    report = f"""
╔══════════════════════════════════════════════╗
║        🚀 STARTUP INTELLIGENCE REPORT        ║
║                                              ║
║   {startup_idea[:45]}
║                                              ║
╚══════════════════════════════════════════════╝

  {verdict_emoji} VERDICT: {decision}   │   Score: {overall}/100

  {revised[:180]}

────────────────────────────────────────────
🔴 WHAT'S WRONG
────────────────────────────────────────────
{wrong_str}

────────────────────────────────────────────
🟢 WHAT'S RIGHT  
────────────────────────────────────────────
{right_str}

────────────────────────────────────────────
🎯 YOUR PIVOT
────────────────────────────────────────────
  {angle}

  First MVP: {mvp[:150]}

────────────────────────────────────────────
📋 NEXT 7 DAYS
────────────────────────────────────────────{steps_str}

────────────────────────────────────────────
⚠️ BIGGEST RISK
────────────────────────────────────────────
  {risk[:180]}

────────────────────────────────────────────
👤 FOUNDER REALITY CHECK
────────────────────────────────────────────
  {fit_summary[:200]}

  Co-founder need: {cofounder_rec[:150]}
  Solo viability: {solo}

────────────────────────────────────────────
💡 WHAT YC WOULD SAY
────────────────────────────────────────────{advice_str}

────────────────────────────────────────────
🎤 FIRST CUSTOMER QUESTION
────────────────────────────────────────────
  "{first_question}"

  (Full 20-question interview script below)

────────────────────────────────────────────
⏱️ VALIDATION PLAN
────────────────────────────────────────────
  Time needed: {est_time}
  Start with: {first_task[:180]}

────────────────────────────────────────────
👥 IDEAL CUSTOMER
────────────────────────────────────────────
  {icp}
  Core pain: {biggest_pain}

────────────────────────────────────────────
💰 PRICING MODEL
────────────────────────────────────────────
  {pricing}

────────────────────────────────────────────
📝 FULL INTERVIEW SCRIPT
────────────────────────────────────────────

{interview_questions if interview_questions else "No interview questions generated."}

══════════════════════════════════════════════
  Founder Intelligence Agent · v2
══════════════════════════════════════════════
"""

    return report