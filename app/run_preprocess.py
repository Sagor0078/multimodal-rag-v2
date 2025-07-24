from app.utils.extractor import extract_text_ocr
from app.rag.chunker import split_text
from app.rag.embedding import embed_chunks
from app.rag.retriver import Retriever

text = extract_text_ocr("data/HSC26-Bangla1st-Paper.pdf")
chunks = split_text(text)
embeds = embed_chunks(chunks)

retr = Retriever()
retr.build(embeds, chunks)
print("Index built and saved.")
