import re
from ingest_pdf import extract_layout_text  # wrapper around pdf2htmlEX or OCR
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from embedder import get_vectorstore

def chunk_and_embed(pdf_path):
    text = extract_layout_text(pdf_path)
    text = re.sub(r'\n{2,}', '\n\n', text.strip())
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=200)
    docs = [Document(page_content=chunk) for chunk in splitter.split_text(text)]
    vectordb = get_vectorstore()
    vectordb.add_documents(docs)
    print(f"✅ Embedded {len(docs)} chunks")
