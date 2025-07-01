from server.usecases import (
    UploadDocuments,
    GenerateMCQ,
    SummarizeDocuments,
    QueryVectorDB,
)

from server.infrastructure.services import (
    UploadedDocumentProcessor,
    GroqLLM,
    DefaultPromptBuilder,
    DefaultMCQGenerator
)


def get_upload_documents_usecase() -> UploadDocuments:
    processor = UploadedDocumentProcessor()
    return UploadDocuments(processor)

def get_generate_mcq_usecase() -> GenerateMCQ:
    llm = GroqLLM(api_key="your-api-key")
    prompt_builder = DefaultPromptBuilder()
    mcq_generator = DefaultMCQGenerator(llm=llm, prompt_builder=prompt_builder)
    return GenerateMCQ(mcq_generator)

def get_summarize_documents() -> SummarizeDocuments:
    summarizer = Summarizer()
    return SummarizeDocuments(summarizer)

def get_query_vector_db() -> QueryVectorDB:
    llm = LLMHandler()
    return QueryVectorDB(llm)

