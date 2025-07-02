from typing import List
from server.domain.models.document import Doc
from server.domain.models.chunk import Chunk

class Splitter:
    """
    Service responsible for splitting documents into semantic chunks.
    """

    def split(self, documents: List[Doc]) -> List[Chunk]:
        pass
