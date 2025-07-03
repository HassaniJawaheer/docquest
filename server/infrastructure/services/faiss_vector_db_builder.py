from typing import List
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from server.infrastructure.adapters.langchain_chunk_converter import chunks_to_docs
from server.interfaces.services.vector_database_builder import VectorDatabaseBuilder
from server.interfaces.services.embedder import Embedder
from server.domain.models.chunk import Chunk

class FaissVectorDatabaseBuilder(VectorDatabaseBuilder):
    def __init__(self, embedder: Embedder):
        self.embedder = embedder

    def build(self, chunks: List[Chunk]) -> FAISS:
        docs: list[Document] = chunks_to_docs(chunks)
        return FAISS.from_documents(docs, self.embedder)
