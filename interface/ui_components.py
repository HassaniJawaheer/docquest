import gradio as gr

def build_sidebar():
    """
    Builds the left sidebar panel with:
    - Documents drag-and-drop zone on bottom
    """
    components = {}

    with gr.Column(scale=1, min_width=200) as sidebar:
        gr.Markdown("### Documents")

        file_upload = gr.File(
            file_types=[".pdf", ".docx", ".txt"],
            label="Glisser vos documents ici",
            interactive=True
        )

    components["sidebar"] = sidebar
    components["file_upload"] = file_upload
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
        buttons["Resume"] = gr.Button(
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
        buttons["VectorDB Query"] = gr.Button(
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

