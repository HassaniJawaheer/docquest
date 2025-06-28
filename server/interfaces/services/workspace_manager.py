from abc import ABC, abstractmethod
from typing import List
from server.domain.models.document import Doc

class WorkspaceManager(ABC):
    """
    Interface for managing user workspaces
    Associates documents to a session and a logical workspace ('mcq', 'summarize', 'user_rag').
    """

    @abstractmethod
    def assign(self, session_id: str, workspace: str, documents: List[Doc]) -> None:
        pass

    @abstractmethod
    def get(self, session_id: str, workspace: str) -> List[Doc]:
        pass

    @abstractmethod
    def remove(self, session_id: str) -> None:
        """
        Optional: Remove all documents for a given session.
        """
        pass
