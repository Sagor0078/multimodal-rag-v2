from rag import get_answer
from embedder import model, get_vectorstore
from sklearn.metrics.pairwise import cosine_similarity

def eval_sample(q, gt):
    history = []
    ans = get_answer(q, history)
    vects = [model.encode(chunk.page_content) for chunk in get_vectorstore().as_retriever().get_relevant_documents(q)]
    sim = cosine_similarity([model.encode(ans)], vects).max()
    print(q, "\n->", ans, "\nGround truth:", gt, "\nRelevance score:", sim)

if __name__ == "__main__":
    samples = [
        ("অনুপমের ভাষায় সুপুরুষ কাকে বলা হয়েছে?", "শুম্ভুনাথ"),
    ]
    for q, gt in samples:
        eval_sample(q, gt)
