from server.domain.services.corpus_loader import CorpusLoader
from server.domain.services.embedder import Embedder
from server.domain.services.docs_splitter import Splitter

def __init__(self, corpus_loader: CorpusLoader, splitter: Splitter, embedder: Embedder):
    self.corpus_loader = corpus_loader
    self.embedder = embedder
    self.splitter = splitter

def run(self, corpus_path: str) -> str:
    docs = self.corpus_loader.load_from_path(corpus_path)
    chunks = self.splitter.split(docs)
    self.embedder.embed(chunks)
    return "Core knowledge vector database updated successfully."