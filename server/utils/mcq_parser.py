import re
from typing import List
from server.domain.models.mcq import Question

def parse_mcq(text: str) -> List[Question]:
    """
    Parse the LLM's response text into a list of Question objects.
    Assumes the format:
      Question 1: ...
      Correct answer: ...
      Distractors: ..., ..., ...
    """
    pattern = re.compile(
        r"Question\s*\d+\s*:\s*(.*?)\n"
        r"Correct answer\s*:\s*(.*?)\n"
        r"Distractors\s*:\s*(.*?)\n",
        re.IGNORECASE | re.DOTALL
    )

    matches = pattern.findall(text)
    questions = []

    for q_text, correct, distractors in matches:
        distractors_list = [d.strip() for d in distractors.split(",") if d.strip()]
        questions.append(Question(
            question=q_text.strip(),
            correct_answer=correct.strip(),
            distractors=distractors_list
        ))

    if not questions:
        raise ValueError("No valid questions parsed from LLM response")

    return questions
