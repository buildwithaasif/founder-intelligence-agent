from agents.customer_interview_questions import (
    generate_interview_questions
)
from agents.customer_discovery import customer_discovery
from agents.startup_recommendation import recommend_startup
from agents.founder_profile import get_founder_profile
from agents.idea_generator import generate_startup_ideas

from agents.founder_fit import analyze_founder_fit
from agents.opportunity_score import calculate_opportunity_score

from tools.competitors import find_competitors
from tools.report_writer import save_report

from agents.analyzer import extract_competitors
from agents.pain_analyzer import extract_pain_points


def analyze_idea():
    startup_idea = input("\nEnter startup idea: ").strip()

    if not startup_idea:
        print("Please enter a startup idea.")
        return

    founder_profile = get_founder_profile()

    print("\nSearching for competitors...\n")

    results = find_competitors(startup_idea)

    print("\nRAW SEARCH RESULTS\n")
    print("=" * 60)

    for i, result in enumerate(results[:5], start=1):
        print(f"\n{i}. {result['title']}")
        print(f"URL: {result['url']}")
        print(f"Snippet: {result['body']}")

    print(f"\nFound {len(results)} search results.\n")

    print("Analyzing competitors with Qwen...\n")

    competitors = extract_competitors(results)

    print("=" * 60)
    print("COMPETITOR ANALYSIS")
    print("=" * 60)
    print()
    print(competitors)
    print()

    pain_points = extract_pain_points(results)

    print("=" * 60)
    print("PAIN ANALYSIS")
    print("=" * 60)
    print()
    print(pain_points)
    print()

    founder_fit = analyze_founder_fit(
        startup_idea,
        competitors,
        pain_points,
        founder_profile,
    )

    print("=" * 60)
    print("FOUNDER FIT ANALYSIS")
    print("=" * 60)
    print()
    print(founder_fit)
    print()

    opportunity_score = calculate_opportunity_score(
        startup_idea,
        competitors,
        pain_points,
        founder_profile,
    )

    print("=" * 60)
    print("OPPORTUNITY SCORE")
    print("=" * 60)
    print()
    print(opportunity_score)
    print()

    print("=" * 60)
    print("STARTUP RECOMMENDATION")
    print("=" * 60)
    print()

    recommendation = recommend_startup(
        startup_idea=startup_idea,
        founder_profile=founder_profile,
        competitors=competitors,
        pain_points=pain_points,
        founder_fit=founder_fit,
        opportunity_score=opportunity_score,
    )

    print(recommendation)
    print()

    customer_analysis = customer_discovery(
        startup_idea,
        recommendation,
    )

    print("=" * 60)
    print("CUSTOMER DISCOVERY")
    print("=" * 60)
    print()

    print(customer_analysis)
    print()

    print("=" * 60)
    print("CUSTOMER INTERVIEW QUESTIONS")
    print("=" * 60)
    print()

    interview_questions = generate_interview_questions(
        startup_idea,
        customer_analysis,
    )

    print(interview_questions)
    print()

    report_file = save_report(
        startup_idea,
        competitors,
        pain_points,
        founder_fit,
        opportunity_score,
    )

    print("=" * 60)
    print(f"Report saved: {report_file}")
    print("=" * 60)


def generate_ideas():
    founder_profile = get_founder_profile()

    print("\nGenerating startup ideas...\n")

    ideas = generate_startup_ideas(founder_profile)

    print("=" * 60)
    print("STARTUP IDEAS")
    print("=" * 60)
    print()
    print(ideas)
    print()


def main():
    print("\n=== Founder Intelligence Agent ===\n")

    print("1. Analyze Existing Idea")
    print("2. Generate Startup Ideas")

    choice = input("\nSelect option: ").strip()

    if choice == "1":
        analyze_idea()

    elif choice == "2":
        generate_ideas()

    else:
        print("\nInvalid option.")


if __name__ == "__main__":
    main()