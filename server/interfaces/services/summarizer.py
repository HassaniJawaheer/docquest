from server.domain.models.document import Document
from server.domain.models.summary import Summary
from typing import List

class Summarizer:
    """
    Document-based summary generation service.
    """
    def summarize(self, documents: List[Document]) -> Summary:
        """
        Summarizes one or more documents.
        """
        pass
