from typing import List
from server.domain.models.chunk import Chunk

class Embedder:
    """
    Embedding generation service for chunks.
    """
    def embed(self, chunks: List[Chunk]) -> List[List[float]]:
        """
        Calculates embeddings for a list of chunks.
        """
        pass