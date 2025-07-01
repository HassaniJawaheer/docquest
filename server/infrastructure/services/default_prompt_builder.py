from typing import List
from server.interfaces.services.prompt_builder import PromptBuilder
from server.domain.models.document import Doc
from server.domain.models.query import Query
from server.domain.models.chunk import Chunk

class DefaultPromptBuilder(PromptBuilder):
    def prompt_for_mcq(self, docs: List[Doc]) -> str:
        text = "\n".join(doc.content for doc in docs)
        return f"""Tu es un générateur de QCM. Lis le texte suivant et génère 10 questions au format JSON :
{{
  "questions": [
    {{
      "question": "...",
      "correct_answer": "...",
      "distractors": ["...", "...", "..."]
    }}
  ]
}}

Texte :
{text}
"""

    def prompt_for_summary(self, docs: List[Doc]) -> str:
        text = "\n".join(doc.content for doc in docs)
        return f"""Résume le texte suivant de manière claire et concise :

Texte :
{text}
"""

    def prompt_for_query(self, query: Query, chunks: List[Chunk]) -> str:
        context = "\n".join(chunk.content for chunk in chunks)
        return f"""Tu dois répondre à une question en te basant uniquement sur les extraits suivants :

Contexte :
{context}

Question :
{query.content}
"""
