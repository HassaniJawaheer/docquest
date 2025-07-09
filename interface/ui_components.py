import gradio as gr

def build_sidebar():
    """
    Builds the sidebar with:
    - Document upload section
    - Vector DB creation section
    """
    components = {}

    with gr.Column(scale=1, min_width=200) as sidebar:
        gr.Markdown("### Documents")

        file_upload = gr.UploadButton(
            "Glisser ou choisir vos documents",
            file_types=[".pdf", ".docx", ".txt"],
            file_count="multiple",
            type="filepath"
        )
        
        upload_status = gr.Label(value="", label="État de l'upload", visible=False)

        gr.Markdown("### Base vectorielle")
        create_db_button = gr.Button("Créer la base vectorielle", variant="primary")
        vector_db_status = gr.Label(value="", label="État de la base vectorielle", visible=False)

    components["sidebar"] = sidebar
    components["file_upload"] = file_upload
    components["upload_status"] = upload_status
    components["create_db_button"] = create_db_button
    components["vector_db_status"] = vector_db_status

    return components

def build_chat_zone():
    """
    Builds the chat zone:
    - Chatbot area taking all space
    - Input at bottom
    """
    with gr.Column(scale=3) as chat_zone:
        chat_history = gr.Chatbot(label="", type="messages", scale=1, height=600)

        with gr.Row():
            user_input = gr.Textbox(
                placeholder="Poser votre question...",
                show_label=False,
                scale=8,
                lines=1
            )
            submit_button = gr.Button(
                value="", 
                scale=1, 
                icon="images/send_icon.png",
                variant="primary",
                elem_classes="circular-btn"
            )

        return chat_history, user_input, submit_button

def build_mode_buttons():
    """
    Builds horizontal circular mode buttons with icons.
    """
    buttons = {}

    with gr.Row(equal_height=True) as mode_row:
        buttons["Summary"] = gr.Button(
            value="Résumé vos documents",
            icon="images/summary_icon.png",
            variant="secondary",
            elem_classes="circular-btn"
        )
        buttons["MCQ"] = gr.Button(
            value="Créer un QCM",
            icon="images/mcq_icon.png",
            variant="secondary",
            elem_classes="circular-btn"
        )
        buttons["Query VectorDB"] = gr.Button(
            value="Intérroger vos documents",
            icon="images/user_vect_db_icon.png",
            variant="secondary",
            elem_classes="circular-btn"
        )
        buttons["Query CentralDB"] = gr.Button(
            value="Intérroger la base central",
            icon="images/central_vect_db_icon.png",
            variant="secondary",
            elem_classes="circular-btn"
        )

    return buttons


def build_mcq_block():
    """
    Builds a MCQ interaction block.
    """
    with gr.Column() as mcq_block:
        mcq_question = gr.Markdown("MCQ Question will appear here")
        mcq_options = gr.Radio(choices=[], label="Choose an answer")
        submit_mcq = gr.Button("Submit Answer")
    
    return mcq_block

