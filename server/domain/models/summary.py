from pydantic import BaseModel

class Summary(BaseModel):
    """
    Represents a summary generated from one or more documents.
    """
    content: str
    