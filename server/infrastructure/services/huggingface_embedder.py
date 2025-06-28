from langchain.embeddings import HuggingFaceEmbeddings
from server.interfaces.services.embedder import Embedder

class HuggingFaceEmbedder(Embedder):
    def __init__(self, model_name: str = "intfloat/e5-small-v2"):
        self.model = HuggingFaceEmbeddings(
            model_name=model_name,
            model_kwargs={"device": "cpu"}
        )

    def get_model(self):
        return self.model
