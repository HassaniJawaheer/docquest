from fastapi import APIRouter, Depends, HTTPException, Request
from server.infrastructure.dependencies import get_summarize_documents
from server.usecases.summarize_documents import SummarizeDocuments
from server.utils.request_helpers import get_session_id

router = APIRouter()

@router.post("/summarize")
def summarize(
    request: Request,
    usecase: SummarizeDocuments = Depends(get_summarize_documents),
):
    # Extract session ID from the request
    session_id = get_session_id(request)

    # Retrieve documents assigned to the 'summarize' workspace
    documents = request.app.state.workspace_manager.get(session_id, "summarize")
    if not documents:
        raise HTTPException(status_code=404, detail="No documents found in workspace 'summarize'")

    # Run summarization use case
    summary = usecase.run(documents)

    # Return the summary as plain JSON
    return {"summary": summary.content}
