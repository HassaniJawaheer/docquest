import os
from typing import List
import fitz
import docx
from server.domain.models.document import Doc
from server.interfaces.services.corpus_loader import CorpusLoader

class LocalCorpusLoader(CorpusLoader):
    """
    Loads all documents (.pdf, .docx, .txt) from one directory.
    """
    def load_from_path(self, path: str) -> List[Doc]:
        docs = []

        for root, _, files in os.walk(path):
            for file in files:
                ext = file.lower().split('.')[-1]
                file_path = os.path.join(root, file)

                if ext == "pdf":
                    docs.append(self._read_pdf(file_path))
                elif ext == "docx":
                    docs.append(self._read_docx(file_path))
                elif ext == "txt":
                    docs.append(self._read_txt(file_path))
        
        return [doc for doc in docs if doc.content.strip()]

    def _read_pdf(self, path: str) -> Doc:
        text = ""
        with fitz.open(path) as pdf:
            for page in pdf:
                text += page.get_text()
        return Doc(
            name=os.path.basename(path),
            content=text
        )

    def _read_docx(self, path: str) -> Doc:
        docx_doc = docx.Document(path)
        full_text = "\n".join([para.text for para in docx_doc.paragraphs])
        return Doc(
            name=os.path.basename(path),
            content=full_text
        )

    def _read_txt(self, path: str) -> Doc:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        return Doc(
            name=os.path.basename(path),
            content=text
        )
