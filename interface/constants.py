import os
from dotenv import load_dotenv

load_dotenv()

SESSION_ID = os.getenv("DEMO_SESSION_ID")
API_BASE_URL = "http://127.0.0.1:8000"

MODES = [
    "Summary",
    "MCQ",
    "Query VectorDB",
    "Query CentralDB"
]
