from fastapi import APIRouter, UploadFile, HTTPException, Depends, Request
from typing import List
from server.usecases.upload_documents import UploadDocuments
from server.infrastructure.dependencies import get_upload_documents_usecase
from server.utils.request_helpers import get_session_id

router = APIRouter()

@router.post("/upload")
async def upload_documents(
    files: List[UploadFile],
    workspace: str,
    request: Request,
    usecase: UploadDocuments = Depends(get_upload_documents_usecase)
):
    # Get session ID from request
    session_id = get_session_id(request)
    
    try:
        workspace_manager = request.app.state.workspace_manager
        await usecase.run(files, workspace, session_id, workspace_manager)
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
