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

def qcm_to_string(qcm_dict: dict, index: int = 1) -> str:
    """
    Converts a MCQ dict into a human-readable markdown string.
    """
    if not qcm_dict:
        return "[No MCQ data]"

    lines = []

    # Numérotation et question
    question = qcm_dict.get("question", "[Question non fournie]")
    lines.append(f"**Question {index} :** {question}\n")

    # Options / distracteurs + bonne réponse
    correct = qcm_dict.get("correct_answer", "[Réponse non fournie]")
    distractors = qcm_dict.get("distractors", [])
    options = distractors + [correct]

    for idx, opt in enumerate(options, 1):
        lines.append(f"    {idx}. {opt}")

    # Réponse
    lines.append(f"\n**Réponse :** {correct}")

    return "\n".join(lines)

def format_server_response(response: dict, mode: str) -> list[dict]:
    """
    Reformats the server response into a list of chat messages.
    """
    content = ""

    if mode == "Summary":
        content = response.get("summary", str(response))

    elif mode == "MCQ":
        qcms = response.get("questions", [])
        if qcms:
            parts = []
            for i, q in enumerate(qcms, 1):
                qcm_dict = {
                    "question": q.get("question"),
                    "distractors": q.get("distractors", []),
                    "correct_answer": q.get("correct_answer")
                }
                parts.append(qcm_to_string(qcm_dict, index=i))
            content = "\n\n".join(parts)
        else:
            content = "[Aucune donnée QCM]"

    elif mode in ["Query CentralDB", "Query VectorDB"]:
        if isinstance(response, dict):
            content = response.get("content", str(response))
        else:
            content = str(response)

    else:
        content = str(response)

    return [{"role": "assistant", "content": content}]
