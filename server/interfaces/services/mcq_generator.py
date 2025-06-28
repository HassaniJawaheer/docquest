from domain.models.document import Doc
from server.domain.models.mcq import MCQ

class MCQGenerator:
    """
    Automatic MCQ generation service.
    """
    def generate(self, document: Doc) -> MCQ:
        """
        Generates a MCQ from a document.
        """
        pass
