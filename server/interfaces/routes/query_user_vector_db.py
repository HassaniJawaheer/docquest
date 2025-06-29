from fastapi import APIRouter, Depends, Request, HTTPException
from server.infrastructure.dependencies import get_query_vector_db
from server.usecases.query_vector_db import QueryVectorDB
from server.domain.models.query import Query
from server.utils.request_helpers import get_session_id

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
    answer = usecase.run(query, vector_db)
    return answer.model_dump()