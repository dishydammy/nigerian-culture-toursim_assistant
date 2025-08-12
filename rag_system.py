class NigerianTourismRAG:
    def __init__(self):
        # placeholder: initialize embeddings/db here later
        self.initialized = False

    def load_documents(self, docs):
        # docs: list of dicts with title/content/url
        raise NotImplementedError("Implement embeddings + vector store in Week 2")

    def query(self, q, n=3):
        # return related document chunks (placeholder)
        return ["RAG not initialized yet."] 
