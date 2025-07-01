import json
from typing import List
from server.interfaces.services.mcq_generator import MCQGenerator
from server.interfaces.services.llm import LLM
from server.interfaces.services.prompt_builder import PromptBuilder
from server.domain.models.document import Doc
from server.domain.models.answer import MCQAnswer
from server.domain.models.mcq import Question

class DefaultMCQGenerator(MCQGenerator):
    def __init__(self, llm: LLM, prompt_builder: PromptBuilder):
        self.llm = llm
        self.prompt_builder = prompt_builder

    def generate(self, docs: List[Doc]) -> MCQAnswer:
        prompt = self.prompt_builder.prompt_for_mcq(docs)
        response = self.llm.generate_answer(prompt)

        try:
            data = json.loads(response)
            questions = [Question(**q) for q in data["questions"]]
            return MCQAnswer(type="qcm", questions=questions)
        except Exception as e:
            raise ValueError("Invalid format returned by LLM") from e
