import os
import uuid
from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import logging
import threading
import time
import redis


# ------ Logging ------
from server.config.logging_config import configure_logging
logger = logging.getLogger(__name__)
configure_logging()

# ------ Routers ------
from server.interfaces.routes.generate_mcq import router as generate_mcq_router
from server.interfaces.routes.summarize import router as summarize_router
from server.interfaces.routes.upload import router as upload_router
from server.interfaces.routes.query_central_vector_db import router as query_central_vector_db_router
from server.interfaces.routes.query_user_vector_db import router as query_user_vector_db_router
from server.interfaces.routes.root import router as root_router
from server.interfaces.routes.create_vector_db import router as create_vector_db_router

# ------ Infrastructure & services ------
from server.infrastructure.stores.inmemory_vector_db_manager import InMemoryVectorDBManager
from server.infrastructure.services.huggingface_embedder import HuggingFaceEmbedder
from server.infrastructure.stores.redis_workspace_manager import RedisWorkspaceManager
from server.infrastructure.stores.redis_session_manager import RedisSessionManager
from server.infrastructure.services.faiss_vector_db_builder import FaissVectorDatabaseBuilder
from server.infrastructure.services.langchain_splitter import LangchainSplitter
from server.infrastructure.services.classic_corpus_loader import LocalCorpusLoader
from server.infrastructure.services.corpus_state_hasher import CorpusStateHasher
from server.usecases.update_central_vector_db import UpdateCentralVectorDB
from server.infrastructure.stores.redis_chat_history_manager import RedisChatHistoryManager
from server.utils.create_demo_session import create_demo_session


# ------ Load environment ------
load_dotenv()
FRONT_BASE_URL = os.getenv("FRONT_BASE_URL", "*")
DEMO_SESSION_ID = os.getenv("DEMO_SESSION_ID", str(uuid.uuid4()))
CLEAN_REDIS = os.getenv("CLEAN_REDIS_ON_SHUTDOWN", "False").lower() == "true"
CENTRAL_CORPUS_PATH = os.getenv("CENTRAL_CORPUS_PATH", "corpus/central")
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 1000))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 200))
TOP_K_SIMILAR_VECTORS = int(os.getenv("TOP_K_SIMILAR_VECTORS", 5))
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_DB = int(os.getenv("REDIS_DB", 0))
REDIS_TTL = int(os.getenv("REDIS_TTL", 3600))


# ------ Shutdown logic ------
def lifespan(app: FastAPI):
    yield  # Start-up phase complete

    if not CLEAN_REDIS:
        logger.info("[shutdown] Redis cleanup skipped (CLEAN_REDIS_ON_SHUTDOWN=False)")
        return

    try:
        logger.info("[shutdown] Cleaning Redis session and document keys...")
        if hasattr(app.state, "session_repo"):
            redis = app.state.session_repo.redis
            session_keys = redis.keys("docquest:*")
            if session_keys:
                redis.delete(*session_keys)
                logger.info(f"[shutdown] Deleted {len(session_keys)} session keys.")
            else:
                logger.info("[shutdown] No session keys found.")
        if hasattr(app.state, "workspace_manager"):
            redis = app.state.workspace_manager.redis
            doc_keys = redis.keys("docquest:*")
            if doc_keys:
                redis.delete(*doc_keys)
                logger.info(f"[shutdown] Deleted {len(doc_keys)} document keys.")
            else:
                logger.info("[shutdown] No document keys found.")
    except Exception as e:
        logger.warning(f"[shutdown] Redis cleanup failed: {e}")

# ------ FastAPI app creation ------
app = FastAPI(lifespan=lifespan)

# ------ Initialize Redis client ------
redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_DB,
    decode_responses=True  # Ensures values are returned as strings, not bytes
)

# ------ Embedding model ------
logger.info("[startup] Loading embedding model...")
embedder = HuggingFaceEmbedder()
app.state.embedding_model = embedder.get_model()
logger.info("[startup] Embedding model loaded.")

# ------ Redis-based repositories ------
logger.info("[startup] Initializing Redis session & document managers...")
app.state.session_manager = RedisSessionManager(redis_client, REDIS_TTL)
app.state.workspace_manager = RedisWorkspaceManager(redis_client)
app.state.chat_history_manager = RedisChatHistoryManager(redis_client)
logger.info("[startup] Redis repositories ready.")

# ------ Create a DEMO session  ------
demo_session_id = create_demo_session(app.state.session_manager)
logger.info(f"[startup] Demo session created with ID: {demo_session_id}")

# ------ In-memory vector DB manager ------
logger.info("[startup] Initializing vector database manager...")
app.state.vector_db_manager = InMemoryVectorDBManager()

# ------ Build central vector DB ------
logger.info("[startup] Building central vector database...")
splitter = LangchainSplitter()
loader = LocalCorpusLoader()
db_builder = FaissVectorDatabaseBuilder(app.state.embedding_model)
hasher = CorpusStateHasher()
updater = UpdateCentralVectorDB(
    corpus_loader=loader,
    splitter=splitter,
    db_builder=db_builder,
    corpus_hasher=hasher
)
central_db = updater.run(CENTRAL_CORPUS_PATH)
app.state.vector_db_manager.set("central", central_db)
logger.info("[startup] Central vector DB created and registered.")

# ------ Background watcher to update central DB ------
def continuous_update_central_vector_db():
    while True:
        try:
            time.sleep(300)  # Every 5 minutes
            logger.info("[watcher] Checking for updates in central corpus...")
            updated_db = updater.run(CENTRAL_CORPUS_PATH)
            if updated_db != "No change detected. Skipped update.":
                app.state.vector_db_manager.set("central", updated_db)
                logger.info("[watcher] Central vector DB updated and re-registered.")
            else:
                logger.info("[watcher] No update needed.")
        except Exception as e:
            logger.warning(f"[watcher] Update failed: {e}")

threading.Thread(target=continuous_update_central_vector_db, daemon=True).start()
logger.info("[startup] Watcher thread started.")

# ------ Middleware ------
logger.info("[startup] Adding CORS middleware...")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONT_BASE_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------ Routes ------
logger.info("[startup] Registering routes...")
app.include_router(root_router, prefix="", tags=["root"])
app.include_router(upload_router, prefix="", tags=["upload"])
app.include_router(create_vector_db_router, prefix="", tags=["create_vector_db_router"])
app.include_router(generate_mcq_router, prefix="", tags=["generate_qcm"])
app.include_router(summarize_router, prefix="", tags=["summarize"])
app.include_router(query_central_vector_db_router, prefix="", tags=["query_central_db"])
app.include_router(query_user_vector_db_router, prefix="", tags=["query_user_db"])
logger.info("[startup] All routes registered.")

