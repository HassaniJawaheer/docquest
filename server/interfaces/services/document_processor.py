from server.domain.models.document import Doc

class DocumentProcessor:
    """
    Service responsible for transforming raw file content into a structured Document.
    """

    def process(self, file_bytes: bytes) -> Doc:
        """
        Process a file (as bytes) and return a Document object.
        """
        pass
