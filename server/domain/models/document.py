from typing import List
from pydantic import BaseModel
from .chunk import Chunk

class Document (BaseModel):
    """
    Represents a document
    """
    name: str
    text: str
    chunks: List[Chunk]