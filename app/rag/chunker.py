from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List

def split_text(text: str) -> List[str]:
    """
    Splits the input text into overlapping chunks using a recursive character-based splitter.

    Args:
        text (str): The raw input text.

    Returns:
        List[str]: A list of text chunks, each with `chunk_size=800` and `chunk_overlap=200`.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=200,
        separators=["\n\n", "\n", ".", "।", "!", "?", " ", ""]
    )
    return splitter.split_text(text)
