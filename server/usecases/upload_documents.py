from typing import List
from fastapi import UploadFile
from server.interfaces.services.document_processor import DocumentProcessor
from server.interfaces.services.workspace_manager import WorkspaceManager

class UploadDocuments:
    """
    Use case to process uploaded files and assign them to a workspace.
    """
    def __init__(self, processor: DocumentProcessor):
        self.processor = processor

    async def run(self, files: List[UploadFile], workspace: str, session_id: str, workspace_manager: WorkspaceManager) -> None:
        documents = []

        for file in files:
            doc = await self.processor.process(file)
            if doc:
                documents.append(doc)

        if not documents:
            raise ValueError("No valid document was processed.")

        workspace_manager.assign(session_id, workspace, documents)
