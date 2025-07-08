import gradio as gr

def build_sidebar():
    """
    Builds the left sidebar panel with:
    - Conversation list en haut
    - New conversation button en dessous
    - Documents drag-and-drop zone en bas
    """
    components = {}

    with gr.Column(scale=1, min_width=200) as sidebar:
        gr.Markdown("### Conversations")

        conversations_list = gr.HighlightedText(
            value=[("No conversations yet.", "default")],
            scale=1,
            show_label=False
        )

        new_conversation_button = gr.Button("New Conversation", variant="primary")

        gr.Markdown("---")

        gr.Markdown("### Documents")

        file_upload = gr.File(
            file_types=[".pdf", ".docx", ".txt"],
            label="Glisser vos documents ici",
            interactive=True
        )

    components["sidebar"] = sidebar
    components["conversation_list"] = conversations_list
    components["new_conversation_button"] = new_conversation_button
    components["file_upload"] = file_upload
    return components


def build_chat_zone():
    """
    Builds the chat zone:
    - Chatbot area taking all space
    - Input at bottom
    """
    with gr.Column(scale=3) as chat_zone:
        logo = gr.HTML("""
            <div style="text-align: center; margin: 20px 0;">
                <img src='.\docquest.png' style="width: 80px; height: auto; border-radius: 0;" alt="DocQuest Logo">
            </div>
        """)


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
                icon="file/send_icon.png",
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
            value="",
            icon="file/summary_icon.png",
            variant="secondary",
            elem_classes="circular-btn"
        )
        buttons["MCQ"] = gr.Button(
            value="",
            icon="file/mcq_icon.png",
            variant="secondary",
            elem_classes="circular-btn"
        )
        buttons["VectorDB Query"] = gr.Button(
            value="",
            icon="file/user_vect_db_icon.png",
            variant="secondary",
            elem_classes="circular-btn"
        )
        buttons["Base Centrale Query"] = gr.Button(
            value="",
            icon="file/central_vect_db_icon.png",
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

