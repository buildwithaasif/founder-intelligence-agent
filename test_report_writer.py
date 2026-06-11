import sys
sys.path.insert(0, '.')

from tools.report_writer import save_report

print("Testing report_writer.py...\n")

competitors = {
    "direct": ["Rover", "Wag!"],
    "indirect": ["Excel spreadsheets", "Pen and paper"],
    "adjacent": ["Google Maps"],
    "potential": ["Petco Wellness App"]
}

pain_points = {
    "pain_points": ["Scheduling takes 5+ hours/week", "Double bookings cost money"],
    "problems": ["Existing apps are expensive", "No route optimization"],
    "market_gaps": ["No B2B tool for independent walkers"]
}

founder_fit = {
    "technical_fit": 85,
    "domain_fit": 20,
    "execution_speed": 70,
    "market_understanding": 30,
    "key_strengths": ["MERN Stack", "Fast learner"],
    "key_weaknesses": ["No fitness industry experience", "No B2B sales"],
    "missing_skills": ["B2B enterprise sales", "Fitness industry knowledge"],
    "co_founder_recommendation": "Business co-founder with B2B SaaS sales experience",
    "solo_viability": "no",
    "solo_viability_reason": "Enterprise B2B sales require specialized industry knowledge",
    "summary": "Technically strong but needs commercial co-founder"
}

opportunity_score = {
    "market_pain_score": 75,
    "competition_score": 60,
    "founder_fit": 65,
    "timing": 70,
    "overall_score": 67,
    "verdict": "MAYBE",
    "reasoning": "Real problem but competitive market"
}

result = save_report(
    startup_idea="AI dog walking scheduler",
    competitors=competitors,
    pain_points=pain_points,
    founder_fit=founder_fit,
    opportunity_score=opportunity_score,
)

print(f"Report saved: {result}\n")

# Read and display
with open(result, 'r') as f:
    content = f.read()

print("=" * 60)
print("REPORT PREVIEW:")
print("=" * 60)
print(content[:1500])
print("...")

# Validations
print("\n" + "=" * 60)
print("VALIDATION:")
print("=" * 60)

checks = [
    ("Has competitor section", "🔍 Competitor Analysis" in content),
    ("Has direct competitors", "🔴 Direct Competitors" in content),
    ("Has indirect competitors", "🟡 Indirect Competitors" in content),
    ("Has adjacent threats", "🟠 Adjacent Threats" in content),
    ("Has potential entrants", "🔵 Potential Entrants" in content),
    ("Has pain points section", "📊 Pain Point Analysis" in content),
    ("Has pain points emoji", "😣 Customer Pain Points" in content),
    ("Has problems emoji", "⚠️ Problems with Existing Solutions" in content),
    ("Has market gaps emoji", "💡 Market Gaps" in content),
    ("Has founder fit section", "👤 Founder Fit Analysis" in content),
    ("Has missing skills", "Missing Skills" in content),
    ("Has co-founder rec", "Co-Founder Recommendation" in content),
    ("Has solo viability", "Solo Viability" in content),
    ("Has opportunity score section", "📈 Opportunity Score" in content),
    ("Has overall score", str(opportunity_score["overall_score"]) in content),
    ("Has verdict", opportunity_score["verdict"] in content),
    ("Has reasoning", opportunity_score["reasoning"] in content),
    ("No raw Python list brackets", "['Rover'" not in content),
    ("No raw Python dict", "{'technical_fit'" not in content),
]

for name, passed in checks:
    print(f"{'✅' if passed else '❌'} {name}")

print("\n✅ All checks complete")
