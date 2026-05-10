import gradio as gr
import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API"))

model = genai.GenerativeModel('gemini-3.1-flash-lite')

conversation_history=[]

def chat(message, history):
    conversation_history.append({"role":"User","parts":[message]})
    try:
       response = model.generate_content(conversation_history)
       conversation_history.append({"role":"model","parts":[response.text]})
       return response.text
    except Exception as e:
        return f"Error:{str(e)}"
    

demo = gr.ChatInterface(
    fn=chat,                
    title="Chat Bot",
    description="You can ask me anything | KhvanEe Api Germini Google",
    examples=["You can help me?", "តើអ្នកអាចជួយខ្ញុំបានទេ","Tell me about python"],
)

if __name__ == "__main__":
    demo.launch(share=True)