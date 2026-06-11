import sys
sys.path.insert(0, '.')

from agents.startup_recommendation import recommend_startup

# Fake data to test with
startup_idea = "Uber for dog walking"
founder_profile = "MERN Stack Developer, learning AI"
competitors = ["Rover", "Wag"]
pain_points = {"pain_points": ["expensive", "unreliable walkers"], "problems": [], "market_gaps": []}
founder_fit = {"technical_fit": 80, "domain_fit": 40, "summary": "Can build but doesn't know the market"}
opportunity_score = {"overall_score": 55, "verdict": "MAYBE"}

print("Testing startup_recommendation.py...\n")
print(f"Idea: {startup_idea}\n")

result = recommend_startup(
    startup_idea=startup_idea,
    founder_profile=founder_profile,
    competitors=competitors,
    pain_points=pain_points,
    founder_fit=founder_fit,
    opportunity_score=opportunity_score,
)

print("=" * 50)
print("RESULT:")
print("=" * 50)
import json
print(json.dumps(result, indent=2))
