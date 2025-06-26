from typing import List
from pydantic import BaseModel

class Question(BaseModel):
    question: str
    correct_answer: str
    distractors: List[str]

class MCQ(BaseModel):
    """
    Represents a multiple-choice questionnaire
    """
    questions : List[Question]