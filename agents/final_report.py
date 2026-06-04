def generate_final_report(
    recommendation,
    opportunity_score,
    customer_discovery,
    founder_fit,
):
    return f"""
=============================
STARTUP INTELLIGENCE REPORT
=============================

DECISION: {recommendation["decision"]}

OPPORTUNITY SCORE: {opportunity_score["overall_score"]}

BEST STARTUP ANGLE:
{recommendation["best_startup_angle"]}

WHY THIS WORKS:
{recommendation["why_this_wins"]}

MVP:
{recommendation["first_mvp"]}

TARGET USERS:
{customer_discovery["icp"]}

PAIN POINT:
{customer_discovery["biggest_pain"]}

PRICING:
{recommendation["pricing_strategy"]}

FOUNDER FIT:
{founder_fit["summary"]}

BIGGEST RISK:
{recommendation["biggest_risk"]}

NEXT 30 DAYS:
{recommendation["next_30_days"]}

=============================
"""
