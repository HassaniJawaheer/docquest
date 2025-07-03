from typing import Dict
from langchain_community.vectorstores import FAISS
from server.interfaces.stores.vector_db_manager import VectorDBManager

class InMemoryVectorDBManager(VectorDBManager):
    def __init__(self):
        self._store: Dict[str, FAISS] = {}

    def set(self, key: str, db: FAISS) -> None:
        self._store[key] = db

    def get(self, key: str) -> FAISS:
        if key not in self._store:
            raise KeyError(f"VectorDB '{key}' not found.")
        return self._store[key]

    def has(self, key: str) -> bool:
        return key in self._store

    def remove(self, key: str) -> None:
        self._store.pop(key, None)
