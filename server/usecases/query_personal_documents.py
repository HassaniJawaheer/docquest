from server.domain.models.answer import Answer
from server.domain.models.query import Query
from server.interfaces.services.llm_handler import LLMHandler
from server.interfaces.services.retriever import Retriever

class QueryPersonalDocuments:
    def __init__(self, retriever: Retriever, llm: LLMHandler):
        self.retriever = retriever
        self.llm = llm
    
    def run(self, query: Query, session_id: str) -> Answer:
        chunks = self.retriever.retrieve_from_session(query, session_id)
        return self.llm.generate_answer(query, chunks)
