from sklearn.metrics.pairwise import cosine_similarity
from app.rag.embedding import EMBED_MODEL


def score_groundedness(question, retrieved_chunks):
    question_emb = EMBED_MODEL.encode([question])[0]
    chunks_emb = EMBED_MODEL.encode(retrieved_chunks)
    scores = cosine_similarity([question_emb], chunks_emb)
    return float(max(scores[0]))
