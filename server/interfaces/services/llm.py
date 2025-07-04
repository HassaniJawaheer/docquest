from abc import ABC, abstractmethod
from typing import List
from server.domain.models.answer import Answer
from server.domain.models.chat_message import ChatMessage

class LLM(ABC):
    """
    Language model call service to generate a response.
    """
    @abstractmethod
    def generate_answer(self, prompt: str) -> str:
        pass
    def generate_chat_answer(self, history: List[ChatMessage], prompt: str) -> str:
        pass