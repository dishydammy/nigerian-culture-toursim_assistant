# src/data_preprocessing.py

import pandas as pd
import json
from pathlib import Path

def load_wikipedia_json(json_path: str) -> pd.DataFrame:
    """Load Wikipedia dataset from a JSON file with encoding handling."""
    with open(json_path, "r", encoding="utf-8", errors="replace") as f:
        wiki_data = json.load(f)
        wiki_df = pd.DataFrame(wiki_data)
    
    # Ensure a 'text' column exists
    if 'text' not in wiki_df.columns:
        # If text is under a different key, adjust here
        wiki_df = wiki_df.rename(columns={wiki_df.columns[1]: 'text'})

    if 'source' in wiki_df.columns:
        # If text is under a different key, adjust here
        wiki_df = wiki_df.rename(columns={wiki_df.columns[2]: 'text'})
    
    wiki_df['source'] = 'wikipedia'
    return wiki_df

def load_hf_csv(csv_path):
    """Load Hugging Face CSV into DataFrame."""
    hf_df = pd.read_csv(csv_path)
    
    # Keep only necessary columns
    hf_df = hf_df[['text', 'link', 'token_count', 'section', 'int_score']]
    hf_df['source'] = 'huggingface'
    return hf_df

def merge_datasets(wiki_df, hf_df):
    """Merge Wikipedia and HF datasets."""
    # We’ll align columns so they can concatenate
    common_cols = ['text', 'source']
    merged_df = pd.concat(
        [
            wiki_df[common_cols],
            hf_df[common_cols]
        ],
        ignore_index=True
    )
    return merged_df

if __name__ == "__main__":
    # Paths
    wiki_json_path = Path("data/raw/wikipedia_data.json")
    hf_csv_path = Path("data/raw/naijaweb_data.csv")
    output_path = Path("data/processed/merged_data.csv")
    
    # Load datasets
    wiki_df = load_wikipedia_json(wiki_json_path)
    hf_df = load_hf_csv(hf_csv_path)
    
    # Merge
    merged_df = merge_datasets(wiki_df, hf_df)
    
    # Save merged data
    output_path.parent.mkdir(parents=True, exist_ok=True)
    merged_df.to_csv(output_path, index=False, encoding="utf-8")
    
    print(f"Merged dataset saved to {output_path}")
