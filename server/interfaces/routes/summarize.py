from fastapi import APIRouter, Depends, HTTPException
from server.infrastructure.dependencies import get_summarize_documents
from server.usecases.summarize_documents import SummarizeDocuments
from server.interfaces.stores.workspace_manager import WorkspaceManager

router = APIRouter()

@router.post("/summarize")
def summarize(
    session_id: str,
    workspace: WorkspaceManager,
    usecase: SummarizeDocuments = Depends(get_summarize_documents),
):
    documents = workspace.get(session_id, "summarize")
    if not documents:
        raise HTTPException(status_code=404, detail="No documents found in workspace 'summarize'")
    summary = usecase.run(documents)
    return summary.model_dump