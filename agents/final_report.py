def generate_final_report(
    recommendation: dict,
    opportunity_score: dict,
    customer_discovery_data: dict,
    founder_fit: dict,
    interview_questions: str = "",
) -> str:
    # Safe getters with defaults
    decision = recommendation.get("decision", "UNKNOWN")
    overall = opportunity_score.get("overall_score", "N/A")
    angle = recommendation.get("best_startup_angle", "N/A")
    why = recommendation.get("why_this_wins", [])
    mvp = recommendation.get("first_mvp", "N/A")
    icp = customer_discovery_data.get("icp", "N/A")
    pain = customer_discovery_data.get("biggest_pain", "N/A")
    pricing = recommendation.get("pricing_strategy", "N/A")
    fit_summary = founder_fit.get("summary", "N/A")
    risk = recommendation.get("biggest_risk", "N/A")
    next_steps = recommendation.get("next_30_days", [])

    # Red flag fields
    red_flags = recommendation.get("red_flags", [])
    red_flag_analysis = recommendation.get("red_flag_analysis", "")

    # YC Advice
    yc_advice = recommendation.get("yc_advice", [])

    # Format lists
    why_str = "\n".join(f"- {w}" for w in why) if why else "- N/A"
    steps_str = "\n".join(f"- {s}" for s in next_steps) if next_steps else "- N/A"

    # Format red flags
    if red_flags:
        flags_str = "\n".join(f"🚩 {flag}" for flag in red_flags)
    else:
        flags_str = "✅ No red flags detected"

    # Format YC advice
    if yc_advice:
        advice_str = "\n".join(f"💬 *\"{advice}\"*" for advice in yc_advice)
    else:
        advice_str = "No specific advice generated."

    report = f"""
=============================================
       STARTUP INTELLIGENCE REPORT
=============================================

DECISION: {decision}

OPPORTUNITY SCORE: {overall}/100

=============================================
              RED FLAG SCAN
=============================================
{flags_str}

{red_flag_analysis}

-------------------------------------------------
BEST STARTUP ANGLE:
{angle}

WHY THIS WINS:
{why_str}

MVP:
{mvp}

TARGET USERS (ICP):
{icp}

PAIN POINT:
{pain}

PRICING STRATEGY:
{pricing}

FOUNDER FIT:
{fit_summary}

BIGGEST RISK:
{risk}

NEXT 30 DAYS:
{steps_str}
-------------------------------------------------

=============================================
       WHAT YC WOULD TELL YOU
=============================================

{advice_str}

=============================================
       CUSTOMER INTERVIEW QUESTIONS
=============================================

{interview_questions if interview_questions else "No interview questions generated."}

=============================================
"""

    return report