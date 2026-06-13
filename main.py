from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

from agents.founder_profile import get_founder_profile
from agents.idea_generator import generate_startup_ideas
from agents.assumptions import extract_assumptions
from agents.analyzer import extract_competitors, get_competitors_flat
from agents.pain_analyzer import extract_pain_points
from agents.validation_tasks import generate_validation_tasks
from agents.evidence_mapper import map_evidence
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

    # ── Step 1: Extract Assumptions ──
    console.print("\n[bold]Step 1/11:[/] Extracting hidden assumptions...")
    assumptions = extract_assumptions(startup_idea, founder_profile)
    assumption_count = len(assumptions.get("assumptions", []))
    console.print(f"  [green]✓[/] Found {assumption_count} key assumptions to test")

    # ── Step 2: Web Search ──
    console.print("[bold]Step 2/11:[/] Searching the web for competitors & market data...")
    search_results = find_competitors(startup_idea)
    console.print(f"  [green]✓[/] Found {len(search_results)} search results")

    # ── Step 3: Extract Competitors ──
    console.print("[bold]Step 3/11:[/] Identifying and categorizing competitors...")
    competitors = extract_competitors(search_results)
    competitors_flat = get_competitors_flat(competitors)
    console.print(f"  [green]✓[/] Found {len(competitors_flat)} competitors ({len(competitors['direct'])} direct, {len(competitors['indirect'])} indirect)")

    # ── Step 4: Extract Pain Points ──
    console.print("[bold]Step 4/11:[/] Analyzing market pain points...")
    pain_points = extract_pain_points(search_results)
    console.print(f"  [green]✓[/] Pain analysis complete")

    # ── Step 5: Generate Validation Tasks ──
    console.print("[bold]Step 5/11:[/] Creating validation tasks for each assumption...")
    validation = generate_validation_tasks(assumptions, startup_idea, competitors, pain_points)
    validation_summary = validation.get("summary", {})
    console.print(f"  [green]✓[/] {validation_summary.get('total_tasks', 0)} tasks created ({validation_summary.get('high_priority_count', 0)} high priority)")

    # ── Step 6: Map Evidence to Assumptions ──
    console.print("[bold]Step 6/11:[/] Mapping evidence against assumptions...")
    evidence = map_evidence(assumptions, competitors, pain_points, search_results)
    overall_evidence = evidence.get("overall", {})
    console.print(f"  [green]✓[/] {overall_evidence.get('supported_count', 0)} supported, {overall_evidence.get('rejected_count', 0)} rejected, {overall_evidence.get('partial_count', 0)} partial, {overall_evidence.get('unclear_count', 0)} unclear")

    # ── Step 7: Founder Fit ──
    console.print("[bold]Step 7/11:[/] Assessing founder-fit...")
    founder_fit = analyze_founder_fit(startup_idea, competitors_flat, pain_points, founder_profile)
    console.print(f"  [green]✓[/] Founder-fit analyzed")

    # ── Step 8: Opportunity Score ──
    console.print("[bold]Step 8/11:[/] Calculating opportunity score...")
    opportunity_score = calculate_opportunity_score(startup_idea, competitors_flat, pain_points, founder_profile)
    console.print(f"  [green]✓[/] Score: {opportunity_score['overall_score']}/100 — {opportunity_score['verdict']}")

    # ── Step 9: Recommendation ──
    console.print("[bold]Step 9/11:[/] Generating strategic recommendation...")
    recommendation = recommend_startup(startup_idea, founder_profile, competitors_flat, pain_points, founder_fit, opportunity_score)
    console.print(f"  [green]✓[/] Decision: {recommendation.get('decision', 'UNKNOWN')}")

    # ── Step 10: Customer Discovery ──
    console.print("[bold]Step 10/11:[/] Running customer discovery...")
    customer_data = customer_discovery(startup_idea, recommendation)
    console.print(f"  [green]✓[/] ICP identified")

    # ── Step 11: Interview Questions ──
    console.print("[bold]Step 11/11:[/] Generating YC-style interview questions...")
    # Use pivot idea for interview questions if original idea was rejected/pivoted
    interview_idea = recommendation.get("best_startup_angle", startup_idea) if recommendation.get("decision") in ["PIVOT", "ABANDON"] else startup_idea
    interview_qs = generate_interview_questions(interview_idea, customer_data)
    console.print(f"  [green]✓[/] Interview script ready")

    # ── Save raw report ──
    saved_path = save_report(startup_idea, competitors, pain_points, founder_fit, opportunity_score)
    console.print(f"\n[dim]Raw data saved to: {saved_path}[/]")

    # ── Generate final report ──
    final_report = generate_final_report(
        startup_idea=startup_idea,
        assumptions=assumptions,
        evidence=evidence,
        validation=validation,
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
        "Test your assumptions before you build.\n"
        "Idea → Assumptions → Research → Validation Tasks → Evidence → Conclusion",
        border_style="cyan"
    ))

    console.print("\n[1] Analyze Existing Idea")
    console.print("[2] Generate Startup Ideas")

    choice = console.input("\n[bold]Select option:[/] ").strip()

    if choice == "1":
        report = analyze_idea()
        if report:
            console.print(Markdown(report))

    elif choice == "2":
        generate_ideas()

    else:
        console.print("\n[red]Invalid option. Please choose 1 or 2.[/]")


if __name__ == "__main__":
    main()