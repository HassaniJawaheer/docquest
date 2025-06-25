from pydantic import BaseModel

class Chunk(BaseModel):
    """
    Represents a text segment extracted from a document
    """
    content: str
    position: int
    score: float = 0.0