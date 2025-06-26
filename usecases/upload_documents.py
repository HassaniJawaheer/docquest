from typing import List
from server.domain.models.document import Document
from server.domain.services.document_processor import DocumentProcessor
from server.domain.services.workspace_manager import WorkspaceManager

class UploadDocuments:
    """
    Takes user files, transforms them into Document objects and associates them with a workspace.
    """
    def __init__(self, processor: DocumentProcessor, workspace_manager: WorkspaceManager):
        self.processor = processor
        self.workspace_manager = workspace_manager

    def run(self, files: List[bytes], workspace: str, session_id: str) -> List[Document]:
        documents = []
        for file in files:
            doc = self.processor.process(file)
            documents.append(doc)
        self.workspace_manager.assign(session_id, workspace, documents)
        return documents