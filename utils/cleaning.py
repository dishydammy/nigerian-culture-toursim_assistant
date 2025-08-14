import re
from bs4 import BeautifulSoup

def clean_text(text: str) -> str:
    if not text:
        return ""
    # Remove HTML tags
    text = BeautifulSoup(text, "html.parser").get_text()
    # Remove special characters (keeping basic punctuation)
    text = re.sub(r"[^a-zA-Z0-9\s.,;:!?'\-]", " ", text)
    # Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()
    return text
