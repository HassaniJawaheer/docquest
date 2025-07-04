from typing import List
from server.interfaces.services.mcq_generator import MCQGenerator
from server.interfaces.services.llm import LLM
from server.interfaces.services.prompt_builder import PromptBuilder
from server.domain.models.document import Doc
from server.domain.models.answer import MCQAnswer
from server.utils.mcq_parser import parse_mcq

class DefaultMCQGenerator(MCQGenerator):
    def __init__(self, llm: LLM, prompt_builder: PromptBuilder):
        self.llm = llm
        self.prompt_builder = prompt_builder

    def generate(self, docs: List[Doc]) -> MCQAnswer:
        # Build the prompt
        prompt = self.prompt_builder.prompt_for_mcq(docs)
        
        # Call LLM
        response_text = self.llm.generate_answer(prompt)

        # Parse the response with regex
        questions = parse_mcq(response_text)

        # Return as MCQAnswer
        return MCQAnswer(type="qcm", questions=questions)
