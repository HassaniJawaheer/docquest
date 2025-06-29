from fastapi import APIRouter, Depends
from server.infrastructure.dependencies import get_query_central_vector_db
from server.usecases.query_central_vector_db import QueryCentralVectorDB
from server.domain.models.query import Query

router = APIRouter()

@router.post("/query/central_vector_db")
def query_central_vector_db(
    query: Query,
    usecase: QueryCentralVectorDB = Depends(get_query_central_vector_db)
):
    answer = usecase.run(query)
    return answer.model_dump()
