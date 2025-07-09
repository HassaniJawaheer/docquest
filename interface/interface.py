import gradio as gr

from ui_components import build_sidebar, build_chat_zone, build_mode_buttons
from callbacks import (
    handle_message,
    handle_mode_change,
    handle_file_upload,
)
from constants import MODES

# Custom CSS
custom_css = """
.circular-btn button {
    border-radius: 50% !important;
    width: 50px !important;
    height: 50px !important;
    padding: 0 !important;
    text-align: center;
}
"""

with gr.Blocks(title="DocQuest", css=custom_css) as demo:
    # Current mode state
    current_mode = gr.State(value="Query CentralDB")  # default mode

    with gr.Row():
        # Left panel (sidebar)
        sidebar = build_sidebar()

        with gr.Column(scale=3):
            # Chat zone (chat display + input)
            chat_history, user_input, submit_button = build_chat_zone()

            # Mode buttons (Résumé, QCM, …)
            mode_buttons = build_mode_buttons()

    # Wire callbacks
    user_input.submit(
        handle_message,
        inputs=[user_input, current_mode, chat_history],
        outputs=[chat_history],
    )

    for mode_name, mode_button in mode_buttons.items():
        mode_button.click(
            handle_mode_change,
            inputs=[gr.State(mode_name), chat_history],
            outputs=[chat_history, current_mode],
        )

    submit_button.click(
        handle_message,
        inputs=[user_input, current_mode, chat_history],
        outputs=[chat_history],
    )

    sidebar["file_upload"].upload(
        handle_file_upload,
        inputs=[sidebar["file_upload"], current_mode],
        outputs=[sidebar["upload_status"]],
    )

if __name__ == "__main__":
    demo.launch(allowed_paths=["images"])
