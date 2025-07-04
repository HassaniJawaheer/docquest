from redis import Redis
from typing import List
import json
from server.interfaces.stores.chat_history_manager import ChatHistoryManager
from server.domain.models.chat_message import ChatMessage

class RedisChatHistoryManager(ChatHistoryManager):
    def __init__(self, redis_client: Redis):
        self.redis = redis_client

    def _key(self, session_id: str) -> str:
        return f"docquest:{session_id}:chat_history"

    def append(self, session_id: str, message: ChatMessage) -> None:
        key = self._key(session_id)
        self.redis.rpush(key, message.model_dump_json())

    def get(self, session_id: str, n_last: int = 10) -> List[ChatMessage]:
        key = self._key(session_id)
        raw_msgs = self.redis.lrange(key, -n_last, -1)
        return [ChatMessage.model_validate(json.loads(m)) for m in raw_msgs]

    def clear(self, session_id: str) -> None:
        key = self._key(session_id)
        self.redis.delete(key)
