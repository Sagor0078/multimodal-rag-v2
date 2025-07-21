from langchain_core.prompts import ChatPromptTemplate

RAG_PROMPT = ChatPromptTemplate.from_template("""
Use context and conversation history for answer.
If answer isn't in context, reply "উত্তর খুঁজে পাওয়া যায়নি।"

Context:
{context}

History:
{history}

Question:
{question}

Answer (বাংলা/English):
""")
