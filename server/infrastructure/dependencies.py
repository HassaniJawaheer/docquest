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
    DefaultMCQGenerator,
    DefaultSummarizer,
    DefaultQueryResponder
)

def get_upload_documents_usecase() -> UploadDocuments:
    processor = UploadedDocumentProcessor()
    return UploadDocuments(processor)

def get_generate_mcq_usecase() -> GenerateMCQ:
    llm = GroqLLM()
    prompt_builder = DefaultPromptBuilder()
    mcq_generator = DefaultMCQGenerator(llm=llm, prompt_builder=prompt_builder)
    return GenerateMCQ(mcq_generator)

def get_summarize_documents() -> SummarizeDocuments:
    llm = GroqLLM()
    prompt_builder = DefaultPromptBuilder()
    summarizer = DefaultSummarizer(llm=llm, prompt_builder=prompt_builder)
    return SummarizeDocuments(summarizer)

def get_query_vector_db() -> QueryVectorDB:
    llm = GroqLLM()
    prompt_builder = DefaultPromptBuilder()
    query_responder = DefaultQueryResponder(llm=llm, prompt_builder=prompt_builder)
    return QueryVectorDB(query_responder)

