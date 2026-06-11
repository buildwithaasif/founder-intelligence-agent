markdown
# 🚀 Founder Intelligence Agent

An AI-powered startup validation tool that uses **Y Combinator's proven methodologies** to analyze startup ideas, identify red flags, assess founder-fit, and generate actionable recommendations — all running locally with Ollama.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔍 **Competitor Intelligence** | Searches the web and categorizes competitors as Direct, Indirect, Adjacent, or Potential threats |
| 📊 **Pain Point Analysis** | Extracts real customer complaints, problems, and market gaps from web data |
| 👤 **Founder Gap Analysis** | Scores founder-fit and identifies missing skills + co-founder recommendations |
| 📈 **Smart Opportunity Scoring** | Weighted scoring where direct competitors hurt more than indirect ones |
| 🚩 **YC Red Flag Scanner** | Detects anti-patterns: "Uber for X" clones, tarpit ideas, solutions looking for problems |
| 🎯 **Strategic Recommendation** | BUILD, PIVOT, or ABANDON with detailed reasoning |
| 🎤 **YC-Style Interview Scripts** | 20 customer discovery questions + interviewer training tips |
| 📝 **Detailed Reports** | Clean markdown reports saved automatically |

---

## 🧠 YC Methodology Built In

- **Red Flag Detection:** Commodity markets, behavior change traps, market graveyards, fake urgency
- **Founder-Market Fit:** Scores technical fit, domain expertise, execution speed, and market understanding
- **Gap Analysis:** Identifies what skills are missing and what type of co-founder you need
- **Customer Discovery:** "Interview 20 customers before building anything" framework
- **Problem vs Solution Focus:** Questions designed to uncover real pain, not validate your idea
- **Willingness to Pay:** Asks about actual past spending, not hypothetical future purchases

---

## 🛠 Tech Stack

| Component | Technology |
|-----------|------------|
| LLM | Ollama with Qwen 3.6 |
| Web Search | DuckDuckGo (ddgs) |
| Language | Python 3.11+ |
| Terminal UI | Rich |
| Reports | Markdown |

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/buildwithaasif/founder-intelligence-agent.git
cd founder-intelligence-agent
2. Set Up Virtual Environment
bash
python -m venv .venv
source .venv/bin/activate
3. Install Dependencies
bash
pip install -r requirements.txt
4. Install Ollama & Pull Model
bash
# Install Ollama from https://ollama.com
ollama pull qwen3.6:latest
Make sure Ollama is running in the background before starting the application.

🚀 Usage
bash
python main.py
You'll see two options:

Option	What It Does
1. Analyze Existing Idea	Full pipeline: web search → competitor analysis → pain points → founder fit → red flags → recommendation → interview questions
2. Generate Startup Ideas	Brainstorms 10 startup ideas based on your founder profile
📊 Sample Output
text
=============================================
       STARTUP INTELLIGENCE REPORT
=============================================

DECISION: PIVOT

OPPORTUNITY SCORE: 58/100

=============================================
              RED FLAG SCAN
=============================================
🚩 Commodity market with low differentiation
🚩 No clear customer acquisition path
🚩 High operational cost risk

The space is a red ocean of AI wrappers competing on price.

-------------------------------------------------
BEST STARTUP ANGLE:
AI-powered validation agent targeting pre-seed founders
actively fundraising, leveraging security background as
a defensible moat.

WHY THIS WINS:
- Leverages founder's offensive security background
- Targets high-intent, urgent workflow (fundraising)
- Avoids head-on competition with data aggregators

MVP:
Single-page app where founders input a startup idea or
competitor URL to get a 10-page automated report.

FOUNDER FIT:
Strong builder but lacks sales/GTM expertise.
Co-Founder Recommendation: B2B SaaS sales co-founder

NEXT 30 DAYS:
- Interview 20 pre-seed founders
- Build functional MVP in 24 hours
- Publish 3 case studies to drive waitlist
📁 Project Structure
text
founder-intelligence-agent/
│
├── main.py                           # Orchestrator - runs the full pipeline
├── config.py                         # Model name and settings
├── requirements.txt                  # Python dependencies
│
├── agents/
│   ├── analyzer.py                   # Competitor extraction & categorization
│   ├── pain_analyzer.py              # Pain point & market gap discovery
│   ├── founder_fit.py                # Founder gap analysis + co-founder rec
│   ├── opportunity_score.py          # Smart weighted opportunity scoring
│   ├── startup_recommendation.py     # Red flags + BUILD/PIVOT/ABANDON
│   ├── customer_discovery.py         # ICP & buyer persona analysis
│   ├── customer_interview_questions.py # YC-style interview scripts
│   ├── final_report.py               # Final report formatting
│   ├── founder_profile.py            # Founder background (customize this!)
│   └── idea_generator.py             # Startup idea brainstorming
│
├── tools/
│   ├── search.py                     # DuckDuckGo web search
│   ├── competitors.py                # Multi-query search strategy
│   └── report_writer.py              # Markdown report saver
│
└── reports/                          # Saved analysis reports
🧪 Testing
Run individual component tests (no full pipeline needed):

bash
python test_analyzer.py              # Competitor categorization
python test_founder_fit.py           # Founder gap analysis
python test_opportunity_score.py     # Smart scoring logic
python test_recommendation.py        # Red flag scanner
python test_interview_questions.py   # YC interview scripts
python test_final_report.py          # Report formatting
python test_report_writer.py         # Markdown saving
🔧 Customization
Change the Founder Profile
Edit agents/founder_profile.py with your own background:

python
def get_founder_profile() -> str:
    return """
    - Your skills here
    - Your experience here
    - Your interests here
    """
Change the LLM Model
Edit config.py:

python
MODEL_NAME = "llama3:latest"  # or mistral, qwen, etc.
🔮 Roadmap
"What YC Would Tell You" coaching section

Web UI with Streamlit or Gradio

Interactive founder profile builder

Multi-idea comparison mode

PDF report export

Integration with Crunchbase/ProductHunt APIs

📄 License
MIT — feel free to use, modify, and share.
