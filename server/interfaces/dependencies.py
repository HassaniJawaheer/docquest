from server.usecases.generate_mcq import GenerateMCQ
from server.usecases.upload_documents import UploadDocuments
from server.interfaces.services.document_processor import DocumentProcessor
from server.interfaces.services.workspace_manager import WorkspaceManager
from server.interfaces.services.mcq_generator import MCQGenerator

def get_upload_documents_usecase() -> UploadDocuments:
    processor = DocumentProcessor()
    workspace = WorkspaceManager()
    return UploadDocuments(processor, workspace)

def get_generate_mcq_usecase() -> GenerateMCQ:
    mcq_generator = MCQGenerator()
    return GenerateMCQ(mcq_generator)