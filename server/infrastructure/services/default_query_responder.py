from typing import List
from server.interfaces.services.quey_responder import QueryResponder
from server.interfaces.services.llm import LLM
from server.interfaces.services.prompt_builder import PromptBuilder
from server.domain.models.chunk import Chunk
from server.domain.models.query import Query
from server.domain.models.answer import TextAnswer

class DefaultQueryResponder(QueryResponder):
    def __init__(self, llm: LLM, prompt_builder: PromptBuilder):
        self.llm = llm
        self.prompt_builder = prompt_builder

    def response(self, query: Query, chunks: List[Chunk]) -> TextAnswer:
        prompt = self.prompt_builder.prompt_for_query(query, chunks)
        try:
            content = self.llm.generate_answer(prompt)
            return TextAnswer(type="text", content=content)
        except Exception as e:
            raise ValueError("Invalid response from LLM") from e
