import google.generativeai as genai
import os
from app.rag.prompts import RAG_PROMPT
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

def generate_answer(question, context, history=""):
    prompt_text = RAG_PROMPT.format(
        context=context,
        history=history,
        question=question
    )
    response = model.generate_content(prompt_text)
    return response.text
