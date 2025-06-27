from server.domain.models.document import Document

class DocumentProcessor:
    """
    Service responsible for transforming raw file content into a structured Document.
    """

    def process(self, file_bytes: bytes) -> Document:
        """
        Process a file (as bytes) and return a Document object.
        """
        pass
