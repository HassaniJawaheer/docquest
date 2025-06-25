from server.domain.models.chunk import Chunk
from server.domain.models.query import Query
from typing import List

class Retriever:
    """
    Search service for relevant chunks based on a query.
    """
    def retrieve(self, query: Query, chunks: List[Chunk]) -> List[Chunk]:
        """
        Returns the most relevant chunks for the query.
        """
        pass
