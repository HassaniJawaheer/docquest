import uuid
from datetime import datetime, timezone
from redis import Redis
from server.domain.models.session import Session
from server.interfaces.stores.session_manager import SessionManager


class RedisSessionManager(SessionManager):
    def __init__(self, redis_client: Redis, ttl: int):
        self.redis = redis_client
        self.ttl = ttl

    def create_session(self) -> Session:
        session_id = str(uuid.uuid4())
        key = f"docquest:{session_id}"
        self.redis.hset(key, "_init", "1")
        self.redis.expire(key, self.ttl)
        return Session(session_id=session_id, created_at=datetime.now(timezone.utc))
    
    def is_valid(self, session_id: str) -> bool:
        return self.redis.exists(f"docquest:{session_id}") == 1
    
    def get_ttl(self, session_id: str) -> int:
        return self.redis.ttl(f"docquest:{session_id}")