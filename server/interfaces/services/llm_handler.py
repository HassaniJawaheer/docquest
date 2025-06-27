from server.domain.models.query import Query
from server.domain.models.chunk import Chunk
from server.domain.models.answer import Answer
from typing import List

class LLMHandler:
    """
    Language model call service to generate a response.
    """
    def generate_answer(self, query: Query, context: List[Chunk]) -> Answer:
        """
        Generates an answer from a question and a context
        """
        pass
