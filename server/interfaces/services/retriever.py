from abc import ABC, abstractmethod
from server.domain.models.query import Query
from server.domain.models.chunk import Chunk
from typing import List

class Retriever(ABC):
    @abstractmethod
    def retrieve(self, query: Query) -> List[Chunk]:
        pass

