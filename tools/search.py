from ddgs import DDGS


def search_web(query: str, max_results: int = 10):
    results = []

    with DDGS() as ddgs:
        search_results = ddgs.text(
            query,
            max_results=max_results
        )

        for result in search_results:
            results.append(
                {
                    "title": result.get("title", ""),
                    "url": result.get("href", ""),
                    "body": result.get("body", ""),
                }
            )

    return results