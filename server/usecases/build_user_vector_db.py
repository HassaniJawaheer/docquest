from server.interfaces.services.workspace_manager import WorkspaceManager
from server.interfaces.services.docs_splitter import Splitter
from server.interfaces.services.embedder import Embedder

class BuildUserVectorDB:
    """
    Construct a personal vector database from the user's upload documents.
    """

    def __init__(self, workspace_manager: WorkspaceManager, splitter: Splitter, embedder: Embedder):
        self.workspace_manager = workspace_manager
        self.splitter = splitter
        self.embedder = embedder

    def run(self, session_id: str) -> str:
        documents = self.workspace_manager.get(session_id, "user_rag")
        if not documents:
            return "No documents available to build the vector database"
        
        chunks = self.splitter.split(documents)
        self.embedder.embed(chunks)
        return "Vector database created successfully"