from langchain_core.documents import Document
from server.domain.models.chunk import Chunk

def docs_to_chunks(documents: list[Document]) -> list[Chunk]:
    return [
        Chunk(
            content=doc.page_content,
            metadata=doc.metadata or {}
        )
        for doc in documents
    ]


def chunks_to_docs(chunks: list[Chunk]) -> list[Document]:
    return [
        Document(
            page_content=chunk.content,
            metadata=chunk.metadata or {}
        )
        for chunk in chunks
    ]