# 🚀 Founder Intelligence Agent

An AI-powered startup validation tool that uses **Y Combinator's proven methodologies** to analyze startup ideas, extract hidden assumptions, test them against real evidence, and generate actionable recommendations — all running locally with Ollama.

---

## 🧠 The Pipeline
Idea → Assumptions → Research → Validation Tasks → Evidence → Conclusion

text

| Step | What It Does |
|------|-------------|
| 🔍 **Assumptions** | Extracts 5-7 hidden beliefs behind your idea |
| 🌐 **Research** | Searches the web for competitors, complaints, and market data |
| 🏷️ **Competitor Intel** | Categorizes competitors as Direct, Indirect, Adjacent, or Potential threats |
| 📊 **Pain Points** | Finds real customer complaints, problems, and market gaps |
| ✅ **Validation Tasks** | Creates specific, actionable tests for each assumption with success/failure criteria |
| 🧪 **Evidence Mapping** | Matches research findings against assumptions — what's true, what's false |
| 👤 **Founder Gap Analysis** | Scores founder-fit and identifies missing skills + co-founder recommendations |
| 📈 **Opportunity Score** | Weighted scoring where direct competitors hurt more than indirect ones |
| 🚩 **Red Flag Scanner** | Detects YC anti-patterns: "Uber for X" clones, tarpit ideas, commodity markets |
| 🎯 **Recommendation** | BUILD, PIVOT, or ABANDON with detailed reasoning |
| 💡 **YC-Style Advice** | Direct, honest coaching in the voice of YC partners |
| 🎤 **Interview Scripts** | 20 YC-style customer discovery questions + interviewer training tips |

---

## ✨ Features

- **Assumptions vs Evidence** — See which of your beliefs are supported, rejected, or unclear
- **Validation Tasks** — Specific actions to test each assumption (with success/failure criteria)
- **YC Red Flag Scanner** — Detects 8 known startup anti-patterns
- **Founder Gap Analysis** — Identifies missing skills and recommends co-founder type
- **Competitor Categorization** — Direct, Indirect, Adjacent, and Potential threats
- **YC-Style Interview Scripts** — 20 questions + 5 interviewer training tips
- **Smart Scoring** — Direct competitors hurt more than indirect ones
- **Clean Reports** — Scannable, decision-first format

---

## 🛠 Tech Stack

| Component | Technology |
|-----------|------------|
| LLM | Ollama (Qwen 3.6 or any model) |
| Web Search | DuckDuckGo |
| Language | Python 3.11+ |
| Terminal UI | Rich |
| Reports | Markdown |

---

## 📦 Installation

### 1. Clone

```bash
git clone https://github.com/buildwithaasif/founder-intelligence-agent.git
cd founder-intelligence-agent
2. Setup
bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
3. Install Ollama
bash
# Install from https://ollama.com
ollama pull qwen3.6:latest
🚀 Usage
bash
python main.py
Option	What It Does
1. Analyze Idea	Full 11-step pipeline: Assumptions → Evidence → Recommendation
2. Generate Ideas	Brainstorms 10 startup ideas based on your founder profile
📊 Sample Report
text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        🚀 STARTUP INTELLIGENCE REPORT
        market research agent for founders
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🟡 VERDICT: PIVOT   │   Score: 48/100

────────────────────────────────────────────
🔴 WHAT'S WRONG
────────────────────────────────────────────
❌ Founders won't pay monthly subscriptions
⚠️ AI hallucination still a problem

────────────────────────────────────────────
🟢 WHAT'S RIGHT
────────────────────────────────────────────
✅ Real pain: Research takes 10+ hrs/week
✅ Existing tools too expensive ($40K+)

────────────────────────────────────────────
🎯 YOUR PIVOT
────────────────────────────────────────────
AI Security & Compliance Audit Agent
→ Uses your OSCP/CPTS as unfair advantage

────────────────────────────────────────────
💡 WHAT YC WOULD SAY
────────────────────────────────────────────
💬 "Your OSCP is your superpower. Own the security niche."
💬 "Do things that don't scale: hand-deliver audits to 10 founders."

────────────────────────────────────────────
⏱️ VALIDATION PLAN
────────────────────────────────────────────
Time needed: 2-3 weeks
Start with: Concierge offer — deliver reports for $49
📁 Project Structure
text
founder-intelligence-agent/
│
├── main.py                           # Orchestrator
├── config.py                         # Model settings
├── requirements.txt                  # Dependencies
│
├── agents/
│   ├── assumptions.py                # Extract hidden assumptions
│   ├── analyzer.py                   # Competitor extraction & categorization
│   ├── pain_analyzer.py              # Pain point discovery
│   ├── validation_tasks.py           # Generate tests for each assumption
│   ├── evidence_mapper.py            # Match research to assumptions
│   ├── founder_fit.py                # Founder gap analysis + co-founder rec
│   ├── opportunity_score.py          # Smart weighted scoring
│   ├── startup_recommendation.py     # Red flags + BUILD/PIVOT/ABANDON
│   ├── customer_discovery.py         # ICP & buyer persona
│   ├── customer_interview_questions.py # YC-style interview scripts
│   ├── final_report.py               # Report formatting
│   ├── founder_profile.py            # Founder background
│   └── idea_generator.py             # Startup idea brainstorming
│
├── tools/
│   ├── search.py                     # DuckDuckGo web search
│   ├── competitors.py                # Multi-query search strategy
│   └── report_writer.py              # Markdown report saver
│
└── reports/                          # Saved analysis reports
🧪 Testing
bash
python test_assumptions.py            # Assumption extraction
python test_analyzer.py               # Competitor categorization
python test_evidence_mapper.py        # Evidence mapping
python test_validation_tasks.py       # Validation task generation
python test_founder_fit.py            # Founder gap analysis
python test_opportunity_score.py      # Scoring logic
python test_recommendation.py         # Red flags + recommendation
python test_interview_questions.py    # YC interview scripts
python test_final_report.py           # Report formatting
python test_report_writer.py          # Markdown saving
🔧 Customization
Change founder profile — Edit agents/founder_profile.py

Change LLM model — Edit config.py:

python
MODEL_NAME = "llama3:latest"
📄 License
MIT