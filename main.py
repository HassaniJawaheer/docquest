import os
import uuid
from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from server.interfaces.routes.generate_mcq import router as generate_mcq_router
from server.interfaces.routes.summarize import router as summarize_router
from server.interfaces.routes.upload import router as upload_router
from server.interfaces.routes.query_central_vector_db import router as query_central_vector_db_router
from server.interfaces.routes.query_user_vector_db import router as query_user_vector_db_router
from server.interfaces.routes.summarize import router as summarize_router
from server.infrastructure.stores.redis_workspace_manager import RedisWorkspaceManager
from server.infrastructure.stores.redis_session_manager import RedisSessionManager
from server.infrastructure.services.faiss_vector_db_builder import FaissVectorDatabaseBuilder


load_dotenv()

FRONT_BASE_URL = os.getenv("FRONT_BASE_URL", "*")
DEMO_SESSION_ID = os.getenv("DEMO_SESSION_ID", str(uuid.uuid4()))

# ---- Initialisation de l'app FastAPI
app = FastAPI()

# ---- Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONT_BASE_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---- Démarrage de l'application
@app.on_event("startup")
def startup_demo():
    # Session
    app.state.session_id = DEMO_SESSION_ID
    app.state.workspace_manager = WorkspaceManager()
    app.state.workspace_manager.create(DEMO_SESSION_ID)

    # Embedding model
    embedding_loader = HuggingfaceEmbeddingLoader(model_path=os.getenv("MODEL_EMBEDDING_PATH"))
    app.state.embedding_model = embedding_loader.load()

    # Redis
    app.state.session_repo = RedisSessionRepository(
        host=os.getenv("REDIS_HOST"),
        port=int(os.getenv("REDIS_PORT")),
        db=int(os.getenv("REDIS_DB")),
        ttl=int(os.getenv("REDIS_TTL"))
    )
    app.state.document_repo = RedisDocumentRepository(app.state.session_repo.redis)

    # FAISS
    app.state.vector_database = FaissVectorDatabase(
        embedding_model=app.state.embedding_model,
        base_path=os.getenv("DB_REPOSITORY", "server/infrastructure/vectorstores"),
        chunk_size=int(os.getenv("CHUNK_SIZE")),
        chunk_overlap=int(os.getenv("CHUNK_OVERLAP")),
        top_k_similar_vectors=int(os.getenv("TOP_K_SIMILAR_VECTORS"))
    )

    print(f"[INIT] Session de démo : {DEMO_SESSION_ID}")
    print("[INIT] Démo prête.")

# ---- Routes 
app.include_router(upload_router, prefix="", tags=["upload"])

# ---- Route de test
@app.get("/")
def root():
    return {
        "status": "ok",
        "session_id": app.state.session_id
    }
