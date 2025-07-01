from typing import List
from server.domain.models.document import Doc
from server.domain.models.answer import MCQAnswer
from server.interfaces.services.mcq_generator import MCQGenerator

class GenerateMCQ:
    """
    Generates a MCQ from a selection of documents
    """
    def __init__(self, mcq_generator: MCQGenerator):
        self.mcq_generator = mcq_generator
    
    def run(self, documents: List[Doc]) -> MCQAnswer:
        return self.mcq_generator.generate(documents)