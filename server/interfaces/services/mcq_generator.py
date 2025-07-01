from abc import ABC, abstractmethod
from typing import List
from server.domain.models.document import Doc
from server.domain.models.answer import MCQAnswer

class MCQGenerator(ABC):
    @abstractmethod
    def generate(self, docs: List[Doc]) -> MCQAnswer:
        pass
