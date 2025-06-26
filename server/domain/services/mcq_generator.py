from domain.models.document import Document
from server.domain.models.mcq import MCQ

class MCQGenerator:
    """
    Automatic MCQ generation service.
    """
    def generate(self, document: Document) -> MCQ:
        """
        Generates a MCQ from a document.
        """
        pass
