import requests
from constants import API_BASE_URL

def post_to_api(endpoint, params=None, json=None, files=None):
    """
    Helper to POST to the API and return the full JSON response.
    """
    url = f"{API_BASE_URL}{endpoint}"

    try:
        response = requests.post(url, params=params, json=json, files=files)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"status": "error", "message": str(e)}

def format_server_response(response: dict, mode: str) -> list[dict]:
    """
    Reformats the server response into a list of chat messages.
    """
    content = ""

    if mode == "Summary":
        content = response.get("Summary", str(response))
    elif mode == "MCQ":
        import json
        content = json.dumps(response.get("MCQ", {}), indent=2)
    elif mode in ["Query CentralDB", "Query VectorDB"]:
        if isinstance(response, dict):
            key = next(iter(response.keys()), None)
            if key:
                content = f"{key}: {response[key]}"
            else:
                content = str(response)
        else:
            content = str(response)
    else:
        content = str(response)

    return [{"role": "assistant", "content": content}]