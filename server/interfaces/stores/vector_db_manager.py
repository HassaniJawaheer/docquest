from abc import ABC, abstractmethod
from typing import Any

class VectorDBManager(ABC):
    @abstractmethod
    def set(self, key: str, db: Any) -> None:
        """Store a vector database under the given key ('central' or a session ID)."""
        pass

    @abstractmethod
    def get(self, key: str) -> Any:
        """Retrieve a vector database by key."""
        pass

    @abstractmethod
    def has(self, key: str) -> bool:
        """Check if a Vector DB exists under this key."""
        pass

    @abstractmethod
    def remove(self, key: str) -> None:
        """Remove the Vector DB associated with the given key."""
        pass
