from server.usecases import (
    UploadDocuments,
    GenerateMCQ,
    SummarizeDocuments,
    QueryVectorDB,
)

from server.infrastructure.services import (
    UploadedDocumentProcessor
)


def get_upload_documents_usecase() -> UploadDocuments:
    processor = UploadedDocumentProcessor()
    return UploadDocuments(processor)

def get_generate_mcq_usecase() -> GenerateMCQ:
    mcq_generator = MCQGenerator()
    return GenerateMCQ(mcq_generator)

def get_summarize_documents() -> SummarizeDocuments:
    summarizer = Summarizer()
    return SummarizeDocuments(summarizer)

def get_query_vector_db() -> QueryVectorDB:
    llm = LLMHandler()
    return QueryVectorDB(llm)
