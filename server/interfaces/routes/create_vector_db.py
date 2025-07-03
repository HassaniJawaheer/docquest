from fastapi import APIRouter, Depends, Request, HTTPException
import os
from server.infrastructure.services.faiss_vector_db_builder import FaissVectorDatabaseBuilder
from server.infrastructure.services.langchain_splitter import LangchainSplitter
from server.utils.request_helpers import get_session_id

CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 1000))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 200))

router = APIRouter()

@router.post("/create_vector_db")
def create_user_vector_db(request: Request):
    # Get session ID from request
    session_id = get_session_id(request)

    # Retrieve documents from workspace
    documents = request.app.state.workspace_manager.get(session_id, "rag")
    if not documents:
        raise HTTPException(status_code=404, detail="No documents found in workspace 'rag'")

    # Split documents into chunks
    splitter = LangchainSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    chunks = splitter.split(documents)

    # Build FAISS vector DB
    db_builder = FaissVectorDatabaseBuilder(request.app.state.embedding_model)
    user_db = db_builder.build(chunks)

    # Register the new DB under the session ID
    request.app.state.vector_db_manager.set(session_id, user_db)

    return {"status": "success", "message": f"Vector DB created for session {session_id}"}
