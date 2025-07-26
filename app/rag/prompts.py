
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

RAG_PROMPT = ChatPromptTemplate.from_messages([
    # System Instruction
    ("system", """
Answer the question **only** based on the context provided below.  
If the answer is not found in the context, respond with: **"উত্তর খুঁজে পাওয়া যায়নি!"**

📘 Context:
{context}

🧠 Conversation History (if any):
{history}
""".strip()),

    # Example
    ("human", "❓ Question:\nবিয়ের সময় কল্যাণীর প্রকৃত বয়স কত ছিল?"),
    ("ai", "📝 Answer (English/Bangla):\n১৫ বছর"),

    # User Question Placeholder
    ("human", "❓ Question:\n{question}"),
    ("ai", "📝 Answer (English/Bangla):"),
])

__all__ = ["RAG_PROMPT"]
