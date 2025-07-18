import os
import requests
from dotenv import load_dotenv
API_URL = "http://127.0.0.1:8000/upload"

# Session ID
load_dotenv()
SESSION_ID = os.getenv("DEMO_SESSION_ID")

# Documents
TEST_DOCS_DIR = os.path.join(os.path.dirname(__file__), "documents")

def main():
    files = []
    for filename in os.listdir(TEST_DOCS_DIR):
        filepath = os.path.join(TEST_DOCS_DIR, filename)
        if os.path.isfile(filepath):
            files.append(("files", open(filepath, "rb")))

    if not files:
        print("No files found in documents/")
        return

    params = {
        "session_id": SESSION_ID,
        "workspace": "rag"
    }

    response = requests.post(API_URL, params=params, files=files)

    print(f"Status code: {response.status_code}")
    try:
        print(f"Response: {response.json()}")
    except Exception:
        print(f"Response: {response.text}")

if __name__ == "__main__":
    main()
