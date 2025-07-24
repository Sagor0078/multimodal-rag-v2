from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.rag import embedding, retriver, generator, evaluator
from app.core.memory import get_short_term, store_short_term

router = APIRouter()
retriever_engine = retriver.Retriever()
retriever_engine.load()

# --- Pydantic Request Model ---
class AskRequest(BaseModel):
    question: str
    user_id: str = "default"
    top_k: int = 3

# --- Response Model (Optional) ---
class AskResponse(BaseModel):
    answer: str
    groundedness: float

# --- API Endpoint ---
@router.post("/ask", response_model=AskResponse)
async def ask(request: AskRequest):
    try:
        question = request.question
        user_id = request.user_id
        top_k = request.top_k

        # Memory (short-term)
        store_short_term(user_id, question)
        history = get_short_term(user_id)

        # Embedding + Context
        question_embedding = embedding.EMBED_MODEL.encode([question])[0]
        context_chunks = retriever_engine.query(question_embedding, k=top_k)
        context = "\n".join(context_chunks + history)

        # Generate answer and score
        answer = generator.generate_answer(question, context)
        grounded_score = evaluator.score_groundedness(question, context_chunks)

        return AskResponse(answer=answer, groundedness=grounded_score)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to answer: {str(e)}")
