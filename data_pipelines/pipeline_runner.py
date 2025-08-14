from data_pipelines.wikipedia_pipeline import collect_wikipedia
from data_pipelines.huggingface_pipeline import collect_naijaweb

if __name__ == "__main__":
    print("=== Running Wikipedia pipeline ===")
    collect_wikipedia()

    print("\n=== Running Naijaweb pipeline ===")
    collect_naijaweb()

    print("\n✅ Both pipelines complete!")
