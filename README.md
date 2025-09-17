# 🤖 Smart Agent Search Engine with LangChain

This project is a web-based AI assistant that acts as a smart search agent. Built with Streamlit and LangChain, it leverages a powerful language model to intelligently select and use specialized tools—like a web search engine, a scientific paper database, and an encyclopedia—to answer user questions.

---

## ✨ Features
- **Intelligent Tool Selection**: The agent uses a large language model (LLM) to decide which tool is best for each query (e.g., general web search, Wikipedia, or scientific articles).
- **Conversational Interface**: A Streamlit-powered chat application provides a simple, interactive way to communicate with the agent.
- **LangSmith Tracing**: The project includes optional tracing with LangSmith to visualize the agent's thought process and debugging.
- **Secure API Key Management**: Environment variables are used to securely handle API keys, keeping sensitive information out of the code.

---

## 🛠️ How It Works
The core of this project is a LangChain agent. An agent is a system that uses an LLM as its "brain" to reason about a user's request and decide on the best course of action. In this case, the agent can choose from a set of predefined tools.

- **Brain (LLM)**: ChatGroq is used as the LLM, providing a fast and powerful reasoning engine.

### Tools:
- **DuckDuckGo Search**: For general questions.
- **Wikipedia**: For broad, encyclopedic knowledge.
- **ArXiv**: For scientific papers and research.

When you ask a question, the LLM analyzes it, selects the most appropriate tool, and then uses that tool to find an answer. The result is then presented to you in the chat interface.

---

## ⚙️ Setup and Installation

Follow these steps to get the project running on your local machine.

```bash
# 1. Clone the Repository
git clone https://github.com/ILIASB1212/Agentic-searcher.git

# 2. Create a Virtual Environment
conda create -p env python==3.10 -y

# 3. Install Dependencies
pip install -r requirements.txt
# Note: The main libraries are langchain, streamlit, langchain-groq, python-dotenv, and the tool-specific libraries like wikipedia and duckduckgo-search.

# 4. Configure Your API Key
# Create a file named `.env` in the root directory of your project and add your LangChain API key to it.
# Example:
# LANGCHAIN_API_KEY="YOUR_LANGCHAIN_API_KEY_HERE"

# 5. Run the Application
streamlit run app.py

Your web browser will automatically open the application. You can now start a conversation with your AI search agent.
