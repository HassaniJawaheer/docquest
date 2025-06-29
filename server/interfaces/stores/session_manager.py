from abc import ABC, abstractmethod
from server.domain.models.session import Session

class SessionManager(ABC):
    @abstractmethod
    def create_session(self, ttl_seconds: int) -> Session:
        pass

    @abstractmethod
    def is_valid(self, session_id: str) -> bool:
        pass

    @abstractmethod
    def get_ttl(self, session_id: str) -> int:
        pass
