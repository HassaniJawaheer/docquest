from abc import ABC, abstractmethod
from typing import List
from server.domain.models.document import Document

class WorkspaceManager(ABC):
    """
    Interface for managing user workspaces
    Associates documents to a session and a logical workspace ('mcq', 'summarize', 'user_rag').
    """

    @abstractmethod
    def assign(self, session_id: str, workspace: str, documents: List[Document]) -> None:
        pass

    @abstractmethod
    def get(self, session_id: str, workspace: str) -> List[Document]:
        pass

    @abstractmethod
    def remove(self, session_id: str) -> None:
        """
        Optional: Remove all documents for a given session.
        """
        pass
