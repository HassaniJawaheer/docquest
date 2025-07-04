from typing import List
from server.interfaces.services.prompt_builder import PromptBuilder
from server.domain.models.document import Doc
from server.domain.models.query import Query
from server.domain.models.chunk import Chunk

class DefaultPromptBuilder(PromptBuilder):
    def prompt_for_mcq(self, docs: List[Doc]) -> str:
        text = "\n".join(doc.content for doc in docs)
        return f"""Tu es un générateur de QCM. En utilisant le texte suivant et génère 10 questions avec 1 bonne réponse et 3 mauvaises réponses (appelées distracteurs) pour chacune. 

Réponds dans le format suivant, sans ajouter de commentaires :
Question 1: <texte de la question>
Correct Answer: <bonne réponse>
Distractors: <distracteur1>, <distracteur2>, <distracteur3>

Question 2: …
Correct Answer: …
Distractors: …

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
