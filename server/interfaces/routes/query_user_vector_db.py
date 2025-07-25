from fastapi import APIRouter, Depends, Request, HTTPException
from typing import List
from server.domain.models.chat_message import ChatMessage
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
    # Extract session ID from the request
    session_id = get_session_id(request)

    # Retrieve the user-specific vector DB
    try:
        vector_db = request.app.state.vector_db_manager.get(session_id)
    except KeyError:
        raise HTTPException(status_code=404, detail=f"No vector DB found for session {session_id}")

    # Retrieve relevant chunks from the vector DB using the retriever
    retriever = LangchainFaissRetriever(vector_db)
    chunks: List[Chunk] = retriever.retrieve(query)

    history = request.app.state.chat_history_manager.get(session_id)

    # Run the query use case to generate an answer
    answer = usecase.run(query, chunks, history)
       
    for msg in [
        ChatMessage(role="user", content=query.content),
        ChatMessage(role="assistant", content=answer.content)
    ]:
        request.app.state.chat_history_manager.append(session_id, msg)

    
    # Return the answer as JSON
    return answer.model_dump()