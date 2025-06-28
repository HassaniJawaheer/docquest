import uuid
from datetime import datetime, timezone
from redis import Redis
from server.domain.models.session import Session
from server.interfaces.services.session_manager import SessionManager


class RedisSessionManager(SessionManager):
    def __init__(self, redis_client: Redis):
        self.redis = redis_client

    def create_session(self, ttl_seconds: int) -> Session:
        session_id = str(uuid.uuid4())
        key = f"docquest:{session_id}"
        self.redis.hset(key, "_init", "1")
        self.redis.expire(key, ttl_seconds)
        return Session(session_id=session_id, created_at=datetime.now(timezone.utc))
    
    def is_valid(self, session_id: str) -> bool:
        return self.redis.exists(f"docquest:{session_id}") == 1
    
    def get_ttl(self, session_id: str) -> int:
        return self.redis.ttl(f"docquest:{session_id}")