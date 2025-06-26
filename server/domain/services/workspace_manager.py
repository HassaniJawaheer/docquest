from typing import Dict, List
from server.domain.models.document import Document

class WorkspaceManager:
    """
    Manages logical association between documents and workspaces
    """

    def __init__(self):
        self.registry: Dict[str, Dict[str, List[Document]]] = {}
    
    def assign(self, session_id: str, workspace: str, documents: List[Document]) -> None:
        if session_id not in self.registry:
            self.registry[session_id] = {}
        if workspace not in self.registry[session_id]:
            self.registry[session_id][workspace] = []
        self.registry[session_id][workspace].extend(documents)
    
    def get(self, session_id: str, workspace: str) -> List[Document]:
        return self.registry.get(session_id, {}).get(workspace, [])