from pdf2image import convert_from_path
import pytesseract

def extract_text_ocr(pdf_path: str) -> str:
    pages = convert_from_path(pdf_path)
    full_text = ""
    for img in pages:
        text = pytesseract.image_to_string(img, lang="ben")
        full_text += text + "\n"
    return full_text