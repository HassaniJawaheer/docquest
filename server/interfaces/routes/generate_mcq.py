from fastapi import APIRouter, HTTPException, Depends
from server.interfaces.dependencies import get_generate_mcq_usecase
from server.usecases.generate_mcq import GenerateMCQ
from server.interfaces.services.workspace_manager import WorkspaceManager

router = APIRouter()

@router.post("/generate_mcq")
def generate_mcq(
    session_id: str,
    workspace: WorkspaceManager,
    usecase: GenerateMCQ = Depends(get_generate_mcq_usecase),
):
    documents = workspace.get(session_id, "mcq")
    if not documents:
        raise HTTPException(status_code=404, detail="No documents found in workspace 'mcq'")
    mcq = usecase.run(documents)
    return mcq.model_dump()