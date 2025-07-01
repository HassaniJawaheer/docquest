from fastapi import APIRouter, Depends, Request
from typing import List
from server.domain.models.chunk import Chunk
from server.infrastructure.dependencies import get_query_vector_db
from server.usecases.query_vector_db import QueryVectorDB
from server.domain.models.query import Query
from server.utils.request_helpers import get_session_id
from server.infrastructure.services.langchain_faiss_retriever import LangchainFaissRetriever

router = APIRouter()

@router.post("/query/user_vector_db")
def query_user_vector_db(
    query: Query,
    request: Request,
    usecase: QueryVectorDB = Depends(get_query_vector_db)
):
    # Get session ID from request
    session_id = get_session_id(request)
    
    vector_db = request.app.state.vector_db_manager.get(session_id, 'central')
    retriever = LangchainFaissRetriever(vector_db)
    chunks: List[Chunk] = retriever.retrieve(query)
    answer = usecase.run(query, chunks)
    return answer.model_dump()