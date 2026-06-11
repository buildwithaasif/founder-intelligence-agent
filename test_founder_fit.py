import sys
sys.path.insert(0, '.')

from agents.founder_fit import analyze_founder_fit

print("Testing founder_fit.py with gap analysis...\n")

# Test 1: Founder with clear gaps
print("=" * 50)
print("TEST 1: Technical founder, non-technical idea")
print("=" * 50)

result = analyze_founder_fit(
    startup_idea="AI-powered fitness coaching app for enterprises",
    competitors={
        "direct": ["Fitbit Coach", "Peloton Corporate"],
        "indirect": ["Personal trainers", "Excel workout plans"],
        "adjacent": [],
        "potential": []
    },
    pain_points={"pain_points": ["expensive", "low engagement"], "problems": [], "market_gaps": []},
    founder_profile="""
    - MERN Stack Developer
    - OSCP Certified
    - Learning AI Engineering
    - Interested in AI Security
    - No fitness industry experience
    - No B2B sales experience
    """,
)

import json
print(json.dumps(result, indent=2))

# Validate new fields
print("\nVALIDATION:")
checks = [
    ("missing_skills", "missing_skills" in result),
    ("co_founder_recommendation", "co_founder_recommendation" in result),
    ("solo_viability", "solo_viability" in result),
    ("solo_viability_reason", "solo_viability_reason" in result),
    ("missing_skills is list", isinstance(result.get("missing_skills"), list)),
    ("solo_viability is yes/maybe/no", result.get("solo_viability") in ["yes", "maybe", "no"]),
]

for name, passed in checks:
    print(f"{'✅' if passed else '❌'} {name}")

# Test 2: Founder with domain expertise
print("\n" + "=" * 50)
print("TEST 2: Founder with domain expertise")
print("=" * 50)

result2 = analyze_founder_fit(
    startup_idea="penetration testing automation platform",
    competitors={"direct": ["Burp Suite"], "indirect": ["Manual pentesting"], "adjacent": [], "potential": []},
    pain_points={"pain_points": ["slow", "expensive"], "problems": [], "market_gaps": []},
    founder_profile="""
    - OSCP Certified
    - CPTS Certified
    - MERN Stack Developer
    - Strong offensive security background
    - Learning AI Engineering
    """,
)

print(json.dumps(result2, indent=2))
print(f"\nTechnical fit: {result2.get('technical_fit')} (should be high for a security founder)")
print(f"Domain fit: {result2.get('domain_fit')} (should be high for a security idea)")
print(f"Solo viability: {result2.get('solo_viability')}")

print("\n" + "=" * 50)
print("ALL TESTS COMPLETE")
print("=" * 50)
