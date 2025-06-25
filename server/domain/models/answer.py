from typing import List
from pydantic import BaseModel
from .chunk import Chunk

class Answer(BaseModel):
    """
    Represents a response generated from a query.
    """
    text: str
    sources: List[Chunk]