from agents.final_report import generate_final_report

recommendation = {
    "decision": "PIVOT",
    "best_startup_angle": "AI Security & Compliance Audit Agent for Tech Founders",
    "first_mvp": "Dashboard where founders paste AI stack URLs to get automated security reports",
    "why_this_wins": ["Leverages OSCP/CPTS", "High-stakes niche"],
    "pricing_strategy": "$79-$299/mo based on scan frequency",
    "biggest_risk": "Competing on features instead of owning the security wedge",
    "next_30_days": [
        "Interview 15 technical founders about AI security blind spots",
        "Build script monitoring GitHub for exposed API keys",
        "Launch waitlist with free AI Security Health Score report"
    ],
    "red_flags": ["Commodity market", "No GTM path"],
    "red_flag_analysis": "Crowded market with weak differentiation",
    "yc_advice": [
        "Your OSCP and CPTS credentials give you instant credibility — own the security niche.",
        "Do things that don't scale: hand-deliver security audits to ten founders.",
        "Your execution speed is an asset, but without a GTM co-founder it helps you fail faster.",
        "Counterintuitively, pivot away from general market research into AI security."
    ]
}

opportunity_score = {"overall_score": 48, "verdict": "MAYBE"}

evidence = {
    "assumptions": [
        {"assumption": "Founders want automated market research", "verdict": "SUPPORTED"},
        {"assumption": "AI can reliably synthesize market data", "verdict": "PARTIALLY SUPPORTED"},
        {"assumption": "Founders will pay monthly subscriptions", "verdict": "REJECTED"},
        {"assumption": "Founder's security background matters", "verdict": "UNCLEAR"},
    ],
    "overall": {
        "biggest_blind_spot": "Founders won't pay subscriptions — rejected by DIY tool evidence",
        "most_validated": "Real pain exists — research takes 10+ hrs/week",
        "revised_direction": "Shift to usage-based pricing and security niche to overcome DIY competition"
    }
}

validation = {
    "summary": {
        "estimated_total_time": "2-3 weeks",
        "recommended_first_task": "Concierge offer: deliver reports for $49 to test willingness to pay"
    }
}

customer_discovery_data = {
    "icp": "Technical founders building AI-native B2B SaaS",
    "biggest_pain": "Fear of AI liability, prompt injection, data leakage"
}

founder_fit = {
    "summary": "Technically capable but lacks B2B GTM. Pair with sales co-founder.",
    "co_founder_recommendation": "GTM co-founder with B2B SaaS sales experience",
    "solo_viability": "no"
}

interview_questions = """
## Customer Interview Questions
1. Walk me through how you currently monitor AI workflows for security issues.
2. When did you last experience a prompt injection or data leakage incident?
3. What would you pay to automate this monitoring?
"""

print("Testing redesigned final_report.py...\n")

report = generate_final_report(
    startup_idea="market research agent for founders",
    assumptions=None,
    evidence=evidence,
    validation=validation,
    recommendation=recommendation,
    opportunity_score=opportunity_score,
    customer_discovery_data=customer_discovery_data,
    founder_fit=founder_fit,
    interview_questions=interview_questions,
)

print(report)

# Quick checks
checks = [
    ("Verdict at top", "VERDICT: PIVOT" in report),
    ("Wrong section", "WHAT'S WRONG" in report),
    ("Right section", "WHAT'S RIGHT" in report),
    ("Rejected item shown", "Founders will pay monthly" in report),
    ("Supported item shown", "Founders want automated" in report),
    ("YC advice section", "WHAT YC WOULD SAY" in report),
    ("First question shown", "Walk me through" in report),
    ("Validation plan", "VALIDATION PLAN" in report),
    ("Ideal customer", "IDEAL CUSTOMER" in report),
    ("Pricing section", "PRICING MODEL" in report),
    ("Not too long", len(report) < 5000),
]

print("\nVALIDATION:")
for name, passed in checks:
    print(f"{'✅' if passed else '❌'} {name}")
