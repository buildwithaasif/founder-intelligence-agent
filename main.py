from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

from agents.founder_profile import get_founder_profile
from agents.idea_generator import generate_startup_ideas
from agents.analyzer import extract_competitors, get_competitors_flat
from agents.pain_analyzer import extract_pain_points
from agents.founder_fit import analyze_founder_fit
from agents.opportunity_score import calculate_opportunity_score
from agents.startup_recommendation import recommend_startup
from agents.customer_discovery import customer_discovery
from agents.customer_interview_questions import generate_interview_questions
from agents.final_report import generate_final_report

from tools.competitors import find_competitors
from tools.report_writer import save_report

console = Console()


def analyze_idea():
    """Full analysis pipeline for a startup idea."""
    startup_idea = console.input("\n[bold cyan]Enter startup idea:[/] ").strip()

    if not startup_idea:
        console.print("[red]Please enter a startup idea.[/]")
        return None

    founder_profile = get_founder_profile()

    # ── Step 1: Web Search ──
    console.print("\n[bold]Step 1/7:[/] Searching the web for competitors & market data...")
    search_results = find_competitors(startup_idea)
    console.print(f"  [green]✓[/] Found {len(search_results)} search results")

    # ── Step 2: Extract Competitors ──
    console.print("[bold]Step 2/7:[/] Identifying and categorizing competitors...")
    competitors = extract_competitors(search_results)
    competitors_flat = get_competitors_flat(competitors)
    console.print(f"  [green]✓[/] Found {len(competitors_flat)} competitors ({len(competitors['direct'])} direct, {len(competitors['indirect'])} indirect)")

    # ── Step 3: Extract Pain Points ──
    console.print("[bold]Step 3/7:[/] Analyzing market pain points...")
    pain_points = extract_pain_points(search_results)
    console.print(f"  [green]✓[/] Pain analysis complete")

    # ── Step 4: Founder Fit ──
    console.print("[bold]Step 4/7:[/] Assessing founder-fit...")
    founder_fit = analyze_founder_fit(startup_idea, competitors_flat, pain_points, founder_profile)
    console.print(f"  [green]✓[/] Founder-fit analyzed")

    # ── Step 5: Opportunity Score ──
    console.print("[bold]Step 5/7:[/] Calculating opportunity score...")
    opportunity_score = calculate_opportunity_score(startup_idea, competitors_flat, pain_points, founder_profile)
    console.print(f"  [green]✓[/] Score: {opportunity_score['overall_score']}/100 — {opportunity_score['verdict']}")

    # ── Step 6: Recommendation ──
    console.print("[bold]Step 6/7:[/] Generating strategic recommendation...")
    recommendation = recommend_startup(startup_idea, founder_profile, competitors_flat, pain_points, founder_fit, opportunity_score)
    console.print(f"  [green]✓[/] Decision: {recommendation.get('decision', 'UNKNOWN')}")

    # ── Step 7: Customer Discovery & Interview Questions ──
    console.print("[bold]Step 7/7:[/] Running customer discovery & generating interview questions...")
    customer_data = customer_discovery(startup_idea, recommendation)
    interview_qs = generate_interview_questions(startup_idea, customer_data)
    console.print(f"  [green]✓[/] Customer insights generated")

    # ── Save raw report (with categorized competitors) ──
    saved_path = save_report(startup_idea, competitors, pain_points, founder_fit, opportunity_score)
    console.print(f"\n[dim]Raw data saved to: {saved_path}[/]")

    # ── Generate final report ──
    final_report = generate_final_report(
        recommendation=recommendation,
        opportunity_score=opportunity_score,
        customer_discovery_data=customer_data,
        founder_fit=founder_fit,
        interview_questions=interview_qs,
    )

    return final_report


def generate_ideas():
    """Generate startup ideas based on founder profile."""
    founder_profile = get_founder_profile()
    console.print("\n[bold]Generating startup ideas...[/]\n")
    ideas = generate_startup_ideas(founder_profile)
    console.print(Panel.fit("[bold]🚀 STARTUP IDEAS[/]", border_style="green"))
    console.print(Markdown(ideas))


def main():
    console.print(Panel.fit(
        "[bold cyan]🚀 Founder Intelligence Agent[/]\n"
        "Analyze your startup idea or generate new ones tailored to your skills.",
        border_style="cyan"
    ))

    console.print("\n[1] Analyze Existing Idea")
    console.print("[2] Generate Startup Ideas")

    choice = console.input("\n[bold]Select option:[/] ").strip()

    if choice == "1":
        report = analyze_idea()
        if report:
            console.print("\n")
            console.print(Panel.fit(Markdown(report), border_style="bold green", title="[bold]FINAL REPORT[/]"))

    elif choice == "2":
        generate_ideas()

    else:
        console.print("\n[red]Invalid option. Please choose 1 or 2.[/]")


if __name__ == "__main__":
    main()