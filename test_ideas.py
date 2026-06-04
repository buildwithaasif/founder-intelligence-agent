from agents.idea_generator import generate_startup_ideas
from agents.founder_profile import get_founder_profile


profile = get_founder_profile()

ideas = generate_startup_ideas(profile)

print("\nSTARTUP IDEAS\n")
print("=" * 60)
print(ideas)
