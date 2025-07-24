from langchain_core.prompts import ChatPromptTemplate

RAG_PROMPT = ChatPromptTemplate.from_template("""
Answer the question **only** based on the context provided below.  
If the answer is not found in the context, respond with: **"উত্তর খুঁজে পাওয়া যায়নি!"**

📘 Context:
{context}

🧠 Conversation History (if any):
{history}

❓ Question:
{question}

📝 Answer (English/Bangla):
""".strip())

__all__ = ["RAG_PROMPT"]
