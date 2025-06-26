from typing import List
from server.domain.models.document import Document
from server.domain.models.mcq import MCQ
from server.domain.services.mcq_generator import MCQGenerator

class GenerateMCQ:
    """
    Generates a MCQ from a selection of documents
    """
    def __init__(self, mcq_generator: MCQGenerator):
        self.mcq_generator = mcq_generator
    
    def run(self, documents: List[Document]) -> MCQ:
        return self.mcq_generator.generate(documents)