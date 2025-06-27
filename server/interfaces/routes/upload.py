from fastapi import APIRouter, UploadFile, HTTPException, Depends
from typing import List
from server.usecases.upload_documents import UploadDocuments
from server.interfaces.dependencies import get_upload_documents_usecase

router = APIRouter()

@router.post("/upload")
async def upload_documents(
    files: List[UploadFile],
    workspace: str,
    session_id: str,
    usecase: UploadDocuments = Depends(get_upload_documents_usecase)
):
    try:
        file_bytes = [await f.read() for f in files]
        usecase.run(file_bytes, workspace, session_id)
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))