from pydantic import BaseModel

class Doc(BaseModel):
    """
    Represents a document
    """
    name: str
    content: str