import easyocr
from preprocess import preprocess_for_ocr

reader = easyocr.Reader(['en'], gpu=True)

def extract_text(image_path):
    processed = preprocess_for_ocr(image_path)
    result = reader.readtext(processed, detail=0)
    return "\n".join(result)
