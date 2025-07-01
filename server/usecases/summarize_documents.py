from typing import List
from server.domain.models.answer import TextAnswer
from server.domain.models.document import Doc
from server.interfaces.services.summarizer import Summarizer

class SummarizeDocuments:
    """
    Generates a summary from a selection of documents
    """
    def __init__(self, summarizer: Summarizer):
        self.summarizer = summarizer

    def run(self, documents: List[Doc]) -> TextAnswer:
        return self.summarizer.summarize(documents)