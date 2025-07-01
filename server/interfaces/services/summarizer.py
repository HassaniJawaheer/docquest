from typing import List
from abc import ABC, abstractmethod
from server.domain.models.answer import TextAnswer
from server.domain.models.document import Doc

class Summarizer(ABC):
    @abstractmethod
    def summarize(self, docs: List[Doc]) -> TextAnswer:
        pass
