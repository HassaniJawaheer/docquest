from server.domain.models.answer import TextAnswer
from server.domain.models.document import Doc
from server.interfaces.services.llm import LLM
from typing import List

class Summarizer:
    """
    Document-based summary generation service.
    """
    def summarize(self, docs: List[Doc], llm: LLM) -> TextAnswer:
        """
        Summarizes one or more documents.
        """
        pass
