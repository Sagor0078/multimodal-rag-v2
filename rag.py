from langchain_google_genai import ChatGoogleGenerativeAI
from embedder import get_vectorstore
from prompts import RAG_PROMPT

llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)
retriever = get_vectorstore().as_retriever(search_type="similarity", k=4)

def format_history(history):
    return "\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in history])

def get_answer(question, history):
    docs = retriever.get_relevant_documents(question)
    context = "\n\n".join([doc.page_content for doc in docs])
    formatted_history = format_history(history)
    prompt = RAG_PROMPT.format(context=context, history=formatted_history, question=question)
    resp = llm.invoke(prompt).content.strip()
    return resp
