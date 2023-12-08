import gradio as gr
from utils import get_chat_routes,answer

chat_routes = get_chat_routes()
assert len(chat_routes) > 0

def chat(message, history, version):
    print(f"Version: {version}  Message: {message} history:{history}")
    if len(version) == 0:
        version = chat_routes[0]
    response = answer(message,version)
    print(f"response {response}")
    return response

with gr.Blocks() as demo:
    # system_prompt = gr.Textbox("You are helpful AI.", label="System Prompt")
    version = gr.Dropdown(choices=chat_routes,label='version')
    gr.ChatInterface(
        chat, additional_inputs=[version]
    )
# 7860
demo.launch(server_name='0.0.0.0')