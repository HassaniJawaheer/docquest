from abc import ABC, abstractmethod
from typing import Any, List, Dict

class ChatHistoryManager(ABC):
    @abstractmethod
    def append(self, session_id: str, message: Dict[str, Any]) -> None:
        """Append a message to the session chat history."""
        pass

    @abstractmethod
    def get(self, session_id: str, n_last: int = 10) -> List[Dict[str, Any]]:
        """
        Get the last `n_last` messages of the chat history for the session.
        """
        pass

    @abstractmethod
    def clear(self, session_id: str) -> None:
        """Clear the chat history for the session."""
        pass
