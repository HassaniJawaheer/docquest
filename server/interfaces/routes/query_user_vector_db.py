from fastapi import APIRouter, Depends
from server.infrastructure.dependencies import get_query_user_vector_db
from server.usecases.query_user_vector_db import QueryUserVectorDB
from server.domain.models.query import Query

router = APIRouter()

@router.post("/query/user_vector_db")
def query_user_vector_db(
    query: Query,
    session_id: str,
    usecase: QueryUserVectorDB = Depends(get_query_user_vector_db),
):
    answer = usecase.run(query, session_id)
    return answer.model_dump()