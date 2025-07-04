from typing import List
from server.interfaces.services.summarizer import Summarizer
from server.interfaces.services.llm import LLM
from server.interfaces.services.prompt_builder import PromptBuilder
from server.domain.models.document import Doc
from server.domain.models.answer import TextAnswer

class DefaultSummarizer(Summarizer):
    def __init__(self, llm: LLM, prompt_builder: PromptBuilder):
        self.llm = llm
        self.prompt_builder = prompt_builder

    def summarize(self, docs: List[Doc]) -> TextAnswer:
        prompt = self.prompt_builder.prompt_for_summary(docs)
        content = self.llm.generate_answer(prompt)
        return TextAnswer(type="text", content=content)
