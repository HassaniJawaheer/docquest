from typing import List
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from server.interfaces.services.retriever import Retriever
from server.domain.models.query import Query
from server.domain.models.chunk import Chunk


class LangchainFaissRetriever(Retriever):
    def __init__(self, db: FAISS):
        self.retriever = db.as_retriever()
    
    def retrieve(self, query: Query) -> List[Chunk]:
        results: List[Document] = self.retriever.get_relevant_documents(query.content)

        return [
            Chunk(
                text=doc.page_content,
                metadata=doc.metadata or {}
            )
            for doc in results
        ]
