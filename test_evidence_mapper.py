import sys
sys.path.insert(0, '.')

from agents.evidence_mapper import map_evidence

print("Testing evidence_mapper.py...\n")

# Fake assumptions (matching the format from assumptions.py)
assumptions = {
    "assumptions": [
        {
            "assumption": "Founders spend significant time on manual market research and would use an automated tool",
            "category": "problem",
            "confidence": "high"
        },
        {
            "assumption": "No existing tool effectively solves this problem",
            "category": "competition",
            "confidence": "medium"
        },
        {
            "assumption": "Founders will pay a monthly subscription for market research automation",
            "category": "customer",
            "confidence": "medium"
        },
        {
            "assumption": "An AI agent can generate trustworthy, accurate market research",
            "category": "solution",
            "confidence": "medium"
        },
        {
            "assumption": "The founder's security background is relevant to customers",
            "category": "founder",
            "confidence": "low"
        }
    ]
}

# Fake competitors
competitors = {
    "direct": ["CB Insights", "Crunchbase", "Gartner"],
    "indirect": ["Manual Google searches", "Hiring analysts"],
    "adjacent": ["ChatGPT market research prompts"],
    "potential": ["PitchBook expanding into AI"]
}

# Fake pain points
pain_points = {
    "pain_points": [
        "Market research takes 10+ hours per week",
        "Existing tools are too expensive for early-stage founders",
        "Generic AI tools hallucinate market data"
    ],
    "problems": [
        "CB Insights costs $40K+/year",
        "No tool combines competitor data with actionable recommendations"
    ],
    "market_gaps": [
        "No affordable market research tool for pre-seed founders",
        "No AI tool that cites sources for every claim"
    ]
}

# Fake search results
search_results = [
    {
        "title": "Founders waste 40% of time on research - IndieHackers",
        "body": "Multiple founders report spending 15-20 hours weekly on manual competitor research and market validation."
    },
    {
        "title": "Best Market Research Tools 2026 - G2 Reviews",
        "body": "CB Insights, Crunchbase, and PitchBook dominate but pricing starts at $12K/year, inaccessible for early-stage startups."
    },
    {
        "title": "AI market research tools are inaccurate - Reddit r/startups",
        "body": "Founders discuss how ChatGPT and generic AI tools make up market statistics. Trust is a major issue."
    },
    {
        "title": "Why we switched from manual research to automated tools - Medium",
        "body": "A founder describes cutting research time from 15 hours to 2 hours using a combination of tools, but still spends $500/month."
    }
]

result = map_evidence(
    assumptions=assumptions,
    competitors=competitors,
    pain_points=pain_points,
    search_results=search_results,
)

print("=" * 60)
print("EVIDENCE MAPPING RESULTS:")
print("=" * 60)
import json
print(json.dumps(result, indent=2))

# Validate
print("\nVALIDATION:")
checks = [
    ("Has assumptions list", "assumptions" in result),
    ("Has overall summary", "overall" in result),
    ("Each assumption has verdict", all("verdict" in a for a in result.get("assumptions", []))),
    ("Valid verdicts", all(a.get("verdict") in ["SUPPORTED", "REJECTED", "PARTIALLY SUPPORTED", "UNCLEAR"] for a in result.get("assumptions", []))),
    ("Overall has supported_count", "supported_count" in result.get("overall", {})),
    ("Overall has rejected_count", "rejected_count" in result.get("overall", {})),
    ("Overall has biggest_blind_spot", "biggest_blind_spot" in result.get("overall", {})),
    ("Overall has most_validated", "most_validated" in result.get("overall", {})),
    ("Overall has revised_direction", "revised_direction" in result.get("overall", {})),
]

for name, passed in checks:
    print(f"{'✅' if passed else '❌'} {name}")

# Summary
overall = result.get("overall", {})
print(f"\n📊 SUMMARY:")
print(f"   Total assumptions: {overall.get('total_assumptions')}")
print(f"   Supported: {overall.get('supported_count')}")
print(f"   Rejected: {overall.get('rejected_count')}")
print(f"   Partial: {overall.get('partial_count')}")
print(f"   Unclear: {overall.get('unclear_count')}")
print(f"   Biggest blind spot: {overall.get('biggest_blind_spot')}")
print(f"   Revised direction: {overall.get('revised_direction')}")
