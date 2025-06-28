from abc import ABC, abstractmethod
from typing import List

class Embedder(ABC):
    @abstractmethod
    def get_model(self):
        pass
