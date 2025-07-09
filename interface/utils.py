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


def qcm_to_string(qcm_dict: dict) -> str:
    """
    Converts a QCM dict into a human-readable markdown string.
    """
    if not qcm_dict:
        return "[No QCM data]"

    parts = []
    question = qcm_dict.get("question", "[No question provided]")
    parts.append(f"**QCM:** {question}\n")

    options = qcm_dict.get("options", [])
    if options:
        for idx, opt in enumerate(options, 1):
            parts.append(f"- {idx}. {opt}")
    else:
        parts.append("_No options provided._")

    answer = qcm_dict.get("answer", "[No answer provided]")
    parts.append(f"\n**Answer:** {answer}")

    return "\n".join(parts)


def format_server_response(response: dict, mode: str) -> list[dict]:
    """
    Reformats the server response into a list of chat messages.
    """
    content = ""

    if mode == "Summary":
        content = response.get("summary", str(response))

    elif mode == "MCQ":
        content = qcm_to_string(response.get("qcm", {}))

    elif mode in ["Query CentralDB", "Query VectorDB"]:
        if isinstance(response, dict):
            content = response.get("content", str(response))
        else:
            content = str(response)

    else:
        content = str(response)

    return [{"role": "assistant", "content": content}]

