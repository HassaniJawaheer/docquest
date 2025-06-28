from pydantic import BaseModel
from datetime import datetime

class Session(BaseModel):
    session_id: str
    created_at: datetime