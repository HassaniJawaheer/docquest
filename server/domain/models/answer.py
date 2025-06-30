from typing import List, Literal
from pydantic import BaseModel
from server.domain.models.mcq import Question

class Answer(BaseModel):
    type: Literal["text", "qcm"]

class TextAnswer(Answer):
    type: Literal["text"] = "text"
    content: str

class MCQAnswer(Answer):
    type: Literal["qcm"] = "qcm"
    questions: List[Question]
