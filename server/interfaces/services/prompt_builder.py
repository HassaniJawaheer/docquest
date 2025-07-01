from abc import ABC, abstractmethod
from typing import List
from server.domain.models.document import Doc
from server.domain.models.query import Query
from server.domain.models.chunk import Chunk

class PromptBuilder(ABC):
    @abstractmethod
    def prompt_for_mcq(self, docs: List[Doc]) -> str:
        pass

    @abstractmethod
    def prompt_for_summary(self, docs: List[Doc]) -> str:
        pass

    @abstractmethod
    def prompt_for_query(self, query: Query, chunks: List[Chunk]) -> str:
        pass
