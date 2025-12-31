import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

OPENAI_CONFIG = {
    "api_key": os.getenv("OPENAI_API_KEY"),
    "default_model": "gpt-4o-2024-08-06",
    "embd_model" : "text-embedding-3-small",
    "temperature": 0.1,
}

TAVILY_CONFIG = {
    "api_key" : os.getenv("TAVILY_API_KEY")
}