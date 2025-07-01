import uuid
from server.infrastructure.redis import get_redis_client
from server.infrastructure.sessions.redis_session_manager import RedisSessionManager

# Exemple UUID fixe pour démo
DEMO_SESSION_ID = "11111111-1111-1111-1111-111111111111"

def create_demo_session():
    redis = get_redis_client()
    session_manager = RedisSessionManager(redis, ttl=3600)

    # Crée la session si elle n’existe pas déjà
    if not session_manager.is_valid(DEMO_SESSION_ID):
        key = f"docquest:{DEMO_SESSION_ID}"
        redis.hset(key, "_init", "1")
        redis.expire(key, 3600)

create_demo_session()
