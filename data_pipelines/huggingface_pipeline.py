from datasets import load_dataset
import pandas as pd
from pathlib import Path
from utils.cleaning import clean_text

RAW_DIR = Path("data/raw")

# Keywords for culture/tourism/tradition
RELEVANT_KEYWORDS = [
    "culture", "tradition", "festival", "ceremony", "heritage",
    "language", "ethnic", "tribe", "people", "belief", "religion",
    "tourism", "travel", "museum", "site", "monument", "landmark", "palace",
    "grove", "park", "rock", "cave", "falls", "waterfall", "beach", "wildlife",
    "nigeria", "yoruba", "hausa", "igbo", "efik", "ijaw", "edo", "kanuri", "tiv",
    "akwa ibom", "cross river", "lagos", "kano", "abuja", "benin", "ife",
    "art", "craft", "bronze", "textile", "cloth", "aso-oke", "agbada", "gele",
    "jollof", "egusi", "amala", "suya", "nkwobi", "pepper soup", "pounded yam"
]

def is_relevant(text: str) -> bool:
    """Check if text contains any relevant keyword."""
    if not isinstance(text, str):
        return False
    lower_text = text.lower()
    return any(kw in lower_text for kw in RELEVANT_KEYWORDS)

def collect_naijaweb():
    # Load CSV dataset from Hugging Face
    dataset = load_dataset("saheedniyi/naijaweb", split="train")  # Adjust split if needed

    # Convert to pandas DataFrame
    df = pd.DataFrame(dataset)

    # Filter by relevance
    df = df[df["text"].apply(is_relevant)]

    # Clean text column
    df["text"] = df["text"].apply(clean_text)

    # Ensure output directory exists
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    # Save as CSV
    out_file = RAW_DIR / "naijaweb_data.csv"
    df.to_csv(out_file, index=False, encoding="utf-8")
    print(f"Saved {len(df)} filtered Naijaweb docs to {out_file}")

if __name__ == "__main__":
    collect_naijaweb()
