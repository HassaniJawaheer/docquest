from constants import SESSION_ID
from utils import post_to_api, format_server_response

def handle_message(user_input, mode):
    """
    Handles SEND button click based on the active mode.
    Returns updated chat history.
    """
    if mode == "Summary":
        endpoint = "/summarize"
        params = {"session_id": SESSION_ID}
        response = post_to_api(endpoint, params=params)
        return format_server_response(response, mode)

    elif mode == "MCQ":
        endpoint = "/generate_mcq"
        params = {"session_id": SESSION_ID}
        response = post_to_api(endpoint, params=params)
        return format_server_response(response, mode)

    elif mode == "Query CentralDB":
        if not user_input.strip():
            return [{"role": "assistant", "content": "Poser une question."}]
        endpoint = "/query/central_vector_db"
        params = {"session_id": SESSION_ID}
        payload = {"content": user_input}
        response = post_to_api(endpoint, params=params, json=payload)
        return format_server_response(response, mode)

    elif mode == "Query VectorDB":
        if not user_input.strip():
            return [{"role": "assistant", "content": "Poser une question."}]
        endpoint = "/query/user_vector_db"
        params = {"session_id": SESSION_ID}
        payload = {"content": user_input}
        response = post_to_api(endpoint, params=params, json=payload)
        return format_server_response(response, mode)

    else:
        return [{"role": "assistant", "content": "Unknown mode."}]


def handle_mode_change(selected_mode, conversations):
    """
    Stores the selected mode. Updates the conversation list.
    """
    conversations = conversations or []
    conversations.append((f"{selected_mode} #{len(conversations)+1}", "info"))

    return (
        [[(f"Activated mode : {selected_mode}", "")]],
        selected_mode,
        conversations,
        conversations
    )


def handle_new_conversation(conversations):
    """
    Resets the chat history and keeps conversations as is.
    """
    return [], conversations, conversations


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
