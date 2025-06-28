from pydantic import BaseModel
from typing import Optional

class Chunk(BaseModel):
    content: str
    doc_id: Optional[str] = None
    position: Optional[int] = None
    metadata: Optional[dict] = None