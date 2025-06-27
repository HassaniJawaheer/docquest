from typing import List
from server.domain.models.document import Document, Chunk

class Splitter:
    """
    Service responsible for splitting documents into semantic chunks.
    """

    def split(self, documents: List[Document]) -> List[Chunk]:
        pass
