from typing import List
from pydantic import BaseModel

class QCMQuestion(BaseModel):
    question: str
    correct_answer: str
    distractors: List[str]

class QCM(BaseModel):
    """
    Represents a multiple-choice questionnaire
    """
    questions : List[QCMQuestion]