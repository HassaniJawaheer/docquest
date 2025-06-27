from server.domain.models.answer import Answer
from server.domain.models.query import Query
from server.interfaces.services.llm_handler import LLMHandler
from server.interfaces.services.retriever import Retriever

class QueryCoreDocuments:
    def __init__(self, retriever: Retriever, llm: LLMHandler):
        self.retriever = retriever
        self.llm = llm
    
    def run(self, query: Query) -> Answer:
        chunks = self.retriever.retrieve_from_core(query)
        return self.llm.generate_answer(query, chunks)
