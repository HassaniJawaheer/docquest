from server.domain.models.answer import Answer
from server.domain.models.query import Query
from server.domain.services.llm_handler import LLMHandler
from server.domain.services.retriever import Retriever

class QueryCoreKnowledge:
    def __init__(self, retriever: Retriever, llm: LLMHandler):
        self.retriever = retriever
        self.llm = llm
    
    def run(self, query: Query) -> Answer:
        chunks = self.retriever.retrieve_from_core(query)
        return self.llm.generate_answer(query, chunks)
