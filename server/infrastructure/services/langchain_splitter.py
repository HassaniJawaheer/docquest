from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter
from server.domain.models.document import Doc
from server.domain.models.chunk import Chunk
from server.interfaces.services.splitter import Splitter

class LangchainSplitter(Splitter):
    def __init__(self, chunk_size: int = 2000, chunk_overlap: int = 200):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

    def split(self, documents: List[Doc]) -> List[Chunk]:
        chunks = []
        for doc in documents:
            lc_docs = self.splitter.create_documents(
                [doc.text],
                metadatas=[doc.metadata or {}]
            )
            for i, d in enumerate(lc_docs):
                chunks.append(Chunk(
                    text=d.page_content,
                    metadata=d.metadata,
                    position=i,
                    doc_id=doc.metadata.get("source") if doc.metadata else None
                ))
        return chunks
