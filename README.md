# 🤖 AI News Summarizer (Agentic AI with LangGraph)

This project is an **end-to-end Agentic AI chatbot framework** built with **LangGraph, LangChain, and Streamlit**.  
It demonstrates how to design **stateful AI agents** capable of multiple use cases such as:

- ✅ **AI News Summarizer** – fetch and summarize the latest AI-related news from trusted sources (Daily, Weekly, Monthly).

The app provides an **interactive Streamlit UI**, integrates with **Groq LLMs** for fast inference, and persists summaries to Markdown files for later review.

## 🚀 Features

- **📰 AI News Summarizer**  
  Fetches AI-related news using **Tavily API**, summarizes them with Groq LLM, and saves the results into Markdown files:
  - `AINews/daily_summary.md`
  - `AINews/weekly_summary.md`
  - `AINews/monthly_summary.md`


- **🌍 Chatbot with Web Search**  
  Integrates **Tavily Search** to fetch real-time information and enhance chatbot responses.

- **📊 Streamlit UI**  
  Intuitive sidebar for LLM/API key setup, use case selection, and live chat interface.

---

## 🛠️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/bhanuteja072-ainewssummarizer.git
cd bhanuteja072-ainewssummarizer

2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

3. Install dependencies
pip install -r requirements.txt

4. Set up API Keys

You will need:
