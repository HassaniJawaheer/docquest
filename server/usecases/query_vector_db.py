from typing import List
from server.domain.models.chunk import Chunk
from server.domain.models.query import Query
from server.domain.models.answer import TextAnswer
from server.domain.models.chat_message import ChatMessage
from server.interfaces.services.quey_responder import QueryResponder

class QueryVectorDB:
    def __init__(self, query_responder: QueryResponder):
        self.query_responder = query_responder
        
    def run(self, query: Query, chunks: List[Chunk], history: List[ChatMessage]) -> TextAnswer:
        return self.query_responder.response(query, chunks, history)
