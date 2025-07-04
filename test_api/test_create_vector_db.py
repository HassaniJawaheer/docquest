import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "http://127.0.0.1:8000/create_vector_db"

# Session ID
SESSION_ID = os.getenv("DEMO_SESSION_ID")

def main():
    params = {
        "session_id": SESSION_ID
    }

    response = requests.post(API_URL, params=params)

    print(f"Status code: {response.status_code}")
    try:
        print(f"Response: {response.json()}")
    except Exception:
        print(f"Response: {response.text}")

if __name__ == "__main__":
    main()
