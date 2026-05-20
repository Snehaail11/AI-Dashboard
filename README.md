# AI-Powered Reporting Dashboard

## 1. What problem does it solve?
Businesses struggle to turn raw data (CSV files, spreadsheets, logs) into actionable insights. Teams spend excessive time manually querying databases, building static reports, and trying to answer ad-hoc questions like "What are the top trends?" or "Why did something change last month?".

This dashboard **automates the reporting process** for ANY CSV file and adds an **AI-powered intelligence layer** that:
- Automatically generates insights from your data
- Detects anomalies and unusual patterns
- Creates executive summaries
- Provides actionable recommendations

**No API key required** – the AI works out of the box using statistical analysis and pattern recognition.

## 2. What tech stack did you use?
| Component | Technology | Purpose |
|-----------|------------|---------|
| **Frontend/UI** | Streamlit | Interactive web app development |
| **Data Processing** | Pandas, NumPy | Cleaning, aggregation, analysis |
| **Visualization** | Plotly | Interactive charts (line, bar, area, pie) |
| **AI Layer** | Custom statistical insights + anomaly detection | No API key required |
| **Optional AI** | OpenAI API (GPT-3.5/4) | Custom Q&A (user can add their key) |
| **Data Storage** | CSV files | Portable, no database needed |

## 3. Why did you choose it?
- **Streamlit**: Builds polished, interactive UI with minimal code – perfect for demonstrating full-stack ability
- **Pandas/NumPy**: Industry-standard data tools; showcases core data science proficiency
- **Plotly**: Interactive charts (zoom, hover, filter) that static libraries lack
- **Custom AI Layer**: Demonstrates understanding of statistics (z-scores, trends, distributions) without relying on external APIs
- **OpenAI Integration (optional)**: Shows ability to integrate LLMs for advanced Q&A
- **CSV storage**: Portable, runnable anywhere, still demonstrates ETL concepts

## 4. What does the AI actually do?

The dashboard has **4 AI-powered features**:

| AI Feature | What it does | Example Output |
|------------|--------------|----------------|
| **🔮 AI Insights** | Analyzes data structure, trends, and patterns | "Top category 'saas' drives 45% of records. Dataset shows right-skewed distribution." |
| **⚠️ Anomaly Detection** | Finds unusual patterns using Z-score analysis | "Found 3 anomalies on Jan 15, Feb 3, Mar 22 – values 2 standard deviations from mean" |
| **📝 Executive Summary** | Generates complete business report | Creates report with metrics, column analysis, and top insights |
| **🎯 Recommendations** | Suggests actionable next steps | "Monitor sales weekly. Analyze top/bottom segments. Add more numeric columns for deeper insights." |

**Optional OpenAI Integration:** Users can add their own API key to ask custom questions like:
- "What are the top trends this month?"
- "Which products should we focus on?"
- "Summarize this data in 3 bullet points"

## 5. How to use

### Prerequisites
- Python 3.9 or higher installed
- Internet connection (for first-time setup)

### Installation

```bash
# 1. Clone or download the project
cd AI-Reporting-Dashboard

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install streamlit pandas numpy plotly openai

# 5. Run the dashboard
streamlit run ai_dashboard.py