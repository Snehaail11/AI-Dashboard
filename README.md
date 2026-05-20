# AI-Powered SaaS Reporting Dashboard

## 1. What problem does it solve?
Businesses struggle to turn raw user activity data into actionable insights. Teams spend excessive time manually querying databases, building static reports, and trying to answer ad-hoc questions like "Why did revenue drop last month?" or "Which features are driving engagement?". This dashboard automates the reporting process and adds an AI-powered assistant that allows users to ask natural-language questions about their data and get instant, contextualized insights—reducing time-to-insight from hours to seconds.

## 2. What tech stack did you use?
- **Frontend/UI**: Streamlit (Python) – for rapid, interactive web app development
- **Data Processing**: Pandas, NumPy – for cleaning, aggregating, and analyzing the dataset
- **Visualization**: Plotly – for interactive, publication-quality charts (line, area, pie)
- **AI/LLM**: OpenAI API (GPT-3.5-turbo) – powers the conversational assistant
- **Data Storage**: CSV files (simulating a data warehouse/logs) – `saas_users.csv` and `saas_product_data.csv`
- **Environment**: Python 3.11 with virtual environment (`saas_env`)

## 3. Why did you choose it?
- **Streamlit**: Enables building a polished, interactive UI with minimal frontend code—ideal for demonstrating full-stack ability without getting bogged down in HTML/CSS/JS.
- **Pandas/NumPy**: Industry-standard tools for data manipulation; showcases proficiency in the core data science stack.
- **Plotly**: Provides interactivity (zoom, hover, filter) that static libraries (Matplotlib/Seaborn) lack, making the dashboard feel like a real product.
- **OpenAI API**: Represents cutting-edge AI integration; using an LLM for data Q&A is a tangible, valuable skill in AI/product roles.
- **CSV storage**: Keeps the project portable and runnable anywhere without requiring a database server, while still demonstrating ETL and querying concepts.

## 4. What challenge did you face?
The biggest challenge was making the AI assistant’s responses relevant and accurate. Initially, I asked the LLM to answer questions based on the entire dataset, which led to generic or misleading answers when users filtered the dashboard (e.g., asking about March revenue while looking at annual data). I solved this by:
   - Creating a concise data summary (KPIs, top features, plan distribution) based on the currently filtered view.
   - Passing that summary as context to the LLM with each user query.
   - This ensured the AI’s answers were grounded in the exact slice of data the user was examining, turning it into a true contextual analyst rather than a chatbot.

Additional challenges included:
   - Managing date/time conversions (ensuring consistency between generated data and filters).
   - Balancing UI responsiveness with data processing (solved with Streamlit’s caching).
   - Handling edge cases like empty filters or no churn in the selected period.

## 5. What would you improve?
Given more time, I would:
- **Add user authentication and role-based access** (e.g., admin vs. viewer) to simulate a multi-tenant SaaS product.
- **Implement report export** (PDF/CSV) so users can share insights outside the app.
- **Save filter presets or custom views** for power users to quickly access their favorite dashboards.
- **Enhance the AI with retrieval-augmented generation (RAG)** for larger datasets, allowing the LLM to query relevant data snippets instead of relying solely on summary statistics.
- **Deploy to the cloud** (Streamlit Community Cloud, Docker, or AWS) to demonstrate DevOps/CI-CD skills.
- **Add more advanced analytics** such as forecasting (using Prophet or scikit-learn) and anomaly detection.
- **Write comprehensive unit and integration tests** to ensure reliability as the app grows.

---

*Built as a showcase of end-to-end skills in data analysis, product thinking, and AI integration.*