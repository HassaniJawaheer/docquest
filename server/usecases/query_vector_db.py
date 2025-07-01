from langchain_community.vectorstores import FAISS
from typing import List
from server.domain.models.answer import TextAnswer
from server.domain.models.chunk import Chunk
from server.domain.models.query import Query
from server.interfaces.services.llm import LLM
from server.infrastructure.services.langchain_faiss_retriever import LangchainFaissRetriever

class QueryVectorDB:
    def __init__(self, llm: LLM):
        self.llm = llm
        
    
    def run(self, query: Query, vector_db: FAISS) -> TextAnswer:
        retriever = LangchainFaissRetriever(vector_db)
        chunks: List[Chunk] = retriever.retrieve(query)
        return self.llm.generate_answer(query, chunks)
