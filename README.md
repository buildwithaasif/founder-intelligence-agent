# Founder Intelligence Agent

Founder Intelligence Agent is a local AI-powered startup research tool that helps founders evaluate startup ideas using competitor research, pain-point analysis, founder-market fit analysis, opportunity scoring, customer discovery, startup recommendations, and customer interview questions.

## Features

* Competitor Analysis
* Pain Point Discovery
* Founder-Market Fit Analysis
* Opportunity Scoring
* Startup Recommendation Engine
* Customer Discovery Analysis
* Customer Interview Question Generation
* Startup Idea Generation

## Tech Stack

* Python
* Ollama
* Qwen
* DuckDuckGo Search

## Installation

```bash
git clone <repo-url>
cd founder-intelligence-agent

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

## Ollama Setup

Install Ollama and pull the required model:

```bash
ollama pull qwen3.6:latest
```

Make sure Ollama is running before starting the application.

## Run

```bash
python main.py
```

## Project Structure

```text
agents/
tools/
prompts/
main.py
requirements.txt
```

## License

MIT
