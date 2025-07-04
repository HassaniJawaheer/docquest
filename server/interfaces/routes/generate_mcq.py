from fastapi import APIRouter, HTTPException, Depends, Request
from server.infrastructure.dependencies import get_generate_mcq_usecase
from server.usecases.generate_mcq import GenerateMCQ
from server.utils.request_helpers import get_session_id

router = APIRouter()

@router.post("/generate_mcq")
def generate_mcq(
    request: Request,
    usecase: GenerateMCQ = Depends(get_generate_mcq_usecase),
):
    # Extract session ID from the request
    session_id = get_session_id(request)

    # Retrieve documents from the 'rag' workspace
    documents = request.app.state.workspace_manager.get(session_id, "mcq")
    if not documents:
        raise HTTPException(status_code=404, detail="No documents found in workspace 'mcq'")

    # Generate MCQ using the provided documents
    mcq = usecase.run(documents)

    # Return the MCQ content as JSON
    return mcq.model_dump()
