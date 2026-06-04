def calculate_opportunity_score(
    startup_idea: str,
    competitors: list,
    pain_points: list,
    founder_profile: str,
):
    competitor_count = len(competitors)
    pain_count = len(pain_points)

    # Simple rule-based scoring (no LLM needed here)
    market_opportunity = min(100, pain_count * 10)

    competition_score = max(0, 100 - competitor_count * 5)

    founder_fit = 70  # fixed baseline for now (we will improve later)

    timing = 80  # fixed baseline (we improve later in next steps)

    overall_score = int(
        (market_opportunity + competition_score + founder_fit + timing) / 4
    )

    if overall_score >= 75:
        verdict = "BUILD"
    elif overall_score >= 50:
        verdict = "MAYBE"
    else:
        verdict = "AVOID"

    return {
        "market_opportunity": market_opportunity,
        "founder_fit": founder_fit,
        "competition": competition_score,
        "timing": timing,
        "overall_score": overall_score,
        "verdict": verdict,
    }