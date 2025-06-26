from typing import List
from server.domain.models.document import Document

class CorpusLoader:
    """
    Abstract service to load a batch of Documents from a local folder path.
    """

    def load_from_path(self, path: str) -> List[Document]:
        pass
