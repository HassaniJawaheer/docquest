from abc import ABC, abstractmethod
from typing import List
from server.domain.models.chunk import Chunk

class VectorDatabaseBuilder(ABC):
    @abstractmethod
    def build(self, chunks: List[Chunk]) -> None:
        pass
