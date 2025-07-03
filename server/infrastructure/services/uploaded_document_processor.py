from io import BytesIO
import fitz
import docx
import logging
from fastapi import UploadFile
from typing import Optional
from server.domain.models.document import Doc
from server.interfaces.services.document_processor import DocumentProcessor

class UploadedDocumentProcessor(DocumentProcessor):
    async def process(self, file: UploadFile) -> Optional[Doc]:
        """
        Transforme un UploadFile en Doc.
        """
        try:
            file_content = await file.read()
            file_name = file.filename.lower()

            if file_name.endswith('.txt'):
                text = file_content.decode("utf-8")
                return Doc(name=file.filename, content=text)

            elif file_name.endswith('.docx'):
                docx_file = docx.Document(BytesIO(file_content))
                text = "\n".join(p.text for p in docx_file.paragraphs)
                return Doc(name=file.filename, content=text)

            elif file_name.endswith('.pdf'):
                try:
                    pdf = fitz.open(stream=file_content, filetype="pdf")
                    text = "\n".join(page.get_text() for page in pdf)
                    return Doc(name=file.filename, content=text)
                except Exception as e:
                    logging.error(f"[DOCUMENT_PROCESSOR] PDF parsing failed: {file.filename} | {e}")

            else:
                logging.warning(f"[DOCUMENT_PROCESSOR] Unsupported file type: {file.filename}")

        except Exception as e:
            logging.error(f"[DOCUMENT_PROCESSOR] Error processing {file.filename}: {e}")

        return None

