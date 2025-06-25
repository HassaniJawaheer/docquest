from pydantic import BaseModel

class Query(BaseModel):
    """
    Represents a question asked by the user.
    """
    text: str