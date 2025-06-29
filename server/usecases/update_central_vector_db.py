import os
from server.infrastructure.services.corpus_state_hasher import CorpusStateHasher
from server.interfaces.services.corpus_loader import CorpusLoader
from server.interfaces.services.embedder import Embedder
from server.interfaces.services.docs_splitter import Splitter
from server.interfaces.services.vector_database_builder import VectorDatabaseBuilder

class UpdateCentralVectorDB:
    def __init__(
        self,
        corpus_loader: CorpusLoader,
        splitter: Splitter,
        embedder: Embedder,
        db_builder: VectorDatabaseBuilder,
        corpus_hasher: CorpusStateHasher,
        hash_file: str = ".central_vector_db.hash"
    ):
        self.corpus_loader = corpus_loader
        self.splitter = splitter
        self.embedder = embedder
        self.db_builder = db_builder
        self.corpus_hasher = corpus_hasher
        self.hash_file = hash_file

    def run(self, corpus_path: str) -> str:
        new_hash = self.corpus_hasher.compute_hash(corpus_path)
        old_hash = None

        if os.path.exists(self.hash_file):
            with open(self.hash_file, "r") as f:
                old_hash = f.read().strip()

        if new_hash == old_hash:
            return "No change detected. Skipped update."

        docs = self.corpus_loader.load_from_path(corpus_path)
        chunks = self.splitter.split(docs)
        self.embedder.embed(chunks)
        self.db_builder.build(chunks)

        with open(self.hash_file, "w") as f:
            f.write(new_hash)

        return "Core knowledge vector database updated successfully."
