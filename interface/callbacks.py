from constants import SESSION_ID
from utils import post_to_api, format_server_response

from constants import SESSION_ID
from utils import post_to_api, format_server_response
import gradio as gr

def handle_message(user_input, mode, chat_history):
    """
    Handles SEND button click based on the active mode.
    Returns updated chat history.
    """
    chat_history = chat_history or []
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
    bot_messages = format_server_response(response, mode)
    chat_history.extend(bot_messages)
    return chat_history


def handle_mode_change(selected_mode, chat_history, user_input):
    """
    Stores the selected mode and updates placeholder text accordingly.
    """
    chat_history = chat_history or []

    placeholder_text = ""
    if selected_mode == "Summary":
        placeholder_text = "Demander un résumé…"
    elif selected_mode == "MCQ":
        placeholder_text = "Demander un QCM…"
    elif selected_mode == "Query VectorDB":
        placeholder_text = "Poser une question sur vos documents…"
    elif selected_mode == "Query CentralDB":
        placeholder_text = "Poser une question sur la base centrale…"
    else:
        placeholder_text = "Poser votre question…"

    return (
        chat_history,
        selected_mode,
        gr.update(placeholder=placeholder_text)
    )

def handle_file_upload(uploaded_files, mode):
    if not uploaded_files:
        return gr.update(value="Aucun fichier reçu", visible=True)

    workspace = "rag"
    if mode == "Summary":
        workspace = "summarize"
    elif mode == "MCQ":
        workspace = "mcq"

    files = []
    open_files = []
    try:
        for filedata in uploaded_files:
            path = filedata.name
            f = open(path, "rb")
            open_files.append(f)
            files.append(("files", f))

        params = {
            "workspace": workspace,
            "session_id": SESSION_ID
        }

        response = post_to_api("/upload", params=params, files=files)

        status = response.get("status", "unknown")
        if status == "success":
            return gr.update(value="Upload réussi", visible=True)
        else:
            return gr.update(value=f"Upload échoué: {response.get('message')}", visible=True)
    finally:
        for f in open_files:
            f.close()

def handle_create_vector_db(mode):
    """
    Calls the backend route to create the vector database.
    Only works if the current mode is 'Query VectorDB'.
    """
    # Check if mode is correct
    if mode != "Query VectorDB":
        return gr.update(value="Please upload your documents and switch to 'Query VectorDB' mode to create the database.", visible=True)

    params = {
        "session_id": SESSION_ID
    }

    # Call backend API
    response = post_to_api("/create_vector_db", params=params)

    status = response.get("status", "unknown")
    message = response.get("message", "")

    if status == "success":
        return gr.update(value="Vector database created", visible=True)
    else:
        return gr.update(value=f"Failed to create vector database: {message}", visible=True)

