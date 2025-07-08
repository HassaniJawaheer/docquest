import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Session ID
SESSION_ID = os.getenv("DEMO_SESSION_ID")

# URL
QUERY_USER_URL = "http://127.0.0.1:8000/query/user_vector_db"

def main():
    question = "Il y a combien de bloc de compétences ?"
    
    params = {
        "session_id": SESSION_ID
    }

    payload = {
        "content": question
    }

    response = requests.post(QUERY_USER_URL, params=params, json=payload)

    print(f"Query status code: {response.status_code}")
    try:
        print(f"Query response: {response.json()}")
    except Exception:
        print(f"Query response: {response.text}")

if __name__ == "__main__":
    main()
