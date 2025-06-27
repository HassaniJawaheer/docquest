from typing import List
from server.domain.models.document import Document
from server.domain.models.summary import Summary
from server.interfaces.services.summarizer import Summarizer

class SummarizeDocuments:
    """
    Generates a summary from a selection of documents
    """
    def __init__(self, summmarizer: Summarizer):
        self.summarizer = summmarizer

    def run(self, documents: List[Document]) -> Summary:
        return self.summarizer.summarize(documents)