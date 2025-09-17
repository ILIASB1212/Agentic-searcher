# config.py
import os
from dotenv import load_dotenv
from LOGGER.log import logging

def setup_environment():
    load_dotenv()
    if not os.getenv("LANGCHAIN_API_KEY"):
        raise ValueError("LANGCHAIN_API_KEY is not set in the environment or .env file.")
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    
    os.environ["LANGCHAIN_PROJECT"] = "Agentic-searcher"
    
    logging.info("Environment setup complete. LangChain tracing is enabled.")
