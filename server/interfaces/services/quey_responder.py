from typing import List
from abc import ABC, abstractmethod
from server.domain.models.chunk import Chunk
from server.domain.models.query import Query
from server.domain.models.answer import TextAnswer
from server.domain.models.chat_message import ChatMessage

class QueryResponder(ABC):
    @abstractmethod
    def response(self, query: Query, chunks: List[Chunk], history: List[ChatMessage]) -> TextAnswer:
        pass
