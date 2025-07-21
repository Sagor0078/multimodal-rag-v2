from fastapi import FastAPI
from pydantic import BaseModel
from rag import get_answer
from memory import get_chat_history, save_message

app = FastAPI()

class Query(BaseModel):
    user_id: str
    question: str

@app.post("/query/")
def query_rag(x: Query):
    history = get_chat_history(x.user_id)
    answer = get_answer(x.question, history)
    save_message(x.user_id, "user", x.question)
    save_message(x.user_id, "assistant", answer)
    return {"question": x.question, "answer": answer}
