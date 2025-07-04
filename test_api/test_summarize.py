import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Session ID
SESSION_ID = os.getenv("DEMO_SESSION_ID")

UPLOAD_URL = "http://127.0.0.1:8000/upload"
SUMMARIZE_URL = "http://127.0.0.1:8000/summarize"

# Path to the document to upload
BASE_DIR = os.path.dirname(__file__)
DOCUMENT_PATH = os.path.join(BASE_DIR, "documents", "aphorismes.txt")

def main():
    if not os.path.isfile(DOCUMENT_PATH):
        print(f"File not found: {DOCUMENT_PATH}")
        return

    # Upload document to 'summarize' workspace
    files = [("files", open(DOCUMENT_PATH, "rb"))]
    params = {
        "session_id": SESSION_ID,
        "workspace": "summarize"
    }

    response = requests.post(UPLOAD_URL, params=params, files=files)

    print(f"Upload status code: {response.status_code}")
    try:
        print(f"Upload response: {response.json()}")
    except Exception:
        print(f"Upload response: {response.text}")

    # Call summarize
    print("Requesting summary…")
    params = {
        "session_id": SESSION_ID
    }

    response = requests.post(SUMMARIZE_URL, params=params)

    print(f"Summarize status code: {response.status_code}")
    try:
        print(f"Summary response: {response.json()}")
    except Exception:
        print(f"Summary response: {response.text}")

if __name__ == "__main__":
    main()

