from pydantic import BaseModel

class Document (BaseModel):
    """
    Represents a document
    """
    name: str
    content: str