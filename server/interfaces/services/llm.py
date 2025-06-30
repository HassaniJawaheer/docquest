from server.domain.models.query import Query
from server.domain.models.chunk import Chunk
from server.domain.models.answer import Answer
from typing import List

class LLM:
    """
    Language model call service to generate a response.
    """
    def generate_answer(self, prompt: str) -> Answer:
        pass
