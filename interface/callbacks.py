from constants import SESSION_ID
from utils import post_to_api, format_server_response

from constants import SESSION_ID
from utils import post_to_api, format_server_response

def handle_message(user_input, mode, chat_history):
    """
    Handles SEND button click based on the active mode.
    Returns updated chat history.
    """
    chat_history = chat_history or []
    print(mode)
    if mode not in ["Summary", "MCQ", "Query CentralDB", "Query VectorDB"]:
        chat_history.append({"role": "assistant", "content": "Problème coté client."})
        return chat_history

    params = {"session_id": SESSION_ID}
    payload = None

    if mode == "Summary":
        chat_history.append({"role": "user", "content": "Crée un Résumé."})
        endpoint = "/summarize"

    elif mode == "MCQ":
        chat_history.append({"role": "user", "content": "Crée un QCM."})
        endpoint = "/generate_mcq"

    elif mode == "Query CentralDB":
        if not user_input.strip():
            chat_history.append({"role": "assistant", "content": "Veuillez poser une question pour interroger la base centrale."})
            return chat_history
        chat_history.append({"role": "user", "content": user_input})
        endpoint = "/query/central_vector_db"
        payload = {"content": user_input}

    elif mode == "Query VectorDB":
        if not user_input.strip():
            chat_history.append({"role": "assistant", "content": "Veuillez poser une question pour interroger la base utilisateur."})
            return chat_history
        chat_history.append({"role": "user", "content": user_input})
        endpoint = "/query/user_vector_db"
        payload = {"content": user_input}

    # Envoie la requête
    response = post_to_api(endpoint, params=params, json=payload)
    print("Réponse brute serveur :", response)
    bot_messages = format_server_response(response, mode)
    chat_history.extend(bot_messages)
    print(chat_history)
    return chat_history


def handle_mode_change(selected_mode, chat_history):
    """
    Stores the selected mode.
    """
    chat_history = chat_history or []

    return (
        chat_history,
        selected_mode,
    )

def handle_file_upload(file_paths, mode):
    """
    Uploads multiple files in one request to the appropriate workspace based on mode.
    Returns a status message.
    """
    workspace = "rag"  # default
    if mode == "Summary":
        workspace = "summarize"
    elif mode == "MCQ":
        workspace = "mcq"

    # Build list of files as expected by FastAPI
    import os
    files = []
    for file_path in file_paths:
        if file_path and os.path.isfile(file_path):
            files.append(("files", open(file_path, "rb")))

    params = {
        "workspace": workspace,
        "session_id": SESSION_ID
    }

    response = post_to_api("/upload", params=params, files=files)

    status = response.get("status", "unknown")
    message = response.get("message", "")

    if status == "success":
        result_text = "All files uploaded successfully."
    else:
        result_text = f"Upload failed: {message}"

    return [{"role": "assistant", "content": result_text}]
