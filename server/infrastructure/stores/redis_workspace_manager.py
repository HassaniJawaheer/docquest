from redis import Redis
from typing import List
import json
from server.domain.models.document import Doc
from server.interfaces.stores.workspace_manager import WorkspaceManager


class RedisWorkspaceManager(WorkspaceManager):
    def __init__(self, redis_client: Redis):
        self.redis = redis_client
    
    def _key(self, session_id: str) -> str:
        return f"docquest:{session_id}"
    
    def assign(self, session_id: str, workspace: str, documents: List[Doc]) -> None:
        key = self._key(session_id)
        existing_json = self.redis.hget(key, workspace)
        if existing_json:
            existing = json.loads(existing_json)
        else:
            existing = []
        
        # Append new documents
        new_docs = [doc.model_dump() for doc in documents]
        combined = existing + new_docs

        # Set updated list
        self.redis.hset(key, workspace, json.dumps(combined))

    def get(self, session_id: str, workspace: str) -> List[Doc]:
        key = self._key(session_id)
        raw = self.redis.hget(key, workspace)
        if not raw:
            return []
        data = json.loads(raw)
        return [Doc(**d) for d in data]
    
    def remove(self, session_id: str) -> None:
        key = self._key(session_id)
        self.redis.delete(key)
