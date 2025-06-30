from typing import List
from domain.models.document import Doc
from server.domain.models.answer import MCQAnswer
from server.interfaces.services.llm import LLM

class MCQGenerator:
    """
    Automatic MCQ generation service.
    """
    def generate_qcm(self, docs: List[Doc], llm: LLM) -> MCQAnswer:
        """
        Generates a MCQ from a document.
        """
        pass
