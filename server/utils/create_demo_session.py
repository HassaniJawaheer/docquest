import os
from dotenv import load_dotenv
from datetime import datetime, timezone
from server.infrastructure.stores.redis_session_manager import RedisSessionManager

load_dotenv()

def create_demo_session(session_manager: RedisSessionManager) -> str:
    """
    Create a demo session using the fixed DEMO_SESSION_ID from .env
    and register it in Redis via the session manager.
    """
    demo_session_id = os.getenv("DEMO_SESSION_ID", "demo-session-id")

    key = f"docquest:{demo_session_id}"
    session_manager.redis.hset(key, "_init", "1")
    session_manager.redis.expire(key, session_manager.ttl)

    created_at = datetime.now(timezone.utc)
    return demo_session_id
