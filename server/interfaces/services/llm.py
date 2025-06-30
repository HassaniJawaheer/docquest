from abc import ABC, abstractmethod
from server.domain.models.answer import Answer

class LLM(ABC):
    """
    Language model call service to generate a response.
    """
    @abstractmethod
    def generate_answer(self, prompt: str) -> str:
        pass
