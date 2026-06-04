from tools.search import search_web


def find_competitors(startup_idea: str):
    search_queries = [
        f"{startup_idea} competitors",
        f"{startup_idea} customer complaints",
        f"{startup_idea} problems",
        f"{startup_idea} challenges",
        f"{startup_idea} reddit",
    ]

    all_results = []

    for query in search_queries:
        results = search_web(query, max_results=5)
        all_results.extend(results)

    return all_results
