import os
from server.infrastructure.services.corpus_state_hasher import CorpusStateHasher
from server.interfaces.services.corpus_loader import CorpusLoader
from server.interfaces.services.splitter import Splitter
from server.interfaces.services.vector_database_builder import VectorDatabaseBuilder

class UpdateCentralVectorDB:
    def __init__(
        self,
        corpus_loader: CorpusLoader,
        splitter: Splitter,
        db_builder: VectorDatabaseBuilder,
        corpus_hasher: CorpusStateHasher,
        hash_file: str = ".central_vector_db.hash"
    ):
        self.corpus_loader = corpus_loader
        self.splitter = splitter
        self.db_builder = db_builder
        self.corpus_hasher = corpus_hasher
        self.hash_file = hash_file
        self.current_db = None  # keep in memory

    def run(self, corpus_path: str):
        new_hash = self.corpus_hasher.compute_hash(corpus_path)
        old_hash = None

        if os.path.exists(self.hash_file):
            with open(self.hash_file, "r") as f:
                old_hash = f.read().strip()

        if new_hash == old_hash and self.current_db is not None:
            print("[CentralDB] No change detected. Using existing vector DB in memory.")
            return self.current_db

        print("[CentralDB] Change detected or no DB yet. Rebuilding vector DB.")
        docs = self.corpus_loader.load_from_path(corpus_path)
        chunks = self.splitter.split(docs)
        self.current_db = self.db_builder.build(chunks)

        with open(self.hash_file, "w") as f:
            f.write(new_hash)

        return self.current_db

