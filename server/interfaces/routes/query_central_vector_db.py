from fastapi import APIRouter, Depends, Request, HTTPException
from typing import List
from server.domain.models.chunk import Chunk
from server.infrastructure.dependencies import get_query_vector_db
from server.usecases.query_vector_db import QueryVectorDB
from server.domain.models.query import Query
from server.utils.request_helpers import get_session_id
from server.infrastructure.services.langchain_faiss_retriever import LangchainFaissRetriever

router = APIRouter()

@router.post("/query/central_vector_db")
def query_central_vector_db(
    query: Query,
    request: Request,
    usecase: QueryVectorDB = Depends(get_query_vector_db)
):  
    # Retrieve the central shared vector DB
    try:
        vector_db = request.app.state.vector_db_manager.get("central")
    except KeyError:
        raise HTTPException(status_code=404, detail="Central vector DB not found.")

    # Retrieve relevant chunks from the vector DB
    retriever = LangchainFaissRetriever(vector_db)
    chunks: List[Chunk] = retriever.retrieve(query)

    # Run the query use case to generate an answer
    answer = usecase.run(query, chunks)

    # Return the answer as JSON
    return answer.model_dump()
