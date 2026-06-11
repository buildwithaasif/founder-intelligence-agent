import sys
sys.path.insert(0, '.')

from agents.startup_recommendation import recommend_startup

print("Testing YC Advice section...\n")

result = recommend_startup(
    startup_idea="Uber for dog walking",
    founder_profile="MERN Stack Developer, OSCP Certified, learning AI",
    competitors=["Rover", "Wag", "Excel spreadsheets"],
    pain_points={"pain_points": ["expensive", "unreliable"], "problems": [], "market_gaps": []},
    founder_fit={"technical_fit": 80, "domain_fit": 40, "summary": "Can build but doesn't know market"},
    opportunity_score={"overall_score": 55, "verdict": "MAYBE"},
)

# Check for yc_advice field
print("=" * 50)
if "yc_advice" in result:
    print(f"✅ yc_advice field found ({len(result['yc_advice'])} advice points)")
    for i, advice in enumerate(result['yc_advice'], 1):
        print(f"  {i}. {advice}")
else:
    print("❌ yc_advice field MISSING")

# Validate
checks = [
    ("Has yc_advice key", "yc_advice" in result),
    ("At least 3 advice points", len(result.get("yc_advice", [])) >= 3),
    ("Advice points are strings", all(isinstance(a, str) for a in result.get("yc_advice", []))),
]

print("\nVALIDATION:")
for name, passed in checks:
    print(f"{'✅' if passed else '❌'} {name}")
